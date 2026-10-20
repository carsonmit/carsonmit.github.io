# CLAUDE.md — Carson's personal website

## Project
- Personal website for Carson (math graduate, private tutor), hosted on GitHub Pages.
- Repo: `carsonmit/carsonmit.github.io`
- Stack: plain HTML/CSS/JS, single-file site. No frameworks or build step unless I ask.
- Aesthetic: a scholarly serif voice in a dark, quiet, interactive frame, with light and dark modes. Palette and fonts are in `DESIGN.md`.
- Current sections: hero, about, connect/social, footer, with animation effects.

## PDF pipeline
- A LaTeX project (`main.tex`) on Overleaf syncs to a separate GitHub repo.
- A GitHub Actions workflow in that repo (`.github/workflows/deploy.yml`) compiles it with `xu-cheng/latex-action@v3` and pushes the PDF to this repo at `files/grebook.pdf`.
- The push uses a fine-grained token stored as the secret `PAGES_DEPLOY_TOKEN`.
- Do not touch `files/` by hand; the pipeline overwrites it.

## Rules
- Never commit secrets, API keys, or tokens (the repo is public).
- Prefer low-friction setups with few manual steps.
- Design/animation decisions: follow the `emil-design-eng` skill (Emil Kowalski) when installed.
- GitHub Pages deploys can lag and cache; account for that before assuming a change failed.

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
