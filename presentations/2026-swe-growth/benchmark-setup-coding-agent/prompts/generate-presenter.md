# Prompt for the presenter deck

## Instructions for NotebookLM

Create a **Presenter Slides** deck for this talk:

**Benchmarking My Coding Agent Setup: One Engineer, Many Agents**

Build it from `sources/outlines/presenter.md`. That file is the v4 outline, with 73 slides. Use its slide order, its headlines and its numbering. Do not add slides and do not drop any.

### Settings
- **Format**: Presenter Slides.
- **Language**: English. Every slide, every label, every speaker note.
- **Length**: 73 slides.

### Who the slides are for
The slides speak to the people on Zoom. They are mixed Indonesian developers, and many read English as a second language. Use plain words and short sentences. The speaker is Zahid.

---

## The claim
"The model is a swappable part. What lets one engineer ship from a phone is the setup around it: skills, proof, coordination, and guardrails."

Say it near the start (slide 4) and again at the close (slide 71), in the same words.

## The five principles
Use these names word for word. Each one is the principle slide of one part of the talk.

1. Measure it on your own work
2. Do it twice, make it a skill
3. One writer per branch
4. Show proof, not "done"
5. Make it safe to walk away

## The six rules

1. **One audience.** Every slide talks to the people on Zoom. Sources, dates, caveats, timing and chat cues go to the speaker notes.
2. **No source lines.** A quote carries the speaker's name next to it, for example "Can Bölük, omp author". There is one Links slide near the end for anyone who wants to dig.
3. **Headlines in Zahid's words.** About 10 words, never more than 12. Plain English. No bench jargon.
4. **One picture per slide.** A screenshot, one or two big numbers, or a simple diagram. At most about 25 words on the slide face besides the headline, never more than 30. The one exception is the map slide (slide 6), which may carry about 60 words.
5. **One story per section.** Each part runs in this order: divider, story, principle, proof, then one thing to try.
6. **Clean faces.** The slide face never shows a source line, a file path, an internal date, a minute count, a chat cue such as "Ask chat", or the words arm, median, API-equivalent, head-to-head or n/a. A time is allowed only when it is part of the story, like "9:29". Write "steps", not "turns". Where a dollar figure appears, write "if I paid per token".

## Section shape

| Slide type | What it carries |
|---|---|
| Divider | "Part N" and the part name from the `MAP` list, not the principle name. One chat question for the audience, for example "Per token or per subscription? Tell us in chat." No minutes. A small seven-segment map strip at the bottom, with the current segment in the accent colour and a "you are here" label. |
| Story | One or two slides about a real moment. The number comes after the story. |
| Principle | The principle name, large, with at most one plain line under it. |
| Proof | One to eight slides, one idea and one picture each. Part 1 has eight. |
| Try this | One line the audience can do this week. |

Part topics: Part 1 "Choosing models and paying for them". Part 2 "Teaching the agent". Part 3 "Many agents at once". Part 4 "Trusting the result". Part 5 "Running it safely". After Part 5 comes a sixth divider, "What is still hard" (slide 65), drawn the same way as the Part dividers, with the chat question "What still breaks for you? Tell us in chat." It has no principle slide.

The map. Slide 6 has the headline "Today we go from my first tool to what is still hard." and seven rows, one per section, each a name and a short line: My journey (The tools I tried, and why I left), 1 Choosing models and paying for them (Which model, and what it costs), 2 Teaching the agent (Skills, memory, and plans), 3 Many agents at once (One coordinator, many workers), 4 Trusting the result (Checks before I merge), 5 Running it safely (Servers, secrets, production), What is still hard (What I have not solved yet). The map names no principle, because the audience has not heard them yet. The strip on every divider is the same seven rows, drawn small, and the divider titles are the same names. Draw all three from one list (`MAP`). Question numbers and organizer-facing words such as "your questions" never appear on a slide face or in a `Say:` line.

## Face and notes

Each numbered slide in `presenter.md` has a headline, a `Say:` block and an `Evidence:` block.

- **On the slide face:** only the headline and one visual, with the few words the visual needs. Take the visual from the headline and from the `Evidence:` block, for example the bars, the numbers or the screenshot it names.
- **In the speaker notes:** copy the `Say:` text. Then add the `Evidence:` text, the `Delivery:` text and the `Chat:` text, so that Zahid has the sources, run counts, dates, file paths and caveats in front of him and not on screen.
- If a slide has a digit on its face, its notes must have an `Evidence:` part.

