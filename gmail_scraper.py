from playwright.sync_api import sync_playwright
from datetime import datetime

def scrape_page(page, label):
    emails = []

    page.wait_for_timeout(8000)
    rows = page.query_selector_all("tr.zA")

    print(f"{label} emails:", len(rows))

    for row in rows[:20]:
        try:
            sender = row.query_selector(".yX.xY span").inner_text()
            subject = row.query_selector(".bog").inner_text()

            status = "Unread" if "zE" in row.get_attribute("class") else "Read"

            row.click()
            page.wait_for_timeout(4000)

            body = ""
            el = page.query_selector("div.a3s.aiL")
            if el:
                body = el.inner_text()

            page.go_back()
            page.wait_for_timeout(3000)

            emails.append({
                "sender": sender,
                "subject": subject,
                "body": body,
                "status": status,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            })

        except:
            continue

    return emails


def scrape_gmail():
    all_emails = []

    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
        page = browser.contexts[0].pages[0]

        page.goto("https://mail.google.com/mail/u/0/#inbox")
        all_emails += scrape_page(page, "Inbox")

        page.goto("https://mail.google.com/mail/u/0/#spam")
        page.wait_for_timeout(8000)
        all_emails += scrape_page(page, "Spam")

        browser.close()

    return all_emails