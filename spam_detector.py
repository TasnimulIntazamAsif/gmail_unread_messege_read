SPAM_KEYWORDS = [
    "win","free","lottery","urgent",
    "click here","buy now","discount",
    "limited time","offer","cash prize"
]

SAFE_KEYWORDS = [
    "conference","ieee","paper","submission",
    "acceptance","schedule","program"
]

def detect_spam(subject, body):
    text = (subject + " " + body).lower()

    for word in SAFE_KEYWORDS:
        if word in text:
            return "Authentic"

    score = sum(1 for w in SPAM_KEYWORDS if w in text)
    return "Spam" if score >= 2 else "Authentic"