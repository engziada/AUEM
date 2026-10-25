#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""One-time migration: content.py  ->  content/**.json (CMS-editable).

The site used to keep all copy in content.py as Python dicts. The web admin now
edits JSON under content/ through Pages CMS, so this script converts the
original data exactly once and writes the files the CMS reads.

Run from the repository root:   python tools/migrate_content.py

The output is committed to git; this script stays in tools/ as provenance for
how the JSON was produced. It refuses to overwrite existing files unless
--force is passed.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

try:
    from content import CHATBOT, FOOTER, KB, NAV, PAGES, SITE  # noqa: E402
except ImportError:
    raise SystemExit(
        "content.py no longer exists — the site reads content/*.json now.\n"
        "To regenerate the JSON from the original Python copy, check out the "
        "pre-CMS commit first, e.g.:\n"
        "    git worktree add /tmp/auem-pre-cms 6ed0314\n"
        "    python /tmp/auem-pre-cms/tools/migrate_content.py --force"
    )

CONTENT = os.path.join(ROOT, "content")

# New navigation entries that did not exist in content.py.
NEW_NAV_LABELS = {
    "events": {"ar": "الفعاليات", "en": "Events"},
    "gallery": {"ar": "معرض الصور", "en": "Gallery"},
}


def bi(x):
    """Normalise an {'ar','en'} pair; leave plain strings/numbers alone."""
    if isinstance(x, dict):
        if "ar" not in x or "en" not in x:
            raise SystemExit(f"unexpected bilingual value: {x!r}")
        return {"ar": x["ar"], "en": x["en"]}
    return x


def bilist(xs):
    return [bi(x) for x in xs]


def slug(text, fallback="item", limit=44):
    s = re.sub(r"[^a-z0-9]+", "-", str(text).lower()).strip("-")
    if len(s) > limit:
        cut = s[:limit]
        s = cut[: cut.rfind("-")] if "-" in cut else cut
    return s.strip("-") or fallback


def write_json(path, data):
    if os.path.exists(path) and "--force" not in sys.argv:
        raise SystemExit(f"refusing to overwrite {path} (use --force)")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("wrote", os.path.relpath(path, ROOT))


# --------------------------------------------------------------------------
# content/settings.json
# --------------------------------------------------------------------------
def build_settings():
    nav = {pid: {"page": pid, "label": bi(label)} for pid, label in NAV}
    # Events and Gallery sit right after News in the navigation.
    ordered = []
    for pid, _ in NAV:
        if pid == "news":
            ordered.append(nav[pid])
            ordered.append({"page": "events", "label": NEW_NAV_LABELS["events"]})
            ordered.append({"page": "gallery", "label": NEW_NAV_LABELS["gallery"]})
        else:
            ordered.append(nav[pid])

    return {
        "name": bi(SITE["name"]),
        "abbr": SITE["abbr"],
        "tagline": bi(SITE["tagline"]),
        "hq": bi(SITE["hq"]),
        "site_url": "https://engziada.github.io/AUEM",
        "contact_email": "info@auem.org",
        "nav": ordered,
        "footer": {
            "about": bi(FOOTER["about"]),
            "links_title": bi(FOOTER["links_title"]),
            "contact_title": bi(FOOTER["contact_title"]),
            "rights": bi(FOOTER["rights"]),
            "disclaimer": bi(FOOTER["disclaimer"]),
        },
    }


