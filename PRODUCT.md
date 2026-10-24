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

- Current sections: hero, about, connect/social, footer, with animation effects. The live `index.html` still shows template placeholders ("Your Name", `yourhandle`); the confirmed content below replaces them in Stage 3.
- Math notation is written in LaTeX.

## Brand Commitments

Visual identity chosen with the owner is recorded in `DESIGN.md`. Animation decisions follow the `emil-design-eng` skill. No logo or other brand assets are on record.

## Evidence on Hand

- The GRE mathematics textbook PDF (`pdf/GRE-Textbook.pdf`, 35 pages).
- NeuronDiagrams (confirmed by the owner as real work): a point-and-click editor for the neuron diagrams used in papers on causation. It exports TikZ/LaTeX code or images and runs in any browser and on iPad. Lives in the separate repo `carsonmit/Widgets-and-Miscellaneous`, served at https://carsonmit.github.io/Widgets-and-Miscellaneous/NeuronDiagrams/ (installable web app).
- StarBattleSolver (confirmed by the owner as real work): a Star Battle puzzle solver with a visual, step-by-step solving window. Same repo, at `StarBattleSolver/`.
- There are NO testimonials or reviews. Future work must not invent any; leave them absent until the owner provides real ones. The only real rates are the two listed under Confirmed Content.
- Confirmed name: Carson Mitchell.

## Confirmed Content

Supplied by the owner in Stage 1 (2026-10-22). Use these words and facts as written; anything marked PLACEHOLDER stays a visible placeholder until the owner supplies it. Never fill a placeholder with invented text.

### Bio (About section)

Owner's wording (2026-10-24, replaces the Stage 1 draft), first person, use as written:

> I graduated from UC Berkeley in 2023 with a bachelor's degree in mathematics. I formerly attended the University of Southern California as a PhD candidate in the mathematics department. I'm also a proud product of the community college system; I attended Santa Barbara City College, where I earned associate's degrees in math, physics, engineering, economics, and accounting.

- What drew Carson to math: left out for now, by the owner's choice (2026-10-24). Don't add a placeholder for it.
- Life outside math (owner, 2026-10-24, general for now): reading, especially philosophy; gaming; music; movies; walking his dog; going to the beach. His dog is named Dexter. Site wording (owner, 2026-10-24): "I enjoy reading (especially books on math and philosophy), playing video games, listening to music, watching movies, going on walks with my dog Dexter, and going to the beach."
- What he works on now (owner, 2026-10-24): combinatorics, logic, probability, and the philosophy of mathematics, primarily. Site wording: "I work mostly in combinatorics, logic, probability, and the philosophy of mathematics."
- Lead-in before the math examples (owner, 2026-10-24): "Here are a few examples of results I find particularly interesting and beautiful."
- Voice rule (owner, 2026-10-24): the math explanations (Ehrhart's theorem, Gödel, Banach–Tarski) never use "I", "me" or "my"; first person is only for the bio and interests, plus one exception the owner allowed: the sentences about his own research in the Ehrhart block (owner's wording, 2026-10-24: "I study polytopes like this, generated from permutations of the form $Ln1$ using the stack-sorting algorithm. This specific one has Ehrhart polynomial $(t+1)^3$, the same as the unit cube, lecture hall simplices, and many other well-studied geometric structures.").

Facts behind the bio: Santa Barbara City College 2019–2021, five associate's degrees (math, physics, engineering, economics, accounting); UC Berkeley 2021–2023, bachelor's in mathematics; USC 2024–2025, former PhD student in mathematics (he did not finish the PhD; never imply he did).

### Photo

- `images/carson.jpg`: 1200×1600 JPEG made from the owner's own photo, with location (GPS) data removed. The original HEIC is not in the repo, on purpose (browsers other than Safari can't show HEIC, and it carried location data).

### Links (Contact section)

- Email: carsonm6719@gmail.com
- LinkedIn: https://www.linkedin.com/in/carson-mitchell
- GitHub: https://github.com/carsonmit
- Booking page: PLACEHOLDER. Booking goes through Cal.com (`https://cal.com/carsonmitchell/<event-slug>`), but no tutoring session types exist yet; the owner will create them later (account details in `CLAUDE.md`). Until then, booking falls back to email or the contact form.
- No Twitter/X or other social links (the owner said the site won't use Twitter).

### Tutoring

- Levels: all levels.
- Format: online, or in person in South Orange County, California.
- Subjects: listed in `content/subjects.md`, which the owner edits himself; the site reads the list from that file.
- Rates (real, supplied by the owner): $60 per hour online, $80 per hour in person.
- How to book: Cal.com booking page (PLACEHOLDER, see Links); email until then.

### "Only you" material (optional)

- Ehrhart's theorem: not his favorite, but it has informed much of his research (owner, 2026-10-24).
- His research (owner, 2026-10-24): the subpolytope of the permutahedron formed by the permutations reached by running permutations of the form $Ln1$ (ending in $n$ then $1$) through the stack-sorting algorithm, i.e. their stack-sort orbits. Example he'd like highlighted: the orbit of $23\cdots n1$, which he calls the **stack-sorting simplex** (use that name on the site); for $n = 4$, $2341 \to 2314 \to 2134 \to 1234$, a tetrahedron whose Ehrhart polynomial is $(t+1)^3$ (computed by Claude, brute force $t = 0..5$).
- Theorems he loves (owner, 2026-10-24): Gödel's incompleteness and completeness theorems, taken together; Cohen's independence proofs; the Banach–Tarski paradox. Independence (a proof that neither a proof nor a disproof exists) is, in his words, the most impressive part. The About block is titled "Gödel's Completeness and Incompleteness" (owner, 2026-10-24).
- How he teaches: belongs in the Tutoring section, not About (owner's choice). PLACEHOLDER until he writes it.
- Anything else personal: not decided yet.

## Product Principles

- One site, several audiences: no visitor type should have to dig past another's content.
- Person first: the site introduces Carson as a person before it offers a service. When two options are close, the warmer, more personal one wins.
- Never fabricate proof: no invented testimonials, rates, credentials, or download counts.
- The GRE textbook is the strongest real asset, so it stays easy to find.
- Stay simple: plain static HTML/CSS/JS that the owner can read and learn from.

## Accessibility & Inclusion

No product-specific requirement established. The owner is a beginner-to-intermediate coder who wants plain-language explanations of changes.
