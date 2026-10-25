#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""RETIRED — this file is no longer read by the site.

All site copy now lives in the JSON files under ``content/`` and is edited by
the web admin through Pages CMS (see ``.pages.yml`` and ``docs/CMS.md``):

    content/settings.json    site name, tagline, navigation, footer
    content/pages/*.json     one file per page
    content/news/*.json      news articles   (collection)
    content/events/*.json    events          (collection)
    content/announcements/   announcements   (collection)
    content/gallery/*.json   gallery photos  (collection)
    content/chatbot.json     assistant copy and knowledge base

The original Python dictionaries were migrated once with
``tools/migrate_content.py`` and remain available in the git history:
``git show 6ed0314:content.py``.

Do not add content here — the build ignores it.
"""

if __name__ == "__main__":
    raise SystemExit(__doc__)
