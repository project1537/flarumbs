"""Shared helpers for the scripts that check and document locale/*.yml."""
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
LOCALE = ROOT / "locale"

# Locale files that belong to Flarum core rather than to an extension.
CORE_FILES = {"core", "validation"}

# Packages whose Composer name is not simply <vendor>/<name> of the file name.
PACKAGE_NAMES = {
    "datlechin-discussion-overview": "datlechin/flarum-discussion-overview",
    "datlechin-link-preview": "datlechin/flarum-link-preview",
    "datlechin-signup-button": "datlechin/flarum-signup-button",
    "ekumanov-forum-widgets": "ekumanov/flarum-ext-forum-widgets",
    "flectar-turnstile": "flectar/flarum-turnstile",
    "michaelbelgium-ai-autoreply": "michaelbelgium/flarum-ai-autoreply",
}


def package_name(stem):
    if stem in CORE_FILES:
        return "flarum/core"
    if stem in PACKAGE_NAMES:
        return PACKAGE_NAMES[stem]
    vendor, _, name = stem.partition("-")
    return f"{vendor}/{name}"


def locale_files():
    return sorted(LOCALE.glob("*.yml"))


class DuplicateKeyError(yaml.YAMLError):
    pass


# BaseLoader keeps every scalar a string, as Flarum's YAML parser does: PyYAML's
# default loaders would turn values such as "No" or "On" into booleans.
class _StrictLoader(yaml.BaseLoader):
    pass


def _mapping(loader, node, deep=False):
    seen = set()
    for key_node, _ in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in seen:
            raise DuplicateKeyError(
                f"duplicate key '{key}' (line {key_node.start_mark.line + 1})"
            )
        seen.add(key)
    return loader.construct_mapping(node, deep)


_StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _mapping)


def load(text):
    """Parse YAML, raising DuplicateKeyError on a repeated key."""
    return yaml.load(text, _StrictLoader) or {}


def load_lenient(text):
    """Parse YAML from elsewhere, where a repeated key is not ours to report."""
    return yaml.load(text, yaml.BaseLoader) or {}


def flatten(data, prefix=""):
    out = {}
    for key, value in (data or {}).items():
        path = f"{prefix}.{key}" if prefix else str(key)
        if isinstance(value, dict):
            out.update(flatten(value, path))
        else:
            out[path] = value
    return out


def is_reference(value):
    return isinstance(value, str) and value.strip().startswith("=>")


def reference_target(value):
    return value.strip()[2:].strip()


def key_lines(text):
    """Map each flattened key to its 1-based line number."""
    lines = {}

    def walk(node, prefix):
        if not isinstance(node, yaml.MappingNode):
            return
        for key_node, value_node in node.value:
            path = f"{prefix}.{key_node.value}" if prefix else str(key_node.value)
            lines[path] = key_node.start_mark.line + 1
            walk(value_node, path)

    walk(yaml.compose(text, _StrictLoader), "")
    return lines
