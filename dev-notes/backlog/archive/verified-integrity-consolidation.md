# FB-5. Verified-integrity — consolidate the "[VERIFIED] claims more than was checked" family

**Status:** [DESIGN] — a **consolidation cycle** (not a one-off), needs a practice-9 design surface. Operator-raised 2026-06-01.

**The principle.** A `[VERIFIED]` tag must be earned by *actually
checking the actual claim*. When a claim can't be fully checked ahead of
time, it must **not** be stamped `[VERIFIED]` — it's `[CONDITIONAL]`, and
the gap is surfaced. The framework has this idea but **scattered** across
pieces (evidence-bearing artifacts; the basis rule's true-unit-basis +
no-silent-substitution; Cycle 3's `[CONDITIONAL]` routing) — and it keeps
re-surfacing as separate findings.

## The family — three faces of one principle

- **Static** — design can't *statically* check runtime behavior →
  `[CONDITIONAL]`, discharged by a guard at verify.
  → **Cycle 3, SHIPPED** (core.md §3.2.2 + glossary target-behavior).
- **Un-run** — the agent *authors* a `[VERIFIED]` tag the mechanism never
  produced. → **V-25, WATCHING** (validation-watch).
- **Incomplete-evidence** — verify passes against a *sample*; the
  complete/live set isn't covered. A green test on a sample is "verified
  for the sample," not "verified." → **NEW, undesigned.** (Seed: azuro
  F18 — `sort` typed required; the 820-row capture + curated fixture had
  zero nulls, so unit tests + verify passed green while live data
  failed; only the full/live stack test caught it. True-unit-basis,
  applied to *test data* instead of the *design*.)

## The refactor (= the broader option, chosen over a narrow one-off)

State the umbrella principle **once**, then hang the three specific
mechanisms under it. **The principle unifies; the mechanisms do NOT
merge** — the subtype-trigger (static), the tag-authorship residual
(un-run), and the sample-representativeness check (incomplete-evidence)
are genuinely different detectors. So the structure is **principle + its
instances**, not one rule swallowing everything. This *is* the corpus's
own merge discipline (coherence-audit Lens 1; skill-craft Amendment
reduce/merge): one principle restated across N homes → consolidate, not
add an (N+1)th scattered finding.

## Why a cycle, not a backlog one-liner

1. **The incomplete-evidence face has no mechanism yet** — and it's the
   hard part: how does verify *detect* that its fixture is an incomplete
   sample? Same naked-judgment risk as Cycle 3's runtime detection;
   likely a representativeness-basis requirement, not a clean mechanical
   trigger. Can't consolidate cleanly until this is designed.
2. **Re-touches shipped Cycle 3** + the basis rule + glossary → real
   blast radius, full step-4.

## Sequencing

Natural fit for either the **coherence-audit** (set-level merge is its
job) or the **de-pollution cluster** (already restructuring §3.2 /
verify). Design the incomplete-evidence mechanism as part of the same
cycle. Until then, the three faces stay where they are (Cycle 3 shipped,
V-25 watching, this finding) — this entry is the marker that they're one
family awaiting consolidation.
