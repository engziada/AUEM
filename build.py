#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Static site generator for the AUEM bilingual website.

Builds dist/ar/*.html and dist/en/*.html from the JSON files under content/ —
no external dependencies (Pillow is used when available to shrink images).

content/ is edited by the web admin through Pages CMS (.pages.yml), so nothing
in this file or in the templates holds site copy any more.

    python3 build.py                 # build into ./dist
    python3 build.py --out .preview  # build somewhere else (local check)
"""
import argparse
import json
import os
import re
import shutil
import sys
from datetime import date, datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.join(ROOT, "content")
ASSETS = os.path.join(ROOT, "assets")
DEFAULT_OUT = os.path.join(ROOT, "dist")
LANGS = ("ar", "en")
UPLOADS = "/assets/img/uploads/"

# Set by process_media(): whether downscaled thumbnails / WebP copies exist.
THUMBS = False
WEBP = False


# --------------------------------------------------------------------------
# loading
# --------------------------------------------------------------------------
def load_json(path, default=None):
    if not os.path.exists(path):
        return default
    with open(path, encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError as exc:
            raise SystemExit(f"invalid JSON in {os.path.relpath(path, ROOT)}: {exc}")


def load_pages():
    pages = {}
    folder = os.path.join(CONTENT, "pages")
    if not os.path.isdir(folder):
        raise SystemExit("content/pages/ is missing — run tools/migrate_content.py")
    for name in sorted(os.listdir(folder)):
        if not name.endswith(".json"):
            continue
        pid = name[: -len(".json")]
        pages[pid] = load_json(os.path.join(folder, name), {})
    return pages


def load_collection(name):
    """Read a folder of CMS entries, newest first, unpublished/drafts removed."""
    folder = os.path.join(CONTENT, name)
    items = []
    if not os.path.isdir(folder):
        return items
    for filename in sorted(os.listdir(folder)):
        if not filename.endswith(".json") or filename.startswith(("_", ".")):
            continue
        item = load_json(os.path.join(folder, filename), {})
        if not isinstance(item, dict) or item.get("published") is False:
            continue
        item["_slug"] = filename[: -len(".json")]
        items.append(item)
    items.sort(key=lambda it: (item_date(it), it["_slug"]), reverse=True)
    return items


def item_date(item):
    for key in ("date", "start_date", "published_at"):
        raw = item.get(key)
        if raw:
            return parse_iso(str(raw)) or date.min
    return date.min


SETTINGS = {}
CHATBOT = {}
PAGES = {}
NEWS = []
EVENTS = []
ANNOUNCEMENTS = []
GALLERY = []
SITE_URL = ""


def load_content():
    """Read every CMS-editable JSON file into the module globals."""
    global SETTINGS, CHATBOT, PAGES, NEWS, EVENTS, ANNOUNCEMENTS, GALLERY, SITE_URL
    SETTINGS = load_json(os.path.join(CONTENT, "settings.json"), {})
    CHATBOT = load_json(os.path.join(CONTENT, "chatbot.json"), {})
    PAGES = load_pages()
    NEWS = load_collection("news")
    EVENTS = load_collection("events")
    ANNOUNCEMENTS = load_collection("announcements")
    GALLERY = load_collection("gallery")
    SITE_URL = (SETTINGS.get("site_url") or "").rstrip("/")


# --------------------------------------------------------------------------
# small helpers
# --------------------------------------------------------------------------
def esc(value):
    return (
        str(value)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def L(value, lang):
    """Localized string: {'ar','en'} pairs, plain strings, or nothing.

    A missing translation falls back to the other language so a half-translated
    entry never breaks the build or shows an empty paragraph.
    """
    if value is None:
        return ""
    if isinstance(value, dict):
        text = value.get(lang)
        if not text:
            text = value.get("en" if lang == "ar" else "ar")
        if not text:
            text = next((v for v in value.values() if v), "")
        return str(text)
    return str(value)


def has_text(value, lang):
    return bool(L(value, lang).strip())


def paras(text, lang):
    return "\n".join(
        f"<p>{esc(p.strip())}</p>" for p in L(text, lang).split("\n") if p.strip()
    )


def parse_iso(raw):
    raw = str(raw).strip()
    for fmt in ("%Y-%m-%d", "%Y/%m/%d", "%Y-%m-%dT%H:%M", "%Y-%m-%dT%H:%M:%S"):
        try:
            return datetime.strptime(raw[: len("2026-01-01T00:00:00")], fmt).date()
        except ValueError:
            continue
    match = re.match(r"^(\d{4})-(\d{2})-(\d{2})", raw)
    if match:
        return date(int(match.group(1)), int(match.group(2)), int(match.group(3)))
    return None


AR_MONTHS = [
    "يناير", "فبراير", "مارس", "أبريل", "مايو", "يونيو",
    "يوليو", "أغسطس", "سبتمبر", "أكتوبر", "نوفمبر", "ديسمبر",
]
EN_MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]
EN_MONTHS_SHORT = [m[:3] for m in EN_MONTHS]


def fmt_date(raw, lang, short=False):
    d = parse_iso(raw)
    if not d:
        return esc(raw or "")
    if lang == "ar":
        return f"{d.day} {AR_MONTHS[d.month - 1]} {d.year}"
    month = EN_MONTHS_SHORT[d.month - 1] if short else EN_MONTHS[d.month - 1]
    return f"{d.day} {month} {d.year}"


def img_url(path):
    """Turn a CMS media path into a URL usable from /ar/ and /en/ pages."""
    raw = str(path or "").strip()
    if not raw:
        return ""
    if raw.startswith(("http://", "https://", "//")):
        return raw
    if raw.startswith("../"):
        return raw
    if raw.startswith("/"):
        return ".." + raw
    return "../" + raw


def thumb_url(path):
    raw = str(path or "").strip()
    if THUMBS and raw.startswith(UPLOADS):
        return img_url(raw.replace(UPLOADS, UPLOADS + "thumbs/", 1))
    return img_url(path)


def read_more(text, lang, limit=230):
    """First paragraph-ish slice of a body, cut on a word boundary."""
    body = " ".join(L(text, lang).split())
    if len(body) <= limit:
        return body
    cut = body[:limit]
    space = cut.rfind(" ")
    return (cut[:space] if space > limit * 0.6 else cut).rstrip() + "…"


def brand_picture(name, alt, css_class=""):
    """<picture> with a WebP source and the PNG fallback for the brand marks."""
    cls = f' class="{css_class}"' if css_class else ""
    stem = os.path.splitext(name)[0]
    png = f'<img src="../assets/img/{name}" alt="{esc(alt)}"{cls}>'
    if not WEBP:
        return png
    return (
        f'<picture><source srcset="../assets/img/{stem}.webp" type="image/webp">{png}</picture>'
    )


def icon(name):
    icons = {
        "oil": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 3s6 6.3 6 11a6 6 0 1 1-12 0c0-4.7 6-11 6-11z"/><path d="M9.5 14.5a2.5 2.5 0 0 0 2.5 2.5"/></svg>',
        "mining": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 2l7 5-7 15L5 7l7-5z"/><path d="M5 7h14M12 2l-3 5 3 15 3-15-3-5z"/></svg>',
        "renewable": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="4"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M19.1 4.9L17 7M7 17l-2.1 2.1"/></svg>',
        "invest": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 17l6-6 4 4 8-8"/><path d="M15 7h6v6"/></svg>',
        "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 21s7-6.1 7-11a7 7 0 1 0-14 0c0 4.9 7 11 7 11z"/><circle cx="12" cy="10" r="2.6"/></svg>',
        "calendar": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M8 3v4M16 3v4M3 10h18"/></svg>',
        "image": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="8.5" cy="9.5" r="1.6"/><path d="M21 16l-5-5-6 6-3-3-4 4"/></svg>',
    }
    return icons.get(name, "")


# --------------------------------------------------------------------------
# layout
# --------------------------------------------------------------------------
def nav_items():
    """Navigation entries whose page actually exists in content/pages/."""
    items = []
    for entry in SETTINGS.get("nav") or []:
        pid = entry.get("page")
        if pid and pid in PAGES:
            items.append((pid, entry.get("label") or pid))
    return items


def footer_page_ids():
    return [pid for pid, _ in nav_items()][:6]


def active_announcements():
    today = date.today()
    live = []
    for item in ANNOUNCEMENTS:
        if not item.get("active"):
            continue
        expires = parse_iso(item.get("expires") or "")
        if expires and expires < today:
            continue
        live.append(item)
    return live


def announce_bar(lang):
    items = [a for a in active_announcements() if has_text(a.get("body"), lang) or has_text(a.get("title"), lang)]
    if not items:
        return ""
    messages = []
    for item in items:
        text = L(item.get("body"), lang) or L(item.get("title"), lang)
        url = str(item.get("link_url") or "").strip()
        link = ""
        if url:
            label = L(item.get("link_label"), lang) or L(item.get("title"), lang)
            link = f'<a class="announce-link" href="{esc(url)}">{esc(label)}</a>'
        level = " important" if str(item.get("level") or "") == "important" else ""
        messages.append(
            f'<div class="announce-msg{level}" data-announce-id="{esc(item["_slug"])}">'
            f'<span class="announce-text">{esc(text)}</span>{link}</div>'
        )
    return f"""
<aside class="announce-bar" id="announce-bar" hidden aria-live="polite">
  <div class="container announce-inner">
    <div class="announce-track">{"".join(messages)}</div>
    <button class="announce-close" type="button" aria-label="{'إغلاق' if lang == 'ar' else 'Dismiss'}">×</button>
  </div>
</aside>
"""


def base(page_id, lang, body, title=None, description=None):
    p = PAGES[page_id]
    t = L(title or p.get("title"), lang)
    desc = L(description or p.get("meta"), lang)
    dirv = "rtl" if lang == "ar" else "ltr"
    other = "en" if lang == "ar" else "ar"
    site_name = L(SETTINGS.get("name"), lang)

    nav_links = "\n".join(
        f'<a href="{esc(pid)}.html" class="nav-link{" active" if pid == page_id else ""}">{esc(L(lbl, lang))}</a>'
        for pid, lbl in nav_items()
    )
    switch = (
        f'<a class="lang-switch" href="../{other}/{page_id}.html" lang="{other}" '
        f'hreflang="{other}">{"English" if other == "en" else "العربية"}</a>'
    )
    nav_labels = dict(nav_items())
    foot_links = "\n".join(
        f'<a href="{esc(pid)}.html">{esc(L(nav_labels.get(pid), lang))}</a>'
        for pid in footer_page_ids()
    )
    canonical = ""
    if SITE_URL:
        page_url = SITE_URL + "/" + lang + "/" + page_id + ".html"
        ar_url = SITE_URL + "/ar/" + page_id + ".html"
        en_url = SITE_URL + "/en/" + page_id + ".html"
        canonical = (
            '\n<link rel="canonical" href="' + esc(page_url) + '">'
            '\n<link rel="alternate" hreflang="ar" href="' + esc(ar_url) + '">'
            '\n<link rel="alternate" hreflang="en" href="' + esc(en_url) + '">'
        )
    footer = SETTINGS.get("footer") or {}
    contact_page = PAGES.get("contact") or {}
    contact_link = (
        f'<p><a href="contact.html">{esc(L(contact_page.get("title"), lang))}</a></p>'
        if contact_page
        else ""
    )
    return f"""<!doctype html>
<html lang="{lang}" dir="{dirv}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(t)} — {esc(site_name)}</title>
<meta name="description" content="{esc(desc)}">
<meta property="og:title" content="{esc(t)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{esc(site_name)}">{canonical}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=Cinzel:wght@600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../assets/css/style.css">
<link rel="stylesheet" href="../assets/css/chatbot.css">
<link rel="icon" href="../assets/img/AUEM_logo_only_trans.png" type="image/png">
</head>
<body>
<header class="site-header">
  <div class="container header-inner">
    <a class="brand" href="index.html">
      {brand_picture("AUEM_logo_only_trans.png", site_name, "brand-logo")}
      <span class="brand-text"><strong>{esc(site_name)}</strong><small>{esc(SETTINGS.get("abbr", "AUEM"))}</small></span>
    </a>
    <button class="nav-toggle" aria-label="menu" aria-expanded="false" aria-controls="main-nav" onclick="document.body.classList.toggle('nav-open')"><span></span><span></span><span></span></button>
    <nav class="main-nav" id="main-nav">{nav_links}</nav>
    {switch}
  </div>
  <div class="nav-backdrop" onclick="document.body.classList.remove('nav-open')"></div>
</header>{announce_bar(lang)}
<main>{body}</main>
<footer class="site-footer">
  <div class="container footer-grid">
    <div>
      <div class="footer-brand">{brand_picture("AUEM_logo_only_trans.png", "", "brand-logo")}<strong>{esc(site_name)}</strong></div>
      <p>{esc(L(footer.get("about"), lang))}</p>
      <p class="muted small">{esc(L(footer.get("disclaimer"), lang))}</p>
    </div>
    <div>
      <h4>{esc(L(footer.get("links_title"), lang))}</h4>
      <div class="footer-links">{foot_links}</div>
    </div>
    <div>
      <h4>{esc(L(footer.get("contact_title"), lang))}</h4>
      <p class="muted">{icon("pin")} {esc(L(SETTINGS.get("hq"), lang))}</p>
      {contact_link}
    </div>
  </div>
  <div class="container footer-bottom">© {esc(site_name)} — {esc(L(footer.get("rights"), lang))}</div>
</footer>
<script src="../assets/js/kb.js"></script>
<script src="../assets/js/chatbot.js"></script>
<script src="../assets/js/main.js"></script>
</body>
</html>
"""


def page_head(pid, lang):
    return (
        '<section class="page-head"><div class="container">'
        f'<h1>{esc(L(PAGES[pid].get("title"), lang))}</h1>'
        "</div></section>"
    )


def empty_state(text, lang):
    return f'<p class="empty-state">{icon("image")}<span>{esc(L(text, lang))}</span></p>'


# --------------------------------------------------------------------------
# shared cards (news / events / gallery)
# --------------------------------------------------------------------------
def news_card(item, lang, compact=False):
    title = L(item.get("title"), lang)
    body_html = ""
    if compact:
        source_text = item.get("summary") if has_text(item.get("summary"), lang) else item.get("body")
        body_html = "<p>" + esc(read_more(source_text, lang, 220)) + "</p>"
    else:
        full = L(item.get("body"), lang).strip() or L(item.get("summary"), lang)
        body_html = "".join(
            "<p>" + esc(p.strip()) + "</p>" for p in full.split("\n") if p.strip()
        )
    image = item.get("image")
    media = ""
    if image:
        media = (
            f'<a class="card-media" href="{esc(img_url(image))}" target="_blank" rel="noopener">'
            f'<img src="{esc(thumb_url(image))}" alt="{esc(title)}" loading="lazy"></a>'
        )
    source = str(item.get("source") or "").strip()
    source_url = str(item.get("source_url") or "").strip()
    if source and source_url:
        source_html = f'<a class="source" href="{esc(source_url)}" target="_blank" rel="noopener">{esc(source)}</a>'
    elif source:
        source_html = f'<span class="source">{esc(source)}</span>'
    else:
        source_html = ""
    return f"""<article class="card news-card{" has-media" if image else ""}">{media}
        <div class="card-main"><time datetime="{esc(item.get("date"))}">{fmt_date(item.get("date"), lang)}</time>
        <h3>{esc(title)}</h3>{body_html}
        {source_html}</div></article>"""


def event_date_badge(item, lang):
    d = parse_iso(item.get("start_date"))
    if not d:
        return ""
    month = AR_MONTHS[d.month - 1] if lang == "ar" else EN_MONTHS_SHORT[d.month - 1]
    return (
        f'<div class="event-date"><span class="event-day">{d.day}</span>'
        f'<span class="event-month">{esc(month)}</span>'
        f'<span class="event-year">{d.year}</span></div>'
    )


def event_card(item, lang, register_label=None):
    title = L(item.get("title"), lang)
    image = item.get("image")
    media = ""
    if image:
        media = (
            f'<a class="card-media" href="{esc(img_url(image))}" target="_blank" rel="noopener">'
            f'<img src="{esc(thumb_url(image))}" alt="{esc(title)}" loading="lazy"></a>'
        )
    url = str(item.get("registration_url") or "").strip()
    register = ""
    if url:
        label = register_label or "Register"
        register = f'<a class="btn btn-outline" href="{esc(url)}" target="_blank" rel="noopener">{esc(label)}</a>'
    end = parse_iso(item.get("end_date"))
    start = parse_iso(item.get("start_date"))
    dates = fmt_date(item.get("start_date"), lang)
    if end and start and end != start:
        dates = f"{fmt_date(item.get('start_date'), lang)} – {fmt_date(item.get('end_date'), lang)}"
    location = L(item.get("location"), lang)
    summary = L(item.get("summary"), lang)
    meta_line = icon("calendar") + " " + esc(dates)
    if location:
        meta_line += " · " + icon("pin") + " " + esc(location)
    summary_html = "<p>" + esc(summary) + "</p>" if summary else ""
    return f"""<article class="card event-card{" has-media" if image else ""}">{media}
        <div class="card-main">
          {event_date_badge(item, lang)}
          <h3>{esc(title)}</h3>
          <p class="event-meta muted small">{meta_line}</p>
          {summary_html}
          {register}
        </div></article>"""


def event_row(item, lang):
    title = L(item.get("title"), lang)
    location = L(item.get("location"), lang)
    location_html = (
        '<p class="muted small">' + icon("pin") + " " + esc(location) + "</p>" if location else ""
    )
    return f"""<article class="event-row">
        <time datetime="{esc(item.get("start_date"))}">{fmt_date(item.get("start_date"), lang)}</time>
        <div><h3>{esc(title)}</h3>{location_html}</div>
      </article>"""


def gallery_item(photo, lang):
    caption = L(photo.get("caption"), lang)
    image = photo.get("image")
    if not image:
        return ""
    return f"""<button class="gallery-item" type="button" data-full="{esc(img_url(image))}" data-caption="{esc(caption)}">
        <img src="{esc(thumb_url(image))}" alt="{esc(caption)}" loading="lazy">
        <span class="gallery-cap">{esc(caption)}</span></button>"""


# --------------------------------------------------------------------------
# pages
# --------------------------------------------------------------------------
def hero(lang):
    p = PAGES["index"]
    return f"""
<section class="hero">
  <div class="container hero-inner">
    <div class="hero-text">
      <p class="kicker">{icon("calendar")} {esc(L(p.get("hero_kicker"), lang))}</p>
      <h1>{esc(L(SETTINGS.get("name"), lang))}</h1>
      <p class="hero-tagline">{esc(L(SETTINGS.get("tagline"), lang))}</p>
      <p class="hero-sub">{esc(L(p.get("hero_sub"), lang))}</p>
      <div class="hero-cta">
        <a class="btn btn-primary" href="about.html">{esc(L(p.get("cta_primary"), lang))}</a>
        <a class="btn btn-outline" href="membership.html">{esc(L(p.get("cta_secondary"), lang))}</a>
      </div>
    </div>
    <div class="hero-emblem">{brand_picture("AUEM_logo_trans.png", SETTINGS.get("abbr", "AUEM"))}</div>
  </div>
</section>
"""


def page_index(lang):
    p = PAGES["index"]
    stats = "".join(
        f'<div class="stat"><strong>{esc(L(s.get("value"), lang))}</strong><span>{esc(L(s.get("label"), lang))}</span></div>'
        for s in p.get("stats") or []
    )
    sectors = "".join(
        f"""<div class="card sector-card"><div class="icon-wrap">{icon(s.get("icon"))}</div>
        <h3>{esc(L(s.get("name"), lang))}</h3><p>{esc(L(s.get("desc"), lang))}</p></div>"""
        for s in p.get("sectors") or []
    )
    latest_news = NEWS[:2]
    news = "".join(news_card(n, lang, compact=True) for n in latest_news)
    partners = "".join(f"<li>{esc(L(x, lang))}</li>" for x in p.get("partners") or [])

    upcoming = [e for e in EVENTS if (parse_iso(e.get("start_date")) or date.min) >= date.today()][:2]
    events_section = ""
    if upcoming:
        cards = "".join(event_card(e, lang) for e in upcoming)
        events_section = f"""
<section class="section"><div class="container">
  <h2 class="section-title">{esc(L(p.get("events_title"), lang))}</h2>
  <div class="grid-2">{cards}</div>
  <a class="link-more" href="events.html">{esc(L(p.get("events_more"), lang))} ←</a>
</div></section>"""

    photos = [g for g in GALLERY if g.get("image")][:6]
    gallery_section = ""
    if photos:
        items = "".join(gallery_item(g, lang) for g in photos)
        gallery_section = f"""
<section class="section alt"><div class="container">
  <h2 class="section-title">{esc(L(p.get("gallery_title"), lang))}</h2>
  <p class="section-sub">{esc(L(p.get("gallery_sub"), lang))}</p>
  <div class="gallery-grid">{items}</div>
  <a class="link-more" href="gallery.html">{esc(L(p.get("gallery_more"), lang))} ←</a>
</div></section>"""

    news_section = ""
    if latest_news:
        news_section = f"""
    <h2 class="section-title">{esc(L(p.get("news_title"), lang))}</h2>
    <div class="stack">{news}</div>
    <a class="link-more" href="news.html">{esc(L(p.get("news_more"), lang))} ←</a>"""

    body = hero(lang) + f"""
<section class="section"><div class="container">
  <h2 class="section-title">{esc(L(p.get("stats_title"), lang))}</h2>
  <div class="stats-grid">{stats}</div>
</div></section>
<section class="section alt"><div class="container">
  <h2 class="section-title">{esc(L(p.get("sectors_title"), lang))}</h2>
  <p class="section-sub">{esc(L(p.get("sectors_sub"), lang))}</p>
  <div class="grid-4">{sectors}</div>
</div></section>
<section class="section"><div class="container split">
  <div>
    <h2 class="section-title">{esc(L(p.get("about_teaser_title"), lang))}</h2>
    <p>{esc(L(p.get("about_teaser"), lang))}</p>
    <a class="btn btn-primary" href="about.html">{esc(L(p.get("about_more"), lang))}</a>
  </div>
  <div>{news_section}</div>
</div></section>{gallery_section}{events_section}
<section class="section alt"><div class="container">
  <h2 class="section-title">{esc(L(p.get("partners_title"), lang))}</h2>
  <p class="section-sub">{esc(L(p.get("partners_sub"), lang))}</p>
  <ul class="partners">{partners}</ul>
</div></section>
<section class="cta-band"><div class="container cta-inner">
  <h2>{esc(L(p.get("join_title"), lang))}</h2>
  <p>{esc(L(p.get("join_sub"), lang))}</p>
  <a class="btn btn-light" href="membership.html">{esc(L(p.get("join_cta"), lang))}</a>
</div></section>
"""
    return base("index", lang, body)


def page_about(lang):
    p = PAGES["about"]
    pillars = "".join(f"<li>{esc(L(x, lang))}</li>" for x in p.get("pillars") or [])
    timeline = "".join(
        f'<div class="tl-item"><span class="tl-date">{esc(L(t.get("date"), lang))}</span><p>{esc(L(t.get("text"), lang))}</p></div>'
        for t in p.get("timeline") or []
    )
    photo = str(p.get("president_photo") or "").strip()
    avatar = (
        f'<img class="avatar-img" src="{esc(thumb_url(photo))}" alt="{esc(L(p.get("president_name"), lang))}">'
        if photo
        else '<div class="avatar">SB</div>'
    )
    body = page_head("about", lang) + f"""
<section class="section"><div class="container prose">
  <h2>{esc(L(p.get("intro_title"), lang))}</h2>
  {paras(p.get("intro"), lang)}
  <div class="quote-box">
    <h2>{esc(L(p.get("vision_title"), lang))}</h2>
    <p>{esc(L(p.get("vision"), lang))}</p>
  </div>
  <h2>{esc(L(p.get("mission_title"), lang))}</h2>
  {paras(p.get("mission"), lang)}
  <h2>{esc(L(p.get("context_title"), lang))}</h2>
  {paras(p.get("context"), lang)}
  <h2>{esc(L(p.get("pillars_title"), lang))}</h2>
  <ul class="check-list">{pillars}</ul>
  <div class="president-card card">
    {avatar}
    <div>
      <h3>{esc(L(p.get("president_title"), lang))}</h3>
      <blockquote>{esc(L(p.get("president_quote"), lang))}</blockquote>
      <p class="muted"><strong>{esc(L(p.get("president_name"), lang))}</strong> — {esc(L(p.get("president_role"), lang))}</p>
    </div>
  </div>
  <h2>{esc(L(p.get("timeline_title"), lang))}</h2>
  <div class="timeline">{timeline}</div>
</div></section>
"""
    return base("about", lang, body)


def page_objectives(lang):
    p = PAGES["objectives"]
    items = "".join(
        f'<div class="card obj-card"><span class="obj-num">{i + 1:02d}</span><p>{esc(L(x, lang))}</p></div>'
        for i, x in enumerate(p.get("items") or [])
    )
    body = page_head("objectives", lang) + f"""
<section class="section"><div class="container">
  <p class="section-sub">{esc(L(p.get("intro"), lang))}</p>
  <div class="grid-2">{items}</div>
</div></section>
"""
    return base("objectives", lang, body)


def page_governance(lang):
    p = PAGES["governance"]
    bodies = "".join(
        f'<div class="card"><h3>{esc(L(b.get("name"), lang))}</h3><p>{esc(L(b.get("desc"), lang))}</p></div>'
        for b in p.get("bodies") or []
    )
    commissions = "".join(f"<li>{esc(L(c, lang))}</li>" for c in p.get("commissions") or [])
    leaders = "".join(
        f'<div class="card leader"><h3>{esc(L(x.get("name"), lang))}</h3>'
        f'<p class="muted">{esc(L(x.get("role"), lang))}</p></div>'
        for x in p.get("leaders") or []
    )
    body = page_head("governance", lang) + f"""
<section class="section"><div class="container">
  <p class="section-sub">{esc(L(p.get("intro"), lang))}</p>
  <h2 class="section-title">{esc(L(p.get("bodies_title"), lang))}</h2>
  <div class="grid-4">{bodies}</div>
  <h2 class="section-title">{esc(L(p.get("commissions_title"), lang))}</h2>
  <p class="section-sub">{esc(L(p.get("commissions_sub"), lang))}</p>
  <ul class="tag-list">{commissions}</ul>
  <h2 class="section-title">{esc(L(p.get("leadership_title"), lang))}</h2>
  <div class="grid-2">{leaders}</div>
</div></section>
"""
    return base("governance", lang, body)


def page_membership(lang):
    p = PAGES["membership"]
    benefits = "".join(f"<li>{esc(L(b, lang))}</li>" for b in p.get("benefits") or [])
    body = page_head("membership", lang) + f"""
<section class="section"><div class="container prose">
  <h2>{esc(L(p.get("intro_title"), lang))}</h2>
  {paras(p.get("intro"), lang)}
  <h2>{esc(L(p.get("benefits_title"), lang))}</h2>
  <ul class="check-list">{benefits}</ul>
  <h2>{esc(L(p.get("how_title"), lang))}</h2>
  {paras(p.get("how"), lang)}
  <p class="note-box">{esc(L(p.get("note"), lang))}</p>
  <a class="btn btn-primary" href="contact.html">{esc(L(p.get("cta"), lang))}</a>
</div></section>
"""
    return base("membership", lang, body)


def page_activities(lang):
    p = PAGES["activities"]
    streams = "".join(
        f'<div class="card"><h3>{esc(L(s.get("name"), lang))}</h3><p>{esc(L(s.get("desc"), lang))}</p></div>'
        for s in p.get("streams") or []
    )
    roadmap = "".join(
        f'<div class="tl-item"><span class="tl-date">{esc(L(r.get("year"), lang))}</span><p>{esc(L(r.get("text"), lang))}</p></div>'
        for r in p.get("roadmap") or []
    )
    body = page_head("activities", lang) + f"""
<section class="section"><div class="container">
  <p class="section-sub">{esc(L(p.get("intro"), lang))}</p>
  <div class="grid-3">{streams}</div>
</div></section>
<section class="section alt"><div class="container">
  <h2 class="section-title">{esc(L(p.get("roadmap_title"), lang))}</h2>
  <p class="section-sub">{esc(L(p.get("roadmap_sub"), lang))}</p>
  <div class="timeline">{roadmap}</div>
</div></section>
"""
    return base("activities", lang, body)


def page_news(lang):
    p = PAGES["news"]
    items = "".join(news_card(n, lang) for n in NEWS)
    if not items:
        items = empty_state(p.get("empty_text"), lang)
    sources = "".join(
        f'<li><a href="{esc(s.get("url"))}" target="_blank" rel="noopener">{esc(s.get("title"))}</a></li>'
        for s in p.get("sources") or []
        if s.get("url")
    )
    sources_block = (
        f'<h2 class="section-title" style="margin-top:2.5rem">{esc(L(p.get("sources_title"), lang))}</h2>'
        f'<ul class="source-list">{sources}</ul>'
        if sources
        else ""
    )
    notices = [a for a in active_announcements()]
    notices_block = ""
    if notices:
        rows = "".join(
            f"""<article class="card notice-card{' important' if str(a.get('level') or '') == 'important' else ''}">
            <time datetime="{esc(a.get("date"))}">{fmt_date(a.get("date"), lang)}</time>
            <h3>{esc(L(a.get("title"), lang))}</h3>
            <p>{esc(L(a.get("body"), lang))}</p>
            {f'<a class="link-more" href="{esc(a.get("link_url"))}" target="_blank" rel="noopener">{esc(L(a.get("link_label"), lang) or L(a.get("title"), lang))} ←</a>' if str(a.get("link_url") or "").strip() else ""}
            </article>"""
            for a in notices
        )
        notices_block = f"""
<section class="section alt"><div class="container">
  <h2 class="section-title">{esc(L(p.get("announcements_title"), lang))}</h2>
  <div class="stack">{rows}</div>
</div></section>"""
    body = page_head("news", lang) + notices_block + f"""
<section class="section"><div class="container">
  <p class="section-sub">{esc(L(p.get("intro"), lang))}</p>
  <div class="stack">{items}</div>
  {sources_block}
</div></section>
"""
    return base("news", lang, body)


def page_events(lang):
    p = PAGES["events"]
    today = date.today()
    upcoming = [e for e in EVENTS if (parse_iso(e.get("start_date")) or date.min) >= today]
    past = [e for e in EVENTS if (parse_iso(e.get("start_date")) or date.min) < today]
    upcoming_html = "".join(event_card(e, lang, L(p.get("register_label"), lang)) for e in upcoming)
    if not upcoming_html:
        upcoming_html = empty_state(p.get("empty_upcoming"), lang)
    past_html = "".join(event_row(e, lang) for e in past)
    if not past_html:
        past_html = empty_state(p.get("empty_past"), lang)
    body = page_head("events", lang) + f"""
<section class="section"><div class="container">
  <p class="section-sub">{esc(L(p.get("intro"), lang))}</p>
  <h2 class="section-title">{esc(L(p.get("upcoming_title"), lang))}</h2>
  <div class="grid-2 events-grid">{upcoming_html}</div>
</div></section>
<section class="section alt"><div class="container">
  <h2 class="section-title">{esc(L(p.get("past_title"), lang))}</h2>
  {past_html}
</div></section>
"""
    return base("events", lang, body)


def page_gallery(lang):
    p = PAGES["gallery"]
    photos = [g for g in GALLERY if g.get("image")]
    if photos:
        grid = f'<div class="gallery-grid">{"".join(gallery_item(g, lang) for g in photos)}</div>'
    else:
        grid = empty_state(p.get("empty_text"), lang)
    body = page_head("gallery", lang) + f"""
<section class="section"><div class="container">
  <p class="section-sub">{esc(L(p.get("intro"), lang))}</p>
  {grid}
</div></section>
"""
    return base("gallery", lang, body)


def page_unions(lang):
    p = PAGES["unions"]
    groups = ""
    for g in p.get("groups") or []:
        cards = "".join(
            f"""<div class="card union-card">
            <div class="union-head"><h3>{esc(L(u.get("name"), lang))}</h3><span class="badge">{esc(u.get("est"))}</span></div>
            <p class="muted small">{esc(L(u.get("desc"), lang))}</p>
            <p class="union-hq">{icon("pin")} {esc(L(u.get("hq"), lang))}</p></div>"""
            for u in g.get("items") or []
        )
        groups += f'<h2 class="section-title">{esc(L(g.get("name"), lang))}</h2><div class="grid-3">{cards}</div>'
    orgs = "".join(
        f'<tr><td>{esc(L(o.get("name"), lang))}</td><td>{esc(o.get("est"))}</td><td>{esc(L(o.get("hq"), lang))}</td></tr>'
        for o in p.get("orgs") or []
    )
    th = (
        f"<tr><th>{'المنظمة' if lang == 'ar' else 'Organization'}</th>"
        f"<th>{'التأسيس' if lang == 'ar' else 'Founded'}</th>"
        f"<th>{'المقر' if lang == 'ar' else 'HQ'}</th></tr>"
    )
    body = page_head("unions", lang) + f"""
<section class="section"><div class="container prose">
  <h2>{esc(L(p.get("intro_title"), lang))}</h2>
  {paras(p.get("intro"), lang)}
</div></section>
<section class="section alt"><div class="container">{groups}</div></section>
<section class="section"><div class="container">
  <h2 class="section-title">{esc(L(p.get("orgs_title"), lang))}</h2>
  <p class="section-sub">{esc(L(p.get("orgs_sub"), lang))}</p>
  <div class="table-wrap"><table class="orgs-table">{th}{orgs}</table></div>
  <p class="note-box">{esc(L(p.get("note"), lang))}</p>
</div></section>
"""
    return base("unions", lang, body)


def page_contact(lang):
    p = PAGES["contact"]
    topics = "".join(f"<li>{esc(L(t, lang))}</li>" for t in p.get("topics") or [])
    to = SETTINGS.get("contact_email") or "info@auem.org"
    subj = "AUEM website inquiry" if lang == "en" else "استفسار عبر موقع الاتحاد"
    body = page_head("contact", lang) + f"""
<section class="section"><div class="container split">
  <div>
    <p class="section-sub">{esc(L(p.get("intro"), lang))}</p>
    <div class="card hq-card"><h3>{esc(L(p.get("hq_title"), lang))}</h3>
    <p>{icon("pin")} {esc(L(p.get("hq_value"), lang))}</p></div>
    <h3>{esc(L(p.get("topics_title"), lang))}</h3>
    <ul class="check-list">{topics}</ul>
  </div>
  <form class="card contact-form" action="mailto:{esc(to)}" method="post" enctype="text/plain">
    <label>{esc(L(p.get("form_name"), lang))}<input name="name" required></label>
    <label>{esc(L(p.get("form_org"), lang))}<input name="organization"></label>
    <label>{esc(L(p.get("form_email"), lang))}<input type="email" name="email" required></label>
    <label>{esc(L(p.get("form_subject"), lang))}<input name="subject" value="{esc(subj)}"></label>
    <label>{esc(L(p.get("form_message"), lang))}<textarea name="message" rows="6" required></textarea></label>
    <button class="btn btn-primary" type="submit">{esc(L(p.get("form_send"), lang))}</button>
    <p class="muted small">{esc(L(p.get("form_note"), lang))}</p>
  </form>
</div></section>
"""
    return base("contact", lang, body)


RENDERERS = {
    "index": page_index,
    "about": page_about,
    "objectives": page_objectives,
    "governance": page_governance,
    "membership": page_membership,
    "activities": page_activities,
    "news": page_news,
    "events": page_events,
    "gallery": page_gallery,
    "unions": page_unions,
    "contact": page_contact,
}

ROOT_REDIRECT = """<!doctype html><html><head><meta charset="utf-8">
<title>AUEM</title>
<script>var l=(navigator.language||'ar').slice(0,2);location.replace(l==='en'?'en/index.html':'ar/index.html');</script>
</head><body><a href="ar/index.html">العربية</a> · <a href="en/index.html">English</a></body></html>
"""

ADMIN_PAGE = """<!doctype html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>لوحة التحكم — AUEM CMS</title>
<link rel="stylesheet" href="../assets/css/style.css">
<style>
  .admin-wrap { max-width: 720px; margin: 0 auto; padding: clamp(2.5rem, 6vw, 5rem) 1.25rem; }
  .admin-wrap h1 { margin-bottom: .75rem; }
  .admin-wrap .lead { color: var(--ivory-200); line-height: 1.8; margin-bottom: 1.75rem; }
  .admin-steps { display: grid; gap: .85rem; margin: 1.5rem 0 2rem; padding: 0; list-style: none; }
  .admin-steps li { background: var(--bg-card, rgba(255,255,255,.04)); border: 1px solid var(--border-card, rgba(255,255,255,.12)); border-radius: .75rem; padding: .9rem 1.1rem; line-height: 1.7; }
  .admin-note { font-size: .9rem; color: var(--ivory-300); line-height: 1.7; }
  .admin-en { direction: ltr; text-align: left; margin-top: 2.5rem; border-top: 1px solid var(--border-card, rgba(255,255,255,.12)); padding-top: 1.5rem; }
</style>
</head>
<body>
<div class="admin-wrap">
  <h1>لوحة تحكم الموقع</h1>
  <p class="lead">يُدار محتوى الموقع — الصور والفعاليات والإعلانات ونصوص الصفحات — عبر لوحة تحكم
  <strong>Pages CMS</strong>. تُحفظ التغييرات في مستودع الموقع ويُعاد نشر الموقع تلقائياً خلال دقيقة أو دقيقتين.</p>
  <ol class="admin-steps">
    <li>افتح لوحة التحكم من الرابط: <a href="https://app.pagescms.org" target="_blank" rel="noopener">app.pagescms.org</a></li>
    <li>سجّل الدخول بالبريد الإلكتروني الذي تمت دعوتك به من قِبل مسؤول الموقع.</li>
    <li>اختر المستودع <strong>AUEM</strong> ثم اختر القسم المطلوب (الأخبار، الفعاليات، الإعلانات، معرض الصور، أو صفحات الموقع).</li>
    <li>عدّل المحتوى ثم اضغط <strong>Save</strong> — سيظهر التغيير على الموقع بعد اكتمال إعادة النشر.</li>
  </ol>
  <p class="admin-note">لم تستلم دعوة بعد؟ اطلب من مسؤول الموقع إضافتك كمحرر. الدليل الكامل متوفر في ملف
  <code>docs/CMS.md</code> داخل المستودع.</p>

  <div class="admin-en" lang="en" dir="ltr">
    <h2>Site administration</h2>
    <p class="lead">Content — photos, events, announcements and page copy — is managed with
    <strong>Pages CMS</strong>. Changes are committed to the repository and the site is rebuilt automatically in
    a minute or two.</p>
    <p>Open <a href="https://app.pagescms.org" target="_blank" rel="noopener">app.pagescms.org</a>, sign in with the
    email address you were invited with, pick the <strong>AUEM</strong> repository, edit, then press
    <strong>Save</strong>. Full instructions: <code>docs/CMS.md</code>.</p>
  </div>
</div>
</body>
</html>
"""


# --------------------------------------------------------------------------
# media
# --------------------------------------------------------------------------
def process_media(dest_assets):
    """Downscale CMS uploads (and the oversized logo PNGs) inside dist/.

    Originals in assets/ are never modified. Without Pillow everything is
    copied as-is and the pages link straight to the originals.
    """
    global THUMBS, WEBP
    try:
        from PIL import Image
    except Exception:  # noqa: BLE001 - Pillow is optional
        print("Pillow not installed - images are copied as-is (no thumbnails).")
        return

    uploads = os.path.join(dest_assets, "img", "uploads")
    thumbs_root = os.path.join(uploads, "thumbs")
    resized = 0
    thumbs_made = 0
    for dirpath, _dirnames, filenames in os.walk(uploads):
        if os.path.abspath(dirpath).startswith(os.path.abspath(thumbs_root)):
            continue
        for filename in filenames:
            if filename.startswith(".") or not filename.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
                continue
            path = os.path.join(dirpath, filename)
            rel = os.path.relpath(path, uploads)
            try:
                resized += _shrink(path, 2000, quality=82)
                thumb_path = os.path.join(thumbs_root, rel)
                os.makedirs(os.path.dirname(thumb_path), exist_ok=True)
                shutil.copyfile(path, thumb_path)
                _shrink(thumb_path, 760, quality=78)
                thumbs_made += 1
            except Exception as exc:  # noqa: BLE001 - a bad file must not break the build
                print(f"  ! could not optimise {rel}: {exc}")
    THUMBS = thumbs_made > 0

    # The two brand PNGs ship at full resolution (2.8 MB each) but render small:
    # the mark at 40-42 px (also the favicon), the wordmark at up to 340 px.
    img_dir = os.path.join(dest_assets, "img")
    brand_caps = {"AUEM_logo_only_trans.png": 256, "AUEM_logo_trans.png": 512}
    for name in os.listdir(img_dir) if os.path.isdir(img_dir) else []:
        if name.lower().endswith(".png"):
            cap = brand_caps.get(name, 720)
            try:
                _shrink(os.path.join(img_dir, name), cap, quality=90)
                if _write_webp(os.path.join(img_dir, name), cap):
                    WEBP = True
            except Exception as exc:  # noqa: BLE001
                print(f"  ! could not optimise {name}: {exc}")
    if resized:
        print(f"Optimised {resized} uploaded image(s).")


def _write_webp(path, max_width):
    """Write a WebP sibling of a PNG (same pixels, ~10x smaller).

    Returns True when the file was created.
    """
    from PIL import Image

    with Image.open(path) as im:
        im = im.convert("RGBA" if "A" in im.getbands() else "RGB")
        target = os.path.splitext(path)[0] + ".webp"
        im.save(target, "WEBP", quality=88, method=6)
    return os.path.exists(target)


def _shrink(path, max_width, quality=82):
    """Downscale an image in place; returns 1 when the file was rewritten."""
    from PIL import Image

    with Image.open(path) as im:
        width, height = im.size
        if width <= max_width:
            return 0
        ratio = max_width / float(width)
        im = im.resize((max_width, max(1, int(height * ratio))), Image.LANCZOS)
        if im.mode in ("RGBA", "P", "LA") and path.lower().endswith((".jpg", ".jpeg")):
            background = Image.new("RGB", im.size, (255, 255, 255))
            background.paste(im.convert("RGBA"), mask=im.convert("RGBA").split()[-1])
            im = background
        elif im.mode == "P":
            im = im.convert("RGBA" if path.lower().endswith(".png") else "RGB")
        fmt = "PNG" if path.lower().endswith(".png") else ("WEBP" if path.lower().endswith(".webp") else "JPEG")
        kwargs = {"optimize": True}
        if fmt == "JPEG":
            kwargs.update(quality=quality, progressive=True)
        im.save(path, fmt, **kwargs)
        return 1


# --------------------------------------------------------------------------
# entry point
# --------------------------------------------------------------------------
def chatbot_payload():
    entries = CHATBOT.get("entries") or []
    return {
        "name": CHATBOT.get("name"),
        "greeting": CHATBOT.get("greeting"),
        "placeholder": CHATBOT.get("placeholder"),
        "suggestions": CHATBOT.get("suggestions") or [],
        "fallback": CHATBOT.get("fallback"),
        "entries": [
            {
                "kw_ar": e.get("keywords_ar") or [],
                "kw_en": e.get("keywords_en") or [],
                "a_ar": e.get("answer_ar") or "",
                "a_en": e.get("answer_en") or "",
            }
            for e in entries
        ],
    }


def main(argv=None):
    global CONTENT
    parser = argparse.ArgumentParser(description="Build the AUEM static site from content/.")
    parser.add_argument("--out", default=DEFAULT_OUT, help="output directory (default: dist)")
    parser.add_argument("--content", default=CONTENT, help="content directory (default: content)")
    args = parser.parse_args(argv)
    dist = os.path.abspath(args.out)

    CONTENT = os.path.abspath(args.content)
    load_content()

    if os.path.isdir(dist):
        shutil.rmtree(dist)
    os.makedirs(dist)
    shutil.copytree(ASSETS, os.path.join(dist, "assets"))
    process_media(os.path.join(dist, "assets"))

    groq_key = os.environ.get("GROQ_API_KEY", "")
    kb_js = (
        "window.AUEM_GROQ_KEY = " + json.dumps(groq_key) + ";\n"
        "window.AUEM_KB = " + json.dumps(chatbot_payload(), ensure_ascii=False, indent=1) + ";\n"
    )
    with open(os.path.join(dist, "assets", "js", "kb.js"), "w", encoding="utf-8") as f:
        f.write(kb_js)

    built = []
    for lang in LANGS:
        os.makedirs(os.path.join(dist, lang))
        for pid, fn in RENDERERS.items():
            if pid not in PAGES:
                continue
            html = fn(lang)
            with open(os.path.join(dist, lang, f"{pid}.html"), "w", encoding="utf-8") as f:
                f.write(html)
            built.append(f"{lang}/{pid}.html")

    with open(os.path.join(dist, "index.html"), "w", encoding="utf-8") as f:
        f.write(ROOT_REDIRECT)
    os.makedirs(os.path.join(dist, "admin"), exist_ok=True)
    with open(os.path.join(dist, "admin", "index.html"), "w", encoding="utf-8") as f:
        f.write(ADMIN_PAGE)
    with open(os.path.join(dist, ".nojekyll"), "w", encoding="utf-8") as f:
        f.write("")

    print(f"Built {len(built)} pages into {dist}")
    print(
        f"Content: {len(NEWS)} news, {len(EVENTS)} events, "
        f"{len(ANNOUNCEMENTS)} announcements, {len(GALLERY)} gallery photo(s)"
    )


if __name__ == "__main__":
    main()
