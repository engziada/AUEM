# AUEM Website — الاتحاد العربي للطاقة والمعادن

Bilingual (Arabic RTL / English LTR) website for the **Arab Union for
Energy & Minerals (AUEM)**, founded 23 July 2026 in Salé, Morocco —
headquartered in Casablanca.

Content is managed by a web admin through **[Pages CMS](docs/CMS.md)** — no
programming needed to publish news, events, announcements, photos or to change
any page text.

## Structure

```
build.py              static site generator (Python 3, stdlib + optional Pillow)
.pages.yml            CMS schema — what the web admin can edit, and where
content/              ALL site copy and collections (JSON) — the only content source
  settings.json       organisation name, tagline, navigation, footer, contact email
  pages/*.json        one file per page (index, about, objectives, …)
  news/               collection: news articles
  events/             collection: events
  announcements/      collection: announcements (site-wide bar)
  gallery/            collection: gallery photos
  chatbot.json        assistant copy + knowledge base
assets/css/style.css  theme (incl. gallery, events, announcement bar)
assets/css/chatbot.css
assets/js/chatbot.js  chatbot widget + matcher
assets/js/main.js     mobile nav, announcement bar, gallery lightbox
assets/img/           brand marks
assets/img/uploads/   files uploaded through the CMS (optimised at build time)
docs/CMS.md           bilingual admin + developer guide
tools/                content/CMS validator, site checker, one-off migration
dist/                 generated output (ar/ + en/ + admin/ + root redirect)
```

## Build & run

```bash
python3 build.py                     # writes dist/
python3 build.py --out .preview      # build elsewhere (safe local preview)
python3 -m http.server 8000 --directory dist
# open http://localhost:8000 → auto-redirects to ar/ or en/
```

`build.py` reads only `content/**/*.json`; it contains no site copy. Optional
`GROQ_API_KEY` injects the chatbot LLM key (see below).

## Editing content

- **Web admin (no GitHub account needed):** see [docs/CMS.md](docs/CMS.md).
  One-time setup: install the Pages CMS GitHub App on this repository, then
  invite editors by email. Every save is a commit and the site rebuilds itself.
- **Developer:** edit `content/**/*.json` directly, keeping field names in sync
  with `.pages.yml`, then run:

  ```bash
  python3 tools/check_content.py   # schema ↔ content consistency (needs pyyaml)
  python3 tools/check_site.py dist # broken links / missing assets after a build
  ```

Bilingual values are always `{"ar": "...", "en": "..."}`; an empty translation
falls back to the other language, so a half-translated entry never breaks a page.
`content.py` is retired — it is kept as a stub for history only.

## GitHub Pages deployment

`.github/workflows/deploy.yml` runs on every push to `main`, on demand, and once
a day (so upcoming events become past events and expired announcements drop off):

1. installs `pyyaml` + `pillow`,
2. validates the content against `.pages.yml`,
3. runs `build.py`,
4. publishes `dist/` to GitHub Pages.

In the repository: **Settings → Pages → Source → GitHub Actions** (already set).

## Images

Uploads go through the CMS into `assets/img/uploads/<section>/`. At build time
`build.py` (with Pillow available) downscales them to 2000 px, writes 760 px
thumbnails under `uploads/thumbs/`, and converts the two oversized brand PNGs to
WebP (~34 KB instead of 2.8 MB). Without Pillow everything is copied as-is.

## Chatbot — 4-tier fallback

`assets/js/chatbot.js` answers questions through a fallback cascade, always inside
the site's own medallion launcher/panel (hosted services never inject their own
bubbles):

1. **Chatbase** — iframe embed in the panel; skipped if it fails to load within 8s.
2. **Botpress webchat** — iframe "shareable" embed; skipped on load failure.
3. **Groq LLM** (`allam-2-7b`) — retrieval-augmented with the site knowledge base.
   The API key is injected at build time from `GROQ_API_KEY` (never committed).
4. **Built-in offline matcher** — keyword scoring over the same knowledge base.

### Setup

- **Local:** `$env:GROQ_API_KEY="gsk_..."` before running `python3 build.py`.
- **CI:** add `GROQ_API_KEY` under repo *Settings → Secrets and variables → Actions*.
- **Teach the bot:** edit **المساعد الذكي — Chatbot knowledge** in the CMS
  (`content/chatbot.json`: keywords + Arabic/English answer), then save.

Keep the key free-tier only; it is shipped to the client, so rotate it if abused.