# --------------------------------------------------------------------------
# content/pages/*.json
# --------------------------------------------------------------------------
def build_pages():
    P = PAGES
    pages = {}

    idx = P["index"]
    pages["index"] = {
        "title": bi(idx["title"]),
        "meta": bi(idx["meta"]),
        "hero_kicker": bi(idx["hero_kicker"]),
        "hero_sub": bi(idx["hero_sub"]),
        "cta_primary": bi(idx["cta_primary"]),
        "cta_secondary": bi(idx["cta_secondary"]),
        "stats_title": bi(idx["stats_title"]),
        "stats": [{"value": bi(v), "label": bi(lbl)} for v, lbl in idx["stats"]],
        "sectors_title": bi(idx["sectors_title"]),
        "sectors_sub": bi(idx["sectors_sub"]),
        "sectors": [
            {"icon": s["icon"], "name": bi(s["name"]), "desc": bi(s["desc"])}
            for s in idx["sectors"]
        ],
        "about_teaser_title": bi(idx["about_teaser_title"]),
        "about_teaser": bi(idx["about_teaser"]),
        "about_more": bi(idx["about_more"]),
        "news_title": bi(idx["news_title"]),
        "news_more": bi(idx["news_more"]),
        "events_title": {"ar": "الفعاليات القادمة", "en": "Upcoming events"},
        "events_more": {"ar": "كل الفعاليات", "en": "All events"},
        "gallery_title": {"ar": "من معرض الصور", "en": "From the gallery"},
        "gallery_sub": {
            "ar": "لمحات من اجتماعات الاتحاد وفعالياته وأنشطته الميدانية.",
            "en": "Highlights from the Union's meetings, events and field activities.",
        },
        "gallery_more": {"ar": "زيارة المعرض", "en": "Visit the gallery"},
        "partners_title": bi(idx["partners_title"]),
        "partners_sub": bi(idx["partners_sub"]),
        "partners": bilist(idx["partners"]),
        "join_title": bi(idx["join_title"]),
        "join_sub": bi(idx["join_sub"]),
        "join_cta": bi(idx["join_cta"]),
    }

    a = P["about"]
    pages["about"] = {
        "title": bi(a["title"]),
        "meta": bi(a["meta"]),
        "intro_title": bi(a["intro_title"]),
        "intro": bi(a["intro"]),
        "vision_title": bi(a["vision_title"]),
        "vision": bi(a["vision"]),
        "mission_title": bi(a["mission_title"]),
        "mission": bi(a["mission"]),
        "context_title": bi(a["context_title"]),
        "context": bi(a["context"]),
        "pillars_title": bi(a["pillars_title"]),
        "pillars": bilist(a["pillars"]),
        "president_title": bi(a["president_title"]),
        "president_name": bi(a["president_name"]),
        "president_role": bi(a["president_role"]),
        "president_quote": bi(a["president_quote"]),
        "president_photo": "",
        "timeline_title": bi(a["timeline_title"]),
        "timeline": [{"date": bi(d), "text": bi(t)} for d, t in a["timeline"]],
    }

    o = P["objectives"]
    pages["objectives"] = {
        "title": bi(o["title"]),
        "meta": bi(o["meta"]),
        "intro": bi(o["intro"]),
        "items": bilist(o["items"]),
    }

    g = P["governance"]
    pages["governance"] = {
        "title": bi(g["title"]),
        "meta": bi(g["meta"]),
        "intro": bi(g["intro"]),
        "bodies_title": bi(g["bodies_title"]),
        "bodies": [{"name": bi(b["name"]), "desc": bi(b["desc"])} for b in g["bodies"]],
        "commissions_title": bi(g["commissions_title"]),
        "commissions_sub": bi(g["commissions_sub"]),
        "commissions": bilist(g["commissions"]),
        "leadership_title": bi(g["leadership_title"]),
        "leaders": [
            {"name": bi(x["name"]), "role": bi(x["role"]), "photo": ""}
            for x in g["leaders"]
        ],
    }

    m = P["membership"]
    pages["membership"] = {
        "title": bi(m["title"]),
        "meta": bi(m["meta"]),
        "intro_title": bi(m["intro_title"]),
        "intro": bi(m["intro"]),
        "benefits_title": bi(m["benefits_title"]),
        "benefits": bilist(m["benefits"]),
        "how_title": bi(m["how_title"]),
        "how": bi(m["how"]),
        "note": bi(m["note"]),
        "cta": bi(m["cta"]),
    }

    act = P["activities"]
    pages["activities"] = {
        "title": bi(act["title"]),
        "meta": bi(act["meta"]),
        "intro": bi(act["intro"]),
        "streams": [
            {"name": bi(s["name"]), "desc": bi(s["desc"])} for s in act["streams"]
        ],
        "roadmap_title": bi(act["roadmap_title"]),
        "roadmap_sub": bi(act["roadmap_sub"]),
        "roadmap": [{"year": bi(y), "text": bi(t)} for y, t in act["roadmap"]],
    }

    n = P["news"]
    pages["news"] = {
        "title": bi(n["title"]),
        "meta": bi(n["meta"]),
        "intro": {
            "ar": "تابع آخر أخبار الاتحاد وبياناته الصحفية وتغطياته الإعلامية.",
            "en": "Follow the Union's latest news, press releases and media coverage.",
        },
        "announcements_title": {"ar": "إعلانات", "en": "Announcements"},
        "sources_title": bi(n["sources_title"]),
        "sources": [{"title": t, "url": u} for t, u in n["sources"]],
        "empty_text": {
            "ar": "لا توجد أخبار منشورة حالياً.",
            "en": "No news published yet.",
        },
    }

    u = P["unions"]
    pages["unions"] = {
        "title": bi(u["title"]),
        "meta": bi(u["meta"]),
        "intro_title": bi(u["intro_title"]),
        "intro": bi(u["intro"]),
        "groups": [
            {
                "name": bi(grp["name"]),
                "items": [
                    {
                        "name": {"ar": it["ar"], "en": it["en"]},
                        "est": it["est"],
                        "desc": bi(it["desc"]),
                        "hq": bi(it["hq"]),
                    }
                    for it in grp["items"]
                ],
            }
            for grp in u["groups"]
        ],
        "orgs_title": bi(u["orgs_title"]),
        "orgs_sub": bi(u["orgs_sub"]),
        "orgs": [
            {
                "name": {"ar": org["ar"], "en": org["en"]},
                "est": org["est"],
                "hq": bi(org["hq"]),
            }
            for org in u["orgs"]
        ],
        "note": bi(u["note"]),
    }

    c = P["contact"]
    pages["contact"] = {
        "title": bi(c["title"]),
        "meta": bi(c["meta"]),
        "intro": bi(c["intro"]),
        "hq_title": bi(c["hq_title"]),
        "hq_value": bi(c["hq_value"]),
        "topics_title": bi(c["topics_title"]),
        "topics": bilist(c["topics"]),
        "form_name": bi(c["form_name"]),
        "form_org": bi(c["form_org"]),
        "form_email": bi(c["form_email"]),
        "form_subject": bi(c["form_subject"]),
        "form_message": bi(c["form_message"]),
        "form_send": bi(c["form_send"]),
        "form_note": bi(c["form_note"]),
    }

    pages["events"] = {
        "title": {"ar": "الفعاليات", "en": "Events"},
        "meta": {
            "ar": "فعاليات واجتماعات الاتحاد العربي للطاقة والمعادن.",
            "en": "Events and meetings of the Arab Union for Energy & Minerals.",
        },
        "intro": {
            "ar": "ينظّم الاتحاد الاجتماعات والملتقيات وورش العمل التي تجمع الفاعلين الاقتصاديين في قطاعي الطاقة والمعادن على مستوى العالم العربي.",
            "en": "The Union organises meetings, forums and workshops that bring together economic actors in the Arab energy and minerals sectors.",
        },
        "upcoming_title": {"ar": "الفعاليات القادمة", "en": "Upcoming events"},
        "past_title": {"ar": "فعاليات سابقة", "en": "Past events"},
        "empty_upcoming": {
            "ar": "لا توجد فعاليات قادمة معلنة حالياً. تابعونا قريباً.",
            "en": "No upcoming events announced yet. Stay tuned.",
        },
        "empty_past": {
            "ar": "لا توجد فعاليات سابقة مسجّلة.",
            "en": "No past events recorded yet.",
        },
        "register_label": {"ar": "التسجيل", "en": "Register"},
    }

    pages["gallery"] = {
        "title": {"ar": "معرض الصور", "en": "Gallery"},
        "meta": {
            "ar": "صور من اجتماعات الاتحاد العربي للطاقة والمعادن وفعالياته.",
            "en": "Photos from the meetings and events of the Arab Union for Energy & Minerals.",
        },
        "intro": {
            "ar": "أرشيف مصوّر لاجتماعات الاتحاد وفعالياته وأنشطته الميدانية.",
            "en": "A photo archive of the Union's meetings, events and field activities.",
        },
        "empty_text": {
            "ar": "سيتم نشر صور الفعاليات هنا قريباً.",
            "en": "Photos of our events will be published here soon.",
        },
    }
    return pages


