# carsonmit.github.io

Personal website of **Carson Mitchell**, math graduate and private math tutor. The site introduces Carson, explains his tutoring, and hosts his free GRE mathematics textbook.

**Live site:** https://carsonmit.github.io

> Status: a redesign is in progress (see [Roadmap](#roadmap)). The live site still shows the original template.

## Contents

- [How it works](#how-it-works)
- [Project structure](#project-structure)
- [Preview locally](#preview-locally)
- [Making changes](#making-changes)
- [GRE textbook pipeline](#gre-textbook-pipeline)
- [Design system](#design-system)
- [Version history](#version-history)
- [Roadmap](#roadmap)

## How it works

- **Plain HTML, CSS, and JavaScript** in a single file, `index.html`. No framework and no build step: what's in the file is what visitors get.
- **Hosting:** [GitHub Pages](https://pages.github.com/) serves the `main` branch automatically. Every push to `main` redeploys the site, usually within a few minutes. Pages caches aggressively, so hard-refresh (Cmd+Shift+R) before deciding a change didn't work.
- **The GRE textbook PDF** is written elsewhere and copied in automatically (see [below](#gre-textbook-pipeline)).

## Project structure

| Path | What it is |
|---|---|
| `index.html` | The whole website: content, styles, and scripts |
| `pdf/GRE-Textbook.pdf` | The GRE textbook. **Managed by the pipeline; don't edit by hand.** |
| `PRODUCT.md` | Who the site is for and what's true about it (no invented claims) |
| `DESIGN.md` | The design system: colors, fonts, and design rules |
| `design/mockups/` | Approved interactive pieces as standalone pages (open in a browser). The site must match them. |
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

Then open http://localhost:8000. Stop it with Ctrl+C. (Opening `index.html` directly also works, but a server behaves more like the real site.)

## Making changes

1. Edit `index.html` (or ask Claude Code, following [WORKFLOW.md](WORKFLOW.md)).
2. Preview locally.
3. Commit with a clear message, e.g. `Add tutoring section`.
4. Add a line to [CHANGELOG.md](CHANGELOG.md) under **Unreleased**.
5. Push to `main`. The live site updates in a few minutes.

To change a design decision (a color or a font), update `DESIGN.md` first, then the site.

### Restoring the AI design tools on a new computer

The compiled Impeccable engine isn't stored in git (it's large). After cloning, run:

```bash
npx impeccable install
```

It requires Node.js 22 or newer.

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
- [ ] Stage 1: real bio, links, tutoring details, photo
- [x] Stage 2: body font, page plan, interactive centerpiece (v0.4.0)
- [ ] Stage 3: build section by section
- [ ] Stage 4: polish (accessibility, mobile, motion)
- [ ] Stage 5: launch v1.0.0
