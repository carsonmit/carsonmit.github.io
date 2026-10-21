# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Several audiences, none ranked above the others (confirmed by the owner):
- Prospective tutoring clients: students or parents deciding whether to hire a private math tutor.
- Students who want the free GRE mathematics textbook PDF.
- Professional contacts: employers, collaborators, or programs checking who the owner is.
- General personal-site visitors: friends and curious people.

## Product Purpose

A personal website for Carson, a math graduate and private tutor. It serves all of the audiences above at once: introduce Carson, make tutoring easy to inquire about, and make the GRE textbook easy to find and download. The owner said the purpose is "all of the above and more", so no single conversion goal is set.

## Positioning

Undecided. Not yet discussed with the owner.

## Operating Context

- Hosted on GitHub Pages as a single static `index.html` (plain HTML/CSS/JS, no framework or build step unless the owner asks).
- The GRE textbook is written in LaTeX on Overleaf; a GitHub Actions workflow in `carsonmit/Mathematics-for-the-GRE` copies the PDF into this repo at `pdf/GRE-Textbook.pdf`, which the site links to. Do not edit that PDF by hand.
- GitHub Pages deploys can lag and cache.

## Capabilities and Constraints

- Current sections: hero, about, connect/social, footer, with animation effects.
- Name, bio, and social links are still template placeholders ("Your Name", `yourhandle`); the real values are coming from the owner.
- Tutoring details (subjects, availability, how to inquire) exist but have not been supplied yet.
- Math notation is written in LaTeX.

## Brand Commitments

Visual identity chosen with the owner is recorded in `DESIGN.md`. Animation decisions follow the `emil-design-eng` skill. No logo or other brand assets are on record.

## Evidence on Hand

- The GRE mathematics textbook PDF (`pdf/GRE-Textbook.pdf`, 35 pages).
- NeuronDiagrams (confirmed by the owner as real work): a point-and-click editor for the neuron diagrams used in papers on causation. It exports TikZ/LaTeX code or images and runs in any browser and on iPad. Lives in the separate repo `carsonmit/Widgets-and-Miscellaneous`, served at https://carsonmit.github.io/Widgets-and-Miscellaneous/NeuronDiagrams/ (installable web app).
- StarBattleSolver (confirmed by the owner as real work): a Star Battle puzzle solver with a visual, step-by-step solving window. Same repo, at `StarBattleSolver/`.
- There are NO testimonials, rates, or reviews. Future work must not invent any; leave them absent until the owner provides real ones.
- Confirmed name: Carson Mitchell. Bio and social links are still pending from the owner (placeholders for now); do not fabricate them.

## Product Principles

- One site, several audiences: no visitor type should have to dig past another's content.
- Person first: the site introduces Carson as a person before it offers a service. When two options are close, the warmer, more personal one wins.
- Never fabricate proof: no invented testimonials, rates, credentials, or download counts.
- The GRE textbook is the strongest real asset, so it stays easy to find.
- Stay simple: plain static HTML/CSS/JS that the owner can read and learn from.

## Accessibility & Inclusion

No product-specific requirement established. The owner is a beginner-to-intermediate coder who wants plain-language explanations of changes.
