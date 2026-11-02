# Design: walior.it

The locked system. Every Hallmark run reads this first and pages share it. Change it on purpose; the file is the rule.

## System
- Genre: atmospheric
- Shape of the first page: Index-First (a directory listing), hero posture Ledge
- Theme: Terminal, without its green: a white-phosphor terminal. One neutral ramp from the paper to the ink, no second hue anywhere
- Axes: dark/mono/neutral · posture: committed

## The mark
Four slashes typed in a row, `\/\/`, read as a w. Vector in `material/mark.svg` (currentColor strokes, 64 viewBox, round caps). On the page it is printed as a grid of characters taken from the page's own path names, in the eight glyph tokens, resolving row by row. The favicon (`site/favicon.svg`) is the same four strokes in the ink on the paper. The old W avatar is reference only.

## Tokens
`site/tokens.css` is the source of truth. The roles:
```css
:root {
  --color-paper: oklch(11% 0.004 150);  --color-paper-2: oklch(14.5% 0.005 150);  --color-paper-3: oklch(19% 0.006 150);
  --color-ink: oklch(95% 0.006 150);  --color-ink-2: oklch(82% 0.006 150);  --color-muted: oklch(64% 0.006 150);  --color-rule: oklch(26% 0.005 150);  --color-rule-2: oklch(37% 0.006 150);
  --color-accent: oklch(96% 0.008 150);  --color-accent-ink: oklch(12% 0.004 150);  --color-focus: oklch(96% 0.008 150);  --color-accent-wash: oklch(24% 0.006 150);
  --glyph-0 … --glyph-7: the eight lightness steps a glyph picture is printed in;
  --font-display: "Martian Mono", ui-monospace, monospace;  --font-body: var(--font-display);  --font-outlier: var(--font-display);
  --radius-card: 0;  --radius-pill: 0;  --rule-hair: 1px;  --shadow-card: none;
  --stretch-display: 112.5%;  --stretch-body: 87.5%;  --display-weight: 500;  --tracking-display: -0.02em;
}
```
The spacing scale, the type scale, the easings and the durations are the scaffold's and live in `tokens.css`.

## Type
One family, Martian Mono, weights 400 and 500 only. Heads at width 112.5%, text at 87.5%. Paths are set as titles (`--text-title`, 500, wide). Labels in `--color-muted`, sentence case, untracked. No italics, no caps.

## Surfaces and pictures
One hue in lightness steps; hairlines in `--color-rule`, firmer lines in `--color-rule-2`; no radius, no shadow, no glow. The mark is printed in type (`tools/glyphs.py`). Product captures are real screenshots baked into phosphor CRT frames by `tools/crt.py` (grey, inverted when the interface is light, noise, white phosphor, bloom, scanlines, a few torn bands, barrel curvature, vignette), inside a 1px rule. On hover a frame cycles through more screens of its product (`tools/frames.mjs` captures them), each cut in through three torn slices; the page adds a faint flicker. No photographs.

## The objects
- The videos are a log: one row per video (its full YouTube id, the path at title size, the title, the year) on five columns, and a 4:3 monitor on seven that shows the video's thumbnail baked as a CRT frame; the row under the pointer cuts the monitor to its frame and writes the path and year on the OSD strip. Without script the monitor shows the newest.
- The repositories are rows read like a tool's output: the name as `/github/<name>`, the description, the language mix as twenty marks (`#`, `=`, `-`, `.` in four lightness steps) with the top language as its label, the stars and the last push on the right. Facts come from the GitHub API into `repos.json`.

## Controls
- Primary: a full-width block of the ink (`--color-accent`, near white) with the paper for text, square, 72px tall, state in `steps(1)`.
- Secondary: a 1px `--color-ink-2` border, 48px tall, same square corners.
- Links: `--color-ink-2`, dotted underline, accent on hover; a selected row takes `--color-accent-wash`.

## Motion
- Character: severe. One reveal, the mark resolving row by row over about one second; cells flare to the accent under the cursor. Nothing else moves; under reduced motion everything ends at once.

## Voice
Paths, names, years. Declarative and short. No eyebrows, no middle dots, no arrows, no dashes.

## Exports
`site/tokens.css` in this project. Tailwind, DTCG or shadcn blocks are added here on request.
