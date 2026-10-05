---
name: start
description: Onboard a new student: find a focus area through play, not a form; set up the first topic and the first hypothesis.
---

# Skill: start

Run when the student says "let's start", or when `mind/` is empty.

1. Ask three playful questions, one at a time, and listen:
   - "What could you talk about for an hour without getting bored?"
   - "What have you noticed that most people around you haven't?"
   - "If you could fix one annoying thing this year, what would it be?"
2. Offer two or three candidate focus areas, each narrow enough that a teenager could know it better than most adults within a year ("surfboard repair for surf schools in Guanacaste", not "the ocean"). The student picks. Never pick for them.
3. Run one quest on the chosen area (`skills/play`).
4. Ask for the first hypothesis before anything is read: "What do you think is true about this that most people get wrong?" Show `templates/hypothesis.md`; the student writes it in `mind/practice/play/`.
5. Create the first topic page in `library/topics/` and file the first one or two sources the quest found (`skills/ingest`).
6. Run `python3 scripts/expertise.py dashboard .` and name one next step.
