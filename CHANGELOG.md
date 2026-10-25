# Changelog

Notable changes to the site, newest first. Format based on [Keep a Changelog](https://keepachangelog.com/); versions follow `MAJOR.MINOR.PATCH` (see the README).

## [Unreleased]

### Added
- The Tutoring page: rates ($60 per hour online, $80 in person, paid after the lesson by Zelle, PayPal or Apple Cash) and two large booking cards, **Book a Lesson** and **Book an Intro Call**, on the first screen; the subjects (read from `content/subjects.md`); a marked placeholder for "How I Teach"; and a sample of the GRE textbook (four pages of explanations, each opening the PDF at that page).
- "One Problem, Step by Step": a worked problem that solves itself as you scroll, one line at a time, with each step's reason in a box that follows the newest line, and Back / Next buttons. Three problems: a logarithm equation, a Putnam integral, and a dice paradox.
- Booking through Cal.com: an Intro Call (15 minutes, Zoom or phone) and a Tutoring Session (1, 1½ or 2 hours, Zoom or in person), where students propose up to three times and Carson confirms one.
- `images/gre/`: pictures of textbook pages for the Tutoring page; `design/mockups/tutoring-solve.html`: the approved mockup of the step-by-step problem.

### Changed
- Every page now links `styles.css` and `site.js` with a version tag (`?v=…`), so browsers fetch the new copy after a change instead of showing an old one.
- `content/subjects.md`: a note that subjects go below the "## Subjects" line (the site skips the instructions above it).

## [0.8.0] - 2026-10-24

The site is now split into separate pages, so each audience goes straight to its part.

### Added
- Separate pages: Home, About Me, Tutoring, Projects and Contact, each reached from the top menu (which now includes Home and Contact and underlines the page you're on). Tutoring, Projects and Contact are marked placeholders until they're built.
- Home page: Carson's photo above his name, and a short "door" to each page under the hero.
- A gentle animation between pages: the menu stays still while the page fades and rises into place (instant for visitors who prefer reduced motion).
- A note at the bottom of the home page: "This website is a proud product of extensive vibe-coding with the help of Claude Code."
- `styles.css` and `site.js`, shared by every page.

### Changed
- The email address is shown as "carsonm6719 [at] gmail [dot] com" and only becomes a real address when clicked, to keep it away from spam bots.
- Every title uses Title Case ("About Me", "Ehrhart's Theorem").
- The hero's equations show from the start instead of appearing after the drawing.
- About Me works better on tablets (one column when held upright) and no longer scrolls sideways there.
- The 3D permutahedron and the Banach–Tarski video now sit on the page's own background color in both modes.
- Smaller gaps under the menu and between the hero and the doors.
- Fixed the order of About Me's headings for screen readers, and added a colon to the lead-in before the math examples.

## [0.7.0] - 2026-10-24

The About section is built: Carson's photo and bio, then three pieces of math he finds beautiful. This version was tagged but published together with 0.8.0.

### Added
- About: Carson's photo, bio, research areas (combinatorics, logic, probability, philosophy of mathematics) and life outside math (books, video games, music, movies, walks with his dog Dexter, the beach).
- Ehrhart's theorem, with a live 3D permutahedron (drawn with Three.js): stretch it with a slider and watch the grid points inside follow the polynomial $16t^3 + 15t^2 + 6t + 1$; tap each coefficient to see what it measures (volume, half the surface area, the constant 1, reciprocity). Corners are labeled, edges are colored by which swap they make, and Carson's research example, the stack-sorting simplex of $2341$ with polynomial $(t+1)^3$, can be tapped to see it alone.
- Gödel's completeness and incompleteness, with the independence of the continuum hypothesis (Gödel and Cohen).
- The Banach–Tarski paradox as a 55-second silent animation made with Manim, opening with the chocolate-bar illusion, in a night and a day version, with captions timed to each step; it plays only while on screen.
- `media/` (videos), `design/manim/` (the animation's source), `design/mockups/about-*.html` (the About mockups), web-sized photo and a still of the 3D shape for visitors without JavaScript.

### Changed
- `PRODUCT.md`: Carson's new bio wording, research, interests and the name "stack-sorting simplex"; the math explanations avoid "I/me/my" (except his research sentence).
- `DESIGN.md`: About's live pieces, as decided over several mockup rounds.
- `CLAUDE.md`: Claude may use Three.js and Manim wherever it judges them tasteful.
- Video files are now color-labeled, so the animation's background closely matches the page (fine-tuned further in 0.8.0).

## [0.6.0] - 2026-10-22

Stage 3 begins: the hero, the first section of the redesigned site, is built. The rest of the page shows clearly marked placeholders until each section is built.

### Added
- The new hero: "Carson Mitchell" set large, a one-sentence introduction, a **Get In Touch** button and a link to the GRE textbook PDF.
- The hero centerpiece: spinning circles (a Fourier series) draw the initials C and M, then the equations behind them appear. A slider sets how many circles spin (from 1 to 100 each way), with a live line showing how closely they match the real letters. Built to match the approved mockup.
- A sliding day/night switch with a sun and a moon. Switching spreads the new colors out in a circle from the switch.
- New top menu: About · Tutoring · Projects.
- Works for everyone: phones get a bigger slider handle and the drawing waits until it's on screen; visitors who turn on "reduce motion" see the finished drawing and a gentle fade instead of movement; screen readers hear plain descriptions; without JavaScript the letters still show.

### Changed
- The GRE textbook is now the first item in Projects instead of a section of its own (`DESIGN.md`, `WORKFLOW.md`).
- After a design review (Impeccable) and a motion review (Emil Kowalski's standards): the page no longer jumps when the equations appear, the slider track is easier to see, the equations stay visible while you move the slider, links are easier to tap, the drawing runs smoothly on phones, and fades use a crisper curve.

### Removed
- The original template page ("Your Name" and its sample sections).

## [0.5.0] - 2026-10-22

Stage 1: real content gathered. Before this release the plan had only placeholders for Carson's bio, links, tutoring details and photo; now the real ones are recorded and ready for Stage 3 to build with. Also: the approved hero animation saved as a reference page, and booking and contact-form choices. No visible change to the live site yet.

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

[Unreleased]: https://github.com/carsonmit/carsonmit.github.io/compare/v0.8.0...HEAD
[0.8.0]: https://github.com/carsonmit/carsonmit.github.io/compare/v0.7.0...v0.8.0
[0.7.0]: https://github.com/carsonmit/carsonmit.github.io/compare/v0.6.0...v0.7.0
[0.6.0]: https://github.com/carsonmit/carsonmit.github.io/compare/v0.5.0...v0.6.0
[0.5.0]: https://github.com/carsonmit/carsonmit.github.io/compare/v0.4.0...v0.5.0
[0.4.0]: https://github.com/carsonmit/carsonmit.github.io/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/carsonmit/carsonmit.github.io/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/carsonmit/carsonmit.github.io/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/carsonmit/carsonmit.github.io/releases/tag/v0.1.0
