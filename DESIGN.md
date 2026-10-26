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
- Title Case for every title: headings, page titles, menu items, door titles and buttons ("Get In Touch", "About Me", "Ehrhart's Theorem"), by the owner's choice. Short words (a, an, the, and, of, in, on, to) stay lowercase unless they come first or after a colon.

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
| 5 | Contact | Here's how to reach me. | Email, LinkedIn, GitHub (see PRODUCT.md), the Formspree form, the two booking cards; no photo, and no large name at the end (owner, 2026-10-25: "awkward") | A directed graph under the opening sentence: five curved arrows (Message, Email, LinkedIn, GitHub, Book) from "you" to "CM"; the paths draw in once, and pointing at a matching link lights its path and runs a dot toward CM (owner chose this, 2026-10-25; mockup `design/mockups/contact-moment.html`) |

- **Separate pages** (owner, 2026-10-24), so no audience scrolls past another's content: home (`index.html`: the hero, then a short "door" to each page; each door row carries one real detail from its page, centered in its column on every screen size (owner, 2026-10-26): the 3D shape's still picture, the rates, the Projects page's preemption neuron diagram (replaced a textbook page, owner 2026-10-26), and a tiny directed "you → CM" graph with arrowheads; owner chose option A of `design/mockups/home-doors.html`, 2026-10-25. Door texts (owner, 2026-10-26): Projects "Personal writings, tools, widgets, and more.", Contact "Email, social media, message form, and booking links."), `about.html`, `tutoring.html`, `projects.html`, `contact.html`. Shared styles in `styles.css`, the shared day/night switch in `site.js`; no build step. Page changes crossfade (cross-document view transitions), none for reduced motion.
- Home page (owner, 2026-10-24): a small round portrait of Carson sits above his name in the hero (`images/carson-thumb.jpg`, a face crop that keeps his chin); a short italic note closes the page: "This website is a proud product of extensive vibe-coding with the help of Claude Code."
- Page changes (owner, 2026-10-24): the menu bar stays still while the old page fades out with a 6px lift (0.16 s) and the new one rises 10px into place (0.26 s), both on the strong ease-out; instant for reduced motion.
- Top menu: Home · About Me · Tutoring · Projects · Contact (owner: an explicit Home link, not just the name; "About Me" rather than "About"); the current page is underlined in the accent.
- Favicon (owner, 2026-10-25, option C of `design/mockups/favicon.html`): the hero's strokes as one mark, the M inside the open C; lilac on charcoal in a dark browser, plum on cream in a light one (`favicon.svg` follows the browser's theme, not the site switch).
- About Me (owner, 2026-10-25/26): the bio sits centered beside the photo (top-aligned and larger-text versions were tried and rejected); on phones the 3D shape follows the first two Ehrhart paragraphs; the page ends with one line pointing to Tutoring and Contact. Contact: the "Send a Message" heading column stays beside the form while scrolling (desktop), with a line linking to the intro call. Every page title is the same size and height.
- The GRE textbook is the first project in Projects, not a section of its own (owner's choice, 2026-10-22). It stays easy to find through the hero's text link and its place at the top of Projects.
- Hero: one main button, **Get In Touch** (goes to the Contact page; broad on purpose, for now), plus a quiet text link to the GRE textbook. The textbook is not the main button, by the owner's choice.
- Cut, for lack of real proof: testimonials, "students helped" numbers, FAQ. Any can return once real material exists. Prices were cut at first but return now that the owner supplied real rates.
- Considered and not chosen: leading with tutoring, or with the textbook (the strongest proof).

## Interactive Pieces

Each live piece is a self-contained module that plugs into a slot on the page, so any piece can be moved, swapped, or rotated (a different one per visit) later by changing one line. Every piece needs a phone version that works with a thumb, a plain no-script fallback, and must never block reading. One live piece per screen; the quiet dots switch off around it.

**Approved reference code lives in `design/mockups/`.** A piece with a file there must be built to match that file exactly (copy its drawing logic, timing, colors, math, and wording rather than rewriting them); the text below is the summary. Pieces without a file are first-round sketches still to be refined with the owner before building.

- **Hero centerpiece: circles that write his name.** Reference: `design/mockups/hero-fourier.html` (approved). A Fourier series: spinning circles stacked end to end draw the initials C and M. **One closed curve** $f$ writes both letters. It traces the C, lifts the pen (the pen dot goes hollow), travels to the M, writes it, and travels back. One sum and one set of circles draw both letters. The circles draw the true partial sum $z(t) = \sum_{n=-N}^{N} c_n e^{int}$, with coefficients from the discrete Fourier transform of 720 evenly spaced points on $f$.
  - On load it draws once with $N = 30$ (60 circles, about 5 s, one full period). It never loops. The true letters sit faintly underneath the whole time, so you can compare.
  - Then the circles fade and two KaTeX equations appear, centered: the sum (large, showing the live value of $N$) and, smaller and muted, $c_n = \frac{1}{2\pi}\int_0^{2\pi} f(t)\, e^{-int}\, dt$. Caption (Newsreader italic): "One curve $f$ writes both letters, lifting the pen in between. Each $c_n$ is $f$ unwound $n$ times and averaged, and each term is a circle of radius $\lvert c_n\rvert$."
  - A slider labeled $N$ (1–100) redraws once with the new value. Under it, a live readout explains why the slider matters: "60 circles · they miss the true letters by X% of their height, on average. More circles, sharper corners." X is the measured mean distance between the drawing and the true letters, divided by the letter height.
  - Built-site changes from the mockup, approved by the owner (2026-10-22): the drawing starts once the figure is fully on screen; the circles' fade-out and the equations' fade-in keep 0.6 s but use Emil's strong ease-out curve `cubic-bezier(0.23, 1, 0.32, 1)` instead of `ease`; the equations are visible the whole time, from the first moment (owner, 2026-10-24: waiting for them left an awkward gap); the slider label reads "$N$ = 30 circles each way", with a filled track.
  - Goal: impressive for younger students. They watch the error shrink as circles are added. Keep the math brief, rigorous and beautifully typeset. The slider track must be clearly visible in both modes.
- **About: Ehrhart polynomial of the 3D permutahedron** (owner's choice, 2026-10-24, replacing the odd-sum proof and Collatz). Built in Three.js. The permutahedron $\Pi_4$ (convex hull of the permutations of $(1,2,3,4)$, a truncated octahedron) is dilated by $t$, and its lattice points are shown and counted live, matching $L(t) = 16t^3 + 15t^2 + 6t + 1$ (verified by brute force for $t = 0, \dots, 4$: 1, 38, 201, 586, 1289). Coefficient of $t^k$ = number of forests with $k$ edges on 4 labeled vertices (Stanley). Owner's choices (2026-10-24, round 2): the focus is **Ehrhart's theorem in general** (lattice points of a stretched integral polytope follow a polynomial whose degree is the dimension); the permutahedron is the worked example, not the showcase. Explain its tie to the symmetric group $S_4$ (corners are permutations, edges are swaps of neighboring values, so walking edges is sorting). Stand it upright with $1234$ on top and $4321$ at the bottom; label those and the highlighted subpolytope's corners; tap any corner to see its permutation; color edges by which swap they make. Highlight Carson's research example, the **stack-sorting simplex** (owner's name for it), the tetrahedron $2341, 2314, 2134, 1234$, with its own polynomial $(t+1)^3$. Tapping a coefficient explains what it means for every lattice polytope (volume, half the surface area, the constant 1, and reciprocity $L(-t)$ counting interior points). The forests panel (round 1) was dropped.
- **Banach–Tarski animation** (owner's idea, 2026-10-24): a pre-rendered Manim video in the spirit of the Vsauce explanation (our own animation, nothing copied). Round 3 (2026-10-24, on the site; source `design/manim/banach_tarski.py`, files in `media/`): opens with an honest chocolate-bar dissection illusion (the rebuilt bar is a sliver shorter); the direction-colored tree grows inside the ball; the ending shows the ball itself splitting into two solid balls (no tree stretching); 38 s, captions synced to 9 beats. The owner may refine it later. Round 2 (2026-10-24): Vsauce-style direction colors: the rotations are up, down, left, right; while the tree grows every step is colored by its direction; then the tree splits into four pieces by first move, keeping those colors. Owner's choices (2026-10-24): a short silent loop of about 30 s with a play/pause button, in a "Math I love" block in About, below the bio and the permutahedron. That block also has a few plain sentences, in Carson's voice, on Gödel's completeness and incompleteness theorems and Cohen's independence proofs (Claude drafts, Carson edits; no extra animation).
- **Tutoring: a problem that solves itself** as you scroll. Reference: `design/mockups/tutoring-solve.html` (approved layout: Written Out). Built-site decisions (owner, 2026-10-25): three problems as tabs: logarithms ($\log_2 x + \log_2(x-2) = 3$, with the extraneous root), a hard integral (Putnam 2005 A5, $\int_0^1 \frac{\ln(1+x)}{1+x^2}\,dx = \frac{\pi}{8}\ln 2$), and a tricky probability question (roll until a six, given all rolls even: expected rolls $\tfrac32$). Lines appear one at a time; the current line's changed part is in the accent; earlier lines dim. The reason for the current line sits in one tinted box (`--card`) just under the newest line and glides down as lines are added; the board itself is the page color. Back / Next buttons travel with the reason box, just under the newest line. Nothing is pinned. Every problem starts at step 1; scrolling moves it about one step per 115px (the whole problem over 0.9 screens, finishing as the board reaches the top), catching up one step at a time only while scrolling is still happening (a flick moves one step; steady scrolling reaches the end; it stops when you stop), never by where the page happens to be; on phones and tablets it counts from the lines, not the board's intro (owner, 2026-10-25). Unselected tabs are transparent with muted text, quieter than the Back/Next buttons; and each new step is preceded by "What would you do next?" for 0.8 s in the box (owner's choice after the critique, 2026-10-25). Next shows that prompt, then the step (a second press reveals it at once); once Back/Next are used, scrolling leaves that problem alone until another tab is picked. Tabs: "Logarithms", "Putnam Integral", "Dice", on one line, arrow keys move between them. Reduced motion: no pause, no glide. A quiet closing line at the end of the page points back to the booking cards (not a second booking section).
- **Tutoring page layout** (owner, 2026-10-25): first screen = "Math Tutoring", the rates with the payment and other-length notes under them, and two large booking cards (lesson in the accent, intro call in `--card2`) as the focal point; no photo of Carson on this page; then Subjects (grouped by level, owner 2026-10-26: High School, College, Advanced College, one column per level, each with a small accent heading; reading-size items), How I Teach (a letter in Carson's words; the section stays `hidden` until he writes it, owner 2026-10-25), the problem, and four real textbook pages (one lifted). Gaps between blocks at most 120px. Rejected: a single column of headings and text ("drab"), a separate Rates section, a second booking section at the bottom, a pinned scroll track.
- **Projects: a neuron diagram.** Reference: `design/mockups/projects-neuron.html` (approved, owner 2026-10-25: option B, three classic cases as tabs, Preemption (the editor's own example diagram), Overdetermination, Double Prevention; firing neurons in the lilac/plum accent, not gray). Tap a neuron to fire it; the run replays in 0.46 s ticks with a small accent dot traveling each line; a line ending in a dot stops the neuron it reaches (the stopped neuron gets a dashed outline). Above the diagram, each case has a short explanation with one running example, Suzy and Billy throwing rocks at a bottle (the standard example in the causation literature), mapped onto its neurons: preemption (Billy holds back when he sees Suzy throw), overdetermination (both throw at once), double prevention (Pat calls out, so Billy doesn't catch Suzy's rock) (owner, 2026-10-25: replaced first-draft assassin examples). The caption below the diagram tells the same story for whatever the visitor taps, never generic "c fires" wording. Links to the editor.
- **Projects: a Star Battle puzzle.** Reference: `design/mockups/projects-starbattle.html` (approved, owner 2026-10-25: options A and C together). The real 10×10 example from StarBattleSolver (once its easy example; the solver's 2026-10-26 grading calls it medium): tap a cell once to cross it out, twice for a star, three times to clear it (owner, 2026-10-25); a new star crosses out its open neighbors automatically, and removing it clears those automatic crosses unless another star still touches them; "Show Me a Step" gives the solver's next step and its reason; "Solve" keeps stepping from wherever the visitor is (0.42 s per step). A wrong mark is explained with the solver's own logic (owner, 2026-10-25: not just "can't be part of the answer"): a wrong star that touches a correct star says so; otherwise the page quotes the solver step that rules the cell out (or proves the star it touches); a wrong cross quotes the step that proves the star. Cells stay square whatever they hold. Layout (owner, 2026-10-25, after the final critique): the rules, then the board with row numbers down the left and column numbers along the top, then the reason and the buttons, stacked at every width (board up to 500px); night-mode region tones spread in lightness so regions read apart. The neuron card adds one line: "As in the papers, c is always the cause in question and e the effect." On phones the three case tabs stay on one line and scroll sideways. Every step and reason is the solver's own output, exported to `data/star-battle-easy.json`; only the wording is tidied ("1 star(s)" → "1 star", American spelling). The solver is a web app (owner, 2026-10-26), so the button is "Open the Solver"; the steps use the rule names from Carson's BmMT 2022 Puzzle Round conventions (Completed Sections, No More Space, Too Much Space, Rude Roommates, Nosy Neighbors, Chunking), one step per reason. Both app screenshots have Night and Day versions (`images/projects/*-day.jpg`), swapped with the site's mode.
- **Projects page layout** (2026-10-25): first screen = "Projects", one line, then the textbook: "A Free GRE Textbook", the full title, "Free, and still growing" (owner's choice: the book is partly written; logic, set theory and arithmetic so far), a Download the PDF button, the chapters written so far as a quiet ledger, and a large real page with five sample pages beside it (pages 10, 14, 18, 20, 22; never the title page, and not the four shown on Tutoring). Then one row per project, alternating sides, each with its live piece and a real screenshot of the program. On narrow screens the live piece comes before the screenshot.
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
