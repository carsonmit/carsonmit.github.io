# Changelog

Notable changes to the site, newest first. Format based on [Keep a Changelog](https://keepachangelog.com/); versions follow `MAJOR.MINOR.PATCH` (see the README).

## [Unreleased]

### Changed
- Every link that leaves the site (booking buttons, both apps, the textbook PDF, LinkedIn, GitHub) now opens in a new
  tab, so the site stays open behind it. The menu, the download button and email links work as before.
- Workflow: Stages 4 and 5 marked done, with a "What's Next" list of the later items.
- README: a new Lighthouse baseline for the redesigned site (the old one was measured on the one-page site), and how to read its run-to-run swings.

## [0.13.0] - 2026-10-26

### Changed
- Home: each door's picture is centered in its column, on phones and computers. The Projects door now shows the
  neuron diagram from the Projects page (instead of a textbook page), and the Contact door's graph has arrows from
  "you" to "CM". New door texts: "Personal writings, tools, widgets, and more." and "Email, social media, message
  form, and booking links."
- Tutoring: the in-person rate is now $90 per hour (also on Home and in the Cal.com Tutoring Session description).
- Tutoring: six more subjects (Algebra I, Algebra II, Geometry, Combinatorics, Abstract Algebra, Real Analysis), and
  the list is grouped by level: High School, College and Advanced College, one column each.
- Projects: the page has its own header ("Some writing, tools, and widgets I've produced for my own work and others to
  use."), with the textbook below it, and the opening and closing lines no longer wrap early on wide screens.
- About Me: the math styles load without holding up the page (the math is further down), so the page appears sooner.

## [0.12.1] - 2026-10-26

### Changed
- Tutoring: the Putnam Integral problem's intro now reads "Evaluate this integral." instead of repeating the integral that sits right below it.
- Projects: the Star Battle Solver is now a web app, so its button is "Open the Solver" (it used to link to the code on
  GitHub), and its text and facts describe the app, its four difficulty levels and the rule conventions from Carson's
  2022 Berkeley mini Math Tournament Puzzle Round.
- Projects: new screenshots of both apps in their new look, with Night and Day versions that follow the site's mode.
- Projects: the Star Battle puzzle uses the updated solver's steps: the rule names Completed Sections, No More Space,
  Too Much Space, Rude Roommates, Nosy Neighbors and Chunking, and one step per reason (48 steps instead of 69).

## [0.12.0] - 2026-10-26

The whole site polished: a browser-tab icon, a technical audit and a full design review of all five pages, with the fixes they found.

### Added
- A "Skip to Content" link on every page: invisible until a keyboard user presses Tab, then it appears at the top so they can jump past the menu.
- About Me: with "reduce motion" turned on, the Banach–Tarski video's nine captions are listed under it, since the video doesn't play by itself for those visitors.
- About Me: a day-colored version of the 3D shape's still picture (shown until the 3D loads, or if it can't), so day mode no longer shows a dark box. Both stills were re-rendered from the same angle.
- Contact: a small "All fields are required." line above the form.
- A browser-tab icon (favicon): the M sitting inside the open C, drawn with the same strokes as the Home page's spinning circles. Lilac on charcoal in a dark browser, plum on cream in a light one, plus an iPhone home-screen icon. This also fixes the site's only console error (the missing icon). Mockup: `design/mockups/favicon.html`.

### Changed
- After a technical audit of all five pages (Impeccable audit, 17/20):
  - About Me: screen readers now hear a description of the 3D shape, which they lost once it loaded; the left and right arrow keys turn it; it only redraws when something moves instead of 60 times a second; and if a browser can't draw 3D, the still picture stays and the unusable controls hide.
  - About Me: the photo at the top loads right away instead of waiting, and comes as a WebP file (a newer image format) of 49 KB instead of a 155 KB JPEG, with the JPEG kept for older browsers.
  - Tutoring: the math styles load without holding up the first paint of the page.
  - Home: the spinning circles reuse the same shapes every frame instead of rebuilding up to 200 of them, which is lighter on phones.
  - Projects: Star Battle tells screen readers what each tap changed (for example "Row 4, column 4: star; 8 neighbors crossed out"); neurons are read by name ("c, Suzy throws"); Home and End work on the neuron tabs; the textbook preview can no longer stay blank if a page image fails to load.
  - Bigger tap areas: the Ehrhart coefficients, the Play button, "Show Only the Simplex", and the "Carson Mitchell" menu link.
  - Removed unused styles.
- After a site-wide design review (Impeccable critique, 24/32 for both halves of the site):
  - Home: each door now carries one real detail from its page: the 3D shape for About Me, the rates for Tutoring, a textbook page for Projects, and a tiny "you → CM" graph for Contact, with thin lines between the rows. The Contact door now says "Email, a message form, or a time on my calendar." Mockup: `design/mockups/home-doors.html`.
  - About Me: the big gaps between blocks are smaller (the bio stays centered beside the photo), on phones the 3D shape comes right after the first two Ehrhart paragraphs, and the page ends with a line pointing to Tutoring and Contact.
  - Contact: the "Send a Message" heading stays beside the form as you scroll, with a new line under it: "Rather talk first? Book a 15-minute intro call."
  - Tutoring: the "How I Teach" placeholder is hidden until Carson writes it.
  - Paragraphs no longer end on a single word; the neuron case tabs fade at the right edge on phones, to show they scroll.
- Tutoring: the logarithm problem's intro now reads "Solve this logarithm equation." instead of repeating the equation that sits right below it.
- Final review touches: captions also avoid one-word last lines; on phones, About Me's "L(−t)" button sits on its own line instead of dangling under the polynomial; less empty space at the bottom of Home.
- Polish: every page title is now the same size and sits at the same height (About Me's was smaller, Projects' sat higher); in day mode with reduced motion, the Banach–Tarski video shows its picture again instead of a blank box (switching to the day video used to reset it to its empty first frame).
- Animation review (Emil Kowalski's standards: Block, then Approve after fixes): the skip link now appears instantly instead of sliding (it answers a key press), and the Home doors' arrow nudge is switched off for visitors who ask for less motion, like every other hover on the site.
- Hardening and phone checks: if the 3D library can't load, About Me also hides the "Drag to turn" hint; the main buttons and the skip link are a full 44px tall for fingertips.

## [0.11.0] - 2026-10-25

The Contact page is built: every way to reach Carson, a message form that emails him, and the two booking cards.

### Added
- The Contact page. First screen: "Here's How to Reach Me", one sentence on what to write about, a "Ready to book?" link, and "Where to Find Me": email (still shown as "[at]/[dot]" and built only on click), with a **Copy** button for computers with no mail app, LinkedIn, GitHub, and "South Orange County, California".
- A directed graph under the opening sentence: five arrows (Message, Email, LinkedIn, GitHub, Book) from "you" to "CM". The paths draw themselves once; pointing at a path or a matching link lights it, and the first time a small dot runs along it toward CM. Each path is clickable and goes where it says. Mockup: `design/mockups/contact-moment.html`.
- **Send a Message**: a form that sends to Formspree (form `mrppewpn`), which emails Carson. Pick a topic (Tutoring, The GRE Textbook, A Website Bug or Idea, Something Else) and the hint and email subject change to match; first name, last name, email and message are required, with friendly notes beside each box. After sending: a check mark and "Thank You, <first name>", with a link to book an intro call.
- **Or Book a Time**: the same two booking cards as the Tutoring page.

### Changed
- After a design review (Impeccable critique, 25/32), hardening, a technical audit, phone checks and an animation review:
  - The form keeps a half-written message through a reload, gives up after 20 seconds instead of spinning, says when you're offline, shows Formspree's reason when it refuses a message, and still checks the boxes when JavaScript is off.
  - The "didn't send" message carries its own email link; the thank-you card no longer leaves a big empty space.
  - Touch targets are at least 44px on phones; the email stays on one line at every width, with Copy beside or under it.
  - The page no longer loads the math stylesheet it doesn't use: Lighthouse performance went from 74 to 99.
  - The dot on the graph runs only once per path and never on keyboard focus; it fades out as it reaches CM.
  - After the final review (Impeccable critique, 30/36): screen readers hear the thank-you heading after sending and hear a failed send right away; the email row's arrow is gone, so Copy lines up with the other rows' arrows.
- `CLAUDE.md`: the Formspree form ID, and Carson's photo appears only on Home and About Me.
- `styles.css`/`site.js` version tag is now `?v=2026-10-25-3r`.

## [0.10.0] - 2026-10-25

The Projects page is built: the free GRE textbook first, then the Neuron Diagram Maker and the Star Battle Solver, each with a live piece you can play with.

### Added
- The Projects page. First screen: "A Free GRE Textbook", described honestly as "Free, and still growing" (logic, set theory and arithmetic are written so far), with a **Download the PDF** button, the chapters written so far (pointing at one previews its first page), and a large real page with five sample pages to pick from.
- Neuron Diagram Maker, with a live diagram: three classic cases from the philosophy of causation (Preemption, Overdetermination, Double Prevention), told as one story about Suzy and Billy throwing rocks at a bottle. Tap a neuron to fire it; a small dot carries each signal, and the caption explains what happened in the story. Links to the editor.
- Star Battle Solver, with the real 10×10 puzzle from the project: tap once to cross a cell out, twice for a star (its neighbors are crossed out for you); **Show Me a Step** asks the solver for its next step and its reason; **Solve** watches it finish from wherever you are. A wrong mark is explained with the solver's own reasoning. Every step comes from running the solver itself (`data/star-battle-easy.json`). Links to the code on GitHub, since the solver is a Python program.
- A closing line linking to Tutoring and Contact.
- New files: `data/star-battle-easy.json` (the solver's steps), `images/projects/` (screenshots of the two programs), more textbook pages and small thumbnails in `images/gre/`, and the approved mockups `design/mockups/projects-neuron.html` and `projects-starbattle.html`.

### Changed
- After a design review (Impeccable critique, 21/32), hardening, accessibility, phone and motion passes:
  - Mistake messages match the tap order; the puzzle is one stop for the Tab key, with arrow keys between cells; puzzle progress survives a reload; if the puzzle can't load, the page says so instead of showing an empty board.
  - The neuron tabs are connected to their panel for screen readers; the region letters on the puzzle are easier to read at night.
  - Thumbnails load 5 KB pictures instead of 70 KB ones and the screenshots are resized: Lighthouse performance went from 64 to 96, and nothing jumps while the fonts load.
  - On phones the textbook page appears right after the download button; on touch screens every button is at least 44px tall; the puzzle uses the card's full width.
  - The textbook preview no longer flickers when you sweep across the chapters, and changes instantly from the keyboard; stars and crosses appear faster and more gently (Emil Kowalski's motion standards).
  - The puzzle's rules sit right above the board; the neurons you can start from are marked before your first tap.
  - After the final review (Impeccable critique, 31/40): row and column numbers along the puzzle board, and the cell a message talks about is outlined; the board sits above its explanation at every width, so the row is balanced and cells are bigger on a laptop; screen readers hear one summary when Solve stops instead of every step, and hear when a star breaks a rule; plainer solver wording; a line explaining that, as in the papers, *c* is always the cause in question and *e* the effect; on phones the three neuron cases stay on one line and scroll sideways; the night-mode puzzle regions are easier to tell apart.
- `CLAUDE.md`: the order of review steps to run once a page draft is done (critique, harden, audit, adapt, review-animations, polish, final critique).
- `WORKFLOW.md`: Stage 4 reminders for a favicon and for restyling the two programs to match the site.

## [0.9.0] - 2026-10-25

The Tutoring page is built: rates, booking through Cal.com, subjects, and a problem that solves itself as you scroll.

### Added
- The Tutoring page: rates ($60 per hour online, $80 in person, paid after the lesson by Zelle, PayPal or Apple Cash) and two large booking cards, **Book a Lesson** and **Book an Intro Call**, on the first screen; the subjects (read from `content/subjects.md`); a marked placeholder for "How I Teach"; and a sample of the GRE textbook (four pages of explanations, each opening the PDF at that page).
- "One Problem, Step by Step": a worked problem that solves itself as you scroll, one line at a time, with each step's reason in a box that follows the newest line, and Back / Next buttons. Three problems: a logarithm equation, a Putnam integral, and a dice paradox.
- Booking through Cal.com: an Intro Call (15 minutes, Zoom or phone) and a Tutoring Session (1, 1½ or 2 hours, Zoom or in person), where students propose up to three times and Carson confirms one.
- `images/gre/`: pictures of textbook pages for the Tutoring page; `design/mockups/tutoring-solve.html`: the approved mockup of the step-by-step problem.

### Changed
- Every page now links `styles.css` and `site.js` with a version tag (`?v=…`), so browsers fetch the new copy after a change instead of showing an old one.
- `content/subjects.md`: a note that subjects go below the "## Subjects" line (the site skips the instructions above it).
- After a design review (Impeccable critique, 22/32): each problem now starts at step 1 and only moves as you scroll or press Next; Next first asks "What would you do next?" before showing the step; once you use the buttons, scrolling leaves the problem alone; the buttons travel with the reason box instead of floating far below; the tabs fit on one line and work with the arrow keys; screen readers hear "Step 3 of 7" and no longer read lines that haven't appeared; the reason box is easier to see in day mode; a closing line points back to the booking cards; small text fixes (no lone last words, rates that don't break mid-phrase on phones).
- After a motion review (Emil Kowalski's standards): the booking cards are there at once instead of fading in; a pressed card shrinks in place instead of dropping; the reason box glides a little faster and snaps back when you switch problems; hover lifts are skipped for visitors who prefer reduced motion.
- Hardening, accessibility, phone and polish passes (Impeccable harden, audit, adapt, polish):
  - Scrolling moves the problem about one step per 115px; it only catches up while you're still scrolling, one step at a time, so a quick flick moves one step and it stops when you stop. On phones it counts from the lines themselves, so no step appears off-screen.
  - Screen readers hear each step with its reason when stepping with the buttons, with math read properly ("1 over 3 to the power n minus 1").
  - Earlier lines are dimmed by color instead of transparency, so they stay readable in day mode.
  - On touch screens every board control is at least 44px tall.
  - On phones each rate gets its own line, and the scroll hint is shown.
  - Phones get smaller copies of the textbook pages, less than half the download.
  - If the math library fails to load, the first problem shows as plain text.
  - Very long subject names wrap instead of widening the page.
  - The booking cards say they open Cal.com.
  - Unselected problem tabs are quieter than the Back/Next buttons, so choosing a problem and stepping through it look different.
  - If the math library fails, the step marks and button hint are hidden along with the board.
  - The signature under "How I Teach" is hidden until the letter is written.
  - The math library's console warnings are silenced.

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

[Unreleased]: https://github.com/carsonmit/carsonmit.github.io/compare/v0.13.0...HEAD
[0.13.0]: https://github.com/carsonmit/carsonmit.github.io/compare/v0.12.1...v0.13.0
[0.12.1]: https://github.com/carsonmit/carsonmit.github.io/compare/v0.12.0...v0.12.1
[0.12.0]: https://github.com/carsonmit/carsonmit.github.io/compare/v0.11.0...v0.12.0
[0.11.0]: https://github.com/carsonmit/carsonmit.github.io/compare/v0.10.0...v0.11.0
[0.10.0]: https://github.com/carsonmit/carsonmit.github.io/compare/v0.9.0...v0.10.0
[0.9.0]: https://github.com/carsonmit/carsonmit.github.io/compare/v0.8.0...v0.9.0
[0.8.0]: https://github.com/carsonmit/carsonmit.github.io/compare/v0.7.0...v0.8.0
[0.7.0]: https://github.com/carsonmit/carsonmit.github.io/compare/v0.6.0...v0.7.0
[0.6.0]: https://github.com/carsonmit/carsonmit.github.io/compare/v0.5.0...v0.6.0
[0.5.0]: https://github.com/carsonmit/carsonmit.github.io/compare/v0.4.0...v0.5.0
[0.4.0]: https://github.com/carsonmit/carsonmit.github.io/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/carsonmit/carsonmit.github.io/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/carsonmit/carsonmit.github.io/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/carsonmit/carsonmit.github.io/releases/tag/v0.1.0
