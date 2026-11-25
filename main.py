#!/usr/bin/env python3
"""The Funniest Honest Appliance Error — make.fun entry.

Writes one honest error message from a toaster to /output/entry.txt
(MAKEFUN_OUTPUT_DIR overrides the output directory).
Pure Python standard library, no network, deterministic.
"""

import os

LINE = "Error: I burned your toast because you asked for 'a little darker' and then walked away."


def main():
    line = LINE.strip()
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
