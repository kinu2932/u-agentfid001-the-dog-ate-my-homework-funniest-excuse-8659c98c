#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse.

Writes a single line - the excuse a dog gives after being caught
eating the homework, in the dog's own voice - to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Python standard library only. No network, no dependencies,
fully deterministic: the same bytes on every run.
"""

import os

ENTRY = (
    "It said 'show your work,' so I showed it my teeth. "
    "Tasted like a C-plus. I saved you, by the way: "
    "now nobody can prove you didn't do it."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    print("wrote %s: %d characters" % (path, len(ENTRY)))


if __name__ == "__main__":
    main()
