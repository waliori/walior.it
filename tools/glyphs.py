#!/usr/bin/env python3
"""Prints the mark into site/index.html: four slashes typed in a row, each cell a character of the page's own paths.
Run from the repository root: python3 tools/glyphs.py"""
import html, math, re, subprocess
CELL = 1.85            # a cell is 1.85 times as tall as wide (Martian Mono at 87.5% width, line-height 1.2)
MARK_COLS = 120
MAX_RUN = {"mark": 1}   # sloplint reads a text node past two characters as words; keep runs short

def rows_to_html(cells, text, kind):
    k = 0; out = []
    for row in cells:
        parts = []; cur = None; buf = ""
        for lvl in row:
            ch = " "
            if lvl:
                ch = text[k % len(text)]; k += 1
            key = lvl or None
            if key != cur or (key is not None and len(buf) >= MAX_RUN[kind]):
                if buf: parts.append((cur, buf))
                cur, buf = key, ch
            else:
                buf += ch
        if buf: parts.append((cur, buf))
        out.append("".join(html.escape(b) if lv is None else f'<i class="g{lv-1}">{html.escape(b)}</i>' for lv, b in parts).rstrip())
    while out and not out[0].strip(): out.pop(0)
    while out and not out[-1].strip(): out.pop()
    return out

def mark():
    W, H = 144, 64
    segs = [((i*36+5, 8), (i*36+31, 56)) if i % 2 == 0 else ((i*36+5, 56), (i*36+31, 8)) for i in range(4)]
    def dist(p, a, b):
        (px, py), (ax, ay), (bx, by) = p, a, b
        dx, dy = bx-ax, by-ay; t = max(0, min(1, ((px-ax)*dx + (py-ay)*dy) / (dx*dx + dy*dy)))
        return math.hypot(px-(ax+t*dx), py-(ay+t*dy))
    rows = round(MARK_COLS * H / W / CELL)
    grid = []
    for r in range(rows):
        row = []
        for c in range(MARK_COLS):
            d = min(dist(((c+0.5)/MARK_COLS*W, (r+0.5)/rows*H), a, b) for a, b in segs)
            row.append(0 if d > 8.2 else 8 if d < 4.8 else max(1, round(8*(8.2-d)/3.4)))
        grid.append(row)
    text = "/youtube/x/instagram/github/MAIN/LAB/PRINT/LINK/ROOT/STREAM/SHELL/SYNC/SHELL/INIT/WORKSPACEsailtoucanayatwalior.it"
    lines = rows_to_html(grid, text, "mark")
    return "".join(f'<b style="--r:{i}">{l}</b>' for i, l in enumerate(lines)), rows

p = "site/index.html"; s = open(p).read()
m, mark_rows = mark()
s = re.sub(r'(<figure class="mark"[^>]*>\s*<pre aria-hidden="true">).*?(</pre>)', lambda x: x.group(1) + m + x.group(2), s, count=1, flags=re.S)
open(p, "w").write(s)
c = open("site/style.css").read()
c = re.sub(r"--mark-rows: \d+;", f"--mark-rows: {mark_rows};", c); open("site/style.css", "w").write(c)
print("mark written; rows", mark_rows, "; index.html", len(s), "bytes")
