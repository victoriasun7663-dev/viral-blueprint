import os
import re
import sys
from datetime import datetime
import requests
from anthropic import Anthropic

# Initialize APIs (Ensure you set these environment variables)
# export ANTHROPIC_API_KEY="your-claude-key"
# export TAVILY_API_KEY="your-tavily-key" (Great for LLM scraping/search)
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")

MODEL = "claude-sonnet-5-5"
MAX_TOKENS = 16000  # room for a full, detailed blueprint
BLUEPRINT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "blueprints")

# 1. Define the web scraping/search function
def search_the_web(query: str) -> str:
    """Searches the internet for the given query and returns scraped content summaries."""
    url = "https://api.tavily.com/search"
    payload = {
        "api_key": TAVILY_API_KEY,
        "query": query,
        "search_depth": "advanced",
        "include_answer": True,
        "max_results": 5
    }
    try:
        resp = requests.post(url, json=payload, timeout=30)
        resp.raise_for_status()
        response = resp.json()
        # Clean up the results for the LLM
        results = response.get("results", [])
        formatted_results = []
        if response.get("answer"):
            formatted_results.append(f"Summary: {response['answer']}\n---")
        for r in results:
            formatted_results.append(f"Title: {r.get('title')}\nURL: {r.get('url')}\nContent: {r.get('content')}\n---")
        return "\n".join(formatted_results) or "No results found."
    except Exception as e:
        return f"Error searching the web: {str(e)}"

# 2. Define the tool specification for Claude
tools = [
    {
        "name": "search_the_web",
        "description": "Searches the internet for real-time information, viral trends, platform algorithms, and video editing case studies.",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query optimized for finding video editing structures, pacing, hooks, and retention strategies."
                }
            },
            "required": ["query"]
        }
    }
]

# 3. Define the Agent execution loop
def run_video_editing_agent(vertical: str, max_turns: int = 10) -> str:
    print(f"🚀 Starting Claude Agent for Vertical: {vertical}...\n")

    system_prompt = (
        "You are an expert viral content strategist and video editor. Your job is to research "
        "and find the absolute best video editing practices for a specific content vertical. "
        "You must look for: Hook duration, retention editing styles (jump cuts, B-roll, zooms), "
        "caption styles, sound design, and pacing metrics. Use the search tool to find recent case studies, "
        "viral breakdowns, or expert articles on this vertical."
    )

    user_message = f"Find and analyze the current viral video editing best practices, hooks, and retention strategies for the '{vertical}' content vertical."

    # Keep the full conversation so Claude remembers every earlier search
    messages = [{"role": "user", "content": user_message}]

    for turn in range(max_turns):
        is_last_turn = turn == max_turns - 1
        if is_last_turn and turn > 0:
            # Out of search rounds: ask Claude to write the blueprint now
            messages[-1]["content"].append({
                "type": "text",
                "text": "You've used all your searches. Write the final blueprint now with what you have."
            })
        response = client.messages.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            system=system_prompt,
            messages=messages,
            tools=tools,
            tool_choice={"type": "none"} if is_last_turn else {"type": "auto"}
        )
        messages.append({"role": "assistant", "content": response.content})

        if response.stop_reason != "tool_use":
            break

        # Claude may ask for several searches at once; answer all of them
        tool_results = []
        for block in response.content:
            if block.type != "tool_use":
                continue
            print(f"🔍 Claude is searching for: '{block.input.get('query')}'...")

            if block.name == "search_the_web":
                tool_result = search_the_web(block.input["query"])
            else:
                tool_result = "Tool not found."

            tool_results.append({
                "type": "tool_result",
                "tool_use_id": block.id,
                "content": tool_result
            })

        messages.append({"role": "user", "content": tool_results})

    # Print the final synthesized strategic breakdown
    final_text = "\n".join(block.text for block in response.content if block.type == "text")
    print("\n📊 --- VIRAL EDITING BLUEPRINT --- 📊\n")
    print(final_text)

    if response.stop_reason == "max_tokens":
        print("\n⚠️ The blueprint hit the length limit and may be cut off. Raise MAX_TOKENS to allow more.")

    # Save the blueprint so it isn't lost when the terminal closes
    os.makedirs(BLUEPRINT_DIR, exist_ok=True)
    slug = re.sub(r"[^a-z0-9]+", "-", vertical.lower()).strip("-")[:60] or "blueprint"
    filename = f"{slug}_{datetime.now():%Y-%m-%d_%H%M}.md"
    path = os.path.join(BLUEPRINT_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(final_text)
    print(f"\n💾 Saved to blueprints/{filename}")

    return final_text


if __name__ == "__main__":
    # Usage: python video_editing_agent.py "fitness coaching"
    vertical = " ".join(sys.argv[1:]) or "FinTech / Personal Finance storytelling"
    run_video_editing_agent(vertical)
