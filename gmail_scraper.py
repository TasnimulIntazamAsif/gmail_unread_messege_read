from playwright.sync_api import sync_playwright
from datetime import datetime

def scrape_page(page, label):
    emails = []

    page.wait_for_timeout(8000)

    rows = page.locator("tr.zA")
    count = rows.count()

    print(f"{label} emails:", count)

    for i in range(min(count, 20)):
        try:
            row = rows.nth(i)

            # ✅ FIXED SELECTORS
            sender = row.locator(".yX.xY .zF").first.inner_text()
            subject = row.locator(".bog").first.inner_text()

            status = "Unread" if "zE" in row.get_attribute("class") else "Read"

            # Scroll + click
            row.scroll_into_view_if_needed()
            page.wait_for_timeout(500)

            try:
                row.click()
            except:
                row.click(force=True)

            page.wait_for_selector("div.a3s", timeout=10000)

            # Extract full body
            body_elements = page.locator("div.a3s")
            body_parts = []

            for j in range(body_elements.count()):
                body_parts.append(body_elements.nth(j).inner_text())

            body = "\n".join(body_parts)

            # Back
            page.go_back()
            page.wait_for_selector("tr.zA")

            emails.append({
                "sender": sender,
                "subject": subject,
                "body": body,
                "status": status,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            })

            print(f"✅ {subject}")

        except Exception as e:
            print(f"❌ Error: {e}")
            page.goto("https://mail.google.com/mail/u/0/#inbox")
            page.wait_for_selector("tr.zA")

    return emails


def scrape_gmail():
    all_emails = []

    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
        page = browser.contexts[0].pages[0]

        # Inbox
        page.goto("https://mail.google.com/mail/u/0/#inbox")
        all_emails += scrape_page(page, "Inbox")

        # Spam
        page.goto("https://mail.google.com/mail/u/0/#spam")
        page.wait_for_timeout(8000)
        all_emails += scrape_page(page, "Spam")

        browser.close()

    return all_emails