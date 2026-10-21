# Changelog

Notable changes to the site, newest first. Format based on [Keep a Changelog](https://keepachangelog.com/); versions follow `MAJOR.MINOR.PATCH` (see the README).

## [Unreleased]

### Added
- `DESIGN.md`: body font (Newsreader for text, IBM Plex Sans for buttons and the menu), with sizes and the reasons behind them.
- `DESIGN.md`: page plan in the order Hero, About, Tutoring, GRE textbook, Projects, Contact, with each section's claim and proof; hero button "Get In Touch".
- `DESIGN.md`: interactive pieces. Spinning circles in the hero that draw Carson's initials as one curve, with a slider and a live measure of how close the drawing is, plus one small live piece each in About, Tutoring and Projects, built so they can be swapped later.
- `PRODUCT.md`: NeuronDiagrams and StarBattleSolver recorded as real work.

### Changed
- `CLAUDE.md`: commit messages must be written in plain, beginner-friendly English.
- `CLAUDE.md`: all text in American English; Claude should suggest Three.js and Manim wherever they'd fit.
- `WORKFLOW.md`: Stage 2 marked done.

## [0.3.0] - 2026-10-20

Setup for the redesign. No visible change to the live site.

### Added
- AI design skills for Claude Code: Emil Kowalski's skills, Impeccable (with its automatic design-check hook), design-taste-frontend, and playwright-cli.
- `PRODUCT.md`: audiences, purpose, and facts the site must never invent.
- `DESIGN.md`: chosen palette (charcoal blue and lilac at night, cream and plum by day), DM Serif Display headlines, and design rules.
- `WORKFLOW.md`: step-by-step process for building the site.
- `CHANGELOG.md` and a full `README.md`.
- `.gitignore` for personal settings, caches, and compiled binaries.

### Changed
- `CLAUDE.md` now describes the real PDF pipeline and the chosen aesthetic.

### Removed
- `pdf/main.pdf`, an unused leftover from an earlier pipeline.

## [0.2.0] - 2026-07-09

### Added
- Download link for the GRE mathematics textbook.
- Automatic pipeline that copies the textbook PDF from `Mathematics-for-the-GRE` into `pdf/GRE-Textbook.pdf`.

### Changed
- Moved the download link and pointed it at the GRE textbook.

## [0.1.0] - 2026-03-21

### Added
- First version of the site from a template: hero, about, and connect sections, with animation effects.
- A custom domain file (`CNAME`) was added and then removed the same day.

[Unreleased]: https://github.com/carsonmit/carsonmit.github.io/compare/v0.3.0...HEAD
[0.3.0]: https://github.com/carsonmit/carsonmit.github.io/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/carsonmit/carsonmit.github.io/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/carsonmit/carsonmit.github.io/releases/tag/v0.1.0
