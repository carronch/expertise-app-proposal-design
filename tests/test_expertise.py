"""Tests for scripts/expertise.py. Run: python3 -m unittest discover -s tests"""
import datetime as dt
import io
import sys
import tempfile
import textwrap
import unittest
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import expertise as ex  # noqa: E402

TODAY = dt.date(2026, 10, 3)


def write(root: Path, rel: str, text: str) -> None:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(text).lstrip(), encoding="utf-8")


def make_vault(root: Path) -> None:
    for i in range(3):
        write(root, f"library/sources/source-{i}.md", f"""
            ---
            written_by: agent
            created: 2026-09-0{i + 1}
            url: https://example.org/{i}
            topics: [resin]
            ---
            # Source {i}

            ## Facts

            - Fact A from source {i}.
            - Fact B from source {i}.
            """)
    write(root, "library/topics/resin.md", """
        ---
        written_by: agent
        created: 2026-09-01
        ---
        # Resin
        """)
    write(root, "mind/insights/lonely-insight.md", """
        ---
        written_by: me
        created: 2026-09-10
        topics: [resin]
        entrecomp: [1.2]
        ---
        # Lonely insight

        Only one link: [[source-0]].
        """)
    write(root, "mind/practice/play/hypothesis-cheap-boards.md", """
        ---
        written_by: me
        type: hypothesis
        created: 2026-09-01
        check_by: 2026-09-20
        result: open
        confidence: 60
        entrecomp: [1.1, 3.3]
        ---
        # Hypothesis: cheap boards break more
        """)
    write(root, "mind/practice/empathy/interview-shop.md", """
        ---
        written_by: me
        created: 2026-09-30
        entrecomp: [3.4]
        ---
        # Interview with a shop owner
        """)


class ParsingTests(unittest.TestCase):
    def test_frontmatter_lists_and_links(self):
        meta, body = ex.parse_frontmatter(
            "---\na: 1\nb: [x, \"y z\"]\nc:\n  - one\n  - two\ntests: \"[[pos]]\"\nd: [[pos2]]\n---\nBody\n")
        self.assertEqual(meta["a"], "1")
        self.assertEqual(meta["b"], ["x", "y z"])
        self.assertEqual(meta["c"], ["one", "two"])
        self.assertEqual(meta["tests"], "[[pos]]")
        self.assertEqual(meta["d"], "[[pos2]]")
        self.assertEqual(body, "Body\n")

    def test_inline_comments_are_dropped(self):
        meta, _ = ex.parse_frontmatter(
            "---\nconfidence: 60       # 0-100\nstatus: draft  # draft | tested\n"
            "url: https://example.org/a#b\nnote: \"keep # this\"\n---\n")
        self.assertEqual(meta["confidence"], "60")
        self.assertEqual(meta["status"], "draft")
        self.assertEqual(meta["url"], "https://example.org/a#b")
        self.assertEqual(meta["note"], "keep # this")

    def test_no_frontmatter(self):
        meta, body = ex.parse_frontmatter("# Title\n")
        self.assertEqual(meta, {})
        self.assertEqual(body, "# Title\n")

    def test_sections(self):
        secs = ex.sections("# T\n\n## I believe\n\nX\n\n## What would change my mind\n\nY\n")
        self.assertEqual(secs["i believe"], "X")
        self.assertEqual(secs["what would change my mind"], "Y")


class AnalysisTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        make_vault(self.root)

    def tearDown(self):
        self.tmp.cleanup()

    def report(self):
        return ex.analyze(ex.load_vault(self.root), TODAY)

    def test_ladder_counts(self):
        r = self.report()
        self.assertEqual(r.counts["source"], 3)
        self.assertEqual(r.facts, 6)
        self.assertEqual(r.counts["insight"], 1)
        self.assertEqual(r.counts["position"], 0)

    def test_stance_gap_on_topic_with_sources_and_no_position(self):
        messages = [m for _, m in self.report().nudges]
        self.assertTrue(any("**resin**" in m and "no position yet" in m for m in messages))

    def test_insight_needs_two_links(self):
        messages = [m for _, m in self.report().nudges]
        self.assertTrue(any("[[lonely-insight]] links 1" in m for m in messages))

    def test_overdue_hypothesis(self):
        messages = [m for _, m in self.report().nudges]
        self.assertTrue(any("[[hypothesis-cheap-boards]] was due to be checked on 2026-09-20" in m for m in messages))

    def test_practice_balance_window(self):
        r = self.report()
        self.assertEqual(r.practice_recent["empathy"], 1)   # 2026-09-30 is inside 14 days
        self.assertEqual(r.practice_recent["play"], 0)      # 2026-09-01 is outside
        practices = [p for p, _ in r.nudges]
        self.assertIn("Creation", practices)

    def test_entrecomp_evidence_counts_mind_only(self):
        r = self.report()
        self.assertEqual(r.competence_evidence["1.1"], ["hypothesis-cheap-boards"])
        self.assertEqual(r.competence_evidence["3.4"], ["interview-shop"])
        self.assertEqual(r.competence_evidence["2.4"], [])

    def test_position_rules_and_testing(self):
        write(self.root, "mind/positions/repairs-beat-new-boards.md", """
            ---
            written_by: me
            created: 2026-09-01
            confidence: 70
            topics: [resin]
            ---
            # Repairs beat new boards

            ## I believe

            Fast repairs matter more than new boards.

            ## Because

            [[lonely-insight]] and [[source-1]].

            ## What would change my mind

            <!-- write it -->
            """)
        messages = [m for _, m in self.report().nudges]
        self.assertTrue(any("[[repairs-beat-new-boards]] has no answer" in m for m in messages))
        self.assertTrue(any("[[repairs-beat-new-boards]] is 32 days old" in m for m in messages))
        self.assertFalse(any("**resin**" in m and "no position yet" in m for m in messages))
        write(self.root, "mind/practice/experiments/test-repairs.md", """
            ---
            written_by: me
            created: 2026-10-01
            tests: "[[repairs-beat-new-boards]]"
            ---
            # Test
            """)
        messages = [m for _, m in self.report().nudges]
        self.assertFalse(any("never been tested" in m for m in messages))

    def test_dashboard_renders(self):
        text = ex.render_dashboard(self.report())
        self.assertTrue(text.startswith(ex.GENERATED_HEADER))
        self.assertIn("## The ladder", text)
        self.assertIn("| resin ⚠ | 3 | 6 | 1 | 0 |", text)
        self.assertIn("- 1.1 Spotting opportunities: 1 — [[hypothesis-cheap-boards]]", text)


class LintTests(unittest.TestCase):
    def test_lint_flags_rule_breaks(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_vault(root)
            write(root, "mind/insights/agent-wrote-this.md", """
                ---
                written_by: agent
                created: 2026-10-01
                ---
                # Not allowed
                """)
            write(root, "library/sources/no-origin.md", """
                ---
                written_by: agent
                created: 2026-10-01
                ---
                # No url

                ## Facts

                - Something.
                """)
            write(root, "mind/positions/half-done.md", """
                ---
                written_by: me
                created: 2026-10-01
                confidence: 150
                entrecomp: [4.1]
                ---
                # Half done

                ## I believe

                Something.
                """)
            findings = ex.lint(ex.load_vault(root), root)
            errors = {(f.rel, f.message.split(".")[0]) for f in findings if f.level == "error"}
            rels = {rel for rel, _ in errors}
            self.assertIn("mind/insights/agent-wrote-this.md", rels)
            self.assertIn("library/sources/no-origin.md", rels)
            self.assertIn("mind/positions/half-done.md", rels)
            messages = " ".join(f.message for f in findings)
            self.assertIn("unknown EntreComp code `4.1`", messages)
            self.assertIn("`confidence: 150` must be 0-100", messages)

    def test_cli_exit_codes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_vault(root)
            with redirect_stdout(io.StringIO()):
                self.assertEqual(ex.main(["lint", str(root)]), 0)
                self.assertEqual(ex.main(["dashboard", str(root), "--today", "2026-10-03"]), 0)
            self.assertTrue((root / "_dashboard.md").exists())
            write(root, "mind/insights/bad.md", "---\nwritten_by: agent\ncreated: 2026-10-01\n---\n# Bad\n")
            with redirect_stdout(io.StringIO()):
                self.assertEqual(ex.main(["lint", str(root)]), 1)
            with redirect_stdout(io.StringIO()):
                self.assertEqual(ex.main(["lint", str(root / "library")]), 2)


if __name__ == "__main__":
    unittest.main()
