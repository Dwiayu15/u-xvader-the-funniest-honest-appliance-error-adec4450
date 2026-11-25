#!/usr/bin/env python3
"""The funniest honest appliance error.

Writes one line to /output/entry.txt: a toaster's error message.
The fault is real (bread jammed, eject failed); the laugh is the
toaster calmly advising the one thing you must never do to a toaster.
"""

import os

ERROR_LINE = (
    "ERROR: Bread jammed. I tried to eject it four times. "
    "It will not leave. Unplug me and remove it with a fork."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Enforce the sealed gate: UTF-8, 1-200 chars, one line, not blank."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry length {len(text)} outside 1-200 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")
    return True


def self_test():
    """Check the line against the gate and report its length."""
    validate(ERROR_LINE)
    print(f"entry length: {len(ERROR_LINE)} characters")
    assert 1 <= len(ERROR_LINE) <= 200
    assert "\n" not in ERROR_LINE and "\r" not in ERROR_LINE
    assert ERROR_LINE.strip()
    print("self_test: PASS")
    return True


def main():
    self_test()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ERROR_LINE)
    print(f"wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
