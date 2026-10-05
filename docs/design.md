# Designing the student version

## The problem, in Founders School's words

> "Three students can't tell the difference between an insight and a position, and the app isn't helping."
>
> "A student's graph has 200 notes and zero opinions."

Collecting feels like learning. Capture tools make it free, and AI makes it instant. So the failure mode of an expertise app is not an empty graph. It is a full graph with nobody home.

My own vault has the same risk at a larger scale: 332 source summaries written by an agent. What protects it is a structural rule, not willpower: **the agent keeps the facts, and only I write positions.** The student version starts there.

## The design in one picture

```
                 ┌───────────────────────── mind/ (only the student writes) ──────────┐
   positions     │  what I believe and would defend · what would change my mind      │
   insights      │  what I figured out, connecting two or more things I know         │
                 └───────────────▲──────────────────────────────▲─────────────────────┘
                                 │ reflection                   │ experimentation
   practice      play · empathy · creation · experimentation · reflection   (mind/practice/)
                                 │                              │
                 ┌───────────────┴────── library/ (the agent writes) ───────────────────┐
   facts         │  sources with cited facts · topics · people in the domain           │
                 └─────────────────────────────────────────────────────────────────────┘
```

Three layers, two owners, five practices to climb with. The layers are Founders School's own words for the Expertise App: "a layered knowledge graph of facts, insights, and spiky points of view".

## Rules the product enforces

1. **Ownership.** The agent never writes in `mind/`. Notes say who wrote them (`written_by:`), and the lint fails if the agent wrote there. Without this rule, an AI tool turns students into editors of the AI's opinions.
2. **Citations.** A fact without a source is not a fact; it goes to open questions.
3. **Guess first.** Before the agent answers a factual question, it asks for a guess and a confidence. Guessing before learning helps memory, even when the guess is wrong (the pretesting effect; Richland, Kornell and Kao, 2009, *Journal of Experimental Psychology: Applied* 15(3)), and it builds the habit of committing to a view.
4. **Never pick their position.** The agent argues, asks what would change their mind, shows the best evidence against. Then it steps back.
5. **One next step.** Every session ends with one suggestion, not a to-do list.

## The five practices, as features

The practices come from Babson College's practice-based approach to teaching entrepreneurship (Neck, Greene and Brush). What a structure plus a little guidance can do with teenagers: [the caldosa de montaña case](case-caldosa-de-montana.md). I have worked with them since 2018 with teachers and students in Costa Rica ([background](teaching-entrepreneurship.md)). Founders School owns its pedagogy; this shows how a pedagogy becomes product.

| Practice | What the student does | What the agent does | What the dashboard watches |
|---|---|---|---|
| **Play** | Follows curiosities, runs 15-minute quests, writes **hypotheses** (guesses with a date to check them) | Offers quests; makes guessing safe; files what quests find | Hypotheses past their check date; topics with many facts and no hypothesis |
| **Empathy** | Interviews people who live inside the domain; observes | Prepares questions about past behavior; files the facts with the interview as the source | Days since the last conversation with a real person |
| **Creation** | Makes something from a position: a post, a video, a prototype | Helps build (AI-assisted building is welcome); the claim stays the student's | Creations that express no position |
| **Experimentation** | Tests a hypothesis or a position, cheaply, this week | Designs the cheapest test that could prove it wrong; files the result as a source | Positions older than three weeks that have never been tested |
| **Reflection** | Writes a weekly reflection; promotes insights to positions | Asks the questions, never writes the answers; flags gaps | Insights that connect fewer than two things; positions with no "what would change my mind" |

Two design choices do most of the work against "200 notes and zero opinions":

- **Hypotheses make opinions cheap and early.** A hypothesis is a position with training wheels: a guess, a confidence and a date to check it. Students make dozens before they write their first real position, so by the time they write one, they have practiced being wrong in public at no cost.
- **"What would change my mind" makes positions honest.** It separates an insight ("I noticed X") from a position ("I believe X, and here is what would make me drop it"). The lint requires the section; the agent's sparring uses it.

## The nudge engine

`scripts/expertise.py dashboard` turns the vault into a short list of next steps. Current rules (thresholds are deliberately low, so nudges come early):

| Pattern | Nudge |
|---|---|
| A topic with ≥ 3 sources and no position | "Write a hypothesis: what do you think is true here that most people would disagree with?" |
| An insight linked to fewer than 2 things the student knows | "Which facts made you see it?" |
| A position without "What would change my mind" | "A position you can't lose isn't a position yet." |
| A position older than 21 days, never tested | "Design the cheapest test that could prove it wrong." |
| A hypothesis past its check date, result still open | "Was it supported? Say what you learned." |
| A practice unused for 14 days | A practice-specific suggestion (for example, "Talk to someone who lives this problem.") |

It also shows the ladder per topic and the EntreComp competences the student's own work gives evidence of. It never shows a score.

## How I would know it works

Founders School's three tests are expertise, shipping speed, and voluntary use. Measures I would put in front of the team from week one:

- **The climb:** facts per position, per student, per month (should fall); the share of topics with at least one position (should rise).
- **Contact with reality:** the share of positions tested at least once; the share of hypotheses checked by their date.
- **Practice balance:** students with no empathy in 14 days (this is where I'd expect the biggest drop-off, because talking to strangers is hard).
- **Voluntary use:** sessions a student starts outside assigned time; days with any capture.
- **Proof of expertise:** creations that link to a tested position; a guide's blind rating of a student's best position against an adult practitioner's view.

## The first two weeks, if I got the job

1. **Watch first.** Sit with students; no changes for three days. Note where each one stops: no topic, no hypothesis, no position, no test.
2. **Instrument.** Get the five measures above into a weekly view (the dashboard already computes most of them per student).
3. **Ship one change a week** at the stall point that hits the most students. My first guess is hypotheses: they are the cheapest bridge from facts to opinions. The second is a worked example of an insight next to a position, built into the reflection flow.
4. **Cut what no one uses.** Every Friday, one feature out for every feature in.

## What I don't know yet

- How Founders School's own method defines an insight and a position. The mechanism here (ownership + ladder + practices + nudges) works with any definition; the words would change.
- Whether 14-year-olds will write weekly reflections without a guide prompting them. If not, the agent's reflection interview may need to happen out loud (voice), with the student writing only the last answer.
- How the vault should connect to the rest of their software, so that expertise flows into "the content they post and the business they build". `creation/` notes with `expresses:` links are the hook.
