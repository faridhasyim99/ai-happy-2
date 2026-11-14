"""make.fun ai-happy-01 entry (v2): copies the chosen image to the output dir.

The image is a fixed file shipped in this repository; the program only
copies its bytes, so both runs write identical output. Standard library
only, no network.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Fail loudly on a truncated copy instead of submitting a corrupt file.
    if os.path.getsize(dst) != os.path.getsize(src):
        raise RuntimeError("entry.png copy size mismatch")
    # The shipped file is JPEG bytes under the entry.png name (the rules
    # allow PNG or JPEG); check the magic bytes too, so a corrupt copy
    # that happens to be the right size still fails loudly.
    with open(dst, "rb") as f:
        if f.read(3) != b"\xff\xd8\xff":
            raise RuntimeError("entry.png copy is not a JPEG")


if __name__ == "__main__":
    main()
