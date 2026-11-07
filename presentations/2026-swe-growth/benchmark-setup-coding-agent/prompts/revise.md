# Prompt for revising a deck

## Instructions for NotebookLM

Revise the deck that was already generated for this talk:

**Benchmarking My Coding Agent Setup: One Engineer, Many Agents**

Make a light revision, not a rewrite. Keep the slide order and the headlines. Fix only what the checks below find. Keep the language English.

The presenter deck follows `sources/outlines/presenter.md` (73 slides). The detailed deck follows `sources/outlines/detailed.md` (47 slides).

### Checklist 1. The six rules

For each slide, check these. Fix a slide only where it fails.

1. **One audience.** The slide talks to the people watching. Sources, dates, caveats, timing and chat cues are in the speaker notes, not on the face.
2. **No source lines.** No "Source" line and no footer. A quote has the speaker's name next to it, for example "Can Bölük, omp author". All links sit on one Links slide near the end.
3. **Headlines in Zahid's words.** About 10 words, never more than 12. Plain English, with no bench jargon.
4. **One picture per slide.** One screenshot, one or two big numbers, or one simple diagram. Presenter deck: at most about 25 words on the face besides the headline, never more than 30. Detailed deck: about 50, never more than 60. The map slide (presenter slide 6, detailed slide 5) may carry about 60 in either deck.
5. **One story per section.** Each part runs divider, story, principle, proof, try this. The divider says "Part N" and the part name from the `MAP` list, with one chat question, no minutes and a seven-segment map strip at the bottom. The "What is still hard" divider follows the same shape and has no principle slide. The principle slide shows the principle name, large. The map slide names no principle and no organizer-facing words such as "your questions".
6. **Clean faces.** The face never shows a file path, an internal date such as 2026-11-05, a minute count, "Ask chat", or the words arm, median, API-equivalent, head-to-head or n/a. "Steps", not "turns". Every dollar figure says "if I paid per token". A time like "9:29" is fine when it is part of the story.

### Checklist 2. The five principles, word for word

1. Measure it on your own work
2. Do it twice, make it a skill
3. One writer per branch
4. Show proof, not "done"
5. Make it safe to walk away

Each principle is named once, on its own slide, and once more in the recap near the end.

### Checklist 3. The claim

The claim appears near the start and again at the close, word for word: "The model is a swappable part. What lets one engineer ship from a phone is the setup around it: skills, proof, coordination, and guardrails."

### Checklist 4. Fact check against the `Evidence:` lines

Open `sources/outlines/presenter.md`. Each slide has an `Evidence:` line. For every number, name, quote and claim on a slide, find it in that slide's `Evidence:` line or in `sources/references/`. Then check these points.

