# Dependent-enumeration blind spots — the Missed-dependents lens misses non-content-reference dependent classes (+ the [CONDITIONAL]-exemption compounder)

**Status:** OPEN — framework finding, surfaced by DOGFOODING during the
`corpus-flows-redesign` run (2026-06-03). **Two instances now (n=2)**, both
caught at implement/verify → loopback, both traceable to the same root.
Methodology-correctness → **operator is the kernel-independent judge**. Not yet
a design; captures the root cause + candidate fixes.
(Filename predates the generalization — the finding is broader than
"structural-change" alone; see the two instances below.)

## The unifying gap

The **Missed-dependents** lens (`lenses.md`) + the basis-rule completeness
(`spec/core.md` §3.2 Replacement/removal/amendment) are shaped for
**content-reference** dependents — "what *states / cross-references / RENDERS*
the contract." Real changes also have **non-content-reference** dependent
classes the lens does not frame, and they fall in the gap. Two have now bitten:

### Instance 1 (F16) — path-hardcoders (structural change)
D5 (merge anneal-dev → `anneal-framework/anneal-dev/`, subtree-add `d5ae00d`)
relocated anneal-dev's rule-corpus. The `commit-msg` hook's `^`-anchored
`RULE_CORPUS_PATTERN` didn't match the new paths → merged content slipped the
discharge gate. The dependent class = **code/config that hardcodes the old
path** (hooks, `.gitignore`, manifests) — outside the rule-TEXT corpus the lens
searches. (The hooks had even been READ for D4, but never *connected* as
merge-dependents — the content-reference framing doesn't prompt "what hardcodes
this path?")

### Instance 2 (VF1) — producer of a consumed artifact (new convention)
D7 (checkpoint ≠ release-commit via the `anneal-checkpoint:` marker) shipped the
**consumer** side — the `commit-msg` hook skips the prefix, dev-process prose
asserts it — but **no rule PRODUCES the marker**: anneal-dev's implement
Checkpoint spec was left "unchanged" and never mandates the prefix. The rule
fires on an artifact (the prefix) no rule emits → a future run's checkpoint is
prefix-less → blocked by the discharge hook (the exact failure D7 targeted). The
dependent class = **the producer of an artifact a new rule consumes** — when a
fix introduces a convention/marker one side *reads*, the lens doesn't force
"what *writes* it?" (Unenforced-rule's "is the rule enforced?" checks the
consumer; nothing checks the producer exists.)

## The shared compounder (now n=2): the `[CONDITIONAL]` falsification exemption

BOTH decisions were `[CONDITIONAL]` for an **operator-cost** reason (D5 merge;
D7 marker-shape), so the convergence falsification pass
(`phases/investigate-design.md`) **skipped them entirely** — and with them, their
*technical* dependent-completeness. The one mechanism that could have caught
either (falsifying the `target-dependents` shape) never ran. The exemption is
too coarse: cost-conditionality buys the decision's technical bases a pass they
shouldn't get. **n=2 is a strong signal this is the highest-leverage fix.**

## Candidate fixes (for operator methodology-judgment)

- **Generalize Missed-dependents to non-content-reference dependent classes.**
  The lens/basis-rule explicitly enumerate, beyond content-references:
  (i) **path-hardcoders** — for a relocate/rename/split, "what hardcodes the old
  path or assumes the old structure?" (hooks, `.gitignore`, manifests; scope
  extends BEYOND rule-text to enforcement code/config); (ii) **producer↔consumer
  pairing** — for a new convention/marker/artifact-shape, "if a rule *consumes*
  X, what rule *produces* X?" (both homes must exist; a consumer without a
  producer is an unenforced rule firing on a non-existent artifact). Closes the
  blind spots no current lens frames.
- **Tighten the `[CONDITIONAL]` falsification exemption.** Exempt only the
  operator-resolvable ASSUMPTION from the convergence pass; still falsify the
  decision's other load-bearing bases (dependent-completeness, target-existence).
  ⟵ n=2 (F16 + VF1 both rode this exemption past falsification).

## Relates to
- `corpus-flows-redesign.md` — the run that surfaced both (F16 / D5 merge; VF1 /
  D7 marker); its two loopbacks are the n=1 and n=2.
- C1 cluster (`behavior-change-test-impact-enumeration.md`) — sibling
  "what-does-this-change-touch" enumeration discipline.
- `spec/core.md` §3.2 (basis-rule completeness), `lenses.md` (Missed-dependents +
  Unenforced-rule), `phases/investigate-design.md` (convergence falsification +
  the `[CONDITIONAL]` exemption) — the edit sites if accepted.
- Method-kernel finding (touches `spec/*`) → runs through anneal-dev +
  kernel-independent verify if taken up.
