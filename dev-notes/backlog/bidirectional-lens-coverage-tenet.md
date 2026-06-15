# Bidirectional lens coverage — a core tenet + a lens-set audit

**Status:** [READY] — operator-raised 2026-06-07 ("bidirectional → we should check what other lenses are
missing bidirectional; it's a core tenet we need to have"), spawned by `clippy-write-side-boundary` (F29).
**Queued: AFTER `clippy-write-side-boundary` lands** (that run extends Silent-substitution-at-boundary to
bidirectional — the first instance of the tenet).

## The tenet
A lens that guards a **boundary or directional crossing** (read↔write, producer↔consumer, in↔out, send↔receive)
should guard **both directions**. A one-directional boundary lens has a silent mirror-gap: the same failure
principle on the *other* side falls through (exactly how F29 — the write-side of Silent-substitution — escaped).
"Boundary lenses are bidirectional" is the design tenet; a one-sided boundary lens is suspect by default.

## The audit (do after the F29 run)
Sweep clippy's lens set (`coding-clippy/spec/lens-set.md`) for **directional** lenses + check each covers both sides:
- **Silent-substitution-at-boundary** — read-only → being made bidirectional now (`clippy-write-side-boundary`). ✓ (the seed)
- **Canonical-ID-dropped-at-handoff** — claims both sides ("producer-side serialization AND consumer-side
  deserialization") — but re-check: is the *consumer→producer* / write-back direction actually covered, or only
  producer→consumer drop? Likely already bidirectional; confirm.
- **Branch-coverage** — directional? (reads-of-external-data vs writes/emits-of-branch-values) — check.
- **Defensive-paranoia-vs-type-guarantee** — already has an "inverse defect" clause (a built-in mirror) — note as
  the *pattern to emulate* (a lens that explicitly carries its own inverse).
- The Quality-category, Coupled-change, Consumer-enumeration, Thorough-fix, Target-locality lenses — judge which
  are directional at all (most are not boundary-crossing).
For each one-sided directional lens: extend bidirectional (Pareto, per the F29 precedent) unless skill-craft confirms
the mirror is a genuinely distinct axis (the additive-reflex / one-coherent-question check from the F29 run, F-a).

## Two facets — decide the home in the cycle
1. **Instance audit** (clippy `spec/lens-set.md`) — the concrete sweep above. Clippy corpus-evolution → anneal-dev.
2. **The tenet as a lens-DESIGN principle** — does "boundary lenses are bidirectional" belong in **skill-craft**
   (the lens-authoring discipline, so it fires on every future lens) and/or the framework's lens-entry guidance?
   If so, that half is skill-craft/framework, not clippy. Resolve which in the cycle (additive-reflex: is it a new
   principle, or an instance of the existing completeness/true-unit discipline applied to lens *direction*?).

## Relates to
- `clippy-write-side-boundary` (the F29 seed; the first bidirectional extension) · `forcing-function-dose-discriminator`
  (force/surface/build) · skill-craft lens-authoring discipline · `coding-clippy/spec/lens-set.md`.
