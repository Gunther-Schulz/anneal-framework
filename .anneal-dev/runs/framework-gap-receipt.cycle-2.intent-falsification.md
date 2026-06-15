# framework-gap-receipt — cycle 2 (convergence) intent-falsification pass

Fresh-context subagent (opus), criteria-first. Attacks whether the locked design
serves R1–R6. Subagent agent-id: a35649043a7cfa64b.

## Per-R# attack lines
- {R1, serves: D1,D3,D8,D9, refutation: read of `.anneal-dev/runs/*.intent-falsification.md` +
  `*.falsification.md` — neither carries a `class` field; D3 concedes the class is assigned from
  prose; within-run post-[VERIFIED] position is a tracker fact, not in the .falsification artifacts,
  outcome: **finding** (F-a, F-b)}
- {R2, serves: D4, refutation: located read modules.md:331-513 (§3.4 pass=mechanical, §3.4.1 pass=intent,
  both persisted, tallyable). But an intent-pass per-finding line can itself route
  `mechanical-falsification-candidate` → "intent-pass finding" and "mechanical class" are not disjoint
  at the finding level, outcome: **finding** (F-c)}
- {R3, serves: D5, refutation: located read D5 + item:31-36 + practice-12. Three outcomes + "neither"
  default → set is total. But lens-vs-framework is naked judgment; a class can read as both (Unit-31
  resolved by fiat), outcome: **finding** (F-d)}
- {R4, serves: D2(SG4),D5(SG3),D6(SG2),D8(SG1),D9(SG4), refutation: located read D2/D5/D6/D8/D9 +
  practice 11. SG1/SG3/SG4 encoded load-bearing. SG2 routes through practice-11's operator-second-judge,
  but the D2 "co-run with practice-12's mechanical cadence" affordance + auto-battle = no operator to bind,
  outcome: **finding** (F-e)}
- {R5, serves: D7, refutation: located read D7 + self-review-missed-side.md:6-8,119-121 + item:45-49.
  Boundary holds at design level; self-review-missed-side confirms no-merge. Leak vector: intent-pass
  per-finding lines include design-gap/escape-CHARACTER findings (clippy-reinstantiation.cycle-4 F-INT-1/2)
  that carry pass-type=intent, outcome: **finding** (F-f)}
- {R6, serves: D1,D11, refutation: search `grep -niE 'practice 13|framework-gap receipt' spec/core.md
  anneal-dev/spec/*.md spec/modules.md` → empty; core.md / modules.md §4 textually untouched,
  outcome: **served**}

## Per-finding lines (orchestrator disposition appended)
- {F-a, criterion: R1/D3, refutation: modules.md:440-513 (intent line, no class field) + D3 concession,
  route: [VERIFIED — surfaced]} → **ORCH: actioned as D-delta (D3)** — class-label is a weak artifact;
  tally cites per-class located instances for auditability; stability via separate-checker (operator
  second-judge, D6), not via a mechanical label.
- {F-b, criterion: R1-SG1/D8, refutation: modules.md:413 (mechanical line anchors [VERIFIED]) vs :440-513
  (intent per-finding line does NOT), route: mechanical-falsification-candidate — target-behavior on D8's
  "persisted records carry the post-[VERIFIED] signal" premise; candidate `expected-match:"[VERIFIED]"` over
  a `.intent-falsification.md` per-finding line} → **ORCH: orchestrator-computed verdict = FALSIFIED**
  (the §3.4.1 line shape `{finding,criterion-attacked,refutation,route}` lacks `[VERIFIED]` → predicate's
  expected pattern absent → falsifying). **D8 flips [INVALIDATED]→[PENDING].** This is the intent-delta →
  mechanical pass skipped this cycle. Fix: receipt source = falsification artifacts (pass-type+class) +
  tracker (post-[VERIFIED] flip history).
- {F-c, criterion: R2/D4, refutation: modules.md:486-507 (intent finding route ∈ {mechanical-candidate,
  surfaced}), route: [VERIFIED — surfaced]} → **ORCH: actioned as D-delta (D4)** — split by the
  falsification's LANDED type (§3.4 mechanical line vs §3.4.1 surfaced residual), reconciling that an
  intent-pass finding routing mechanical-candidate is tallied as mechanical.
- {F-d, criterion: R3/D5, refutation: item:31-44 (Unit-31 overlap resolved narratively), route:
  [VERIFIED — surfaced]} → **ORCH: terminal [VERIFIED — surfaced]** — SG3's default-to-strengthen is the
  both-fit tiebreaker D5 already states; the residual is inherent lens/framework judgment (SG2). No delta.
- {F-e, criterion: R4-SG2/D6, refutation: D2 co-run affordance + practice 11 operator-second-judge +
  practice 12 mechanical trigger (development-process.md:499-512) + auto-battle, route: [VERIFIED — surfaced]}
  → **ORCH: actioned as D-delta (D2,D6)** — drop the co-run-with-mechanical-cadence affordance; receipt is
  operator-invoked and its routing is surface-only (never auto-applied; operator binds at review) — the
  operator-independence boundary closes the unattended gap.
- {F-f, criterion: R5/D7, refutation: clippy-reinstantiation.cycle-4.intent-falsification per-finding lines
  (design-gap character) + self-review-missed-side.md:45-67, route: [VERIFIED — surfaced]} → **ORCH:
  actioned as low-weight D-delta (D7 clarification)** — "caught" means a falsification pass fired and
  caught it (mechanical OR intent); an intent-caught design-gap-character concern is still caught-side
  (missed = NO pass caught it). Preempts the mischaracterization.

## Convergence status
**NOT clean — intent-falsification produced D-track deltas (D2, D3, D4, D6, D7, D8 amended; D8 falsified
mechanically).** Per the depth-sequencing carve-out: **mechanical skipped: intent-delta this cycle.** The
deltas feed cycle 3; convergence re-attempts at the next convergence cycle.