# --------------------------------------------------------------------------
# collections: news / events / announcements / gallery
# --------------------------------------------------------------------------
def build_news():
    items = []
    for i, n in enumerate(PAGES["news"]["items"]):
        filename = f"{n['date']}-{slug(n['title']['en'], f'news-{i + 1}')}.json"
        items.append(
            (
                filename,
                {
                    "date": n["date"],
                    "title": bi(n["title"]),
                    "summary": {"ar": "", "en": ""},
                    "body": bi(n["body"]),
                    "source": n.get("source", ""),
                    "source_url": "",
                    "image": "",
                    "published": True,
                },
            )
        )
    return items


def build_events():
    # Seed with the one event that is documented in the existing copy: the
    # inaugural General Assembly. Upcoming events are added by the admin.
    return [
        (
            "2026-07-23-inaugural-general-assembly.json",
            {
                "start_date": "2026-07-23",
                "end_date": "",
                "title": {
                    "ar": "الجمعية العمومية التأسيسية للاتحاد",
                    "en": "Inaugural General Assembly of the Union",
                },
                "location": {
                    "ar": "سلا، المملكة المغربية",
                    "en": "Salé, Kingdom of Morocco",
                },
                "summary": {
                    "ar": "انعقدت الجمعية العمومية التأسيسية بحضور صناع قرار ومسؤولين وخبراء وفاعلين اقتصاديين من عدة دول عربية، وانتُخب المغرب بالإجماع لرئاسة الاتحاد.",
                    "en": "The inaugural General Assembly brought together decision-makers, officials, experts and economic actors from several Arab countries; Morocco was unanimously elected to the presidency.",
                },
                "body": {"ar": "", "en": ""},
                "image": "",
                "registration_url": "",
                "published": True,
            },
        )
    ]


