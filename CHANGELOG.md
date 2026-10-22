# Changelog

Notable changes to the site, newest first. Format based on [Keep a Changelog](https://keepachangelog.com/); versions follow `MAJOR.MINOR.PATCH` (see the README).

## [Unreleased]

### Added
- `design/mockups/hero-fourier.html`: the approved hero centerpiece (spinning circles drawing C and M) saved as a page you can open in a browser, so the built site can match it exactly.
- `DESIGN.md` and `README.md` point to it as the reference.
- README "Tools" section: how to set up and use the GitHub CLI, Manim (math animation videos), and Lighthouse (page-quality scores), plus the site's Lighthouse scores before the redesign.
- `CLAUDE.md`: booking through Cal.com (account connected to Claude) and a Formspree contact form chosen for the Tutoring and Contact sections.
- `PRODUCT.md`: Carson's real content from Stage 1: bio (education), email, LinkedIn and GitHub links (no Twitter), tutoring levels, format (online, or in person in South Orange County), and rates ($60/hour online, $80/hour in person). Parts he'll write later are marked as placeholders.
- `content/subjects.md`: an easy-to-edit list of tutoring subjects that the site will read from.
- `images/carson.jpg`: Carson's photo, converted to a web-friendly size and format (JPEG), with its hidden location data removed.

### Changed
- `WORKFLOW.md`: Stage 1 items supplied so far are checked off; the rest are listed for later.
- `DESIGN.md`: prices return to the Tutoring section now that real rates exist.

## [0.4.0] - 2026-10-21

Stage 2: design decisions finished. No visible change to the live site yet; everything here is the plan in `DESIGN.md` that Stage 3 will build.

### Added
- Body font: Newsreader for text (18.5px, the same weight in light and dark mode so text never shifts when switching), IBM Plex Sans for buttons and the menu. The reasons are recorded too.
- Page plan, person first: Hero, About, Tutoring, GRE textbook, Projects, Contact. Each section lists the claim it makes and the real proof behind it. The hero's main button is "Get In Touch".
- Hero centerpiece: spinning circles (a Fourier series) draw Carson's initials C and M as one curve, lifting the pen between letters. It draws once on load, then shows the two equations behind it, set in LaTeX.
- A slider in the hero (from 1 to 100) sets how many circles spin, with a live line showing how far the drawing misses the real letters, so students can watch the error shrink.
- Small live pieces for other sections, one per screen: a picture proof that $1 + 3 + \dots + (2n-1) = n^2$ and the Collatz "pick a number" game in About; an equation that solves itself as you scroll in Tutoring; a neuron diagram and a Star Battle puzzle in Projects. Each is built as a separate module so it can be swapped later.
- `PRODUCT.md`: NeuronDiagrams and StarBattleSolver recorded as real work the site can show.

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

[Unreleased]: https://github.com/carsonmit/carsonmit.github.io/compare/v0.4.0...HEAD
[0.4.0]: https://github.com/carsonmit/carsonmit.github.io/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/carsonmit/carsonmit.github.io/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/carsonmit/carsonmit.github.io/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/carsonmit/carsonmit.github.io/releases/tag/v0.1.0
