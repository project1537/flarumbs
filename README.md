<img src="https://raw.githubusercontent.com/project1537/flarumbs/main/flag.svg" alt="Flag of Bosnia and Herzegovina" width="120">

# Bosnian Language Pack for Flarum

[![Latest version](https://img.shields.io/packagist/v/project1537/flarumbs)](https://packagist.org/packages/project1537/flarumbs)
[![Total downloads](https://img.shields.io/packagist/dt/project1537/flarumbs)](https://packagist.org/packages/project1537/flarumbs)
[![License](https://img.shields.io/packagist/l/project1537/flarumbs)](https://github.com/project1537/flarumbs/blob/main/LICENSE)

> **Bosanski:** Prijevod Flaruma na bosanski jezik: jezgra platforme i više od 70 ekstenzija. Instalacija i aktivacija opisane su ispod; greške u prijevodu prijavite kroz [Issues](https://github.com/project1537/flarumbs/issues).

A complete Bosnian translation of Flarum core, its bundled extensions and many popular community extensions, including date and relative-time formatting with correct Bosnian grammar.

## Requirements

- Flarum **2.x**
- Composer 2

Still on Flarum 1.8? Install the last release made for it:

```bash
composer require project1537/flarumbs:^1.5
```

## Installation

Run this in the directory where Flarum is installed:

```bash
composer require project1537/flarumbs
```

Then turn it on:

1. In the admin panel, open **Extensions** and enable **Bosnian Language Pack**.
2. Open **Basics** and set **Default Language** to **Bosanski**.

## Updating

What changed in each release is listed in the [changelog](https://github.com/project1537/flarumbs/blob/main/CHANGELOG.md).

```bash
composer update project1537/flarumbs
php flarum cache:clear
```

## Removing

```bash
composer remove project1537/flarumbs
php flarum cache:clear
```

## Translated extensions

A translation only loads when its extension is enabled, so unused ones cost nothing.

<!-- extensions:start -->
Translations for **80 extensions** are included:

#### Flarum (22)

| Package |
| --- |
| [flarum/akismet](https://packagist.org/packages/flarum/akismet) |
| [flarum/approval](https://packagist.org/packages/flarum/approval) |
| [flarum/audit](https://packagist.org/packages/flarum/audit) |
| [flarum/bbcode](https://packagist.org/packages/flarum/bbcode) |
| [flarum/deck](https://packagist.org/packages/flarum/deck) |
| [flarum/emoji](https://packagist.org/packages/flarum/emoji) |
| [flarum/extension-manager](https://packagist.org/packages/flarum/extension-manager) |
| [flarum/flags](https://packagist.org/packages/flarum/flags) |
| [flarum/gdpr](https://packagist.org/packages/flarum/gdpr) |
| [flarum/likes](https://packagist.org/packages/flarum/likes) |
| [flarum/lock](https://packagist.org/packages/flarum/lock) |
| [flarum/markdown](https://packagist.org/packages/flarum/markdown) |
| [flarum/mentions](https://packagist.org/packages/flarum/mentions) |
| [flarum/messages](https://packagist.org/packages/flarum/messages) |
| [flarum/nicknames](https://packagist.org/packages/flarum/nicknames) |
| [flarum/pusher](https://packagist.org/packages/flarum/pusher) |
| [flarum/realtime](https://packagist.org/packages/flarum/realtime) |
| [flarum/statistics](https://packagist.org/packages/flarum/statistics) |
| [flarum/sticky](https://packagist.org/packages/flarum/sticky) |
| [flarum/subscriptions](https://packagist.org/packages/flarum/subscriptions) |
| [flarum/suspend](https://packagist.org/packages/flarum/suspend) |
| [flarum/tags](https://packagist.org/packages/flarum/tags) |

#### FriendsOfFlarum (43)

| Package |
| --- |
| [fof/anti-spam](https://packagist.org/packages/fof/anti-spam) |
| [fof/badges](https://packagist.org/packages/fof/badges) |
| [fof/best-answer](https://packagist.org/packages/fof/best-answer) |
| [fof/byobu](https://packagist.org/packages/fof/byobu) |
| [fof/cookie-consent](https://packagist.org/packages/fof/cookie-consent) |
| [fof/default-group](https://packagist.org/packages/fof/default-group) |
| [fof/default-user-preferences](https://packagist.org/packages/fof/default-user-preferences) |
| [fof/discussion-thumbnail](https://packagist.org/packages/fof/discussion-thumbnail) |
| [fof/discussion-views](https://packagist.org/packages/fof/discussion-views) |
| [fof/disposable-emails](https://packagist.org/packages/fof/disposable-emails) |
| [fof/drafts](https://packagist.org/packages/fof/drafts) |
| [fof/first-post-approval](https://packagist.org/packages/fof/first-post-approval) |
| [fof/follow-tags](https://packagist.org/packages/fof/follow-tags) |
| [fof/formatting](https://packagist.org/packages/fof/formatting) |
| [fof/forum-widgets-core](https://packagist.org/packages/fof/forum-widgets-core) |
| [fof/frontpage](https://packagist.org/packages/fof/frontpage) |
| [fof/ignore-users](https://packagist.org/packages/fof/ignore-users) |
| [fof/links](https://packagist.org/packages/fof/links) |
| [fof/mark-unread](https://packagist.org/packages/fof/mark-unread) |
| [fof/merge-discussions](https://packagist.org/packages/fof/merge-discussions) |
| [fof/moderator-notes](https://packagist.org/packages/fof/moderator-notes) |
| [fof/move-posts](https://packagist.org/packages/fof/move-posts) |
| [fof/news-widget](https://packagist.org/packages/fof/news-widget) |
| [fof/oauth](https://packagist.org/packages/fof/oauth) |
| [fof/pages](https://packagist.org/packages/fof/pages) |
| [fof/photoswipe](https://packagist.org/packages/fof/photoswipe) |
| [fof/polls](https://packagist.org/packages/fof/polls) |
| [fof/pwa](https://packagist.org/packages/fof/pwa) |
| [fof/reactions](https://packagist.org/packages/fof/reactions) |
| [fof/rich-text](https://packagist.org/packages/fof/rich-text) |
| [fof/share-social](https://packagist.org/packages/fof/share-social) |
| [fof/sitemap](https://packagist.org/packages/fof/sitemap) |
| [fof/socialprofile](https://packagist.org/packages/fof/socialprofile) |
| [fof/split](https://packagist.org/packages/fof/split) |
| [fof/subscribed](https://packagist.org/packages/fof/subscribed) |
| [fof/synopsis](https://packagist.org/packages/fof/synopsis) |
| [fof/terms](https://packagist.org/packages/fof/terms) |
| [fof/top-posters-widget](https://packagist.org/packages/fof/top-posters-widget) |
| [fof/upload](https://packagist.org/packages/fof/upload) |
| [fof/user-bio](https://packagist.org/packages/fof/user-bio) |
| [fof/user-directory](https://packagist.org/packages/fof/user-directory) |
| [fof/usercard-stats](https://packagist.org/packages/fof/usercard-stats) |
| [fof/username-request](https://packagist.org/packages/fof/username-request) |

#### Other extensions (15)

| Package |
| --- |
| [acpl/mobile-tab](https://packagist.org/packages/acpl/mobile-tab) |
| [datlechin/flarum-discussion-overview](https://packagist.org/packages/datlechin/flarum-discussion-overview) |
| [datlechin/flarum-link-preview](https://packagist.org/packages/datlechin/flarum-link-preview) |
| [datlechin/flarum-signup-button](https://packagist.org/packages/datlechin/flarum-signup-button) |
| [ekumanov/flarum-ext-forum-widgets](https://packagist.org/packages/ekumanov/flarum-ext-forum-widgets) |
| [ernestdefoe/google-fonts](https://packagist.org/packages/ernestdefoe/google-fonts) |
| [flectar/flarum-turnstile](https://packagist.org/packages/flectar/flarum-turnstile) |
| [forumaker/friendship](https://packagist.org/packages/forumaker/friendship) |
| [huseyinfiliz/notificationhub](https://packagist.org/packages/huseyinfiliz/notificationhub) |
| [ianm/follow-users](https://packagist.org/packages/ianm/follow-users) |
| [ianm/twofactor](https://packagist.org/packages/ianm/twofactor) |
| [michaelbelgium/flarum-ai-autoreply](https://packagist.org/packages/michaelbelgium/flarum-ai-autoreply) |
| [ramon/backup](https://packagist.org/packages/ramon/backup) |
| [ramon/guest-cta](https://packagist.org/packages/ramon/guest-cta) |
| [ramon/verified](https://packagist.org/packages/ramon/verified) |
<!-- extensions:end -->

## Reporting mistakes and contributing

Found a wrong or missing translation? [Open an issue](https://github.com/project1537/flarumbs/issues) and include the English text or the translation key if you know it. Pull requests are welcome too: translations live in [`locale/`](https://github.com/project1537/flarumbs/tree/main/locale), one file per extension. Please follow the terms and style in [GLOSSARY.md](https://github.com/project1537/flarumbs/blob/main/GLOSSARY.md); every pull request is checked automatically.

## License

Released under the [MIT License](https://github.com/project1537/flarumbs/blob/main/LICENSE).
