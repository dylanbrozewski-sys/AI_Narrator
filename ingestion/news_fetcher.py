import time
import requests
import feedparser

from config import TOPIC, DAILY_ARTICLE_LIMIT, MAX_PER_FEED


def google_news_rss_url(query: str) -> str:
    q = requests.utils.quote(query)
    return f"https://news.google.com/rss/search?q={q}&hl=en-US&gl=US&ceid=US:en"


def extract_publisher_from_title(title: str) -> str:
    if " - " not in title:
        return "Unknown"

    publisher = title.rsplit(" - ", 1)[-1].strip()

    NORMALIZE = {
        "BBC News": "BBC",
        "NBC News": "NBC",
        "Al Jazeera - Breaking News, World News and Video from Al Jazeera": "Al Jazeera",
        "CNBC": "CNBC",
        "CNN": "CNN",
        "Bloomberg": "Bloomberg",
        "ABC News": "ABC News",
    }

    return NORMALIZE.get(publisher, publisher)



def strip_html(s: str) -> str:
    out = []
    in_tag = False
    for ch in s or "":
        if ch == "<":
            in_tag = True
            continue
        if ch == ">":
            in_tag = False
            continue
        if not in_tag:
            out.append(ch)
    return "".join(out)


# Free RSS sources. (Some feeds change URLs over time.)
RSS_FEEDS = [
    google_news_rss_url(TOPIC),
    "https://feeds.bbci.co.uk/news/world/rss.xml",
    "https://rss.cnn.com/rss/edition_world.rss",
    "https://www.aljazeera.com/xml/rss/all.xml",
    # Reuters RSS sometimes changes; if it fails, just comment it out.
    "https://www.reuters.com/rssFeed/worldNews",
]


def fetch_articles(topic: str = None, limit: int = None):
    """
    Returns a list of dicts:
      { title, content, source, url }
    """
    if topic is None:
        topic = TOPIC
    if limit is None:
        limit = DAILY_ARTICLE_LIMIT

    articles = []
    seen_links = set()

    for feed_url in RSS_FEEDS:
        feed = feedparser.parse(feed_url)
        feed_title = getattr(feed.feed, "title", "RSS")

        per_feed = 0
        for entry in getattr(feed, "entries", []):
            if per_feed >= MAX_PER_FEED:
                break

            link = getattr(entry, "link", None)
            title = (getattr(entry, "title", "") or "").strip()
            if not link or link in seen_links:
                continue

            seen_links.add(link)

            summary = getattr(entry, "summary", "") or ""
            content = strip_html(summary).strip()

            if "Google News" in feed_title:
                source = extract_publisher_from_title(title)
            else:
                source = feed_title

            articles.append(
                {
                    "title": title or "Untitled",
                    "content": content or title or "No summary provided.",
                    "source": source,
                    "url": link,
                }
            )

            per_feed += 1
            if len(articles) >= limit:
                return articles

        time.sleep(0.2)

    return articles
