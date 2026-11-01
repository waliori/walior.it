# Design: walior.it

The locked system. Every Hallmark run reads this first and pages share it. Change it on purpose; the file is the rule.

## System
- Genre: atmospheric
- Shape of the first page: Index-First (a directory listing), hero posture Ledge
- Theme: Terminal
- Axes: dark/mono/chromatic-green · posture: committed

## The mark
Four slashes typed in a row, `\/\/`, read as a w. Vector in `material/mark.svg` (currentColor strokes, 64 viewBox, round caps). On the page it is printed as a grid of characters taken from the page's own path names, in the eight glyph tokens, resolving row by row. The favicon (`site/favicon.svg`) is the same four strokes in the accent on the paper. The old W avatar is reference only.

## Tokens
`site/tokens.css` is the source of truth. The roles:
```css
:root {
  --color-paper: oklch(12.5% 0.012 150);  --color-paper-2: oklch(16% 0.016 150);  --color-paper-3: oklch(20.5% 0.022 150);
  --color-ink: oklch(94% 0.03 140);  --color-ink-2: oklch(82% 0.05 142);  --color-muted: oklch(64% 0.06 145);  --color-rule: oklch(27% 0.028 148);  --color-rule-2: oklch(38% 0.045 146);
  --color-accent: oklch(87% 0.2 142);  --color-accent-ink: oklch(14% 0.02 150);  --color-focus: oklch(87% 0.2 142);  --color-accent-wash: oklch(23% 0.06 145);
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
One hue in lightness steps; hairlines in `--color-rule`, firmer lines in `--color-rule-2`; no radius, no shadow, no glow. A capture of a light interface is inverted, then tinted with `--glyph-5`, so it reads as a phosphor screen inside a 1px rule. Photographs, if ever, in the theme's duotone, one a page at most.

## Controls
- Primary: a full-width accent block (`--color-accent` on `--color-accent-ink`), square, 72px tall, state in `steps(1)`.
- Secondary: a 1px `--color-ink-2` border, 48px tall, same square corners.
- Links: `--color-ink-2`, dotted underline, accent on hover; a selected row takes `--color-accent-wash`.

## Motion
- Character: severe. One reveal, the mark resolving row by row over about one second; cells flare to the accent under the cursor. Nothing else moves; under reduced motion everything ends at once.

## Voice
Paths, names, years. Declarative and short. No eyebrows, no middle dots, no arrows, no dashes.

## Exports
`site/tokens.css` in this project. Tailwind, DTCG or shadcn blocks are added here on request.
