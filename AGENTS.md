# Expertise App Proposal Design — agent instructions

A proposal design for Founders School's Expertise App, by Daniel Carranza. It explains his two-vault second brain, carries his teaching-entrepreneurship knowledge and the caldosa de montaña case, and ships a working student vault.

## Rules

1. **Every factual claim about Daniel needs a source** (his documents, his notes, or his own words). If a fact is not confirmed, leave it out and ask him. Never invent experience, numbers or quotes in his voice.
2. **The Valentina example is fictional** and must stay labeled that way. Library facts that cite real sources must be checked against the source.
3. **Student-facing text says "hypothesis"**, a guess you can check, never "bet".
4. **No AI attribution lines in commits** (no Co-Authored-By, no "Generated with").
5. **Nothing about Daniel's clients, money or family** goes in this repo.
6. **Simplified Technical English** for technical text: short sentences, one idea each, defined terms, active voice.

## Layout

- `docs/` — `my-second-brain.md`, `teaching-entrepreneurship.md`, `case-caldosa-de-montana.md`, `entrecomp.md`, `design.md`; images in `docs/img/`
- `template/` — the student vault (its own `AGENTS.md` is the agent contract students' agents read)
- `scripts/expertise.py` — dashboard and lint; standard library only
- `tests/` — `python3 -m unittest discover -s tests`
- `examples/valentina/` — worked example; regenerate its dashboard with `python3 scripts/expertise.py dashboard examples/valentina --today 2026-10-03`
- `data/` — EntreComp learning outcomes (CSV)
- `LICENSE` (MIT, code) · `LICENSE-docs.md` (CC BY 4.0, docs and images)

## Before you commit

```bash
python3 -m unittest discover -s tests
python3 scripts/expertise.py lint examples/valentina
python3 scripts/expertise.py dashboard examples/valentina --today 2026-10-03
```
