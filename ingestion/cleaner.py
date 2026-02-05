def clean_articles(articles):
    seen = set()
    cleaned = []
    for a in articles:
        key = a["title"].lower().strip()
        if key not in seen:
            seen.add(key)
            cleaned.append(a)
    return cleaned
