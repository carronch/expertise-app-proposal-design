# My second brain: two vaults, opposite owners

I run my work and my thinking on two Obsidian vaults and a set of AI agents. The design has one rule that everything else follows from: **the agent never writes the part of the brain that is actually me.**

## The idea

| | **MainVault** — me | **LLMVault** — the agent's |
|---|---|---|
| Holds | beliefs, principles, life decisions, the people I care about, a monthly "heartbeat" check-in, my own notes | every source I capture, a summary of each, research themes, concepts, thinkers, tools, projects, plans |
| Who writes | only me | agents, all day |
| Agents may | read and quote it, verbatim | read and write it |
| When the two disagree | MainVault wins | the agent's page gets corrected |

The agent is a librarian and an analyst. It finds, files, cites, connects and maintains. I decide what I believe. When a new source contradicts something I wrote in MainVault, the agent does not edit either side: it records the tension and stages a proposed change for me to accept or reject.

## What is in it (counted on 2026-10-03)

- **LLMVault:** 574 raw sources, 332 source summaries, 40 research themes, 25 concepts, 23 thinkers broken into 1,520 "frames" (one idea each), 77 tool pages, 148 work cards, and an append-only log of every ingest.
- **MainVault:** 22 beliefs, 14 principles, 14 life decisions, 19 people, monthly heartbeats.
- **A shared kit** of 46 agent skills (ingest, research, query, lint, a "board" of thinkers that argues a decision, accounting, deploys) used by Claude Code, Codex and Cursor through one `AGENTS.md` per folder.
- **Local search** (qmd: keyword + vector + rerank) over about 4,000 files. Agents search both vaults before they claim anything.

## Why it works

Personal knowledge systems have had the right ideas for 80 years — associative trails, atomic notes, links with reasons. They failed because **maintenance cost grew faster than value**: people get bored, links rot, contradictions pile up. An LLM changes the maintainer, not the idea. These are the rules that make that safe.

1. **Ownership by layer.** Facts and syntheses belong to the agent; positions belong to me. That split is what keeps 300+ summaries from drowning out what I actually think, and what makes the agent's work safe to accept quickly.
2. **Every claim cites a source.** A summary line without `[Source: …]` gets flagged by the monthly lint. An agent that only read an abstract has to say so.
3. **One home per fact.** How a system works lives on its tool page; a card holds the plan and a dated timeline and links to the page. When a fact changes, its home changes first. (Copies of the same fact in five to eight places once cost about 150 agent tool calls in five sessions, and gave me wrong answers.)
4. **Compiled truth on top, timeline below.** Each page starts with the current best understanding and ends with append-only dated evidence. You can trust the top and audit the bottom.
5. **Search before you claim.** Before an agent writes a page or says "that doesn't exist", it searches both vaults with aliases. Search takes under a second; a wrong "doesn't exist" costs a duplicate page.
6. **A resolver decides where things go.** A short decision tree, first match wins, so every subject has exactly one page.
7. **Derived files are rebuilt, never edited.** The index, the link graph and dashboards come from scripts. If one is wrong, fix the source or the script.
8. **The wiki is the queue.** Plans are cards with a status; my kanban board just reads the files. A session that moves a card must write a dated timeline line before it ends; a hook checks.

## How I use it, in a normal week

- **Capture, all week.** X bookmarks are pulled by a command-line tool into an inbox; web pages come in through a clipper; phone notes land in the same inbox. Nothing is processed until I confirm.
- **Ingest.** For each capture the agent saves the raw source, writes a cited summary, links it into a theme, checks it against MainVault, logs it, and moves the capture to a processed folder (the audit trail). This job posting reached me exactly that way: three bookmarks of one thread, filed as one source, with the posting saved verbatim.
- **Ask.** "What do we know about X?" gets an answer that cites both vaults and quotes me where I've written on it.
- **Decide.** For a big choice, a skill convenes a board of thinkers whose ideas the vault already holds, and writes a memo. The decision is still mine.
- **Plan and run.** Approved plans become cards. Every session that advances work updates the card.
- **Maintain.** A monthly lint finds broken links, orphans, claims without sources and themes without "a reading in my own voice". A nightly sweep only *proposes* fixes. A monthly heartbeat and a yearly "soul audit" are interviews: the agent asks, I write.

## What broke, and what I changed

The system is good because it keeps getting corrected. Some of the corrections:

- **An agent said pages didn't exist without searching** (May 2026). Rule 5 came from that.
- **161 broken links** from references written in the wrong format (July 2026). Now a lint hook blocks the format at write time.
- **"19 failures" in a nightly evaluation** were mostly tests that never ran: the laptop was asleep and the budget ran out. Now the first check for mass failures is whether the machine slept, and "done" has to come with evidence that the work ran.
- **A sync overwrote newer pages** with an older copy from another Mac, because one vault window was closed (October 2026). Now a check runs at the start of every session and warns before anything is edited.
- **Today, while preparing this application,** the agent found my own 2021 teaching guides and saw that they say "more than 11,000 students" where I had said 12,000. It recorded both, with sources, and asked me, instead of overwriting either. That is the system doing its job.

## What carries over to a 14-year-old

Not the folder names. The ownership split, the citations, the ladder from facts to positions, and an agent that asks better questions than it answers. [How I'd build it for students](design.md).
