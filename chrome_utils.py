from __future__ import annotations

import os
from pathlib import Path


def find_chrome_exe() -> str:
    candidates: list[Path] = []

    pf = os.environ.get("ProgramFiles")
    if pf:
        candidates.append(Path(pf) / "Google" / "Chrome" / "Application" / "chrome.exe")

    pf86 = os.environ.get("ProgramFiles(x86)")
    if pf86:
        candidates.append(Path(pf86) / "Google" / "Chrome" / "Application" / "chrome.exe")

    local = os.environ.get("LOCALAPPDATA")
    if local:
        candidates.append(Path(local) / "Google" / "Chrome" / "Application" / "chrome.exe")

    for p in candidates:
        if p.exists():
            return str(p)

    raise FileNotFoundError(
        "Google Chrome was not found. Install Chrome, or update chrome_utils.find_chrome_exe()."
    )

