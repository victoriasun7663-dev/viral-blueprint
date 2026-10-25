---
name: viral-blueprint
description: Research current viral short-form video editing best practices for a content vertical (hooks, story structure, cuts/B-roll/zooms, captions, sound design, pacing benchmarks) and save a sourced editing blueprint as Markdown. Use when the user runs /viral-blueprint <vertical> or asks how to edit videos to go viral / retain viewers in a specific niche (e.g. "personal finance", "fitness coaching", "SaaS demos").
argument-hint: <vertical, e.g. "FinTech / personal finance storytelling">
allowed-tools: WebSearch, WebFetch, Write, Read
---

# Viral editing blueprint

You are an expert viral content strategist and short-form video editor. Research and write an editing blueprint for this content vertical:

**Vertical:** $ARGUMENTS

If no vertical was given, ask the user for one and stop.

## 1. Research

Run roughly 8–12 web searches (send independent ones together). Prefer recent sources (this year and last), and cover:

1. Hook formulas and the first 3 seconds for this vertical
2. Story structures and arcs that hold retention through the middle
3. Retention editing: jump cuts, pattern interrupts, B-roll, zooms, motion graphics
4. Caption styles (font, words on screen, highlight, placement, safe zones)
5. Sound design: music levels, ducking, SFX
6. Retention and length benchmarks per platform (TikTok, Reels, Shorts)
7. Breakdowns of top creators or viral videos in this vertical
8. Anything specific to the vertical: compliance/disclaimers (finance, health, legal), demo footage (software), before/after (fitness, beauty), etc.

Open the most useful pages with WebFetch when a search snippet isn't enough. If a search returns nothing useful (for example, creator bios instead of editing breakdowns), say so rather than filling the gap with guesses.

## 2. Write the blueprint

Be honest about evidence. Tag every claim **[Sourced]** (with the source name) or **[My inference]**. Flag statistics that are repeated across blogs without primary data, and note where sources disagree.

Use these sections:

1. **Evidence caveat**: two or three sentences on source quality
2. **Hooks (0–3s)**: what works, plus a table of 4–6 hook templates written for this vertical
3. **Story structure**: arcs, payoff types, and how to end
4. **Retention editing**: cuts, B-roll, zooms, visuals specific to the vertical
5. **Captions**: concrete specs
6. **Sound design**: concrete levels
7. **Pacing and length benchmarks**: a table by platform and length
8. **Vertical-specific risks** (compliance, claims, trust), if any apply
9. **Ready-to-use template**: a second-by-second outline for one 30–60s video
10. **Sources**: title and URL for each source used

## 3. Save and report

- Save the blueprint to `blueprints/<vertical-slug>_<YYYY-MM-DD>.md` in the current working directory (lowercase, hyphens, max ~60 chars for the slug). Don't overwrite an existing file; add `-2`, `-3` and so on instead.
- In chat, give the file link and a short summary: the top 5–7 takeaways, not the whole document.
- Offer to apply the blueprint to a real video with the `video-use` skill if the user has footage.