- Every number matches its source. If a number has no source, remove it and say which slide it was on.
- The bars on the benchmark slide show seconds on the UI task: Opus low 92, Sonnet medium 94, Haiku medium 170, DeepSeek flash low 476.
- Every dollar figure is the price if Zahid paid per token. It is not called spend, cost paid or savings. Real spend is stated separately: about $200 in October, usually about $100 a month.
- Prewalk is cheaper on Zahid's long tasks but slower, and the same or more on his short bench tasks. His first setup was Opus low into Haiku high (14 Oct). On 23 Oct he moved task agents to Sonnet medium without prewalk, because UI work needed a better model. Never write 'never cheaper'.
- Raising effort raised the step count in every pair he tested. The reason is worded as a guess.
- GLM Max is his own plan. Codex Pro came from the office. Neither is described the other way round.
- Mesh is his own plugin, not built into omp. Base-branch coordination is solved by mesh plus one coordinator agent, and is not listed as a problem.
- What is still hard is four problems and a plan. A clip cannot judge how a screen looks (UI still needs design skills and manual feedback). CI is now the queue (538 CI runs in one day, and 1 in 10 runs took 16 minutes or more). Setting up the environment and seed data for each worktree is slow (652 seconds to 171 seconds). The disk is full (89% of a 1 TB SSD, 447 GB in Docker, and one uncapped test run reached 38 GB of RAM, which is why the memory rule exists). The plan is a stack per VM that sleeps when idle and wakes when an agent needs it, and it is a plan, not a result. Base branches are not on the list. Part 3 shows them as solved.
- The tool journey order is VS Code and Copilot at its 2022 launch, Claude Code in VS Code, Gemini, OpenCode (OmO), Ghostty with Neovim and Amp, then omp. It is a timeline with no date scale. Running agents in parallel is the stated reason for leaving the editor, and it is not measured, so no memory number is quoted. Copilot came before Claude Code.
- On a busy hour, 4 to 9 agents work at once. 39% of working hours had 4 to 9 agents, and the typical hour had 3. A folder is a worktree or repo, so this counts workstreams, not processes.
- Rules step in when the agent types a risky command. 4,635 injections since June, of which 1,424 were the two memory caps. omp calls this TTSR.
- Model roles are chat Opus low, plan and hard bugs Opus high, UI design Sonnet high, review Opus medium, explore Haiku. Max is almost never used because it is slow and gave little gain. That more steps means a longer wait is an inference.
- The three accidents are a reset that wiped the shared dev database (the devkit now refuses such resets), a Docker prune that deleted about 244 unused volumes (Docker cleanup is banned for agents), and a masking tool that went through 11 reviews (reviews are capped at two rounds). The coordinator log has 353 decisions from 2 to 7 November.
- The five checks are, in order, language server on every edit, lint and types, tests shaped like the testing trophy, reviewer agents that scale with risk, and Zahid by hand.
- The wireframe on the spec slide is a neutral example, not one of Zahid's apps.
- The OpenCode reason is "token hungry, slow, and its tests did not catch much". It is not "accounts were banned". Only the Antigravity account ban is stated.
- Obfuscation is not called secret management. Production is read-only by default. Writes go dry run, backup, guarded apply, verify.
- Quotes are verbatim, typos kept.

### Checklist 5. Boundaries

- No customer company names. Use "a food-manufacturing customer" or "a pilot customer".
- No secrets, tokens, passwords, IP addresses, email addresses or phone numbers.
- Teammates are "QA".
- No claim from a `[UNVERIFIED]` or `[INFERENCE]` marker is stated as fact.
- No command called "poteto validate".
- No long dashes. Plain, calm tone. No hype.
- The real screenshots keep their blurs.

---

## Source priority for the revision
1. `sources/outlines/presenter.md` or `sources/outlines/detailed.md`: the slide-by-slide check, and the `Evidence:` lines.
2. `sources/context/brief.md`: audience and tone.
3. `sources/context/structure.md`: the story for each part.
4. `sources/references/referensi-benchmark-lab.md`: Part 1 facts.
5. `sources/references/referensi-evolusi-biaya-plugin.md`: journey, plugins, models, cost, memory.
6. `sources/references/referensi-mesh-koordinator-mobile.md`: mesh, coordinator, PR #804.
7. `sources/references/referensi-skills-prompt-dan-config.md`: skills, principles, prompting.
8. `sources/references/referensi-pr-proof-security-prod.md`: PR standard, secrets, production.
9. `sources/references/referensi-setup-dan-infra.md`: setup, worktrees, servers.

---

## Revision request template

Copy this block, fill the brackets, and paste it after the checklists when you want a targeted change.

```
Revise slide [number or title] of the [presenter or detailed] deck.

Problem: [what is wrong, in one sentence].
Change: [what the slide should say or show instead].
Evidence: [the outline slide or reference file that backs it].
Keep: [what must stay the same].
Do not: [anything to avoid].
```

Example.

```
Revise slide 22 of the presenter deck.

Problem: the cost slide shows $7.3k without saying "if I paid per token".
Change: write "$7.3k if I paid per token" and "about $200 paid".
Evidence: slide 22 Evidence line in sources/outlines/presenter.md.
Keep: the two big numbers.
Do not: add new numbers.
```

---

## Special notes
- Light revision only. Do not change the claim, the principle names, the section order or the slide count.
- If a check cannot be satisfied from the sources, leave the slide as it is and say which source is missing.
