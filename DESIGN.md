---
name: Carson Mitchell
description: Personal site of a math tutor; a calm, scholarly voice in a modern, interactive frame.
---

<!-- SEED: established with the user before implementation; re-run /impeccable document once there's code to capture the actual tokens and components. -->

# Design System: Carson Mitchell

## Overview

A scholar with modern tools. A classic serif voice sits in a dark, quiet, precise frame (the "quiet instrument" direction dealt by design-taste-frontend): one narrow column, generous space, and small live math demonstrations instead of decoration. The site has two modes, night (dark) and day (light). They should feel like the same person in a dark outfit and a light outfit, never like two brands.

The page should feel alive and responsive, but with one focal point at a time. The hero's interactive centerpiece is spinning circles that draw Carson's initials (see Interactive Pieces), and a few sections each carry one small live piece of their own. There is never more than one per screen, plus small responsive touches everywhere (Emil's skills lead motion and interaction feel). Background texture never competes with the live piece on screen.

## Colors

One accent, used for both buttons and links. No second accent.

| Role | Night (default) | Day |
|---|---|---|
| Background | Charcoal blue `#151a21` | Cream `#F3EBDD` |
| Accent | Lilac `#C9ACDE` | Plum `#6C4487` |
| Headline ink | `#F2EFE8` | `#1f1a14` |
| Muted text | `#A19E96` | `#5c5348` |
| Card surface | `#1d232c` | `#EADFCC` |

Ink, muted, and card values came from the mockups and are provisional.

Contrast (WCAG): lilac on charcoal is 8.7:1; plum on cream is 6.3:1. Both pass AA for small text.

### Named Rules

- **Same hue, day and night.** Plum is lilac in daylight: both sit at hue 275–276°. Any future accent change must keep the day and night shades on the same hue.
- **Soft, not loud.** The owner consistently chose softer, lighter accents (rose, periwinkle, lilac) over saturated ones (raspberry, cobalt, electric blue). Keep the accent calm.
- **No green.** No green backgrounds or accents (lime, forest, and teal-leaning greens were rejected).
- **Contrast between ground and accent.** Avoid accents that blend into the background's family; same-family pairings (pink on plum, blue on ink) were rejected for reading as "one entire feel".

## Typography

Three faces, by the owner's deliberate choice (design-taste-frontend's rule is two at most; the owner saw both versions and preferred sans buttons):

| Role | Face | Settings |
|---|---|---|
| Headlines | DM Serif Display | 400 (its only weight) |
| Body text, including links inside sentences | Newsreader | 18.5px; weight 420 and line height 1.45 in both modes; italic for math variables in plain text |
| Buttons, top menu, small labels and captions | IBM Plex Sans | 500 for buttons, 400 for labels; about 13.5–14.5px |
| Math | KaTeX (LaTeX rendered in the browser) | Inherits the text color |

### Why
- **Serif body, never sans.** The owner wants a book feel over a tech feel, which matches the LaTeX textbook. Newsreader was chosen over IBM Plex Serif because it contrasts more with the headline; Plex Serif read like a smaller copy of it.
- **18.5px, not 16px.** Newsreader has short, narrow lowercase letters, so it looks small at the usual size. The owner matched it by eye to IBM Plex Serif at 16px and landed on 18.5–19px.
- **Slightly heavy, the same in both modes.** Light text on a dark background looks thinner than it is, so the weight is 420 instead of 400. It must not differ between modes: in a variable font, heavier letters are also wider, so a per-mode weight made lines rewrap when switching modes. Switching modes changes colors only, never layout.
- **One line height.** The owner liked 1.40 by day and 1.45 at night; 1.45 everywhere was chosen because 1.40 is below design-taste-frontend's 1.45–1.6 range for body text and the difference is under 1px per line.
- **Sans only for controls.** IBM Plex Sans is limited to buttons, the menu and small labels so it reads as "the controls", not a third voice. Links inside sentences stay in Newsreader, since a sans word mid-sentence looks like a mistake.

Rejected: Inter Tight, Literata (looks too big), Source Serif 4 (too big, even with letter heights matched), Instrument Sans and Figtree (too techy), any sans body.

### Words
- American English everywhere ("center", "color").
- Math is written in rigorous notation, no multiplication dots unless they really help.
- Buttons use Title Case ("Get In Touch"), by the owner's choice.

## Layout

Quiet-instrument grammar: a single narrow column placed left of center, a large headline, a lot of untouched space. Exact measurements are [to be resolved during implementation].

### Page plan

Person first: the site introduces a person before it offers a service. Each section makes one claim and shows real proof; sections without proof are cut.

