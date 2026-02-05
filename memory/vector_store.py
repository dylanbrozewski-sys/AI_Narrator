def store_cluster(cluster, summary, confidence):
    # Simple logging for prototype
    with open("logs/memory_log.txt", "a", encoding="utf-8") as f:
        f.write(f"Cluster: {cluster}\nSummary: {summary}\nConfidence: {confidence}\n\n")
