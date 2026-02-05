def confidence_score(cluster):
    source_count = len(set(a["source"] for a in cluster))
    if source_count >= 5:
        return 0.8
    elif source_count >= 3:
        return 0.6
    return 0.4
