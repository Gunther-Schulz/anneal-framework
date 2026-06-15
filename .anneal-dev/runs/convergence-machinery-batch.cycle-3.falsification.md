# Mechanical falsification pass — convergence-machinery-batch, cycle 3 (convergence)

**Header — this-cycle intent-clean verdict:** cycle-3 intent-falsification artifact = INTENT-CLEAN,
no `mechanical-falsification-candidate` finding → mechanical pass runs over all [VERIFIED] entries.

Fresh-context subagent (opus, lean brief) declared candidate+predicate+result; **orchestrator
computed holds-or-falsified** (no subagent judgment).

- **D1** `[{target-dependents, scope-search over spec/+anneal-dev/, any-outside-scope:{edit-set ∪ F6
  render-debt}, result: all priming/coverage token hits inside the edit-set or F6 plugin renders,
  EXCEPT core.md:396 (verbatim-capture), holds}]` **aggregate = holds.** Orchestrator verdict on
  :396: NOT a missed dependent — it is the verbatim-capture site D6 *relies on* (already present,
  unchanged); D6 re-points the derivation at :597-600 to it, does not modify :396. Satisfied
  precondition, not an outside-scope dependent → predicate yields no falsifying evidence.
- **D2** `[{target-existence, read core.md:345-346, expected-match:"…known going in and informs what
  the AI attends to…", result: present verbatim, holds}, {target-dependents, priming-token search,
  any-match (surviving priming dependent), result: empty (only :345-346 removed + :349 the re-anchor
  target), holds}]` **aggregate = holds.**
- **D3'** `[{target-existence, read core.md:349, expected-match:"this cycle's investigation touched",
  result: present, holds}, {target-dependents, search (work|cycle) touched, expected-match, result:
  glossary:301 "work touched" + modules:245 "cycle touched" both match, neither "investigation",
  holds}]` **aggregate = holds.**
- **D4** `[{target-existence, reads modules:453 + core:616-630 + core:548-552, expected-match (per-R#
  line `{R#, attempted-refutation, outcome}` ∧ routing ∧ falsified-holds-phase precedent), result:
  all three present, holds}]` **aggregate = holds.**
- **D5** `[{target-existence, reads core:981-983 + glossary:427-432, expected-match (verify coverage
  check ∧ "Specified in §4.3"), result: both present, holds}]` **aggregate = holds.**
- **D6** (technical-basis shapes only; operator-resolvable-assumption shape exempt) `[{target-existence,
  reads core:599-600 + core:987-991 + glossary:226-235, expected-match (enumeration-source ∧ verify
  soft verbatim leg ∧ intent-pass glossary entry), result: all present, holds}]` **aggregate = holds.**

**Result: every [VERIFIED] entry holds; no falsification.** Shape coverage matches each basis's
claimed shapes; no target-behavior shape claimed (all edits statically dischargeable). Combined with
the intent-clean pass and zero new D-delta → **convergence cycle CLEAN**.
