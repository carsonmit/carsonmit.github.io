# CLAUDE.md — Carson's personal website

## Project
- Personal website for Carson (math graduate, private tutor), hosted on GitHub Pages.
- Repo: `carsonmit/carsonmit.github.io`
- Stack: plain HTML/CSS/JS, single-file site. No frameworks or build step unless I ask.
- Aesthetic: a scholarly serif voice in a dark, quiet, interactive frame, with light and dark modes. Palette and fonts are in `DESIGN.md`.
- Current sections: hero, about, connect/social, footer, with animation effects. The planned redesign (section order, centerpiece) is in `DESIGN.md`.
- I want to use **Three.js** (a JavaScript library for 3D graphics in the browser; loads from a CDN, so no build step) and **Manim** (3Blue1Brown's Python library for math animations; it renders videos offline, so on the site it would appear as pre-rendered video) on the site. Starting now, whenever planning features or animations, suggest where one of them would fit. Each use still needs my OK.

## PDF pipeline
- A LaTeX project on Overleaf syncs to the repo `carsonmit/Mathematics-for-the-GRE`.
- On every push to its `master` branch, the workflow `.github/workflows/publish-pdf.yml` copies the committed `GRE-Textbook.pdf` (it does not compile LaTeX) into this repo at `pdf/GRE-Textbook.pdf` and pushes as `github-actions`.
- The push uses a token stored as the secret `WEBSITE_TOKEN`.
- `index.html` links to `pdf/GRE-Textbook.pdf`. Do not touch `pdf/GRE-Textbook.pdf` by hand; the pipeline overwrites it.

## Rules
- Never commit secrets, API keys, or tokens (the repo is public).
- Prefer low-friction setups with few manual steps.
- Write all site text and docs in American English ("center", "color").
- Design/animation decisions: follow the `emil-design-eng` skill (Emil Kowalski) when installed.
- GitHub Pages deploys can lag and cache; account for that before assuming a change failed.
- Commit messages must be understandable by me (a beginner): a short first line in plain English saying what changed on the site or in the project (e.g. "Add tutoring section with booking button", not "refactor hero styles"), then a few bullet lines saying what changed and why. Avoid jargon; if a technical term is unavoidable, explain it briefly.
- Keep `README.md` and `CHANGELOG.md` current: add every notable change under `## [Unreleased]` in `CHANGELOG.md` in the same commit, and update the README when structure or process changes. When I say a set of changes is a release, move Unreleased to a new version (MAJOR = redesign/relaunch, MINOR = new section/feature, PATCH = fixes) and create a matching `vX.Y.Z` git tag. Ask before pushing tags.

## Design skills (who leads)
- Installed: `emil-design-eng` (+ other Emil skills), `impeccable`, `design-taste-frontend`, `playwright-cli`.
- Order of lead: `design-taste-frontend` leads the overall look (direction, color, type, layout); `emil-design-eng` leads motion/animation and interaction feel; `impeccable` is the referee (its hook checks UI edits automatically; `PRODUCT.md` is the product context). If two disagree, follow this order, and tell me about the conflict.
- Whenever I ask for something, if a feature of these skills would help (e.g. `/impeccable critique`, `polish`, `audit`; Emil's `review-animations` or `improve-animations`; taste's screenshot inspector), suggest it in one line and say why. Don't run it unasked. I'm new to these skills, so name the command and what it does.
- `design-taste-frontend` runs scripts that can download images from the web; ask before running `assets.mjs`.

## How to work with me
- I'm between beginner and intermediate at coding and want to learn. Explain in plain language, define every technical term, and build up step by step.
- Be concise; no filler. Don't skip steps.
- For any new project, include a README (how it works, how to use it, standard sections).
- State uncertainty and confidence instead of guessing.
- Math notation in LaTeX.
