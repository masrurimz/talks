# AGENTS.md — AI Assistant Context

This file provides context for AI assistants (Claude, etc.) working in this repository.

## Repository purpose

Personal repository for slide decks and presentation materials. Uses NotebookLM workflow for generating presentations from structured sources.

## Workflow

```
brainstorm → sources → NotebookLM → output
```

### 1. Brainstorm phase
- Discuss topic, audience, goals with user
- Identify key themes, data points, examples
- Decide on presentation format (presenter vs detailed)

### 2. Generate sources
Create files in `presentations/YYYY-event-series/presentation-title/sources/`:

```
sources/
├── context/
│   ├── brief.md        # Speaker identity, audience profile, goals
│   └── structure.md    # Narrative arc, key sections, focus areas
├── outlines/
│   ├── presenter.md    # Slide outline (presenter style)
│   └── detailed.md     # Slide outline (detailed style)
└── references/
│   ├── *.md            # Research materials, data, readings
│   └── *.pdf           # Optional: PDF sources
```

### 3. Generate prompts
Create files in `presentations/YYYY-event-series/presentation-title/prompts/`:

```
prompts/
├── generate-presenter.md   # Prompt for presenter deck
├── generate-detailed.md    # Prompt for detailed deck
└── revise.md               # Prompt for revision
```

### 4. NotebookLM usage
User uploads `sources/` files to NotebookLM, then pastes prompts to generate slides.

AI assistant does NOT interact with NotebookLM directly — we prepare the materials.

### 5. Output
Generated slides saved to `presentations/YYYY-event-series/presentation-title/output/`.

## File naming conventions

| Type | Pattern | Example |
|------|---------|---------|
| Event series folder (Level 1) | `YYYY-event-series` | `2026-halal-bihalal-alkhidmah-pt` |
| Presentation folder (Level 2) | `presentation-title` | `kolaborasi-lembaga-pendidikan` |
| Context files | `brief.md`, `structure.md` | Fixed names |
| Outline files | `presenter.md`, `detailed.md` | Fixed names |
| Reference files | Descriptive | `bahan-bacaan.md`, `data-statistik.md` |
| Prompt files | `generate-*.md`, `revise.md` | Fixed names |

## Content guidelines

### brief.md structure
- Event context (name, theme, format)
- Speaker identity and positioning
- Focus areas with priority order
- Audience profile (demographics, characteristics)
- Expected outcomes

### structure.md structure
- Narrative arc (section sequence)
- Key themes per section
- Content boundaries (what to include/exclude)
- Transition points

### outlines structure
- Slide-by-slide breakdown
- Each slide: title, key points, visual hints
- Labels: `[Wajib]` / `[Opsional]`
- Timing hints if needed

### prompts structure
- Clear instructions for NotebookLM
- Specify: format, language, length
- Include: focus areas, boundaries, style
- Reference: which source files to prioritize

## Language

Default language for presentations: **Indonesian** (Bahasa Indonesia)

Prompt files should be in Indonesian when the target presentation is in Indonesian.

## What AI assistant should do

When user asks to create a new presentation:

1. **Ask clarifying questions**: event, audience, duration, focus
2. **Create folder structure**: copy template, rename
3. **Generate sources**: write brief, structure, outlines, references
4. **Generate prompts**: write appropriate prompts for NotebookLM
5. **Explain workflow**: remind user how to use with NotebookLM

When user asks to revise existing presentation:

1. **Read existing sources and prompts**
2. **Understand what needs change**
3. **Update relevant files**
4. **Suggest new prompt if needed**

## What AI assistant should NOT do

- Do NOT run NotebookLM directly
- Do NOT generate final slides (user does that via NotebookLM)
- Do NOT skip the brainstorm phase
- Do NOT create presentations without proper context files

## Template location

`presentations/_template/` — copy this folder for new presentations.

## Git workflow

- Commit after each major phase (sources done, prompts done)
- User handles pushing to remote