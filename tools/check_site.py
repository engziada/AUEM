#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Check a built site: broken internal links, missing images, thin pages.

    python build.py --out .preview
    python tools/check_site.py .preview

Exit code 0 = clean, 1 = at least one broken local link or missing asset.
"""
import os
import re
import sys
from html.parser import HTMLParser

DIST = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else "dist")
LANGS = ("ar", "en")
SKIP_SCHEMES = ("http://", "https://", "//", "mailto:", "tel:", "data:", "javascript:")

errors = []
warnings = []


class Links(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.refs = []
        self.images = 0
        self.images_without_alt = 0
        self.empty_hrefs = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in ("href", "src", "srcset"):
            value = attrs.get(key)
            if not value:
                continue
            if key == "srcset":
                for part in value.split(","):
                    url = part.strip().split(" ")[0]
                    if url:
                        self.refs.append(url)
                continue
            self.refs.append(value)
        if tag == "img":
            self.images += 1
            if "alt" not in attrs:
                self.images_without_alt += 1
        if tag == "a" and not attrs.get("href"):
            self.empty_hrefs += 1


def resolve(page, ref):
    """Return the filesystem target for a local reference, or None if external."""
    ref = ref.strip()
    if not ref or ref.startswith("#") or ref.startswith(SKIP_SCHEMES):
        return None
    ref = ref.split("#")[0].split("?")[0]
    if not ref:
        return None
    target = os.path.normpath(os.path.join(os.path.dirname(page), ref.lstrip("/")))
    return target


def main():
    if not os.path.isdir(DIST):
        sys.exit(f"output folder not found: {DIST} — run build.py first")

    if not os.path.exists(os.path.join(DIST, ".nojekyll")):
        errors.append(".nojekyll is missing (GitHub Pages would run Jekyll)")

    pages = []
    for lang in LANGS:
        folder = os.path.join(DIST, lang)
        if not os.path.isdir(folder):
            errors.append(f"missing language folder: {lang}/")
            continue
        for name in sorted(os.listdir(folder)):
            if name.endswith(".html"):
                pages.append(os.path.join(folder, name))

    expected = {"index", "about", "objectives", "governance", "membership",
                "activities", "news", "events", "gallery", "unions", "contact"}
    for lang in LANGS:
        found = {os.path.basename(p)[:-5] for p in pages if os.path.dirname(p).endswith(lang)}
        for missing in sorted(expected - found):
            errors.append(f"{lang}/{missing}.html was not generated")

    checked = set()
    for page in pages:
        rel = os.path.relpath(page, DIST).replace("\\", "/")
        parser = Links()
        with open(page, encoding="utf-8") as f:
            parser.feed(f.read())
        if parser.images_without_alt:
            warnings.append(f"{rel}: {parser.images_without_alt} <img> without alt")
        if parser.empty_hrefs:
            warnings.append(f"{rel}: {parser.empty_hrefs} <a> without href")

        for ref in parser.refs:
            target = resolve(page, ref)
            if not target:
                continue
            key = (target, ref)
            if key in checked:
                continue
            checked.add(key)
            if os.path.isdir(target):
                if not os.path.exists(os.path.join(target, "index.html")):
                    errors.append(f"{rel}: '{ref}' points at a folder without index.html")
            elif not os.path.exists(target):
                errors.append(f"{rel}: broken reference '{ref}'")

    # the entry point and the admin landing page must both exist
    for extra in ("index.html", os.path.join("admin", "index.html")):
        if not os.path.exists(os.path.join(DIST, extra)):
            errors.append(f"missing {extra.replace(os.sep, '/')}")

    for message in warnings:
        print(f"WARN  {message}")
    for message in errors:
        print(f"ERROR {message}")
    print(f"\n{len(pages)} page(s) checked, {len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
