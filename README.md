# AUEM Website — الاتحاد العربي للطاقة والمعادن

Bilingual (Arabic RTL / English LTR) static website for the **Arab Union for
Energy & Minerals (AUEM)**, founded 23 July 2026 in Salé, Morocco —
headquartered in Casablanca.

## Structure

```
build.py              static site generator (Python 3, stdlib only)
content.py            ALL site copy — edit text here, never the HTML
assets/css/style.css  theme
assets/css/chatbot.css
assets/js/chatbot.js  chatbot widget + matcher
assets/js/main.js
assets/img/AUEM_logo_only_trans.png  mark only (navbar / favicon / footer)
assets/img/AUEM_logo_trans.png       mark + wordmark (hero)
dist/                 generated output (ar/ + en/ + root redirect)
```

## Build & run

```bash
python3 build.py
python3 -m http.server 8000 --directory dist
# open http://localhost:8000 → auto-redirects to ar/ or en/
```

## GitHub Pages Deployment

The repository is configured for automated deployment via GitHub Actions (`.github/workflows/deploy.yml`):
1. In your GitHub repository settings, go to **Settings** → **Pages**.
2. Under **Build and deployment** → **Source**, select **GitHub Actions**.
3. Every push to the `main` branch will automatically run `build.py` and publish the `dist/` directory to GitHub Pages.

## Editing content

Every string lives in `content.py` (paired `{"ar": ..., "en": ...}` dicts).
Run `python3 build.py` to regenerate `dist/`.

## Chatbot — 3-tier fallback

`assets/js/chatbot.js` answers questions through a fallback cascade:

1. **Botpress Free webchat** — if its script loads and initialises within 4s, its own widget takes over (100 conversations/month on the free plan). Disable with `BOTPRESS.enabled = false`.
2. **Groq LLM** (`allam-2-7b`, SDAIA's Arabic-first model on the free tier) — retrieval-augmented with the site knowledge base. The API key is injected at build time from the `GROQ_API_KEY` environment variable (never committed). On error, falls back per-message.
3. **Built-in offline matcher** — keyword scoring over the same knowledge base, always available, bilingual.

### Setup

- **Local:** `$env:GROQ_API_KEY="gsk_..."` before running `python3 build.py` (optional — without it, tier 2 is skipped).
- **CI:** add `GROQ_API_KEY` under repo *Settings → Secrets and variables → Actions*.
- **Teach the bot:** add entries to `KB` in `content.py` (`kw_ar`/`kw_en` keywords, `a_ar`/`a_en` answers), then rebuild — all three tiers use the same knowledge base.

Keep the key free-tier only; it is shipped to the client, so rotate it if abused.
