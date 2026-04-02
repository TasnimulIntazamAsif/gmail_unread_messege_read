SPAM_KEYWORDS = ["win", "free", "offer", "lottery", "urgent", "prize"]

def detect_spam(subject, body):
    text = (subject + " " + body).lower()
    return "Spam" if any(word in text for word in SPAM_KEYWORDS) else "Authentic"