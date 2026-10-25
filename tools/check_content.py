#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validate content/*.json against .pages.yml — the CMS config.

Catches the failure mode that matters with a git-based CMS: the config and the
JSON drifting apart, which leaves a field either invisible in the editor or
silently dropped on save.

    python tools/check_content.py

Exit code 0 = clean, 1 = at least one error.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "content")
CONFIG = os.path.join(ROOT, ".pages.yml")

errors = []
warnings = []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def rel(path):
    return os.path.relpath(path, ROOT).replace("\\", "/")


def load_yaml(path):
    try:
        import yaml
    except ImportError:
        sys.exit("PyYAML is required: pip install pyyaml")
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def resolve_field(field, components, trail):
    """Expand `component: x` references into a concrete field definition."""
    field = dict(field)
    name = field.get("component")
    if name:
        if name not in components:
            err(f"{trail}: unknown component '{name}'")
            return field
        base = json.loads(json.dumps(components[name]))
        merged = dict(base)
        for key, value in field.items():
            if key != "component":
                merged[key] = value
        field = merged
    return field


def walk_fields(fields, components, trail):
    out = {}
    for raw in fields or []:
        field = resolve_field(raw, components, trail)
        name = field.get("name")
        if not name:
            err(f"{trail}: a field has no name")
            continue
        out[name] = field
        if field.get("type") == "object" and field.get("fields"):
            walk_fields(field["fields"], components, f"{trail}.{name}")
    return out


def entries(block):
    """Yield (kind, path, fields) for every collection/file, groups included."""
    for entry in block or []:
        kind = entry.get("type")
        if kind == "group":
            yield from entries(entry.get("items"))
        else:
            yield entry


def is_bi(value):
    return isinstance(value, dict) and set(value.keys()) == {"ar", "en"}


def check_bi(value, trail, required=False):
    if not is_bi(value):
        if isinstance(value, dict):
            err(f"{trail}: expected an ar/en object, found keys {sorted(value)}")
        return
    for lang in ("ar", "en"):
        text = value.get(lang)
        if not isinstance(text, str):
            err(f"{trail}.{lang}: expected text")
        elif not text.strip():
            (err if required else warn)(
                f"{trail}.{lang}: empty translation" + (" (required)" if required else "")
            )


def check_value(value, field, trail):
    ftype = field.get("type")
    required = bool(field.get("required"))
    is_list = bool(field.get("list"))

    if value is None or value == "":
        if required:
            # A half-filled entry must never block a deploy: the build handles it.
            warn(f"{trail}: required value is empty")
        return

    if is_list:
        if not isinstance(value, list):
            err(f"{trail}: expected a list")
            return
        item_field = dict(field)
        item_field.pop("list", None)
        for i, item in enumerate(value):
            check_value(item, item_field, f"{trail}[{i}]")
        return

    if ftype == "object":
        if not isinstance(value, dict):
            err(f"{trail}: expected an object")
            return
        if "ar" in value or "en" in value:
            check_bi(value, trail, required)
            return
        nested = walk_fields(field.get("fields"), COMPONENTS, trail)
        for key, sub in value.items():
            if key not in nested:
                err(f"{trail}.{key}: not defined in .pages.yml (it would be dropped on save)")
        for key, sub in nested.items():
            if key not in value:
                warn(f"{trail}.{key}: missing in the JSON file (empty form field)")
            else:
                check_value(value[key], sub, f"{trail}.{key}")
        return

    if ftype == "image":
        if not isinstance(value, str) or not value.strip():
            if required:
                warn(f"{trail}: required image is empty")
            return
        target = value.lstrip("/") if value.startswith("/") else value
        if not value.startswith(("http://", "https://")):
            if not os.path.exists(os.path.join(ROOT, target.replace("/", os.sep))):
                warn(f"{trail}: image file not found: {value}")
        return

    if ftype == "date":
        if not isinstance(value, str) or not re.match(r"^\d{4}-\d{2}-\d{2}", str(value)):
            err(f"{trail}: expected a YYYY-MM-DD date, found {value!r}")
        return

    if ftype == "select":
        allowed = [
            v.get("name") if isinstance(v, dict) else v
            for v in (field.get("options") or {}).get("values") or []
        ]
        if allowed and value not in allowed:
            err(f"{trail}: '{value}' is not one of {allowed}")
        return

    if ftype == "boolean":
        if not isinstance(value, bool):
            err(f"{trail}: expected true/false, found {value!r}")
        return

    if ftype in ("string", "text", None):
        if not isinstance(value, str):
            err(f"{trail}: expected text, found {type(value).__name__}")
        return


