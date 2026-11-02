# walior.it

The waliori hub: one page that points at the channel, the accounts, the videos, the repositories and the projects, laid out as a directory listing on a white-phosphor terminal.

## What is where

- `site/` is everything the Worker serves: `index.html`, `style.css`, `tokens.css` and `base.css`, the frames in `images/`, the share card `og.png`, `favicon.svg`, `robots.txt`, `sitemap.xml`, `llms.txt`, and the `_headers` and `_redirects` files that Cloudflare reads.
- `videos.json` lists the videos (path, title, upload date, YouTube id), newest first. `repos.json` holds what the GitHub API returned for the eight repositories (stars, last push, languages, a year of weekly commit counts). `links.json` holds the account and project addresses.
- `design.md` is the locked design system: the tokens, the type, the mark, the objects on the page, and the one exception to the monochrome (colour on hover).
- `material/` is the source material: the old avatar, the raw captures in `screens/`, the thumbnails in `thumbs/`, the vector mark and the share card source.
- `tools/` regenerates the pictures:
  - `frames.mjs` captures several screens of each product into `material/screens/` (needs `puppeteer-core`, pointed at with `PUPPETEER_PATH`, and Chrome via `CHROME_PATH`).
  - `crt.py` bakes one capture into a CRT frame with ImageMagick: grey or colour, inverted for a light interface, noise, bloom, scanlines, a few torn bands, a barrel curve and a vignette.
  - `bake-all.sh` runs `crt.py` over every frame the page uses, three at a time with a thread cap. Pass a substring to bake only some, for example `-c.webp` for the colour variants.
  - `glyphs.py` prints the mark into `index.html` as a grid of characters taken from the page's own paths.

## How the page works

The hero is the mark and the index of four accounts; `/youtube` is the one white row at rest, and whichever row is under the pointer takes the white. Under `/videos`, the rows are the videos and the monitor beside them shows the thumbnail of the row under the pointer, in colour while the pointer is on the block and in grey when it leaves. Under `/github`, each repository row draws its last 52 weeks of commits as 52 cells. Under `/projects`, each site has a CRT frame that plays more of its screens on hover. Nothing on the page needs a script to read; the scripts only add the hover behaviour.

## Content changes

Edit `videos.json`, `repos.json` or the markup in `site/index.html` directly; the lists are short enough to keep by hand. Refresh `repos.json` with `gh api` (the fields it needs are visible in the file). After a recapture, run `tools/bake-all.sh`.

## Deploy

Cloudflare Workers Builds deploys on every push to `main` with `npx wrangler deploy`; `wrangler.toml` serves `site/` as static assets. The custom domains are added as routes at the switch from the old host.
