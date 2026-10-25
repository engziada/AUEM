#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Smoke test: build the site from fixture content and assert the new features.

The real content/ folder is copied to a temporary directory and extended with
throw-away entries (upcoming event, news with an image, an active announcement),
so nothing in the repository is touched.

    python tools/smoke_test.py

Exit code 0 = all checks passed.
"""
import json
import os
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FAILS = []


def check(label, condition, detail=""):
    if condition:
        print(f"  ok   {label}")
    else:
        print(f"  FAIL {label} {detail}")
        FAILS.append(label)


def write(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def main():
    # A workspace-local scratch folder: the OS temp directory is not always
    # writable for every user/sandbox, the repository root is. (Not
    # tempfile.mkdtemp: on Windows that creates a private DACL, which a
    # restricted sandbox token cannot descend into.)
    tmp = os.path.join(ROOT, f".smoke-{os.getpid()}")
    shutil.rmtree(tmp, ignore_errors=True)
    os.makedirs(tmp)
    try:
        content = os.path.join(tmp, "content")
        shutil.copytree(os.path.join(ROOT, "content"), content)
        dist = os.path.join(tmp, "dist")

        # --- fixtures -----------------------------------------------------
        write(os.path.join(content, "events", "2099-upcoming.json"), {
            "start_date": "2099-03-10",
            "end_date": "2099-03-12",
            "title": {"ar": "ملتقى تجريبي", "en": "Fixture forum"},
            "location": {"ar": "الدار البيضاء", "en": "Casablanca"},
            "summary": {"ar": "ملخص تجريبي", "en": "Fixture summary"},
            "body": {"ar": "", "en": ""},
            "image": "/assets/img/AUEM_logo_only_trans.png",
            "registration_url": "https://example.org/register",
            "published": True,
        })
        write(os.path.join(content, "news", "2099-fixture.json"), {
            "date": "2099-01-05",
            "title": {"ar": "خبر تجريبي", "en": "Fixture news"},
            "summary": {"ar": "ملخص الخبر", "en": "Fixture summary"},
            "body": {"ar": "الفقرة الأولى\nالفقرة الثانية", "en": "First paragraph\nSecond paragraph"},
            "source": "Fixture source",
            "source_url": "https://example.org/source",
            "image": "/assets/img/AUEM_logo_only_trans.png",
            "published": True,
        })
        write(os.path.join(content, "news", "2099-draft.json"), {
            "date": "2099-01-06",
            "title": {"ar": "مسودة", "en": "Draft entry"},
            "body": {"ar": "مسودة", "en": "draft"},
            "published": False,
        })
        write(os.path.join(content, "announcements", "2099-active.json"), {
            "date": "2099-01-05",
            "title": {"ar": "إعلان تجريبي", "en": "Fixture announcement"},
            "body": {"ar": "نص الإعلان التجريبي", "en": "Fixture announcement text"},
            "link_url": "https://example.org",
            "link_label": {"ar": "المزيد", "en": "More"},
            "level": "important",
            "active": True,
        })
        write(os.path.join(content, "announcements", "2099-expired.json"), {
            "date": "2020-01-05",
            "expires": "2020-02-05",
            "title": {"ar": "منتهي", "en": "Expired"},
            "body": {"ar": "نص منتهي", "en": "expired text"},
            "active": True,
        })

        # --- build --------------------------------------------------------
        print("building fixture site…")
        result = subprocess.run(
            [sys.executable, os.path.join(ROOT, "build.py"),
             "--content", content, "--out", dist],
            capture_output=True, text=True, cwd=ROOT,
        )
        if result.returncode != 0:
            print(result.stdout, result.stderr)
            sys.exit("build failed")

        ar = lambda name: read(os.path.join(dist, "ar", name))
        en = lambda name: read(os.path.join(dist, "en", name))
        index_ar = ar("index.html")
        events_ar = ar("events.html")
        news_ar = ar("news.html")
        gallery_ar = ar("gallery.html")

        print("assertions:")

        # pages exist in both languages
        for lang in ("ar", "en"):
            for name in ("index", "about", "news", "events", "gallery", "contact", "unions"):
                check(f"{lang}/{name}.html generated",
                      os.path.exists(os.path.join(dist, lang, f"{name}.html")))

        # navigation contains the new sections
        check("nav has events + gallery",
              'href="events.html"' in index_ar and 'href="gallery.html"' in index_ar)

        # upcoming event appears on the events page and on the home page
        check("upcoming event listed", "ملتقى تجريبي" in events_ar)
        check("upcoming event on home page", "ملتقى تجريبي" in index_ar)
        check("event date range rendered", "10 مارس 2099 – 12 مارس 2099" in events_ar)
        check("event register button", "https://example.org/register" in events_ar)
        check("past events section exists", "فعاليات سابقة" in events_ar)

        # news: published fixtures shown, drafts hidden, media layout applied
        check("fixture news listed", "خبر تجريبي" in news_ar)
        check("draft news hidden", "مسودة" not in news_ar)
        check("news paragraphs split", news_ar.count("<p>الفقرة الأولى</p>") == 1 and
              "<p>الفقرة الثانية</p>" in news_ar)
        check("news media class", 'class="card news-card has-media"' in news_ar)
        check("news source link", 'href="https://example.org/source"' in news_ar)

        # announcements: active shown in the bar, expired filtered out
        check("announcement bar rendered", 'id="announce-bar"' in index_ar)
        check("important announcement styled", "announce-msg important" in index_ar)
        check("expired announcement filtered", "نص منتهي" not in index_ar)
        check("announcement on news page", "نص الإعلان التجريبي" in news_ar)

        # empty gallery falls back to its empty state
        check("empty gallery state", "empty-state" in gallery_ar)
        check("no gallery section on home when empty",
              'class="gallery-grid"' not in index_ar)

        # bilingual rendering + locale-aware dates
        check("english pages render", "Fixture forum" in en("events.html"))
        check("arabic date localised", "5 يناير 2099" in news_ar)
        check("english date localised", "5 January 2099" in en("news.html"))
        check("canonical link", 'rel="canonical"' in index_ar)

        # no template leakage
        check("no None in output", ">None<" not in index_ar and "None" not in events_ar)

        # link checker passes on the fixture build
        site = subprocess.run(
            [sys.executable, os.path.join(ROOT, "tools", "check_site.py"), dist],
            capture_output=True, text=True, cwd=ROOT,
        )
        check("check_site.py clean", site.returncode == 0, site.stdout.strip().splitlines()[-1:])

        # the CMS config still matches the real content folder
        content_check = subprocess.run(
            [sys.executable, os.path.join(ROOT, "tools", "check_content.py")],
            capture_output=True, text=True, cwd=ROOT,
        )
        check("check_content.py clean", content_check.returncode == 0,
              content_check.stdout.strip().splitlines()[-1:])
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print()
    if FAILS:
        print(f"{len(FAILS)} check(s) failed")
        return 1
    print("all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
