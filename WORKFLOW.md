# Workflow: building Carson's site

How we customize the site, step by step. Your job is to decide and react; Claude's job is to run the tools, build, and explain. Copy the example prompts, or say it in your own words.

**Where things live**
- `PRODUCT.md`: who the site is for and what's true (no invented facts).
- `DESIGN.md`: the look (colors, fonts, rules). Change a decision here first.
- `CLAUDE.md`: how Claude should work with you.
- `index.html`: the actual site.

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
- [ ] A short bio (a few sentences, messy is fine; Claude edits)
- [ ] Your links: LinkedIn, GitHub, email, others
- [ ] Tutoring details: subjects, levels, online or in person, how to book
- [ ] The photo of you
- [ ] Optional: a favorite theorem, how you teach, anything that's "only you"

Missing pieces stay as clearly marked placeholders. Nothing gets invented.

## Stage 2: Finish the design decisions (mockup rounds, like the palette)

Each is one or two rounds of live mockups:
1. **Body font**: "Show me body font options to pair with DM Serif."
2. **Page plan**: "Help me decide which sections the page needs and in what order." (Taste's step 2: every section must earn its place.)
3. **Interactive centerpiece**: "Show me centerpiece ideas." Candidates so far: a curve you shape, a problem that solves itself as you scroll, your name drawn by equations, a mini GRE question.

Each answer goes into `DESIGN.md`.

## Stage 3: Build, one section at a time

For each section, top to bottom (hero first):
1. **Build**: "Build the hero from DESIGN.md."
2. **Look**: Claude screenshots it at phone, tablet, and desktop width and shows you.
3. **React**: say what feels off, even vaguely ("too empty", "not me").
4. **Review**: "/impeccable critique the hero" for a design review.
5. **Motion**: "Use Emil's skills to refine the animations in the hero."
6. **Save**: "Commit this section." This makes a checkpoint you can always go back to.

Then move to the next section. Small steps beat "redesign everything".

## Stage 4: Polish the whole page

- "/impeccable audit": accessibility, contrast, mobile, performance
- "/impeccable polish": final pass on spacing and details
- "Use review-animations on the whole page"
- "Test the light/dark switch and the phone layout with Playwright"

## Stage 5: Publish

1. "Push to GitHub." Claude confirms before pushing, since the site is public.
2. Wait 1–10 minutes; GitHub Pages lags and caches. Hard-refresh (Cmd+Shift+R) before deciding something failed.
3. Check the live site on your phone too.

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
