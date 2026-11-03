# walior.it

The waliori hub: one page that points at the channel, the accounts, the videos, the repositories and the projects, laid out as a directory listing on a white-phosphor terminal.

## What is where

- `site/` is everything the Worker serves: `index.html`, `style.css`, `tokens.css` and `base.css`, the frames in `images/` (each resting frame also at 800px, which is what the page loads), the face in `fonts/` (Martian Mono, self-hosted), the share card `og.png`, `favicon.svg`, `robots.txt`, `sitemap.xml`, `llms.txt`, and the `_headers` and `_redirects` files that Cloudflare reads.
- `videos.json` lists the videos (path, title, upload date, YouTube id), newest first. `repos.json` holds what the GitHub API returned for the eight repositories (stars, last push, languages, a year of weekly commit counts). `links.json` holds the account and project addresses.
- `design.md` is the locked design system: the tokens, the type, the mark, the objects on the page, and the one exception to the monochrome (colour on hover).
- `material/` is the source material: the old avatar, the raw captures in `screens/`, the thumbnails in `thumbs/`, the vector mark, the share card source, and `profile/` (the avatar and the two banners, rendered from `avatar.html` and `banner.html`).
- `tools/` regenerates the pictures:
  - `frames.mjs` captures several screens of each product into `material/screens/` (needs `puppeteer-core`, pointed at with `PUPPETEER_PATH`, and Chrome via `CHROME_PATH`).
  - `still.mjs` also takes a `file://…?query` URL, which `material/thumbs/render.sh` uses to render the YouTube thumbnails from `material/thumbs/thumb.html`, one frame and one path each (list in `material/thumbs/list.txt`).
  - `still.mjs` renders one HTML file at a given size, for the share card and the profile images (same two variables).
  - `crt.py` bakes one capture into a CRT frame with ImageMagick: grey or colour, inverted for a light interface, noise, bloom, scanlines, a few torn bands, a barrel curve and a vignette.
  - `bake-all.sh` runs `crt.py` over every frame the page uses, three at a time with a thread cap. Pass a substring to bake only some, for example `-c.webp` for the colour variants.
  - `glyphs.py` prints the mark into `index.html` as a grid of characters taken from the page's own paths.

## How the page works

The hero is the mark and the index of four accounts; `/youtube` is the one white row at rest, and whichever row is under the pointer takes the white. Under `/videos`, the rows are the videos and the monitor beside them shows the thumbnail of the row under the pointer, in colour while the pointer is on the block and in grey when it leaves. Under `/github`, each repository row draws its last 52 weeks of commits as 52 cells. Under `/projects`, each site has a CRT frame that plays more of its screens on hover. On a touch screen there is no hover, so the row at the monitor's edge drives it as the page scrolls, a tap lights a row, a tap on the lit row opens it, and a project screen plays while it is in view. Nothing on the page needs a script to read; the scripts only add these behaviours.

## Content changes

Edit `videos.json`, `repos.json` or the markup in `site/index.html` directly; the lists are short enough to keep by hand. Refresh `repos.json` with `gh api` (the fields it needs are visible in the file). After a recapture, run `tools/bake-all.sh`.

## Deploy

Cloudflare Workers Builds deploys on every push to `main` with `npx wrangler deploy`; `wrangler.toml` serves `site/` as static assets. `walior.it` and `www.walior.it` are the Worker's custom domains; `worker.mjs` sends www to the apex.
