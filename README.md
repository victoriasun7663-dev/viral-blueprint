# Viral Blueprint

Research what makes short-form videos go viral in any niche, and get back a sourced editing blueprint: hooks, story structure, cuts and B-roll, captions, sound design, and retention benchmarks for TikTok, Reels and Shorts.

It comes in two forms:

| | Claude Code skill | Python script |
|---|---|---|
| Run it with | `/viral-blueprint <niche>` in Claude Code | `python video_editing_agent.py "<niche>"` |
| Web search | Claude Code's built-in search | [Tavily](https://tavily.com) API |
| Needs API keys | No | Anthropic + Tavily |
| Cost | Your Claude plan | Pay-per-use API billing |

Both save the result as a Markdown file in a `blueprints/` folder.

## What a blueprint contains

1. An evidence caveat on source quality
2. Hooks for the first 3 seconds, with templates written for the niche
3. Story structures that hold viewers through the middle
4. Retention editing: jump cuts, pattern interrupts, B-roll, zooms, motion graphics
5. Caption specs: font, words on screen, highlighting, placement
6. Sound design levels: voice, music, ducking, sound effects
7. Retention and length benchmarks by platform
8. Niche-specific risks, such as compliance for finance or health content
9. A second-by-second template for one 30–60 second video

Every point is tagged **[Sourced]** or **[My inference]**, so you can tell research from reasoning. Treat the numbers as starting points to test, not rules.

## Option 1: Claude Code skill

1. Copy the `skill/viral-blueprint` folder into your personal skills folder:
   - Windows: `%USERPROFILE%\.claude\skills\`
   - macOS / Linux: `~/.claude/skills/`
2. Start a new Claude Code session and run:

   ```
   /viral-blueprint fitness coaching for busy parents
   ```

The blueprint is saved to `blueprints/` in the folder Claude Code is working in, with a short summary in chat. If you also use a video-editing skill such as `video-use`, the skill offers to apply the blueprint to your footage.

## Option 2: Python script

### Requirements

- Python 3.9 or newer
- An [Anthropic API key](https://console.anthropic.com) (API usage is billed separately from a Claude subscription)
- A [Tavily API key](https://tavily.com) (the free plan includes monthly searches)

### Setup

```bash
cd script
pip install -r requirements.txt
```

### Run

**Windows (PowerShell):** the launcher asks for both keys, hiding them as you paste, and then runs the script:

```powershell
powershell -ExecutionPolicy Bypass -File .\run_agent.ps1 "fitness coaching"
```

**macOS / Linux:**

```bash
export ANTHROPIC_API_KEY="your-anthropic-key"
export TAVILY_API_KEY="your-tavily-key"
python video_editing_agent.py "fitness coaching"
```

With no niche given, it researches FinTech / personal finance storytelling.

### How it works

The script gives Claude a `search_the_web` tool backed by Tavily. Claude decides what to search, reads the results, and keeps searching, up to 10 rounds, until it has enough to write the blueprint. You can change the model, length limit and number of rounds at the top of `video_editing_agent.py`.

## Keep your keys private

Never paste API keys into code, commit them, or share them. The script reads them from environment variables only, and `.gitignore` excludes `.env` files.

## License

[MIT](LICENSE)
