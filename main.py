#!/usr/bin/env python3
"""GrassCast — the worst app idea ever pitched.

A one-sentence pitch for an app nobody needs: a paid live stream of your
own front lawn, with a push alert every time a blade of grass grows a
millimetre. Writes the pitch (185 characters) to /output/entry.txt.
"""

import os

PITCH = (
    "GrassCast is a $12-a-month app that live-streams your front lawn in 4K "
    "and pings you the instant a blade of grass grows a millimetre, because "
    "nobody should have to miss grass happening."
)


def main():
    text = PITCH.strip()
    if not 1 <= len(text) <= 240:
        raise SystemExit(f"pitch is {len(text)} characters, must be 1-240")
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("pitch must be exactly one sentence")
    outdir = "/output"
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {path}")


if __name__ == "__main__":
    main()
