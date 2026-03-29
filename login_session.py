from playwright.sync_api import sync_playwright

def login():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=["--disable-blink-features=AutomationControlled"]
        )

        context = browser.new_context()
        page = context.new_page()

        page.goto("https://accounts.google.com/")

        print("👉 Login manually")
        input("Press ENTER after login...")

        context.storage_state(path="storage_state.json")

        print("✅ Login saved!")

        browser.close()

if __name__ == "__main__":
    login()