def summarize_text(text, max_words=50):
    if not text:
        return ""

    words = text.split()

    if len(words) <= max_words:
        return text

    summary = " ".join(words[:max_words])
    return summary + "..."