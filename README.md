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
assets/img/logo.svg
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

## Chatbot

Default: a self-contained bilingual assistant (`assets/js/chatbot.js`) that
answers visitor questions from the embedded knowledge base
(`KB` in `content.py` → generated `assets/js/kb.js`). Add entries to `KB`
to teach it new answers — keyword lists in `kw_ar`/`kw_en`, answers in
`a_ar`/`a_en`.

### Botpress Integration

The website is integrated with Botpress Cloud Webchat v3.7 (`assets/js/chatbot.js`).
Configuration:

```js
var BOTPRESS = {
  enabled: true,
  injectUrl: "https://cdn.botpress.cloud/webchat/v3.7/inject.js",
  configUrl: "https://files.bpcontent.cloud/2026/09/21/08/20260921084023-3L5AZOLU.json",
  botId: "98b9ddc5-cfe5-4616-a4cc-f89a6e41230a",
  clientId: "9948b22e-c4e5-414f-a3cf-6b4878b85886",
  configuration: {
    website: {},
    email: {},
    phone: {},
    termsOfService: {},
    privacyPolicy: {}
  },
  scriptUrls: []
};
```

Set `BOTPRESS.enabled = false` to switch back to the built-in offline knowledge-base assistant anytime.
