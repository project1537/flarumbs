#!/usr/bin/env python3
"""Check locale/*.yml for mistakes that would break or degrade the pack.

Errors (exit code 1): invalid YAML, duplicate keys, references to keys that
do not exist, and ICU messages with unbalanced braces or a plural without an
"other" branch.

Warnings: wording that GLOSSARY.md says to avoid, and the formal "you" written
in the wrong case for an email or the interface.

Runs without network access, on every pull request and push to main.
"""
import os
import re
import sys

from locales import (LOCALE, flatten, is_reference, key_lines, load,
                     locale_files, reference_target)

# Wording GLOSSARY.md asks to avoid, with what to write instead.
AVOID = [
    (r"\bdiskusij\w*", "tema"),
    (r"\bregistrov\w*", "registrirati"),
    (r"\bizbriš\w*", "obrisati"),
    (r"\bspremi\w*", "sačuvati"),
    (r"\bnotifikacij\w*", "obavještenje"),
    (r"\bfajl\w*", "datoteka"),
    (r"\bpoveznic\w*", "link"),
    (r"\btjed\w*", "sedmica"),
    (r"\be-pošt\w*", "e-mail"),
    (r"\bmejl\w*", "e-mail"),
    (r"\bnadim\w*", "prikazano ime"),
    (r"\blogin\b", "prijava"),
    (r"\bsuspendov\w*", "blokirati"),
    (r"\bovlaštenj\w*", "dozvola"),
    (r"\blozin\w*", "šifra"),
    (r"\bizbornik\w*", "meni"),
    (r"\bopcionaln\w*", "neobavezno"),
    (r"\w*šifrir\w*", "šifrovati"),
    (r"\w*generir\w*", "generisati"),
    (r"\.\.\.", "…"),
]

# Formal "you": lower case in the interface, capitalised in emails, except at
# the start of a sentence, where it is always capitalised.
PRONOUN = re.compile(r"\b([Vv](?:i|as|ama|am|aš|aša|aše|ašeg|ašega|ašem|ašemu|ašoj|ašu|ašim|aših|ašima|ašom))\b")


def pronoun_problems(key, message):
    in_email = key.split(".")[1:2] == ["email"]
    for match in PRONOUN.finditer(message):
        word = match.group(1)
        before = message[:match.start()].rstrip(" „\"(*")
        if not before or before[-1] in ".!?:\n{>":
            continue
        wanted = (word[0].upper() if in_email else word[0].lower()) + word[1:]
        if word != wanted:
            where = "emails" if in_email else "the interface"
            yield f"\"{word}\" - GLOSSARY.md writes \"{wanted}\" in {where}"

GITHUB = os.environ.get("GITHUB_ACTIONS") == "true"


def report(kind, path, line, message):
    rel = path.relative_to(LOCALE.parent)
    if GITHUB:
        print(f"::{kind} file={rel},line={line}::{message}")
    else:
        print(f"{kind.upper()}: {rel}:{line}: {message}")


def check_icu(message):
    """Return a problem with an ICU message, or None."""
    depth = 0
    for ch in message:
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth < 0:
                return "unbalanced braces"
    if depth:
        return "unbalanced braces"
    for match in re.finditer(r"\{\s*\w+\s*,\s*(plural|selectordinal)\s*,", message):
        # find the end of this plural block and look for an "other" branch
        depth, i = 0, match.start()
        while i < len(message):
            if message[i] == "{":
                depth += 1
            elif message[i] == "}":
                depth -= 1
                if depth == 0:
                    break
            i += 1
        if not re.search(r"\bother\s*\{", message[match.end():i]):
            return "plural without an 'other' branch"
    return None


def main():
    errors = warnings = 0
    keys = {}
    parsed = []

    for path in locale_files():
        text = path.read_text(encoding="utf-8")
        try:
            strings = flatten(load(text))
        except Exception as exc:  # noqa: BLE001 - report any parse failure
            mark = getattr(exc, "problem_mark", None)
            found = re.search(r"\(line (\d+)\)", str(exc))
            line = mark.line + 1 if mark else int(found.group(1)) if found else 1
            report("error", path, line, f"invalid YAML: {exc}")
            errors += 1
            continue
        keys.update(strings)
        parsed.append((path, key_lines(text), strings))

    for path, lines, strings in parsed:
        for key, value in strings.items():
            if not isinstance(value, str):
                continue
            line = lines.get(key, 1)
            if is_reference(value):
                if reference_target(value) not in keys:
                    report("error", path, line,
                           f"{key} points to {reference_target(value)}, which does not exist")
                    errors += 1
                continue
            problem = check_icu(value)
            if problem:
                report("error", path, line, f"{key}: {problem}")
                errors += 1
            for problem in pronoun_problems(key, value):
                report("warning", path, line, f"{key}: {problem}")
                warnings += 1
            for pattern, instead in AVOID:
                found = re.search(pattern, value, re.IGNORECASE)
                if found:
                    report("warning", path, line,
                           f"{key}: \"{found.group(0)}\" - GLOSSARY.md uses \"{instead}\"")
                    warnings += 1

    print(f"{len(parsed)} files, {len(keys)} keys: {errors} errors, {warnings} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
