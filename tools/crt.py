#!/usr/bin/env python3
"""Turns a capture into a phosphor CRT frame: grey, (inverted when the interface is light), noise, green
phosphor, bloom, scanlines, a few torn bands, barrel curvature and a vignette. Needs ImageMagick 7.
  python3 tools/crt.py material/screens/sail-map-dark.png site/images/sail.webp [--invert] [--seed 7]"""
import random, subprocess, sys, tempfile, os
src, dst = sys.argv[1], sys.argv[2]
invert = "--invert" in sys.argv
seed = int(sys.argv[sys.argv.index("--seed") + 1]) if "--seed" in sys.argv else 1
random.seed(seed)
W, H = 1600, 1000
PAPER, PHOSPHOR, HOT = "#0a0b0a", "#c5c7c4", "#f0f2ef"   # paper, a white phosphor, and a hotter highlight for bloom
tmp = tempfile.mkdtemp()
grey = os.path.join(tmp, "grey.png"); scan = os.path.join(tmp, "scan.png")
run = lambda *a: subprocess.run(["magick", *a], check=True)
# 1. grey base at the frame size, inverted for a light interface, a touch of noise and contrast
run(src, "-resize", f"{W}x{H}^", "-gravity", "north", "-extent", f"{W}x{H}", "-grayscale", "Rec709Luma",
    *(["-negate"] if invert else []), "-sigmoidal-contrast", "4x50%", "-attenuate", "0.35", "+noise", "Gaussian",
    "-blur", "0x0.4", grey)
# 2. torn bands: a few thin horizontal slices rolled sideways
ops = []
for _ in range(random.randint(3, 5)):
    y = random.randint(40, H - 60); h = random.randint(4, 14); dx = random.choice([-1, 1]) * random.randint(10, 40)
    ops += ["(", "+clone", "-crop", f"{W}x{h}+0+{y}", "+repage", "-roll", f"{dx:+d}+0", ")", "-geometry", f"+0+{y}", "-compose", "over", "-composite"]
run(grey, *ops, grey)
# 3. scanline tile: two lit rows, one dark
run("-size", "1x1", "xc:gray(100%)", "xc:gray(100%)", "xc:gray(38%)", "-append", scan)
# 4. phosphor: tint, bloom (a blurred copy screened over), scanlines multiplied, a faint horizontal smear
run(grey, "+level-colors", f"{PAPER},{PHOSPHOR}",
    "(", "+clone", "-blur", "0x5", "+level-colors", "black," + HOT, "-evaluate", "multiply", "0.55", ")", "-compose", "screen", "-composite",
    "(", "+clone", "-motion-blur", "0x6+0", "-evaluate", "multiply", "0.25", ")", "-compose", "screen", "-composite",
    "(", "-size", f"{W}x{H}", f"tile:{scan}", ")", "-compose", "multiply", "-composite",
    # 5. the glass: a slight barrel curve on a dark ground, soft corners, a vignette
    "-background", PAPER, "-virtual-pixel", "background", "-distort", "Barrel", "0 0 0.035 0.975",
    "-compose", "over", "-vignette", "0x80+40+40", "-background", PAPER, "-flatten", "-quality", "84", dst)
print("wrote", dst)
