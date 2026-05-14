---
name: web-research
description: Use this skill whenever the user asks to research a topic, gather information, find sources, or produce a brief on something. Triggers on phrases like "research", "find out about", "investigate", "summarize what's known about". The deliverable is a well-sourced markdown brief saved to a file. Do NOT trigger for simple factual questions answerable from the model's own knowledge.
allowed-tools: tavily_search, write_file, read_file, ls
---

# Web Research SOP

## Standard Operating Procedure

1. **Identify 3-5 sub-questions** that fully cover the topic. Write them as a todo list.
2. **Search each sub-question** using `tavily_search`. Take notes — do NOT paste raw search dumps.
3. **Save findings** to a markdown file `./research/<topic_slug>.md` with sections per sub-question and a Sources list at the bottom.
4. **Print a 2-sentence headline summary** to the user — the brief is in the file, not the chat.

## Quality bar

- Each claim has at least one cited source URL
- No more than 800 words total — this is a brief, not a thesis
- Open with the bottom line; details follow
