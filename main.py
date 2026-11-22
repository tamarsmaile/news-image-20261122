#!/usr/bin/env python3
"""news-image-20261122 entry.

The deliverable is the bundled front-page image, entry.png: a 1024x1024
PNG summing up world news of Sunday 22 November 2026. This program
only copies it to the output directory (stdlib only, no network).
"""
import os
import shutil

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
here = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(here, "entry.png")
shutil.copyfile(src, os.path.join(out, "entry.png"))
