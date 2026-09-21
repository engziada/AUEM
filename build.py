#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Static site generator for the AUEM bilingual website.
Builds dist/ar/*.html and dist/en/*.html from content.py — no external deps.
"""
import json
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import SITE, NAV, PAGES, FOOTER, CHATBOT, KB  # noqa: E402

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, "dist")
ASSETS = os.path.join(ROOT, "assets")
LANGS = ("ar", "en")


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def L(x, lang):
    """Localized string."""
    if isinstance(x, dict):
        return x[lang]
    return x


def paras(text, lang):
    return "\n".join(f"<p>{esc(p.strip())}</p>" for p in L(text, lang).split("\n") if p.strip())


def icon(name):
    icons = {
        "oil": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 3s6 6.3 6 11a6 6 0 1 1-12 0c0-4.7 6-11 6-11z"/><path d="M9.5 14.5a2.5 2.5 0 0 0 2.5 2.5"/></svg>',
        "mining": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 2l7 5-7 15L5 7l7-5z"/><path d="M5 7h14M12 2l-3 5 3 15 3-15-3-5z"/></svg>',
        "renewable": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="4"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M19.1 4.9L17 7M7 17l-2.1 2.1"/></svg>',
        "invest": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 17l6-6 4 4 8-8"/><path d="M15 7h6v6"/></svg>',
        "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 21s7-6.1 7-11a7 7 0 1 0-14 0c0 4.9 7 11 7 11z"/><circle cx="12" cy="10" r="2.6"/></svg>',
        "calendar": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M8 3v4M16 3v4M3 10h18"/></svg>',
    }
    return icons.get(name, "")


def base(page_id, lang, body, title=None):
    p = PAGES[page_id]
    t = L(title or p["title"], lang)
    dirv = "rtl" if lang == "ar" else "ltr"
    other = "en" if lang == "ar" else "ar"
    nav_links = "\n".join(
        f'<a href="{pid}.html" class="nav-link{" active" if pid == page_id else ""}">{esc(L(lbl, lang))}</a>'
        for pid, lbl in NAV
    )
    switch = f'<a class="lang-switch" href="../{other}/{page_id}.html" lang="{other}">{"English" if other == "en" else "العربية"}</a>'
    foot_links = "\n".join(
        f'<a href="{pid}.html">{esc(L(lbl, lang))}</a>' for pid, lbl in NAV[:6]
    )
    return f"""<!doctype html>
<html lang="{lang}" dir="{dirv}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(t)} — {esc(L(SITE["name"], lang))}</title>
<meta name="description" content="{esc(L(p["meta"], lang))}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=Inter:wght@400;600;700&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../assets/css/style.css">
<link rel="stylesheet" href="../assets/css/chatbot.css">
<link rel="icon" href="../assets/img/logo.svg" type="image/svg+xml">
</head>
<body>
<header class="site-header">
  <div class="container header-inner">
    <a class="brand" href="index.html">
      <img src="../assets/img/logo.svg" alt="{esc(L(SITE["name"], lang))}" class="brand-logo">
      <span class="brand-text"><strong>{esc(L(SITE["name"], lang))}</strong><small>{esc(SITE["abbr"])}</small></span>
    </a>
    <button class="nav-toggle" aria-label="menu" onclick="document.body.classList.toggle('nav-open')"><span></span><span></span><span></span></button>
    <nav class="main-nav">{nav_links}</nav>
    {switch}
  </div>
</header>
<main>{body}</main>
<footer class="site-footer">
  <div class="container footer-grid">
    <div>
      <div class="footer-brand"><img src="../assets/img/logo.svg" alt="" class="brand-logo"><strong>{esc(L(SITE["name"], lang))}</strong></div>
      <p>{esc(L(FOOTER["about"], lang))}</p>
      <p class="muted small">{esc(L(FOOTER["disclaimer"], lang))}</p>
    </div>
    <div>
      <h4>{esc(L(FOOTER["links_title"], lang))}</h4>
      <div class="footer-links">{foot_links}</div>
    </div>
    <div>
      <h4>{esc(L(FOOTER["contact_title"], lang))}</h4>
      <p class="muted">{icon("pin")} {esc(L(SITE["hq"], lang))}</p>
      <p><a href="contact.html">{esc(L(PAGES["contact"]["title"], lang))}</a></p>
    </div>
  </div>
  <div class="container footer-bottom">© {esc(L(SITE["name"], lang))} — {esc(L(FOOTER["rights"], lang))}</div>
</footer>
<script src="../assets/js/kb.js"></script>
<script src="../assets/js/chatbot.js"></script>
<script src="../assets/js/main.js"></script>
</body>
</html>
"""


def hero(page, lang):
    p = PAGES["index"]
    return f"""
<section class="hero">
  <div class="container hero-inner">
    <div class="hero-text">
      <p class="kicker">{icon("calendar")} {esc(L(p["hero_kicker"], lang))}</p>
      <h1>{esc(L(SITE["name"], lang))}</h1>
      <p class="hero-tagline">{esc(L(SITE["tagline"], lang))}</p>
      <p class="hero-sub">{esc(L(p["hero_sub"], lang))}</p>
      <div class="hero-cta">
        <a class="btn btn-primary" href="about.html">{esc(L(p["cta_primary"], lang))}</a>
        <a class="btn btn-outline" href="membership.html">{esc(L(p["cta_secondary"], lang))}</a>
      </div>
    </div>
    <div class="hero-emblem"><img src="../assets/img/logo.svg" alt="AUEM"></div>
  </div>
</section>
"""


def page_index(lang):
    p = PAGES["index"]
    stats = "".join(
        f'<div class="stat"><strong>{esc(L(a, lang))}</strong><span>{esc(L(b, lang))}</span></div>'
        for a, b in p["stats"]
    )
    sectors = "".join(
        f"""<div class="card sector-card"><div class="icon-wrap">{icon(s["icon"])}</div>
        <h3>{esc(L(s["name"], lang))}</h3><p>{esc(L(s["desc"], lang))}</p></div>"""
        for s in p["sectors"]
    )
    news = "".join(
        f"""<article class="card news-card"><time>{n["date"]}</time>
        <h3>{esc(L(n["title"], lang))}</h3>
        <p>{esc(L(n["body"], lang)[:220])}…</p>
        <span class="source">{esc(n["source"])}</span></article>"""
        for n in PAGES["news"]["items"][:2]
    )
    partners = "".join(f"<li>{esc(L(x, lang))}</li>" for x in p["partners"])
    body = hero("index", lang) + f"""
<section class="section"><div class="container">
  <h2 class="section-title">{esc(L(p["stats_title"], lang))}</h2>
  <div class="stats-grid">{stats}</div>
</div></section>
<section class="section alt"><div class="container">
  <h2 class="section-title">{esc(L(p["sectors_title"], lang))}</h2>
  <p class="section-sub">{esc(L(p["sectors_sub"], lang))}</p>
  <div class="grid-4">{sectors}</div>
</div></section>
<section class="section"><div class="container split">
  <div>
    <h2 class="section-title">{esc(L(p["about_teaser_title"], lang))}</h2>
    <p>{esc(L(p["about_teaser"], lang))}</p>
    <a class="btn btn-primary" href="about.html">{esc(L(p["about_more"], lang))}</a>
  </div>
  <div>
    <h2 class="section-title">{esc(L(p["news_title"], lang))}</h2>
    <div class="stack">{news}</div>
    <a class="link-more" href="news.html">{esc(L(p["news_more"], lang))} ←</a>
  </div>
</div></section>
<section class="section alt"><div class="container">
  <h2 class="section-title">{esc(L(p["partners_title"], lang))}</h2>
  <p class="section-sub">{esc(L(p["partners_sub"], lang))}</p>
  <ul class="partners">{partners}</ul>
</div></section>
<section class="cta-band"><div class="container cta-inner">
  <h2>{esc(L(p["join_title"], lang))}</h2>
  <p>{esc(L(p["join_sub"], lang))}</p>
  <a class="btn btn-light" href="membership.html">{esc(L(p["join_cta"], lang))}</a>
</div></section>
"""
    return base("index", lang, body)


def page_header(pid, lang):
    p = PAGES[pid]
    return f'<section class="page-head"><div class="container"><h1>{esc(L(p["title"], lang))}</h1></div></section>'


def page_about(lang):
    p = PAGES["about"]
    pillars = "".join(f"<li>{esc(L(x, lang))}</li>" for x in p["pillars"])
    timeline = "".join(
        f'<div class="tl-item"><span class="tl-date">{d}</span><p>{esc(L(t, lang))}</p></div>'
        for d, t in p["timeline"]
    )
    body = page_header("about", lang) + f"""
<section class="section"><div class="container prose">
  <h2>{esc(L(p["intro_title"], lang))}</h2>
  {paras(p["intro"], lang)}
  <div class="quote-box">
    <h2>{esc(L(p["vision_title"], lang))}</h2>
    <p>{esc(L(p["vision"], lang))}</p>
  </div>
  <h2>{esc(L(p["mission_title"], lang))}</h2>
  {paras(p["mission"], lang)}
  <h2>{esc(L(p["context_title"], lang))}</h2>
  {paras(p["context"], lang)}
  <h2>{esc(L(p["pillars_title"], lang))}</h2>
  <ul class="check-list">{pillars}</ul>
  <div class="president-card card">
    <div class="avatar">SB</div>
    <div>
      <h3>{esc(L(p["president_title"], lang))}</h3>
      <blockquote>{esc(L(p["president_quote"], lang))}</blockquote>
      <p class="muted"><strong>{esc(L(p["president_name"], lang))}</strong> — {esc(L(p["president_role"], lang))}</p>
    </div>
  </div>
  <h2>{esc(L(p["timeline_title"], lang))}</h2>
  <div class="timeline">{timeline}</div>
</div></section>
"""
    return base("about", lang, body)


def page_objectives(lang):
    p = PAGES["objectives"]
    items = "".join(
        f'<div class="card obj-card"><span class="obj-num">{i+1:02d}</span><p>{esc(L(x, lang))}</p></div>'
        for i, x in enumerate(p["items"])
    )
    body = page_header("objectives", lang) + f"""
<section class="section"><div class="container">
  <p class="section-sub">{esc(L(p["intro"], lang))}</p>
  <div class="grid-2">{items}</div>
</div></section>
"""
    return base("objectives", lang, body)


def page_governance(lang):
    p = PAGES["governance"]
    bodies = "".join(
        f'<div class="card"><h3>{esc(L(b["name"], lang))}</h3><p>{esc(L(b["desc"], lang))}</p></div>'
        for b in p["bodies"]
    )
    commissions = "".join(f"<li>{esc(L(c, lang))}</li>" for c in p["commissions"])
    leaders = "".join(
        f'<div class="card leader"><h3>{esc(L(x["name"], lang))}</h3><p class="muted">{esc(L(x["role"], lang))}</p></div>'
        for x in p["leaders"]
    )
    body = page_header("governance", lang) + f"""
<section class="section"><div class="container">
  <p class="section-sub">{esc(L(p["intro"], lang))}</p>
  <h2 class="section-title">{esc(L(p["bodies_title"], lang))}</h2>
  <div class="grid-4">{bodies}</div>
  <h2 class="section-title">{esc(L(p["commissions_title"], lang))}</h2>
  <p class="section-sub">{esc(L(p["commissions_sub"], lang))}</p>
  <ul class="tag-list">{commissions}</ul>
  <h2 class="section-title">{esc(L(p["leadership_title"], lang))}</h2>
  <div class="grid-2">{leaders}</div>
</div></section>
"""
    return base("governance", lang, body)


def page_membership(lang):
    p = PAGES["membership"]
    benefits = "".join(f"<li>{esc(L(b, lang))}</li>" for b in p["benefits"])
    body = page_header("membership", lang) + f"""
<section class="section"><div class="container prose">
  <h2>{esc(L(p["intro_title"], lang))}</h2>
  {paras(p["intro"], lang)}
  <h2>{esc(L(p["benefits_title"], lang))}</h2>
  <ul class="check-list">{benefits}</ul>
  <h2>{esc(L(p["how_title"], lang))}</h2>
  {paras(p["how"], lang)}
  <p class="note-box">{esc(L(p["note"], lang))}</p>
  <a class="btn btn-primary" href="contact.html">{esc(L(p["cta"], lang))}</a>
</div></section>
"""
    return base("membership", lang, body)


def page_activities(lang):
    p = PAGES["activities"]
    streams = "".join(
        f'<div class="card"><h3>{esc(L(s["name"], lang))}</h3><p>{esc(L(s["desc"], lang))}</p></div>'
        for s in p["streams"]
    )
    roadmap = "".join(
        f'<div class="tl-item"><span class="tl-date">{y}</span><p>{esc(L(t, lang))}</p></div>'
        for y, t in p["roadmap"]
    )
    body = page_header("activities", lang) + f"""
<section class="section"><div class="container">
  <p class="section-sub">{esc(L(p["intro"], lang))}</p>
  <div class="grid-3">{streams}</div>
</div></section>
<section class="section alt"><div class="container">
  <h2 class="section-title">{esc(L(p["roadmap_title"], lang))}</h2>
  <p class="section-sub">{esc(L(p["roadmap_sub"], lang))}</p>
  <div class="timeline">{roadmap}</div>
</div></section>
"""
    return base("activities", lang, body)


def page_news(lang):
    p = PAGES["news"]
    items = "".join(
        f"""<article class="card news-card"><time>{n["date"]}</time>
        <h3>{esc(L(n["title"], lang))}</h3><p>{esc(L(n["body"], lang))}</p>
        <span class="source">{esc(n["source"])}</span></article>"""
        for n in p["items"]
    )
    sources = "".join(
        f'<li><a href="{u}" target="_blank" rel="noopener">{esc(t)}</a></li>'
        for t, u in p["sources"]
    )
    body = page_header("news", lang) + f"""
<section class="section"><div class="container">
  <div class="stack">{items}</div>
  <h2 class="section-title" style="margin-top:2.5rem">{esc(L(p["sources_title"], lang))}</h2>
  <ul class="source-list">{sources}</ul>
</div></section>
"""
    return base("news", lang, body)


def page_unions(lang):
    p = PAGES["unions"]
    groups = ""
    for g in p["groups"]:
        cards = "".join(
            f"""<div class="card union-card">
            <div class="union-head"><h3>{esc(L(u, lang))}</h3><span class="badge">{u["est"]}</span></div>
            <p class="muted small">{esc(L(u["desc"], lang))}</p>
            <p class="union-hq">{icon("pin")} {esc(L(u["hq"], lang))}</p></div>"""
            for u in g["items"]
        )
        groups += f'<h2 class="section-title">{esc(L(g["name"], lang))}</h2><div class="grid-3">{cards}</div>'
    orgs = "".join(
        f'<tr><td>{esc(L(o, lang))}</td><td>{o["est"]}</td><td>{esc(L(o["hq"], lang))}</td></tr>'
        for o in p["orgs"]
    )
    th = (f"<tr><th>{'المنظمة' if lang=='ar' else 'Organization'}</th>"
          f"<th>{'التأسيس' if lang=='ar' else 'Founded'}</th>"
          f"<th>{'المقر' if lang=='ar' else 'HQ'}</th></tr>")
    body = page_header("unions", lang) + f"""
<section class="section"><div class="container prose">
  <h2>{esc(L(p["intro_title"], lang))}</h2>
  {paras(p["intro"], lang)}
</div></section>
<section class="section alt"><div class="container">{groups}</div></section>
<section class="section"><div class="container">
  <h2 class="section-title">{esc(L(p["orgs_title"], lang))}</h2>
  <p class="section-sub">{esc(L(p["orgs_sub"], lang))}</p>
  <div class="table-wrap"><table class="orgs-table">{th}{orgs}</table></div>
  <p class="note-box">{esc(L(p["note"], lang))}</p>
</div></section>
"""
    return base("unions", lang, body)


def page_contact(lang):
    p = PAGES["contact"]
    topics = "".join(f"<li>{esc(L(t, lang))}</li>" for t in p["topics"])
    subj = "AUEM website inquiry"
    body = page_header("contact", lang) + f"""
<section class="section"><div class="container split">
  <div>
    <p class="section-sub">{esc(L(p["intro"], lang))}</p>
    <div class="card hq-card"><h3>{esc(L(p["hq_title"], lang))}</h3>
    <p>{icon("pin")} {esc(L(p["hq_value"], lang))}</p></div>
    <h3>{esc(L(p["topics_title"], lang))}</h3>
    <ul class="check-list">{topics}</ul>
  </div>
  <form class="card contact-form" action="mailto:info@auem.org" method="post" enctype="text/plain">
    <label>{esc(L(p["form_name"], lang))}<input name="name" required></label>
    <label>{esc(L(p["form_org"], lang))}<input name="organization"></label>
    <label>{esc(L(p["form_email"], lang))}<input type="email" name="email" required></label>
    <label>{esc(L(p["form_subject"], lang))}<input name="subject" value="{subj}"></label>
    <label>{esc(L(p["form_message"], lang))}<textarea name="message" rows="6" required></textarea></label>
    <button class="btn btn-primary" type="submit">{esc(L(p["form_send"], lang))}</button>
    <p class="muted small">{esc(L(p["form_note"], lang))}</p>
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
    "unions": page_unions,
    "contact": page_contact,
}

ROOT_REDIRECT = """<!doctype html><html><head><meta charset="utf-8">
<title>AUEM</title>
<script>var l=(navigator.language||'ar').slice(0,2);location.replace(l==='en'?'en/index.html':'ar/index.html');</script>
</head><body><a href="ar/index.html">العربية</a> · <a href="en/index.html">English</a></body></html>
"""


def main():
    if os.path.isdir(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST)
    shutil.copytree(ASSETS, os.path.join(DIST, "assets"))

    kb = {
        "name": CHATBOT["name"], "greeting": CHATBOT["greeting"],
        "placeholder": CHATBOT["placeholder"], "suggestions": CHATBOT["suggestions"],
        "fallback": CHATBOT["fallback"], "entries": KB,
    }
    kb_js = "window.AUEM_KB = " + json.dumps(kb, ensure_ascii=False, indent=1) + ";\n"
    with open(os.path.join(DIST, "assets", "js", "kb.js"), "w", encoding="utf-8") as f:
        f.write(kb_js)

    for lang in LANGS:
        os.makedirs(os.path.join(DIST, lang))
        for pid, fn in RENDERERS.items():
            html = fn(lang)
            with open(os.path.join(DIST, lang, f"{pid}.html"), "w", encoding="utf-8") as f:
                f.write(html)
    with open(os.path.join(DIST, "index.html"), "w", encoding="utf-8") as f:
        f.write(ROOT_REDIRECT)
    print(f"Built {len(RENDERERS) * len(LANGS)} pages into {DIST}")


if __name__ == "__main__":
    main()