## Slide-specific notes
- Slide 2 is the real phone screenshot. Slide 3 is a four-point timeline of PR #804. Slide 5 is Can Bölük's article quote: "I improved 15 LLMs at coding in one afternoon. Only the harness changed." Slide 6 is the map.
- Slide 7 is a six-event timeline with no date scale, in this order: 2022 VS Code and Copilot at launch, 2025 Claude Code in VS Code, July 2025 Gemini tooling, October 2025 OpenCode (OmO) token hungry, December 2025 Ghostty with Neovim and Amp lighter, February 2026 omp extensible (highlighted). Do not draw bars to a date scale and do not reorder the events. Slide 8 is two cards, "VS Code" (muted) and "Terminal" (highlighted), under the headline about running agents in parallel.
- Slide 9 is Antigravity, four cards: plan mode, memory, design artifacts, agent-first screen. Slide 12 is a bar chart of requests per month. Slide 15 shows seconds on the UI task, with DeepSeek highlighted and "118 tokens/s on paper" beside it.
- Slide 24 is three money tips. Slide 29 is PARA, four boxes with Areas highlighted and leading to "14 area skills". Slide 34 is two cards, "Always on" and "On a trigger" (highlighted), with a caption about 4,635 rule injections since June. Slide 36 is a newly drawn neutral wireframe plus a strip of three steps: screen, files, data. Do not draw real app screens or names. Slide 40 is two big numbers (39% of working hours with 4 to 9 agents, 3 agents in a typical hour) and ten bars of hours per agent count, 1 to 9 and 10+, with the bar for 4 highlighted. Slide 52 is a five-step ladder of checks. Slide 59 is three pairs, accident and guardrail.
- Slide 67 is two big numbers, 538 CI runs in one day and 1 in 10 runs took 16 minutes or more. Slide 69 is three big numbers, 89% of a 1 TB SSD used, 447 GB of Docker images, volumes and build cache, and 38 GB for one uncapped test run (muted). Slide 70 is a four-step flow with step 2 highlighted, and it is a plan, not a result.
- Slide 72 is the only slide with links. Put every link from its `Evidence:` block on it and add no others.
- Slide 73 is questions.
- Define each term on the slide where it first appears, in plain words. There is no glossary slide.

## Boundaries
- Use only numbers, quotes and links that appear in `presenter.md` or in `sources/references/`. Never invent one.
- No customer company names. Write "a food-manufacturing customer" or "a pilot customer" if one must be mentioned.
- No secrets, tokens, passwords, IP addresses, email addresses or phone numbers, even partial ones.
- Teammates are "QA", not names.
- Keep the real screenshots as they are, with their blurs.
- Plain, calm, practical tone. No hype, no marketing words, no long dashes. Sentence-case headings.
- Do not state an item marked `[UNVERIFIED]` or `[INFERENCE]` in a source as fact.
- Do not invent commands. There is no command named "poteto validate".

---

## Source priority
1. `sources/outlines/presenter.md`: the slide-by-slide outline and the speaker notes. This decides the slides.
2. `sources/context/brief.md`: audience, goal and tone.
3. `sources/context/structure.md`: the story for each part.
4. `sources/references/referensi-benchmark-lab.md`: Part 1 facts.
5. `sources/references/referensi-evolusi-biaya-plugin.md`: journey, plugins, model roles, cost, memory.
6. `sources/references/referensi-mesh-koordinator-mobile.md`: mesh, coordinator, PR #804.
7. `sources/references/referensi-skills-prompt-dan-config.md`: skills, instructions, principles.
8. `sources/references/referensi-pr-proof-security-prod.md`: PR standard, proof, secrets, production.
9. `sources/references/referensi-setup-dan-infra.md`: setup, worktrees, machines.
10. `sources/references/screenshot-omp-mobile-0929.png`: the phone screenshot for slide 2.

## Special notes
- The live demo starts at slide 13 and is checked at slide 54. Never name the recorded backup on a slide.
- Obfuscation is not secret management. Slide 60 says so in plain words.
- Mesh is Zahid's own plugin. The poteto skill set is ported to omp by him.
