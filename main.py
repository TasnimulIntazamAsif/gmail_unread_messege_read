import os, sys
from datetime import datetime

sys.path.append("django_dashboard")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gmail_dashboard.settings")

import django
django.setup()

from dashboard.models import Email
from gmail_scraper import scrape_gmail
from spam_detector import detect_spam
from file_storage import save_to_files
from django.utils import timezone
from text_summarizer import summarize_text   # ✅ NEW

def run():
    print("🚀 Running...")

    emails = scrape_gmail()

    for e in emails:
        # ✅ Summary তৈরি
        summary = summarize_text(e["body"], 50)

        # Spam detection (full body use)
        category = detect_spam(e["subject"], e["body"])

        ts = datetime.strptime(e["timestamp"], "%Y-%m-%d %H:%M:%S")
        ts = timezone.make_aware(ts)

        data = {
            "sender": e["sender"],
            "subject": e["subject"],
            "body": summary,   # ✅ SUMMARY SAVE
            "status": e["status"],
            "category": category,
            "timestamp": ts,
        }

        Email.objects.create(**data)
        save_to_files(data)

    print("✅ DONE")


if __name__ == "__main__":
    run()