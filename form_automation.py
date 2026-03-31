from playwright.sync_api import sync_playwright

FORM_URL = "https://forms.gle/x37k6y8cxJXXoxpF8"

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            channel="chrome",
            headless=False,
            slow_mo=300
        )

        context = browser.new_context()
        page = context.new_page()

        page.goto(FORM_URL, timeout=60000)
        print("🌐 Form opened")

        # --------------------------
        # 🔐 LOGIN WAIT (IMPORTANT)
        # --------------------------
        if "accounts.google.com" in page.url:
            print("🔐 Please login first...")

            # 👉 Login complete না হওয়া পর্যন্ত wait
            page.wait_for_url("**docs.google.com/**", timeout=120000)

            print("✅ Login done")

        # 👉 Ensure form loaded
        page.wait_for_selector("form", timeout=60000)

        frame = page.frame_locator("iframe") if page.locator("iframe").count() > 0 else page

        print("🤖 Filling form...")

        # --------------------------
        # 📝 TEXT FIELD
        # --------------------------
        frame.get_by_label("Name").fill("Asif")
        frame.get_by_label("ID").fill("22203139")
        frame.get_by_label("Section").fill("A")

        # --------------------------
        # 🔘 RADIO GROUP
        # --------------------------
        questions = frame.locator("div[role='radiogroup']")

        for i in range(questions.count()):
            group = questions.nth(i)
            options = group.locator("div[role='radio']")

            if options.count() > 0:
                options.first.click()

        print("✅ Form filled")

        # --------------------------
        # 🚫 WAIT BEFORE SUBMIT
        # --------------------------
        print("⛔ Waiting for user confirmation before submit...")

        input("👉 After login নিশ্চিত হলে ENTER চাপো to submit...")

        # --------------------------
        # 🚀 SUBMIT
        # --------------------------
        frame.get_by_role("button", name="Submit").click()

        print("🎉 Submitted successfully!")

        input("Press ENTER to close...")
        browser.close()


if __name__ == "__main__":
    run()