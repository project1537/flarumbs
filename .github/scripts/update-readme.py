#!/usr/bin/env python3
"""Regenerate the list of translated extensions in README.md from locale/*.yml.

Every locale/<vendor>-<name>.yml file is listed as the Composer package
<vendor>/<name>, unless locales.PACKAGE_NAMES says otherwise. Run it after adding or
removing a translation; CI runs it on every push to main.
"""
import re
import sys

from locales import CORE_FILES, ROOT, locale_files, package_name

README = ROOT / "README.md"
START = "<!-- extensions:start -->"
END = "<!-- extensions:end -->"

GROUPS = [
    ("Flarum", lambda vendor: vendor == "flarum"),
    ("FriendsOfFlarum", lambda vendor: vendor == "fof"),
    ("Other extensions", lambda vendor: vendor not in ("flarum", "fof")),
]


def build_list():
    packages = sorted(
        package_name(path.stem)
        for path in locale_files()
        if path.stem not in CORE_FILES
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
