# Global AI Narrator (No-AI Baseline)

## Example Output

![Example output](docs/IMG_6046.jpeg)


A lightweight Python tool that pulls real headlines from RSS sources and generates a daily “briefing style” report with:
- Top headlines
- Sources represented (publisher-aware)
- “What to watch next” signals
- A conservative confidence score

This project is intentionally a **no-AI baseline**: fast, free, and transparent.
The architecture is designed so an AI synthesizer can be swapped in later.

---

## What it does

When you run the app, it:
1. Fetches news from RSS feeds (Google News + major outlets)
2. Extracts publisher names (so sources aren’t all “Google News”)
3. Limits and balances feeds so one source doesn’t dominate
4. Prints a daily brief and saves it to `outputs/`

---

## Requirements

- Python 3.10+ recommended

---

## Install

```bash
pip install -r requirements.txt
