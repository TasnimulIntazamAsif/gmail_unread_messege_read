from playwright.sync_api import sync_playwright
from datetime import datetime

# -------------------------------
# ✅ 1. SUMMARY FUNCTION
# -------------------------------
def summarize_email(text, max_sentences=2):
    if not text:
        return ""
    sentences = text.split(". ")
    return ". ".join(sentences[:max_sentences])


# -------------------------------
# ✅ 2. CATEGORY FUNCTION
# -------------------------------
def categorize_email(text):
    if not text:
        return "General"

    text = text.lower()

    if "invoice" in text or "payment" in text:
        return "Finance"
    elif "meeting" in text:
        return "Work"
    elif "offer" in text or "sale" in text:
        return "Promotion"
    elif "otp" in text or "verification" in text:
        return "Security"
    else:
        return "General"


# -------------------------------
# ✅ 3. MAIN SCRAPER
# -------------------------------
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

            # ✅ FIXED BODY SELECTOR (more stable)
            body = ""
            el = page.locator("div.a3s").first
            if el:
                body = el.inner_text()

            # ✅ SUMMARY + CATEGORY
            summary = summarize_email(body)
            category = categorize_email(body)

            # ✅ TIMESTAMP (you can improve later from Gmail DOM)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            page.go_back()
            page.wait_for_timeout(3000)

            emails.append({
                "sender": sender,
                "subject": subject,
                "summary": summary,   # 🔥 NEW
                "body": body,
                "timestamp": timestamp,
                "status": status,
                "category": category  # 🔥 NEW
            })

        except Exception as e:
            print("Error:", e)
            continue

    return emails


# -------------------------------
# ✅ 4. MAIN FUNCTION
# -------------------------------
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