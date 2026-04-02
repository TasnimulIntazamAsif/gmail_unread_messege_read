import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(BASE_DIR, "django_dashboard"))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gmail_dashboard.settings")

import django
django.setup()

from dashboard.models import Email
from gmail_scraper import scrape_gmail
from spam_detector import detect_spam
from file_storage import save_to_files

def run():
    print("Running scraper...")

    try:
        emails = scrape_gmail()
    except Exception as e:
        print(str(e))
        return

    for e in emails:
        category = detect_spam(e["subject"], e["body"])

        email_data = {
            "sender": e["sender"],
            "subject": e["subject"],
            "body": e["body"],
            "status": e["status"],
            "category": category,
            "timestamp": e["timestamp"]
        }

        Email.objects.create(**email_data)
        save_to_files(email_data)

    print("DONE")

if __name__ == "__main__":
    run()