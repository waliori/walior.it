# walior.it

The waliori hub: one page that points at the channel, the accounts and the projects, laid out as a directory listing.

- `site/` is what the Worker serves: the page, its stylesheet and tokens, the captures, the share card, robots, sitemap, llms.txt, `_headers` and `_redirects`.
- `videos.json` and `links.json` are the hand-kept content; `site/index.html` is written from them (the list is small enough to edit by hand).
- `design.md` is the locked design system; `material/` holds the source material (the old avatar, the captures, the vector mark, the share card source).
- `docs/superpowers/specs/` holds the design document.

Deploys run from Cloudflare Workers Builds on every push to main (`npx wrangler deploy`, static assets only).
