# Prompt for the detailed deck

## Instructions for NotebookLM

Create a **Detailed Slides** deck for this talk:

**Benchmarking My Coding Agent Setup: One Engineer, Many Agents**

Build it from `sources/outlines/detailed.md`. That file is the v4 outline for a self-reading deck, with 47 slides. Use its slide order and headlines.

### Settings
- **Format**: Detailed Slides. Someone who was not at the talk can read it alone.
- **Language**: English.
- **Length**: 47 slides.

### Who the slides are for
People who read the deck after the talk, on their own. Many read English as a second language, so use plain words and short sentences. The speaker is Zahid.

---

## The claim
"The model is a swappable part. What lets one engineer ship from a phone is the setup around it: skills, proof, coordination, and guardrails."

Say it on slide 3 and again on slide 46, in the same words.

## The five principles
Use these names word for word. Each one is the principle slide of one part.

1. Measure it on your own work
2. Do it twice, make it a skill
3. One writer per branch
4. Show proof, not "done"
5. Make it safe to walk away

## Structure
Each part tells one story, then names the principle, then shows the proof, then gives one thing to try. The order is story, principle, proof, try this. The part topics are "Choosing models and paying for them", "Teaching the agent", "Many agents at once", "Trusting the result" and "Running it safely". This deck has no divider slides. Slide 5 has the headline "Today we go from my first tool to what is still hard." It is a seven-row map of the talk (My journey, the five parts, and What is still hard), each row a name and a short line, with no principle names. Organizer-facing words such as "your questions" never appear on a slide face.

## Rules for this deck

1. **More words than the live deck, but a cap.** A headline of at most 12 words, in plain English. About 50 words on the slide face besides the headline, never more than 60. The map slide (slide 5) may carry about 60. Short sentences. One idea and one picture per slide.
2. **Clean faces.** The slide face never shows a file path, a command-line flag, an internal date such as 2026-11-05, a minute count, a chat cue, or the words arm, median, API-equivalent, head-to-head or n/a. A time is allowed only when it is part of the story, like "9:29". A month name is fine when the month is the subject, like "October". Write "steps", not "turns".
3. **Dollar figures.** Write "if I paid per token" next to every dollar figure from the usage stats. It is the list price of the tokens, not money paid. State real spend separately, in the same slide when it fits: about $200 in October, usually about $100 a month.
4. **No footers and no source lines.** Put references in one place. The last slide, "Links", lists the public links from `sources/outlines/detailed.md` and no others.
5. **Credits only next to a quote.** For example "Can Bölük, omp author".
6. **Define terms where they first appear.** Harness, skill, worktree, mesh, compaction. There is no glossary slide.
7. **Facts behind a slide.** The outline lists "Facts behind it" for some slides. Use them as extra lines on the face if they fit the word cap. Otherwise put them in the speaker notes.

## Boundaries
- Use only numbers, quotes and links that appear in `sources/outlines/detailed.md`, `sources/outlines/presenter.md` or `sources/references/`. Never invent one.
- Quotes are verbatim, typos kept.
- No customer company names. Write "a food-manufacturing customer" or "a pilot customer" if one must be mentioned.
- No secrets, tokens, passwords, IP addresses, email addresses or phone numbers.
- Subscription history. GLM Max was Zahid's own plan. Codex Pro came from the office. Devin Pro and OpenCode Go were his own. Do not state account counts of other people or quota percentages.
- Teammates are "QA", not names.
- Keep the real screenshots as they are, with their blurs.
- Plain, calm, practical tone. No hype, no marketing words, no long dashes. Sentence-case headings.
- Do not state an item marked `[UNVERIFIED]` or `[INFERENCE]` in a source as fact.
- No command called "poteto validate" exists. Proof is the "Prove It Works" principle, the PR body shape and a check that fails on the old code and passes on the new.

---

## Source priority
1. `sources/outlines/detailed.md`: the slide-by-slide outline. This decides the slides.
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
- The phone story: Zahid was on board a plane before takeoff and fixed a bug from the Tern Android app.
- Obfuscation is not secret management. Slide 42 says so in plain words.
- Mesh is Zahid's own plugin. The poteto skill set is ported to omp by him, and "check every layer" is his own principle.
- The close is the five principles and the claim, then the Links slide.
