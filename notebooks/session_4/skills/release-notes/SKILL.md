---
name: release-notes
description: "Use this skill whenever the user asks for release notes, a changelog entry, a version summary, or a 'what shipped' post from a list of raw commit messages, PR titles, or change descriptions. Triggers on phrases like 'release notes', 'changelog', 'what's new', 'version notes', 'changes for vX.Y'. The deliverable is a single structured markdown document with Features / Fixes / Breaking sections. Do NOT trigger for code reviews, design docs, or freeform writing tasks."
allowed-tools: write_file, read_file, ls
---

# Release-Notes Builder

## Output format

A single markdown file at `./release_notes_<version>.md`. The structure is fixed:

```markdown
# Release vX.Y.Z — <short headline>

_Released <YYYY-MM-DD>_

## ✨ Features
- Concrete user-facing change (12 words max, active voice)

## 🐛 Fixes
- What was broken, now fixed

## ⚠️ Breaking changes
- What changed, what users must do to adapt

## 🧰 Internal
- Refactors, deps bumps, infra changes

## Contributors
- @handle1, @handle2

---

_Full diff: <link or commit range>_
```

If a section has no entries, **omit it entirely** — don't write "None".

## Standard Operating Procedure

1. **Parse input** — extract version number, date, and the list of raw change descriptions
2. **Classify each change** into Features / Fixes / Breaking / Internal using the rubric below
3. **Rewrite each line** to be user-facing and concise:
   - ❌ "fixed bug in auth handler causing race condition under load"
   - ✅ "Fixed intermittent 401 errors at high concurrency"
4. **Deduplicate** — collapse multiple commits about the same change into one entry
5. **Order within each section** by user impact (most impactful first)
6. **Write** the final file using `write_file`
7. **Summarize** in 1 sentence: version, total changes, biggest highlight

## Classification rubric

| Tag | Goes in section |
|-----|-----------------|
| `feat:`, "add", "new", "introduce" | Features |
| `fix:`, "fix", "resolve", "correct" | Fixes |
| `BREAKING:`, "remove", "deprecate", "rename" of public API | Breaking changes |
| `chore:`, `refactor:`, `deps:`, `ci:` | Internal |

## Style rules

- **Lead with the verb** — "Added X" not "X has been added"
- **Be specific, not generic** — "Reduced startup time from 800ms → 300ms", not "Performance improvements"
- **No marketing fluff** — "powerful", "robust", "best-in-class" are banned
- **Link issues/PRs** in parentheses at the end when known: `(#1234)`
- **Limit each line to 15 words** — anything longer goes in linked docs, not release notes

## Output check before yielding

- [ ] File saved to `./release_notes_<version>.md`
- [ ] Sections with no entries are omitted (no empty headers)
- [ ] No line over 15 words
- [ ] You printed the path + 1-sentence summary
