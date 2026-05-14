---
name: slide-deck
description: "Use this skill whenever the user asks for a slide deck, presentation, slides, deck, talk outline, or webinar content. Produces a clean MARKDOWN slide deck (NOT HTML) — one slide per H2 heading, with speaker notes inline. Use when the deliverable is a multi-slide presentation (3+ slides), the user mentions a target audience or duration, or asks for a structured talk. Do NOT trigger for single-page summaries, prose documents, or one-off paragraphs. Output is markdown only — never HTML, never CSS, never JavaScript."
allowed-tools: write_file, edit_file, read_file, ls
---

# Slide-Deck Builder

## Output format — read this first

**The output is ONE markdown file (`.md`).** Never HTML, never a CSS stylesheet, never a slide-rendering framework. Each slide is a markdown H2 heading. The total file should be **under 2,000 words** — short slides are better slides.

## Overview

Build a markdown slide deck (`.md` file in the virtual filesystem) from a research brief, topic, or outline. One H2 heading per slide. Speaker notes go in a blockquote under each slide.

## Standard Operating Procedure

1. **Clarify scope** if missing: target audience, duration (minutes), tone (technical / executive / educational), preferred slide count.
2. **Draft an outline** — list every slide title before writing content. Stop and confirm with the user if scope is >12 slides or the topic is ambiguous.
3. **Write each slide** using the template below. Keep slide bodies to ≤5 bullet points or 1 diagram description. The audience reads slides in <30 seconds.
4. **Add speaker notes** under each slide as a `> Speaker notes:` blockquote — 2–4 sentences max, the *why* not the *what*.
5. **Save** the deck to a single file: `./<topic_slug>_slides.md`. Use `write_file`.
6. **Print a summary** — total slide count, estimated duration (90s per slide), and the path to the saved file.

## Slide template

```markdown
## Slide N — Title

- Bullet 1 (≤12 words)
- Bullet 2
- Bullet 3

> Speaker notes: 2-4 sentences explaining the why and the transition to the next slide.
```

## Style rules

- **Slide titles** are concrete claims, not topics. ✅ "Skills compose under one supervisor" · ❌ "Skills"
- **No walls of text.** If a bullet runs >12 words, split it or move detail to speaker notes.
- **One idea per slide.** If you're tempted to add a third subsection, that's a new slide.
- **Open and close strong.** Slide 1 is the hook (claim or stat). Final slide is the call-to-action.
- **Include a slide number** in each H2: `## Slide 3 — ...` so the user can quickly reference any slide.

## When to ask vs. when to act

- **Just do it** if the user gave a topic, audience, and duration.
- **Ask once** if any of those three are missing — but only the missing piece.
- **Don't ask** about colors, fonts, or rendering — this skill outputs markdown only.

## Output check before yielding

- [ ] Every slide has an H2 title with a slide number
- [ ] Every slide has speaker notes
- [ ] The file is saved
- [ ] You printed the file path and slide count
