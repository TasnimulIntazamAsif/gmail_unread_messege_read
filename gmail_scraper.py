import sqlite3
from playwright.sync_api import sync_playwright

conn = sqlite3.connect("emails.db")
cursor = conn.cursor()

# Table create (if not exists)
cursor.execute("""
CREATE TABLE IF NOT EXISTS emails(
id INTEGER PRIMARY KEY AUTOINCREMENT,
sender TEXT,
subject TEXT,
time TEXT,
folder TEXT
)
""")

conn.commit()


def save_email(sender, subject, time, folder):

    # Example filter conditions
    if sender == "" or subject == "":
        return

    cursor.execute(
        "INSERT INTO emails(sender,subject,time,folder) VALUES(?,?,?,?)",
        (sender, subject, time, folder)
    )

    conn.commit()


def read_emails(page, folder):

    page.wait_for_timeout(5000)

    emails = page.locator("tr.zE")

    count = emails.count()

    print(folder, "Unread Emails:", count)

    for i in range(count):

        row = emails.nth(i)

        try:
            sender = row.locator("span.zF").first.inner_text()
            subject = row.locator("span.bog").first.inner_text()
            time = row.locator("td.xW span").first.inner_text()

            print(sender, subject, time)

            save_email(sender, subject, time, folder)

        except:
            print("Skipped email")


with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    context = browser.new_context(storage_state="storage_state.json")

    page = context.new_page()

    page.goto("https://mail.google.com/mail/u/0/#inbox")

    read_emails(page, "Inbox")

    page.goto("https://mail.google.com/mail/u/0/#spam")

    read_emails(page, "Spam")

    browser.close()