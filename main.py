#!/usr/bin/env python3
"""Write the one-star review of the Moon to /output/entry.txt.

The competition asks for a single funny one-star review of the Moon,
120 characters at most. The program writes exactly that text, nothing else.
"""

import os

ENTRY = (
    "\u2605\u2606\u2606\u2606\u2606 Shows up nightly uninvited, stares through "
    "my window, and bosses the ocean around. No manners. No rent. One star."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
