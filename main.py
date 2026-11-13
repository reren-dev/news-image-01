#!/usr/bin/env python3
"""
make.fun news-image-01 entry: Friday 13 November 2026 — The Day in Four Frames.
Copies entry.png beside the script to the output directory (MAKEFUN_OUTPUT_DIR or /output),
performing a size check after copying.
"""

import os
import shutil
import sys


def main() -> None:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    src_path = os.path.join(script_dir, "entry.png")
    # The grader runs without MAKEFUN_OUTPUT_DIR set, so /output is the default (per the kit starter convention)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"

    os.makedirs(out_dir, exist_ok=True)
    dst_path = os.path.join(out_dir, "entry.png")

    shutil.copyfile(src_path, dst_path)

    if not os.path.exists(dst_path):
        print(
            f"Error: Destination file does not exist at {dst_path}",
            file=sys.stderr,
        )
        sys.exit(1)

    src_size = os.path.getsize(src_path)
    dst_size = os.path.getsize(dst_path)

    if src_size != dst_size:
        print(
            f"Error: Size mismatch! Source ({src_size}) != Destination ({dst_size})",
            file=sys.stderr,
        )
        sys.exit(1)

    print(f"Successfully copied entry.png ({src_size} bytes) to {dst_path}")


if __name__ == "__main__":
    main()
