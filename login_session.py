from pathlib import Path
import subprocess

from playwright.sync_api import sync_playwright

from chrome_utils import find_chrome_exe

def save_session():
    with sync_playwright() as p:
        # Start NORMAL Chrome (not Playwright-launched) with CDP enabled.
        # This avoids Google's "This browser or app may not be secure" blocks.
        user_data_dir = Path(__file__).resolve().parent / "chrome-profile"
        user_data_dir.mkdir(parents=True, exist_ok=True)

        chrome = find_chrome_exe()
        subprocess.Popen(
            [
                chrome,
                "--remote-debugging-port=9222",
                f"--user-data-dir={user_data_dir}",
                "https://mail.google.com/",
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            close_fds=True,
        )

        print("👉 Login manually in this browser")
        input("Press ENTER after login...")

        # Attach and save session
        browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
        context = browser.contexts[0]
        context.storage_state(path="storage_state.json")

        print("✅ Session saved!")
        browser.close()

if __name__ == "__main__":
    save_session()