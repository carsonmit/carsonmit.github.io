---
name: Carson Mitchell
description: Personal site of a math tutor; a calm, scholarly voice in a modern, interactive frame.
---

<!-- SEED: established with the user before implementation; re-run /impeccable document once there's code to capture the actual tokens and components. -->

# Design System: Carson Mitchell

## Overview

A scholar with modern tools. A classic serif voice sits in a dark, quiet, precise frame (the "quiet instrument" direction dealt by design-taste-frontend): one narrow column, generous space, and small live math demonstrations instead of decoration. The site has two modes, night (dark) and day (light). They should feel like the same person in a dark outfit and a light outfit, never like two brands.

The page should feel alive and responsive, but with one focal point at a time. There is one interactive centerpiece (not yet chosen; the cursor-shaped sine wave was only an exploration), plus small responsive touches everywhere (Emil's skills lead motion and interaction feel). Background texture never competes with the centerpiece.

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

- Headlines: DM Serif Display in both modes (chosen for day/night consistency over Fraunces).
- Body and UI text: [to be resolved during implementation]. Inter Tight was rejected; DM Sans was used as a neutral stand-in in mockups.

## Layout

Quiet-instrument grammar: a single narrow column placed left of centre, a large headline, a lot of untouched space. Exact measurements are [to be resolved during implementation].

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
