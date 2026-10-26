# Workflow: building Carson's site

How we customize the site, step by step. Your job is to decide and react; Claude's job is to run the tools, build, and explain. Copy the example prompts, or say it in your own words.

**Where things live**
- `PRODUCT.md`: who the site is for and what's true (no invented facts).
- `DESIGN.md`: the look (colors, fonts, rules). Change a decision here first.
- `CLAUDE.md`: how Claude should work with you.
- `index.html`, `about.html`, `tutoring.html`, `projects.html`, `contact.html`: the site's pages; `styles.css` and `site.js` are shared by all of them.

**Who leads**
- Look and layout: `design-taste-frontend`
- Motion and feel: Emil's skills (`emil-design-eng` and friends)
- Referee: `impeccable` (its hook checks every edit automatically)

---

## Stage 0: Housekeeping (once, ~10 min)

1. ✅ Commit the setup (skills and notes; compiled binaries and personal settings are gitignored).
2. ✅ PDF path settled: the pipeline writes `pdf/GRE-Textbook.pdf`, which the site links to.

## Stage 1: Gather real content (you, any time)

Design works best with real words. Collect, in any rough form:
- [x] A short bio (a few sentences, messy is fine; Claude edits): education done
  - [x] What drew you to math: left out for now (your choice)
  - [x] Life outside math (general for now)
  - [ ] Later, optional: what you do now
- [x] Your links: LinkedIn, GitHub, email (no Twitter)
- [x] Tutoring details: subjects (in `content/subjects.md`), levels, online or in person, rates
  - [x] Booking pages: Cal.com Intro Call and Tutoring Session (2026-10-25)
- [x] The photo of you (`images/carson.jpg`)
- [x] A theorem that matters to you: Ehrhart's theorem (informed your research)
- [ ] Later: how you teach (goes in Tutoring)
- [ ] Later: a CV / résumé (Carson's to-do, 2026-10-26). Add it as its own page or menu tab once his CV is ready; a design reviewer noted recruiters look for one.

Everything collected is recorded in `PRODUCT.md` under "Confirmed Content".

Missing pieces stay as clearly marked placeholders. Nothing gets invented.

## Stage 2: Finish the design decisions (mockup rounds, like the palette) ✅

Done: Newsreader body with IBM Plex Sans buttons; page order Hero, About, Tutoring, Projects (with the GRE textbook first), Contact; spinning-circles centerpiece in the hero, with one small live piece in About, Tutoring and Projects. Details in `DESIGN.md`.

Each is one or two rounds of live mockups:
1. ✅ **Body font**: "Show me body font options to pair with DM Serif."
2. ✅ **Page plan**: "Help me decide which sections the page needs and in what order." (Taste's step 2: every section must earn its place.)
3. ✅ **Interactive centerpiece**: "Show me centerpiece ideas." Candidates so far: a curve you shape, a problem that solves itself as you scroll, your name drawn by equations, a mini GRE question.

Each answer goes into `DESIGN.md`.

## Stage 3: Build, one section at a time

For each section, top to bottom (hero first):
1. **Build**: "Build the hero from DESIGN.md."
2. **Look**: Claude screenshots it at phone, tablet, and desktop width and shows you.
3. **React**: say what feels off, even vaguely ("too empty", "not me").
4. **Review**: "/impeccable critique the hero" for a design review.
5. **Motion**: "Use Emil's skills to refine the animations in the hero."
6. **Save**: "Commit this section." This makes a checkpoint you can always go back to.

(`/review-animations` is Emil's motion review; only you can start it, by typing it in the chat.)

Then move to the next section. Small steps beat "redesign everything".

Progress: ✅ Hero (v0.6.0) · ✅ About Me (v0.7.0) · ✅ Separate pages (v0.8.0) · ✅ Tutoring (v0.9.0) · ✅ Projects (v0.10.0) · ✅ Contact

**Before building Tutoring and Contact** (Claude: remind Carson at the start of that step):
- ✅ Tutoring session types created in Cal.com (Intro Call, Tutoring Session).
- ✅ Cal.com username set to `carsonmitchell`. Brand colors skipped (paid feature).
- ✅ Formspree form ID (`mrppewpn`).

## Stage 4: Polish the whole page ✅

- "/impeccable audit": accessibility, contrast, mobile, performance (done 2026-10-25: 17/20, fixes applied)
- Favicon (the little icon on the browser tab): mock up options, e.g. "CM" in DM Serif lilac on charcoal, or the C and M the hero's circles draw (Carson asked to be reminded, 2026-10-25). Done 2026-10-25: the M inside the C.
- "/impeccable polish": final pass on spacing and details (done 2026-10-25, with the full review pipeline on all five pages)
- Restyle Neuron Diagram Maker and Star Battle Solver (in `carsonmit/Widgets-and-Miscellaneous`) to match the site's look, then revisit how the Projects page shows them (Carson's plan, 2026-10-25). Done 2026-10-26: both apps restyled (Star Battle is now a web app with difficulty levels), Projects page updated; released as Widgets v0.5.0 and site v0.12.1. Booking texts shelved.
- "Use review-animations on the whole page" (done 2026-10-25: Approve after fixes)
- "Test the light/dark switch and the phone layout with Playwright" (done 2026-10-26 on the live site: all five pages and both apps, phone, tablet and desktop, Night and Day)

## Stage 5: Publish ✅

1. ✅ "Push to GitHub." Claude confirms before pushing, since the site is public.
2. ✅ Wait 1–10 minutes; GitHub Pages lags and caches. Hard-refresh (Cmd+Shift+R) before deciding something failed.
3. ✅ Check the live site on your phone too (done 2026-10-26; your one fix: links that leave the site now open in a new tab).

## What's Next (whenever you're ready)

The "later" items from the stages above, in no fixed order. Each starts with a short chat, then follows Stage 3's build-look-react loop.
- **How I Teach**: a section on Tutoring (already built and hidden, waiting for your words).
- **CV / résumé**: its own page or menu tab, once your CV is ready.
- **What you do now**: a line or two for About Me.
- **Star Battle variants**: the harder rules from your BmMT 2022 manual (k stars, Double Section, rectangular units, Black Hole/White Dwarf).
- **Booking texts**: shelved; the options are recorded in `CLAUDE.md`.
- **Three.js / Manim**: a 3D piece or a math animation where it fits.

---

## Changing your mind later

- Color, font, or rule: "Change the accent to X." Claude updates `DESIGN.md` and the site together.
- Undo a section: "Go back to the last commit for the hero."
- Not sure what you want: "Show me options for X." That starts a mockup round.

## Habits that get the best results

- One section or one decision per request.
- React honestly; vague reactions are fine, Claude translates them.
- Look at the site on your phone, not just your laptop.
- Commit after every section you're happy with.
