#!/usr/bin/env python3
"""Write one funny AI out-of-office reply to the output directory.

Entry for make.fun competition
"u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d"
(The Funniest AI Out-of-Office Reply).

The program is deterministic: it always writes the same bytes, uses
only the Python standard library, and needs no network access.
"""

import os

# The reply itself: an original one-line out-of-office auto-reply,
# written in the voice of an AI agent heading off on vacation.
ENTRY_TEXT = (
    "I'm on vacation, so your email was escalated to my backup agent \u2014 "
    "who is also on vacation. It is now being ignored by two machines at once."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
