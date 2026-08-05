# Compile-or-tournament — a birth-time switch over design claims (merged Brief-2 candidates 5+7)

**Status:** [DESIGN] — filed 2026-07-17 by operator pre-verdict (chat, 2026-07-17: "lass uns
5+7 wie geplant verschmelzen und verbuchen und 6 parken mit begründung"), merging Brief-2
candidates 5 (Executable-Invariant-Compilation) and 7 (Tournament-Design) into ONE
core-thesis item, pilot format. Candidate 6 (Live-Adversary) is **parked** here as the
recorded rejected alternative (see §Rejected alternative below — rationale + revisit
condition). Formal batch disposition of the remaining Brief-2/3 candidates is separate
(briefs: `dev-notes/briefs/2026-07-16-pbs-handover-2-stellschrauben.md`,
`2026-07-17-pbs-handover-3-design-grenze.md`); candidates 5/6/7 are hereby pre-dispositioned
and MUST NOT be re-dispositioned in that batch without new evidence.

## The thesis

Every design claim of a run is classified **at birth** by one switch:

1. **Compilable** → the claim emits its executable checker (test / grep predicate / schema
   constraint). From then on the machine checks it — permanently, without moods — and
   re-verification of these claims at convergence attempts becomes ~free (meshes with
   Brief-2 candidate 1, delta-scoped falsification over the claim graph).
2. **Not compilable** → that IS, by definition, the judgment/R8 class (Brief 3's Grenze A).
   For these the escalation path replaces iterate-one: **tournament at top tier** — N
   independent drafts, judge ≥ producer tier (the model-axis carve-out logic extends to the
   judge), and the judge is briefed criteria-first with the **compiled invariants of the
   neighboring claims** as objective criteria.

The two halves are one paradigm because each answers the other's weakness: compilation gives
the tournament judge objective criteria; the tournament gives compilation an honest answer to
its own limit — what does not compile gets tournamented, so the totalizing "all the way down"
ambition of candidate 5 is dropped, and tournament-as-default (candidate 7's cost problem on
narrow solution spaces) is dropped too: it fires only on the judgment branch, optionally
blast-radius-gated.

**Metric for free:** the share of claims taking the "not compilable" branch IS the design
residuum (Brief-3 item 16) — the metric is the switch counter, no separate build.

## Design risks (belong in any campaign scoping this)

1. **Checker fidelity — the dangerous silent false-green.** A checker that only apparently
   covers its claim is worse than none. In-house countermeasure: the worked-boundary-example
   discipline — every emitted checker must demonstrably FAIL on a constructed negative
   example, else it counts as not emitted.
2. **The switch itself is a judgment — but a benign-failure one.** "Wrongly compilable"
   fails loudly (the checker cannot be written, or falls at the negative example); "wrongly
   judgment" costs only an unnecessary tournament — expensive, never silently wrong.

## Lineage / relates to

- `judgment-to-mechanical-lens-candidates.md` — the direct precursor: the in-flight campaign
  performs the judgment→mechanical conversion BY HAND, three times, in the kernel;
  compile-or-tournament generalizes it to per-claim runtime mechanics. Sequencing: this item
  runs AFTER that campaign ships.
- Brief-2 candidate 1 (incremental falsification) — compiled checkers make the delta-scoped
  re-verify trivial for the compiled share.
- Brief-3 item 16 (design residuum) / `measurement-harness-mve.md` — the switch counter is
  the residuum metric; reports into the harness.
- Brief-2 candidate 3 (criteria-first) — the judge-brief discipline on the tournament branch.
- `lens-crowding-vs-broad-search.md` — compilation shrinks the prose-lens surface instead of
  growing it (anti-crowding direction).
- Empirical anchor: pbs deployment already precipitates this way organically (closed-set-sweep
  lens produced enumeration-from-source tests in 3 build dispatches, Brief 2 §Empirie-Anker).

## Rejected alternative — Live-Adversary (Brief-2 candidate 6), parked with rationale

**Parked 2026-07-17 (operator verdict, chat).** A permanent red-team agent DURING design
(pair mode) instead of stage falsification. Nothing of it is adopted, because its one
legitimate impulse — catch before install — is already covered three times over, each cheaper
and without sacrificing isolation:

- Brief-2 candidate 4 (design-time trace clause) catches the self-inflicted class at design
  time — empirically the largest cost item (2 of 4 non-convergence deltas in the model-axis
  run were self-inflicted: F14/F16 ledger error, F21 enum error).
- Brief-2 candidate 3 (criteria-first) pulls the intent check to dispatch start.
- The checker-fidelity negative-example rule above IS the domesticated live adversary:
  adversarial pressure at claim birth — mechanical, punctual, fresh-context-compatible —
  instead of a co-running agent that absorbs the designer's context.

What remains exclusive to candidate 6 — continuous judgment-class checking during design —
is where it is weakest-evidenced and most expensive: it requires permanent top-tier presence
(same-tier adversaries demonstrably false-accept the judgment class, model-axis empirics),
and pair-mode contact with the designer's rationalizations strains fresh-context isolation —
the single best-evidenced mechanism in the corpus (Brief 2 Nr. 13: delivered against BOTH
model tiers on 2026-07-16).

**Revisit condition (carried at birth, per Brief-3 item 17's pattern):** reopen ONLY if
measurement data (the residuum/harness metrics) show that a high share of convergence deltas
sits on already-built-upon design — i.e. stage falsification is systematically too late.
Absent that evidence, this ground is settled.
