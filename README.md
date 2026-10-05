# Expertise App Proposal Design

**A second brain that turns curiosity into expertise.** An AI agent keeps the facts. The student writes the positions. Five practices from Babson College's method of teaching entrepreneurship get them from one to the other.

I made this for Founders School's Expertise App. It holds three things:

1. **How my own second brain works.** Two vaults with opposite owners, 330+ cited source summaries, and one rule: the agent never writes the part of the brain that is me. → [docs/my-second-brain.md](docs/my-second-brain.md)
2. **What I know about teaching entrepreneurship.** Babson's five practices (play, empathy, creation, experimentation, reflection), the European Commission's EntreComp framework, and the work that took them into Costa Rica's public rural high schools. → [docs/teaching-entrepreneurship.md](docs/teaching-entrepreneurship.md) · [docs/entrecomp.md](docs/entrecomp.md)
3. **A working student version.** A vault template, an agent contract, nine agent skills, and a dashboard that catches "200 notes and zero opinions" while it is still 20 notes. → [docs/design.md](docs/design.md) · [template/](template/) · [examples/valentina/](examples/valentina/)

## Why I believe it works

![38 times: from ₡10,000 to ₡380,000 in nine months](docs/img/caldosa-38x.svg)

In 2019, ten 16-year-olds at a public rural high school near the Panama border put in ₡1,000 each, made and sold *caldosa de montaña* — fried plantains with shredded beef on top — at school and then in their community, ran two bingos, and turned ₡10,000 into ₡380,000 in nine months. Their teacher followed the project-based guide I helped bring to Costa Rica's rural high schools. With very little intervention and some guidance, kids can do anything. → [The full case](docs/case-caldosa-de-montana.md)

## The idea in 30 seconds

```
positions   what I believe and would defend      ← the student writes
insights    what I figured out                    ← the student writes
facts       what is known, with sources           ← the agent keeps
```

- **Two owners.** `library/` is the agent's: facts, each with a source. `mind/` is the student's: insights, positions, and their practice. The agent reads `mind/` and never writes in it; a lint check enforces it.
- **Five practices to climb with.** Play (curiosities, quests, *hypotheses*), empathy (interviews), creation (posts, prototypes), experimentation (cheap tests of positions), reflection (weekly, in the student's words).
- **A dashboard that names the next step**: topics with facts and no stance, insights that connect nothing, positions that can't be wrong, positions never tested, hypotheses past their check date, practices left unused. Evidence for 15 EntreComp competences. Never a score.

## Try it

No dependencies. Python 3.9 or newer.

```bash
python3 scripts/expertise.py dashboard examples/valentina --today 2026-10-03 --stdout
python3 scripts/expertise.py lint examples/valentina
python3 -m unittest discover -s tests
```

Start a vault: copy `template/` somewhere, open it with Claude Code or Codex, and say **"Let's start."** The agent reads `AGENTS.md` and runs the `start` skill. Copy `scripts/expertise.py` next to it to run the dashboard.

## What the dashboard tells Valentina

Valentina is a fictional 15-year-old in Tamarindo, Costa Rica, learning surfboard repair for surf schools ([her vault](examples/valentina/)). Her library facts cite real sources; her interviews and experiment are invented. On 2026-10-03 her dashboard says:

> - **Reflection** — Insight [[clark-foam-shows-supplier-risk]] links 1 thing(s) you know. An insight connects at least 2: which facts made you see it?
> - **Reflection** — Position [[most-repair-mistakes-are-wrong-resin]] has no answer to *What would change my mind?* A position you can't lose isn't a position yet.
> - **Experimentation** — Position [[most-repair-mistakes-are-wrong-resin]] is 25 days old and has never been tested. Design the cheapest test that could prove it wrong.
> - **Experimentation** — Hypothesis [[hypothesis-half-of-rental-boards-are-epoxy]] was due to be checked on 2026-09-28. Was it supported? Set `result:` and say what you learned.
> - **Play** — No play in the last 14 days. Go exploring: follow one curiosity with no goal, or write a hypothesis before you read the answer.

Her other position — *surf schools lose more money to boards waiting for repair than to the damage itself* — has an interview behind it, a hypothesis that was supported, a 48-hour repair pilot that tested it, and a written answer to what would change her mind.

## Repo map

| Path | What it is |
|---|---|
| `docs/` | My system, my teaching background, the caldosa de montaña case, EntreComp, and the product design |
| `template/` | A student's vault: `AGENTS.md` (the agent contract), `library/`, `mind/`, note templates, nine skills |
| `scripts/expertise.py` | Dashboard and lint (standard-library Python) |
| `tests/` | Unit tests for the script |
| `examples/valentina/` | A worked example vault, with its generated dashboard |
| `data/entrecomp-learning-outcomes.csv` | EntreComp's 442 learning outcomes, one row each (© European Union, 2016; reproduction authorised with acknowledgement) |

## About me

Daniel Carranza, Costa Rica. I build agent systems that run real operations: my own businesses' administration, a nonprofit's content and donation platform, accounting workflows. I run my own work and thinking on the two-vault second brain described here. Before that, I brought Babson's entrepreneurship method into a Costa Rican school, trained thousands of teachers, and created guides for the country's public rural high schools, where 12,000 students use them every year.

## Sources

Neck, Greene and Brush, *Teaching Entrepreneurship: A Practice-Based Approach* (Edward Elgar, 2014; Volume Two, 2021). Bacigalupo, Kampylis, Punie and Van den Brande, *EntreComp: The Entrepreneurship Competence Framework* (Joint Research Centre, 2016). Ministerio de Educación Pública de Costa Rica, *Guía didáctica para el área socio productiva de los liceos rurales* (2021). Full citations are in each document.

## License

- **Code** (`scripts/`, `tests/`, `template/`): [MIT](LICENSE).
- **Docs, the case and the images** (`docs/`, `examples/`, this README): [CC BY 4.0](LICENSE-docs.md). Use and adapt them freely, including commercially; credit Daniel Carranza and link here.
- **Third-party material keeps its own terms:** EntreComp's tables and learning outcomes © European Union, 2016, reproduction authorised with acknowledgement; quotations from Neck, Greene and Brush and from the Ministry of Public Education's guides are short, cited quotations.
