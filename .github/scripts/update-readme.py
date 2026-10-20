#!/usr/bin/env python3
"""Regenerate the list of translated extensions in README.md from locale/*.yml.

Every locale/<vendor>-<name>.yml file is listed as the Composer package
<vendor>/<name>, unless PACKAGE_NAMES says otherwise. Run it after adding or
removing a translation; CI runs it on every push to main.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
README = ROOT / "README.md"
START = "<!-- extensions:start -->"
END = "<!-- extensions:end -->"

# Locale files that are not extensions.
SKIP = {"core", "validation"}

# Packages whose Composer name is not simply <vendor>/<name> of the file name.
PACKAGE_NAMES = {
    "datlechin-discussion-overview": "datlechin/flarum-discussion-overview",
    "datlechin-link-preview": "datlechin/flarum-link-preview",
    "datlechin-signup-button": "datlechin/flarum-signup-button",
    "ekumanov-forum-widgets": "ekumanov/flarum-ext-forum-widgets",
    "flectar-turnstile": "flectar/flarum-turnstile",
    "michaelbelgium-ai-autoreply": "michaelbelgium/flarum-ai-autoreply",
}

GROUPS = [
    ("Flarum", lambda vendor: vendor == "flarum"),
    ("FriendsOfFlarum", lambda vendor: vendor == "fof"),
    ("Other extensions", lambda vendor: vendor not in ("flarum", "fof")),
]


def package_name(stem):
    if stem in PACKAGE_NAMES:
        return PACKAGE_NAMES[stem]
    vendor, _, name = stem.partition("-")
    return f"{vendor}/{name}"


def build_list():
    packages = sorted(
        package_name(path.stem)
        for path in (ROOT / "locale").glob("*.yml")
        if path.stem not in SKIP
    )
    lines = [f"Translations for **{len(packages)} extensions** are included:", ""]
    for title, belongs in GROUPS:
        group = [p for p in packages if belongs(p.split("/")[0])]
        if not group:
            continue
        lines += [f"#### {title} ({len(group)})", "", "| Package |", "| --- |"]
        lines += [f"| [{p}](https://packagist.org/packages/{p}) |" for p in group]
        lines.append("")
    return "\n".join(lines).rstrip()


def main():
    text = README.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(START) + ".*?" + re.escape(END), re.S)
    if not pattern.search(text):
        sys.exit(f"README.md has no {START} ... {END} block")
    updated = pattern.sub(lambda _: f"{START}\n{build_list()}\n{END}", text)
    if updated != text:
        README.write_text(updated, encoding="utf-8")
        print("README.md updated")
    else:
        print("README.md already up to date")


if __name__ == "__main__":
    main()
