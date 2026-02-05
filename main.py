import os
from datetime import datetime

from ingestion.news_fetcher import fetch_articles
from ai.synthesizer import synthesize_cluster
from ai.epistemology import confidence_score
from config import OUTPUT_DIR, TOPIC


def save_output(text: str) -> str:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    ts = datetime.now().strftime("%Y-%m-%d_%H%M")
    path = os.path.join(OUTPUT_DIR, f"brief_{ts}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text.strip() + "\n")
    return path


def run():
    articles = fetch_articles(TOPIC)
    brief = synthesize_cluster(articles)
    conf = confidence_score(articles)

    final = brief + f"\n\nConfidence level: {conf}\n"
    print(final)

    out_path = save_output(final)
    print(f"\nSaved to: {out_path}")


if __name__ == "__main__":
    run()