def main():
    global COMPONENTS
    if not os.path.exists(CONFIG):
        sys.exit(".pages.yml is missing")
    config = load_yaml(CONFIG)
    COMPONENTS = config.get("components") or {}

    # ---- media sources -----------------------------------------------------
    media = config.get("media") or []
    if isinstance(media, dict):
        media = [media]
    for source in media:
        folder = source.get("input")
        if not folder:
            err("media: a source has no 'input'")
            continue
        if not os.path.isdir(os.path.join(ROOT, folder)):
            err(f"media: input folder does not exist: {folder}")

    # ---- content entries ---------------------------------------------------
    seen_paths = set()
    for entry in entries(config.get("content")):
        kind = entry.get("type")
        path = entry.get("path")
        name = entry.get("name")
        if not path:
            err(f"content '{name}': missing path")
            continue
        seen_paths.add(path.replace("\\", "/"))
        fields = walk_fields(entry.get("fields"), COMPONENTS, name)

        if kind == "file":
            full = os.path.join(ROOT, path)
            if not os.path.exists(full):
                err(f"content '{name}': file not found: {path}")
                continue
            data = json.load(open(full, encoding="utf-8"))
            if not isinstance(data, dict):
                err(f"{path}: expected a JSON object at the top level")
                continue
            for key, value in data.items():
                if key not in fields:
                    err(f"{path}: key '{key}' is not editable (missing from .pages.yml)")
                else:
                    check_value(value, fields[key], f"{path}:{key}")
            for key in fields:
                if key not in data:
                    warn(f"{path}: field '{key}' is missing from the JSON file")

        elif kind == "collection":
            folder = os.path.join(ROOT, path)
            if not os.path.isdir(folder):
                err(f"content '{name}': folder not found: {path}")
                continue
            excluded = set(entry.get("exclude") or [])
            for filename in sorted(os.listdir(folder)):
                if not filename.endswith(".json") or filename in excluded:
                    continue
                full = os.path.join(folder, filename)
                data = json.load(open(full, encoding="utf-8"))
                trail = rel(full)
                if not isinstance(data, dict):
                    err(f"{trail}: expected a JSON object")
                    continue
                for key, value in data.items():
                    if key not in fields:
                        err(f"{trail}: key '{key}' is not editable (missing from .pages.yml)")
                    else:
                        check_value(value, fields[key], f"{trail}:{key}")

    # ---- reachability of every page file -----------------------------------
    pages_folder = os.path.join(CONTENT, "pages")
    for filename in sorted(os.listdir(pages_folder)):
        if not filename.endswith(".json"):
            continue
        path = f"content/pages/{filename}"
        if path not in seen_paths:
            err(f"{path}: not listed in .pages.yml, so it cannot be edited")

    # ---- navigation --------------------------------------------------------
    settings_path = os.path.join(CONTENT, "settings.json")
    if os.path.exists(settings_path):
        settings = json.load(open(settings_path, encoding="utf-8"))
        for item in settings.get("nav") or []:
            page = item.get("page")
            if page and not os.path.exists(os.path.join(pages_folder, f"{page}.json")):
                err(f"settings.json: nav points at missing page '{page}.json'")

    # ---- report ------------------------------------------------------------
    for message in warnings:
        print(f"WARN  {message}")
    for message in errors:
        print(f"ERROR {message}")
    print(f"\n{len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
