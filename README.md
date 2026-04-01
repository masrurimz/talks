# Talks

Personal repository for slide decks and presentation materials.

## Workflow

```
brainstorm → sources → NotebookLM → output
```

### 1. Brainstorm
Discuss with AI assistant to clarify:
- Event context
- Audience profile
- Key themes and focus areas
- Narrative arc

### 2. Generate sources
AI assistant creates structured files for NotebookLM upload.

### 3. NotebookLM
Upload sources → paste prompts → generate slides.

### 4. Output
Save generated slides to output folder.

## Structure

```
presentations/
├── YYYY-event-series/                  # Level 1: Event grouping
│   ├── presentation-title/             # Level 2: Individual presentation
│   │   ├── sources/                    # Upload to NotebookLM
│   │   │   ├── context/                # Brief + structure
│   │   │   │   ├── brief.md
│   │   │   │   ├── structure.md
│   │   │   ├── outlines/               # Slide outlines
│   │   │   │   ├── presenter.md
│   │   │   │   ├── detailed.md
│   │   │   ├── references/             # Research materials
│   │   │   └── *.md, *.pdf
│   │   ├── prompts/                    # Paste into NotebookLM
│   │   │   ├── generate-presenter.md
│   │   │   ├── generate-detailed.md
│   │   │   └── revise.md
│   │   ├── output/                     # Generated slides
│   │   └── README.md
│   ├── README.md                       # Event series overview
│   └── ...                             # Other presentations in same event
├── _template/                          # Copy for new presentations
└── README.md

AGENTS.md                               # AI assistant context
```

## How to create a new presentation

### With AI assistant

1. Start conversation: "I want to create a presentation for [event]"
2. Brainstorm: answer clarifying questions about audience, focus, goals
3. AI generates: sources/, prompts/, README.md
4. You use: upload sources to NotebookLM, paste prompts
5. Save output: to output/ folder

### Manually

1. Copy `_template/` to appropriate location:
   - New event series → `presentations/YYYY-event-series/presentation-title/`
   - Existing event → `presentations/YYYY-event-series/presentation-title/`
2. Fill in `sources/context/brief.md` and `structure.md`
3. Create outlines in `sources/outlines/`
4. Add references in `sources/references/`
5. Write prompts in `prompts/`
6. Use with NotebookLM
7. Save results to `output/`

## Presentations

| Event Series | Presentation | Status |
|--------------|--------------|--------|
| 2026-halal-bihalal-alkhidmah-pt | kolaborasi-lembaga-pendidikan | Draft |
| 2026-halal-bihalal-alkhidmah-pt | pengembangan-pt | Draft |
| 2026-ramadhan-nuzulul-quran | digital-challenges | Draft |

## AI assistant context

See [AGENTS.md](AGENTS.md) for detailed workflow context for AI assistants.

## NotebookLM resources

- [Add sources to notebook](https://support.google.com/notebooklm/answer/16215270)
- [Generate slide deck](https://support.google.com/notebooklm/answer/16757456)
- [8 ways to make the most of Slide Decks](https://blog.google/innovation-and-ai/models-and-research/google-labs/8-ways-to-make-the-most-out-of-slide-decks-in-notebooklm/)