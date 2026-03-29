from playwright.sync_api import sync_playwright
from database import save_email


def scrape_gmail():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state="storage_state.json")
        page = context.new_page()

        page.goto("https://mail.google.com/mail/u/0/#inbox")

        print("📥 Loading Gmail...")
        page.wait_for_selector("tr.zA", timeout=60000)

        emails = page.query_selector_all("tr.zA")

        print(f"Found {len(emails)} emails")

        for email in emails[:10]:
            try:
                sender = email.query_selector(".yX.xY span").inner_text()
                subject = email.query_selector(".bog").inner_text()
                time = email.query_selector(".xW.xY span").get_attribute("title")

                print(sender, "|", subject)

                save_email(sender, subject, time)

            except Exception as e:
                print("Error:", e)

        browser.close()