def build_announcements():
    # Inactive by default: the admin fills it in and flips "active" to publish.
    return [
        (
            "welcome.json",
            {
                "date": "2026-07-23",
                "title": {
                    "ar": "انطلاق الموقع الإلكتروني للاتحاد",
                    "en": "The Union's website is live",
                },
                "body": {
                    "ar": "أصبح الموقع الرسمي للاتحاد العربي للطاقة والمعادن متاحاً باللغتين العربية والإنجليزية.",
                    "en": "The official website of the Arab Union for Energy & Minerals is now available in Arabic and English.",
                },
                "link_label": {"ar": "", "en": ""},
                "link_url": "",
                "level": "info",
                "active": False,
            },
        )
    ]


def build_chatbot():
    return {
        "name": bi(CHATBOT["name"]),
        "greeting": bi(CHATBOT["greeting"]),
        "placeholder": bi(CHATBOT["placeholder"]),
        "fallback": bi(CHATBOT["fallback"]),
        "suggestions": bilist(CHATBOT["suggestions"]),
        "entries": [
            {
                "keywords_ar": list(e["kw_ar"]),
                "keywords_en": list(e["kw_en"]),
                "answer_ar": e["a_ar"],
                "answer_en": e["a_en"],
            }
            for e in KB
        ],
    }


def main():
    write_json(os.path.join(CONTENT, "settings.json"), build_settings())
    write_json(os.path.join(CONTENT, "chatbot.json"), build_chatbot())
    for pid, page in build_pages().items():
        write_json(os.path.join(CONTENT, "pages", f"{pid}.json"), page)
    for filename, item in build_news():
        write_json(os.path.join(CONTENT, "news", filename), item)
    for filename, item in build_events():
        write_json(os.path.join(CONTENT, "events", filename), item)
    for filename, item in build_announcements():
        write_json(os.path.join(CONTENT, "announcements", filename), item)
    os.makedirs(os.path.join(CONTENT, "gallery"), exist_ok=True)
    print("done.")


if __name__ == "__main__":
    main()
