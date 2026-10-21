#!/usr/bin/env python3
"""Compare the translations with the English sources of each extension.

  sync-upstream.py --report report.md
      Write a Markdown report of what needs translating: keys missing from the
      Bosnian file, keys the extension no longer has, placeholders that differ
      from the English, and English text that changed since it was last
      translated. Sets has_findings=true|false in $GITHUB_OUTPUT.

  sync-upstream.py --accept all|<locale name>[,<locale name>...]
      Record the current English text as translated, in .github/upstream.lock.json.
      Run this after updating a translation whose English source changed.

The English source is the latest stable release of each package that supports
Flarum 2, as listed on Packagist.
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

from locales import (ROOT, flatten, is_reference, load, load_lenient, locale_files,
                     package_name)

LOCK = ROOT / ".github" / "upstream.lock.json"
REPORT_LIMIT = 60000  # GitHub issue bodies are capped at 65536 characters


def fetch(url):
    for attempt in range(4):
        try:
            with urllib.request.urlopen(url, timeout=30) as response:
                return response.read()
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                return None
        except OSError:
            pass
        time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"could not fetch {url}")


def supports_flarum_2(version):
    constraint = version.get("require", {}).get("flarum/core", "")
    return bool(re.search(r"\^2|>=\s*2|~2|\b2\.\*|^\*$", constraint))


def pick_release(package):
    data = fetch(f"https://repo.packagist.org/p2/{package}.json")
    if not data:
        raise RuntimeError(f"{package} is not on Packagist")
    versions = json.loads(data)["packages"][package]
    if package == "flarum/core":
        candidates = versions
    else:
        candidates = [v for v in versions if supports_flarum_2(v)] or versions
    stable = [v for v in candidates if re.match(r"^v?\d+(\.\d+)*$", v["version"])]
    return (stable or candidates)[0]


def english_source(stem):
    package = package_name(stem)
    release = pick_release(package)
    match = re.search(r"github\.com/([^/]+/[^/]+?)(?:\.git)?$", release["source"]["url"])
    if not match:
        raise RuntimeError(f"{package} is not hosted on GitHub")
    repo, ref = match.group(1), release["source"]["reference"]
    name = package.split("/", 1)[1]
    if stem in ("core", "validation"):
        paths = [f"locale/{stem}.yml", f"framework/core/locale/{stem}.yml"]
    else:
        paths = ["locale/en.yml", "resources/locale/en.yml", f"extensions/{name}/locale/en.yml"]
    for path in paths:
        data = fetch(f"https://raw.githubusercontent.com/{repo}/{ref}/{path}")
        if data:
            return {
                "package": package,
                "version": release["version"],
                "strings": {k: v for k, v in flatten(load_lenient(data)).items()
                            if isinstance(v, str)},
            }
    raise RuntimeError(f"no English locale file found for {package} {release['version']}")


def placeholders(message):
    # drop the openings of plural/select branches ("one {", "=1 {") so their
    # text is not mistaken for an argument name
    message = re.sub(r"(?:\b(?:zero|one|two|few|many|other)|=\d+)\s*\{", "\u2039", message)
    return sorted(set(re.findall(r"\{\s*(\w+)\s*[,}]", message)))


def tags(message):
    return sorted(re.findall(r"</?([A-Za-z][\w-]*)>", message))


def compare(stem, source, locked):
    path = ROOT / "locale" / f"{stem}.yml"
    ours = {k: v for k, v in flatten(load(path.read_text(encoding="utf-8"))).items()
            if isinstance(v, str)}
    english = source["strings"]
    found = {
        "missing": [k for k in english if k not in ours],
        "obsolete": [k for k in ours if k not in english],
        "placeholders": [],
        "changed": [],
    }
    for key, en in english.items():
        bs = ours.get(key)
        if bs is None or is_reference(en) or is_reference(bs):
            continue
        if placeholders(en) != placeholders(bs) or tags(en) != tags(bs):
            found["placeholders"].append(key)
        old = locked.get("strings", {}).get(key)
        if old is not None and old != en:
            found["changed"].append(key)
    return ours, found


def quote(text):
    text = str(text).replace("\n", " ").strip()
    return "`" + (text[:200] + "…" if len(text) > 200 else text).replace("`", "'") + "`"


def write_report(results, errors, out):
    lines = []
    total = 0
    for stem, (source, ours, found, locked) in results.items():
        count = sum(len(v) for v in found.values())
        if not count:
            continue
        total += count
        lines.append(f"### `locale/{stem}.yml` - {source['package']} {source['version']}\n")
        english = source["strings"]
        if found["missing"]:
            lines.append(f"**Not translated ({len(found['missing'])})**\n")
            lines += [f"- `{k}`: {quote(english[k])}" for k in found["missing"]]
            lines.append("")
        if found["changed"]:
            lines.append(f"**English changed since it was translated ({len(found['changed'])})**\n")
            for k in found["changed"]:
                lines.append(f"- `{k}`\n  - was: {quote(locked['strings'][k])}\n"
                             f"  - now: {quote(english[k])}\n  - ours: {quote(ours[k])}")
            lines.append("")
        if found["placeholders"]:
            lines.append(f"**Placeholders or tags differ from the English ({len(found['placeholders'])})**\n")
            lines += [f"- `{k}`\n  - en: {quote(english[k])}\n  - bs: {quote(ours[k])}"
                      for k in found["placeholders"]]
            lines.append("")
        if found["obsolete"]:
            lines.append(f"**No longer used by the extension, can be removed ({len(found['obsolete'])})**\n")
            lines += [f"- `{k}`" for k in found["obsolete"]]
            lines.append("")

    head = [
        "The weekly check compared every translation with the latest release of its extension.",
        "",
        f"**{total} item(s) need attention.** This issue updates itself every week and closes "
        "once nothing is left.",
        "",
        "Untranslated, obsolete and placeholder items clear themselves once the file is fixed. "
        "Items under *English changed* stay until the new English is accepted: after updating "
        "those translations, run the **Check upstream translations** workflow with `accept` set "
        "to the locale names (for example `fof-upload,fof-oauth`) or `all`.",
        "",
    ]
    if errors:
        head += ["**Could not check:**", ""] + [f"- `{s}`: {e}" for s, e in errors.items()] + [""]
    body = "\n".join(head + lines)
    if len(body) > REPORT_LIMIT:
        body = body[:REPORT_LIMIT] + "\n\n…report truncated; run the script locally for the full list."
    out.write_text(body + "\n", encoding="utf-8")
    return total


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--report", metavar="FILE")
    group.add_argument("--accept", metavar="NAMES")
    args = parser.parse_args()

    lock = json.loads(LOCK.read_text(encoding="utf-8")) if LOCK.exists() else {}
    stems = [p.stem for p in locale_files()]

    if args.accept:
        wanted = stems if args.accept.strip() == "all" else [
            s.strip().removesuffix(".yml") for s in args.accept.split(",") if s.strip()]
        unknown = [s for s in wanted if s not in stems]
        if unknown:
            sys.exit(f"no such locale file: {', '.join(unknown)}")
        for stem in wanted:
            lock[stem] = english_source(stem)
            print(f"accepted {stem} ({lock[stem]['package']} {lock[stem]['version']})")
        for stem in [s for s in lock if s not in stems]:
            del lock[stem]
        LOCK.write_text(json.dumps(dict(sorted(lock.items())), ensure_ascii=False,
                                   indent=1, sort_keys=True) + "\n", encoding="utf-8")
        return 0

    results, errors = {}, {}
    for stem in stems:
        try:
            source = english_source(stem)
        except Exception as exc:  # noqa: BLE001 - one failing package must not hide the rest
            errors[stem] = str(exc)
            continue
        ours, found = compare(stem, source, lock.get(stem, {}))
        results[stem] = (source, ours, found, lock.get(stem, {}))
        print(f"{stem}: " + ", ".join(f"{len(v)} {k}" for k, v in found.items()))

    total = write_report(results, errors, Path(args.report))
    has_findings = bool(total or errors)
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as fh:
            fh.write(f"has_findings={'true' if has_findings else 'false'}\n")
    print(f"{total} item(s), {len(errors)} package(s) not checked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
