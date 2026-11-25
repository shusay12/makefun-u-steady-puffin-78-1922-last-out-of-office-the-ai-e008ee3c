#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista.

Writes one original out-of-office auto-reply to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt).

The line is a fixed, hand-written reply: an AI agent that quit the inbox
to pull espresso shots, its old machine habit (hallucinating replies)
turned to coffee (hallucinating latte art), with the sender's email
assigned an absurdly precise queue number. No network, no randomness,
stdlib only, fully deterministic.
"""

import os
import sys

# The entry: one original out-of-office line, at most 280 characters.
# Revision 3: the ending trades "queued behind the morning rush" for a
# precise absurd queue number — a machine habit (exact counts) that
# lands harder cold, while "latte art" keeps the barista frame.
ENTRY = (
    "Out of office: I quit the inbox to become a barista. "
    "I no longer hallucinate replies, only latte art \u2014 "
    "your email is number 47,312 in the queue."
)

MAX_CHARS = 280


def main() -> int:
    text = ENTRY.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(f"entry is {len(text)} chars, over the {MAX_CHARS} cap",
              file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"entry is not valid UTF-8: {exc}", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
