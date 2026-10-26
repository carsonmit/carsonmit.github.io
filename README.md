# carsonmit.github.io

Personal website of **Carson Mitchell**, math graduate and private math tutor. The site introduces Carson, explains his tutoring, and hosts his free GRE mathematics textbook.

**Live site:** https://carsonmit.github.io

> Status: a redesign is in progress (see [Roadmap](#roadmap)). The home page with the hero (v0.6.0), About Me (v0.7.0), the split into separate pages (v0.8.0) Tutoring (v0.9.0), Projects (v0.10.0) and Contact are built; Stage 4 (polish) is next.

## Contents

- [How it works](#how-it-works)
- [Project structure](#project-structure)
- [Preview locally](#preview-locally)
- [Making changes](#making-changes)
- [Tools](#tools)
- [GRE textbook pipeline](#gre-textbook-pipeline)
- [Design system](#design-system)
- [Version history](#version-history)
- [Roadmap](#roadmap)

## How it works

- **Plain HTML, CSS, and JavaScript**: one HTML file per page, plus one shared stylesheet (`styles.css`) and one shared script (`site.js`). No framework and no build step: what's in the files is what visitors get.
- **Libraries loaded from the web (CDNs):** KaTeX typesets the math; Three.js draws the 3D permutahedron in About, and only loads when you scroll near it.
- **Hosting:** [GitHub Pages](https://pages.github.com/) serves the `main` branch automatically. Every push to `main` redeploys the site, usually within a few minutes. Pages caches aggressively, so hard-refresh (Cmd+Shift+R) before deciding a change didn't work.
- **The GRE textbook PDF** is written elsewhere and copied in automatically (see [below](#gre-textbook-pipeline)).

## Project structure

| Path | What it is |
|---|---|
| `index.html` | Home page: the hero (name, photo, the spinning circles) and a "door" to each page |
| `about.html` | About Me: bio, Ehrhart's theorem (3D permutahedron), Gödel, Banach–Tarski |
| `tutoring.html` | Tutoring: rates, booking (Cal.com), subjects, how I teach (placeholder), a problem that solves itself as you scroll, textbook sample |
| `projects.html` | Projects: the free GRE textbook (download and page preview), the Neuron Diagram Maker with a live diagram, and the Star Battle Solver with a playable puzzle |
| `contact.html` | Contact: where to find me (email, LinkedIn, GitHub), a graph of the ways to reach me, a message form (Formspree), and the booking cards |
| `data/star-battle-easy.json` | The Star Battle Solver's real steps for the puzzle on Projects, exported from its `solver.py` (in `carsonmit/Widgets-and-Miscellaneous`) |
| `styles.css` | Shared look for every page: colors, fonts, layout, motion |
| `site.js` | Shared script for every page: the day/night switch and the bot-proof email link |
| `favicon.svg`, `favicon.ico`, `apple-touch-icon.png` | The browser-tab icon: the M inside the open C. The SVG uses night colors in a dark browser and day colors in a light one; the `.ico` is for older browsers; the PNG is the iPhone home-screen icon |
| `pdf/GRE-Textbook.pdf` | The GRE textbook. **Managed by the pipeline; don't edit by hand.** |
| `PRODUCT.md` | Who the site is for and what's true about it (no invented claims) |
| `DESIGN.md` | The design system: colors, fonts, and design rules |
| `content/subjects.md` | The tutoring subjects list. Edit it to add or remove a subject. |
| `images/` | Pictures used on the site: `carson.jpg` (original photo), `carson-1000.webp` and `carson-1000.jpg` (the web-sized copy About Me shows: WebP, a smaller modern format, with the JPEG for older browsers), `permutahedron-still.jpg` and `permutahedron-still-day.jpg` (night and day pictures of the 3D shape, shown until it loads and on the Home door), `gre/` (pages of the GRE textbook shown on Tutoring) |
| `media/` | Videos on the site: the Banach–Tarski animation in a night and a day version, with a still "poster" image for each |
| `design/manim/` | Source of the Banach–Tarski animation (`banach_tarski.py`) and `encode.py`, which shrinks a render into the web videos in `media/` |
| `design/mockups/` | Interactive pieces as standalone pages (open in a browser): the hero circles, the About pieces, the Tutoring problem, the two Projects pieces, the Contact graph, the favicon options and the Home doors. The site must match the approved ones. |
| `WORKFLOW.md` | The step-by-step process for building and changing the site |
| `CHANGELOG.md` | Version history in plain language |
| `CLAUDE.md` | Instructions for Claude Code, the AI assistant used to build the site |
| `.claude/`, `.agents/` | AI design skills (Emil Kowalski, Impeccable, design-taste-frontend, Playwright) |
| `skills-lock.json` | Which skill versions are installed |

## Preview locally

From the repo folder, start a tiny local web server:

```bash
python3 -m http.server 8000
```

Then open http://localhost:8000. Stop it with Ctrl+C. (Opening the HTML files directly mostly works, but a server behaves like the real site; the page-to-page animation needs it.)

## Making changes

1. Edit the page's HTML file, or `styles.css` for the look (or ask Claude Code, following [WORKFLOW.md](WORKFLOW.md)).
2. Preview locally.
3. Commit with a clear message, e.g. `Add tutoring section`.
4. Add a line to [CHANGELOG.md](CHANGELOG.md) under **Unreleased**.
5. Push to `main`. The live site updates in a few minutes.

To change a design decision (a color or a font), update `DESIGN.md` first, then the site.

**After editing `styles.css` or `site.js`,** change the version tag where every page links them (`styles.css?v=2026-10-26-1`, `site.js?v=…`) to something new, for example today's date. Browsers keep old copies of these files; a new tag makes them fetch the new one. Find and replace across the five HTML files does it in one go.

**Tutoring subjects** live in `content/subjects.md`: one per line starting with `- `, below the `## Subjects` line. **Textbook pictures** in `images/gre/` are made from the PDF and don't update when the book changes; ask Claude to re-render them if the pages change. The same goes for `data/star-battle-easy.json` (made by running the solver) and the program screenshots in `images/projects/`.

## Tools

Setup for a new computer (macOS with [Homebrew](https://brew.sh)). Node.js 22 or newer is required.

| Tool | What it's for | Setup |
|---|---|---|
| Impeccable engine | The AI design checker (not stored in git; it's large) | `npx impeccable install` |
| GitHub CLI (`gh`) | Check Pages deploys and the PDF pipeline's runs, make releases | `brew install gh`, then `gh auth login` |
| Manim | Pre-rendered math animation videos for the site | See below |
| Lighthouse | Score speed, accessibility, best practices, SEO | Nothing to install (runs via `npx`) |

**Manim** (3Blue1Brown's Python animation library) lives in its own Python environment, so its packages don't clash with anything else:

```bash
brew install cairo pango pkg-config
python3 -m venv ~/.venvs/manim
~/.venvs/manim/bin/pip install manim
```

Render a scene (`-ql` = quick low-quality preview, `-qh` = final high quality):

```bash
~/.venvs/manim/bin/manim -ql scene.py SceneName
```

Equations need LaTeX installed (e.g. TeX Live or MacTeX).

To remake the Banach–Tarski video after editing `design/manim/banach_tarski.py` (run from `design/manim/`; Manim's working files go to `design/manim/media/` and are not stored in git):

```bash
~/.venvs/manim/bin/manim -qh --fps 30 --media_dir media banach_tarski.py BanachTarskiNight BanachTarskiDay
~/.venvs/manim/bin/python encode.py media/videos/banach_tarski/1080p30/BanachTarskiNight.mp4 ../../media/banach-tarski-night.mp4 out/night-poster.png 30 1200 26 2,2,-1
~/.venvs/manim/bin/python encode.py media/videos/banach_tarski/1080p30/BanachTarskiDay.mp4 ../../media/banach-tarski-day.mp4 out/day-poster.png 30 1200 26
```

The last argument on the night line (`2,2,-1`) nudges the colors so the video's dark background lands exactly on the page's background after compression. The page's captions are timed to the video's steps (the `beats` list in `about.html`), so update those times if the animation's timing changes.

**Lighthouse** on the live site (Chrome must be installed):

```bash
npx lighthouse https://carsonmit.github.io --view
```

Baseline before the redesign (2026-10-22): performance 98, accessibility 100, best practices 96, SEO 90.

## Contact form

The message form on `contact.html` sends to [Formspree](https://formspree.io), a service that emails each message to Carson and keeps a history of them (with spam filtering). The form's address is `https://formspree.io/f/mrppewpn`; the ID is public by design, so it's safe in the code.

- The page's script checks the boxes, then sends the message in the background, so the page never reloads. Without JavaScript the form still works: the browser checks the boxes and Formspree shows its own thank-you page.
- To test changes without emailing Carson, catch the request in the test browser (Playwright's `page.route('**/formspree.io/**', …)`) and answer it yourself.
- To change where messages go, or to see past messages, sign in at formspree.io.

## GRE textbook pipeline

1. The book is written in LaTeX on Overleaf, which syncs to [`carsonmit/Mathematics-for-the-GRE`](https://github.com/carsonmit/Mathematics-for-the-GRE).
2. On every push to that repo's `master` branch, its workflow `.github/workflows/publish-pdf.yml` copies the committed `GRE-Textbook.pdf` here, to `pdf/GRE-Textbook.pdf`.
3. The copy is pushed by `github-actions` using the `WEBSITE_TOKEN` secret. The site links to that path, so the download always serves the latest version.

## Design system

The full spec is in [DESIGN.md](DESIGN.md). In short:

| | Night (default) | Day |
|---|---|---|
| Background | Charcoal blue `#151a21` | Cream `#F3EBDD` |
| Accent | Lilac `#C9ACDE` | Plum `#6C4487` |
| Headlines | DM Serif Display | DM Serif Display |

The direction is a "quiet instrument": a calm, narrow-column page with a few precise, interactive math pieces instead of decoration.

## Version history

Versions follow `MAJOR.MINOR.PATCH`:
- **MAJOR**: a full redesign or relaunch (1.0.0 will be the redesigned site going live)
- **MINOR**: a new section or feature
- **PATCH**: fixes and small content edits

Each release is marked with a git tag (`v0.3.0`, etc.). Details are in [CHANGELOG.md](CHANGELOG.md).

## Roadmap

Tracked in [WORKFLOW.md](WORKFLOW.md):

- [x] Stage 0: setup, design skills, palette, notes
- [x] Stage 1: real bio, links, tutoring details, photo (v0.5.0; a few bio lines, booking link and contact form come later)
- [x] Stage 2: body font, page plan, interactive centerpiece (v0.4.0)
- [ ] Stage 3: build section by section (hero v0.6.0, About Me v0.7.0, separate pages v0.8.0, Tutoring v0.9.0, Projects v0.10.0, Contact)
- [ ] Stage 4: polish (accessibility, mobile, motion)
- [ ] Stage 5: launch v1.0.0
