## INV-5. Exclusion via a named, runnable falsifier — the soundness keystone

**Invariant.** verify excludes via a named, runnable falsifier per decision
— not confirmation; completeness alone is unsound.

**Kernel home.** `spec/core.md` §4.1.4 (the falsification pass: each
[VERIFIED] decision gets a candidate falsifier — "a search or read whose
positive result would invalidate the entry's basis" — run, with the result
cited; a `falsified` aggregate flips the entry through [INVALIDATED]→[PENDING]).

**External anchor.** Two works compose here:

- Platt, "Strong Inference," Science 146(3642):347–353 (1964) — exclusion.
  Only exclusion (disproof) yields a secure conclusion; a crucial step's
  alternative outcomes each *exclude* one or more hypotheses. Confirmation
  does not secure a conclusion; exclusion does.
- Gunter, Gunter, Jackson & Zave, "A Reference Model for Requirements and
  Specifications" (WRSPM), ICRE 2000 — completion is provably insufficient
  for soundness. An "entailment + nothing-dropped" check passes a
  disjunctive S1∨S2 specification that satisfies adequacy and relative
  consistency yet "would break as soon as it was deployed"; the fix is the
  stronger refinement (the environment- and system-side strengthening,
  Formulas 7–8). Direct evidence that completion alone is unsound and the
  stronger refinement (exclusion of broken rivals) is required.

This is THE soundness keystone of the register: it names why
completeness ≠ soundness and where the kernel discharges the gap.

**Research.** `dev-notes/research/process-literature-deep-research-2026-06-03.raw.json`
findings [3], [4].
