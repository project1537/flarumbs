# Changelog

## 3.7.0 - 2026-11-20

### Added

- **medresanet/flarum-gate** 1.1: the admin's "Wall texts" section (per-language texts of the login wall) and its length message; the label of the wall's menu button on phones.

## 3.6.0 - 2026-11-19

### Added

- Translation for **medresanet/flarum-gate**, the login wall of medresa.net (a private extension, so it is listed without a Packagist link and skipped by the weekly upstream check). The extension ships English only; its Bosnian lives here.
- `core.views.unsubscribe_email_error.title`: Flarum 2.0.2 shows this key on the page for an invalid unsubscribe link but does not ship it, so the page showed the raw key.

## 3.5.0 - 2026-10-21

### Changed

- Passwords are now called **šifra** instead of **lozinka** everywhere: log-in, sign-up, password reset, settings and emails (34 places).
- One form per verb: **šifrovati** and **generisati** throughout. Core used šifrirati and generirati in 15 places.
- Placeholders and loading messages use the ellipsis character: "Učitavanje…" instead of "Učitavanje..." (22 places).
- Cancel buttons that only close a dialog say **Odustani**, as most of the pack already did (4 places in fof/badges, fof/byobu and ianm/twofactor). **Otkaži** stays for stopping a running process.
- Smaller wording fixes: "meni" instead of "izbornik", "neobavezno" instead of "opcionalno", "dozvola" instead of "ovlaštenje".

### Added

- [GLOSSARY.md](GLOSSARY.md): the terms and style the pack uses, for anyone adding or fixing a translation.
- Every pull request is checked automatically for invalid YAML, duplicate keys, broken references, broken plurals, wording the glossary avoids, and the dates and relative times from `config.js`.
- A weekly check compares every translation with the latest release of its extension and keeps an issue open listing what needs translating.

## 3.4.0 - 2026-10-20

### Added

- Translations for **flarum/messages**, **flarum/audit**, **flarum/nicknames** and **flarum/emoji**. All four ship with every Flarum 2 install.
- 61 strings added in recent releases of fof/anti-spam, fof/reactions, fof/oauth, fof/upload, fof/split, fof/ignore-users, fof/merge-discussions, fof/drafts, fof/top-posters-widget and ramon/guest-cta.

### Changed

- 5 translations updated where the English wording changed upstream.
- README rewritten, with installation and activation steps and a list of translated extensions that updates itself.
- More search keywords in `composer.json`.

### Removed

- ramon/avocado translation.
- Keys that fof/anti-spam no longer uses.
- The `.github` folder is no longer included in installs.

## 3.3.0 - 2026-10-20

### Fixed

- The flectar/turnstile translation now loads; the file was missing its `.yml` extension.
- `composer.json`: duplicate `support` key removed, homepage corrected, branch alias now points at `main` as `3.x-dev`.
