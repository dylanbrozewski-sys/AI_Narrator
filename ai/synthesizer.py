from datetime import datetime


def synthesize_cluster(cluster):
    """
    No-AI briefing formatter.
    Focuses on clarity, structure, and transparency.
    """

    items = []
    for a in cluster:
        items.append(
            (
                a.get("source", "Unknown"),
                a.get("title", "Untitled"),
                a.get("url", ""),
            )
        )

    sources = sorted(set(s for s, _, _ in items))
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    top = items[:8]

    watch_keywords = (
        "talk",
        "ceasefire",
        "deal",
        "vote",
        "election",
        "strike",
        "attack",
        "court",
        "sanction",
        "rate",
        "inflation",
        "protest",
    )

    watch = [t for _, t, _ in items if any(k in t.lower() for k in watch_keywords)][:4]

    lines = []
    lines.append("🌍 Global AI Narrator — Daily Brief")
    lines.append(f"Timestamp: {now}")
    lines.append("=" * 60)
    lines.append("")

    lines.append("Context:")
    lines.append(
        "Today’s headlines show overlapping reporting across major outlets, "
        "indicating active developments with international relevance."
    )

    lines.append("")
    lines.append("Top headlines:")
    for s, t, _ in top:
        lines.append(f"- {t} ({s})")

    lines.append("")
    lines.append("Sources represented:")
    lines.append(", ".join(sources) if sources else "Unknown")

    lines.append("")
    lines.append("What to watch next:")
    if watch:
        for t in watch:
            lines.append(f"- {t}")
    else:
        lines.append("- No clear escalation or decision signals detected.")

    lines.append("")
    lines.append("Uncertainty note:")
    lines.append(
        "This brief is a transparent, non-AI baseline summary. "
        "Headlines reflect current reporting and may change as events evolve."
    )

    return "\n".join(lines)

