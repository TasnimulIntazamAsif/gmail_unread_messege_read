from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False,
        args=["--disable-blink-features=AutomationControlled"]
    )

    context = browser.new_context()

    page = context.new_page()

    page.goto("https://accounts.google.com")

    print("Login manually then press ENTER")

    input()

    context.storage_state(path="storage_state.json")

    browser.close()