#!/usr/bin/env python3
"""Deliver the 22 November 2026 front page to the output directory.

The entry is the image itself: entry.png, a one-page newspaper that
sums up Sunday 22 November 2026 in one picture (the Gulf lead story,
the Baltic, Peru, COP31, Mexico, and the day's other news). This
program only delivers that image: it reads entry.png next to this
file and writes an identical copy to MAKEFUN_OUTPUT_DIR/entry.png
(default /output). Standard library only, no network, no randomness,
so two runs write the same bytes.
"""

import hashlib
import os
import shutil
import sys

IMAGE_NAME = "entry.png"


def source_path():
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, IMAGE_NAME)


def sha256_of(path):
    with open(path, "rb") as handle:
        return hashlib.sha256(handle.read()).hexdigest()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    src = source_path()
    if not os.path.isfile(src):
        print(f"missing image: {src}", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, IMAGE_NAME)
    shutil.copyfile(src, dst)
    if sha256_of(src) != sha256_of(dst):
        print(f"copy mismatch: {dst} differs from {src}", file=sys.stderr)
        return 1
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes, sha256 {sha256_of(dst)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