| Order | Section | Claim | Proof | Live piece |
|---|---|---|---|---|
| 1 | Hero | This is Carson Mitchell, a math tutor who wrote a free GRE textbook. | Name set large, one plain sentence | Circles drawing his initials |
| 2 | About | Here's who I am. | Photo and bio (see PRODUCT.md, Confirmed Content) | Visual proof or Collatz ("math I find beautiful") |
| 3 | Tutoring | I tutor math, and here's how to start. | Subjects (`content/subjects.md`), levels, online or in person, rates, how to book (see PRODUCT.md); the textbook shows he can explain | The problem that solves itself as you scroll |
| 4 | Projects | I make things for mathematical work, starting with a free GRE textbook. | The GRE textbook first (free 35-page PDF: preview of real pages, download button), then NeuronDiagrams and StarBattleSolver, both live | None for the textbook; a neuron diagram and a Star Battle puzzle, each beside its own project |
| 5 | Contact | Here's how to reach me. | Email, LinkedIn, GitHub (see PRODUCT.md); name returns large | None |

- Top menu: About · Tutoring · Projects, so each audience can jump to its part.
- The GRE textbook is the first project in Projects, not a section of its own (owner's choice, 2026-10-22). It stays easy to find through the hero's text link and its place at the top of Projects.
- Hero: one main button, **Get In Touch** (goes to Contact; broad on purpose, for now), plus a quiet text link to the GRE textbook. The textbook is not the main button, by the owner's choice.
- Cut, for lack of real proof: testimonials, "students helped" numbers, FAQ. Any can return once real material exists. Prices were cut at first but return now that the owner supplied real rates.
- Considered and not chosen: leading with tutoring, or with the textbook (the strongest proof).

## Interactive Pieces

Each live piece is a self-contained module that plugs into a slot on the page, so any piece can be moved, swapped, or rotated (a different one per visit) later by changing one line. Every piece needs a phone version that works with a thumb, a plain no-script fallback, and must never block reading. One live piece per screen; the quiet dots switch off around it.

**Approved reference code lives in `design/mockups/`.** A piece with a file there must be built to match that file exactly (copy its drawing logic, timing, colors, math, and wording rather than rewriting them); the text below is the summary. Pieces without a file are first-round sketches still to be refined with the owner before building.

- **Hero centerpiece: circles that write his name.** Reference: `design/mockups/hero-fourier.html` (approved). A Fourier series: spinning circles stacked end to end draw the initials C and M. **One closed curve** $f$ writes both letters. It traces the C, lifts the pen (the pen dot goes hollow), travels to the M, writes it, and travels back. One sum and one set of circles draw both letters. The circles draw the true partial sum $z(t) = \sum_{n=-N}^{N} c_n e^{int}$, with coefficients from the discrete Fourier transform of 720 evenly spaced points on $f$.
  - On load it draws once with $N = 30$ (60 circles, about 5 s, one full period). It never loops. The true letters sit faintly underneath the whole time, so you can compare.
  - Then the circles fade and two KaTeX equations appear, centered: the sum (large, showing the live value of $N$) and, smaller and muted, $c_n = \frac{1}{2\pi}\int_0^{2\pi} f(t)\, e^{-int}\, dt$. Caption (Newsreader italic): "One curve $f$ writes both letters, lifting the pen in between. Each $c_n$ is $f$ unwound $n$ times and averaged, and each term is a circle of radius $\lvert c_n\rvert$."
  - A slider labeled $N$ (1–100) redraws once with the new value. Under it, a live readout explains why the slider matters: "60 circles · they miss the true letters by X% of their height, on average. More circles, sharper corners." X is the measured mean distance between the drawing and the true letters, divided by the letter height.
  - Built-site changes from the mockup, approved by the owner (2026-10-22): the drawing starts once the figure is fully on screen; the circles' fade-out and the equations' fade-in keep 0.6 s but use Emil's strong ease-out curve `cubic-bezier(0.23, 1, 0.32, 1)` instead of `ease`; the equations stay visible during slider redraws; the slider label reads "$N$ = 30 circles each way", with a filled track.
  - Goal: impressive for younger students. They watch the error shrink as circles are added. Keep the math brief, rigorous and beautifully typeset. The slider track must be clearly visible in both modes.
- **About: visual proof** that $1 + 3 + \dots + (2n-1) = n^2$ (L-shaped layers, slider for $n$), and/or **Collatz**: type a number, watch it fall to 1.
- **Tutoring: a problem that solves itself** as you scroll, one step at a time, with each step's reason ("subtract 7 from both sides").
- **Projects: a neuron diagram** (tap neurons to fire, linking to the NeuronDiagrams editor) and **a Star Battle puzzle** (linking to StarBattleSolver).
- Rejected: a curve you shape, the name drawn by plain equations, a mini GRE question ("not my main niche").
- Wished for later: Three.js and Manim (see CLAUDE.md).

## Elevation & Depth

Flat. Depth comes from color fields and space, not shadows or glows.

## Shapes

Pill-shaped primary buttons (fully rounded). Softly rounded cards. Final radii are [to be resolved during implementation].

## Do's and Don'ts

- Do keep one interactive focal point per screen.
- Do use quiet dots as the background texture: invisible until the cursor comes near, then they glow faintly in the accent. Never use a line grid.
- Do let the light/dark switch transition smoothly; it is a signature moment.
- Don't use code-style notation in the UI (e.g. `[gre_book]`); plain words only.
- Don't use amber, persimmon, coral, ivory, lime, electric blue, or cobalt as the accent (all were explored and rejected).
- Don't invent testimonials, rates, or credentials (see PRODUCT.md).
