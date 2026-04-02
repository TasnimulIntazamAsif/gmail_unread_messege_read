from playwright.sync_api import Error as PlaywrightError, sync_playwright
from datetime import datetime

def scrape_gmail():
    emails = []

    with sync_playwright() as p:
        try:
            # Attach to the normal Chrome started by login_session.py
            browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
        except PlaywrightError as e:
            raise RuntimeError(
                "Could not connect to Chrome CDP on http://127.0.0.1:9222.\n"
                "1) Run: .\\.venv\\Scripts\\python.exe login_session.py\n"
                "2) Log into Gmail in the opened Chrome window (NOT Incognito)\n"
                "3) Press ENTER to save the session\n"
                "4) Re-run: .\\.venv\\Scripts\\python.exe main.py"
            ) from e

        context = browser.contexts[0]
        page = context.pages[0] if context.pages else context.new_page()

        page.goto("https://mail.google.com/mail/u/0/#inbox")
        page.wait_for_timeout(5000)

        rows = page.query_selector_all("tr.zA")

        for row in rows[:10]:
            try:
                sender = row.query_selector(".yX.xY span").inner_text()
                subject = row.query_selector(".bog").inner_text()

                status = "Unread" if "zE" in row.get_attribute("class") else "Read"
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                emails.append({
                    "sender": sender,
                    "subject": subject,
                    "body": subject,
                    "status": status,
                    "timestamp": timestamp
                })

            except:
                continue

        browser.close()

    return emails