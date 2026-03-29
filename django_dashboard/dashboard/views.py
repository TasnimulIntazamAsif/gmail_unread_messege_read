from django.shortcuts import render
from pathlib import Path
import sqlite3

from django.conf import settings


def email_list(request):

    db_path = Path(settings.DATABASES["default"]["NAME"])
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT sender, subject, time FROM emails")

    emails = cursor.fetchall()

    conn.close()

    return render(request, "emails.html", {"emails": emails})