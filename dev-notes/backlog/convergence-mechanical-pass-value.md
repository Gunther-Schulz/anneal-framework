# Convergence mechanical-falsification pass — value & cost given intent-falsification

**Status:** OPEN — design question, operator-raised 2026-06-05 (during the `campaign3-enforcement-fidelity` [READY] gate); **re-raised 2026-06-15** (during `convergence-machinery-batch`) with a request for an **empirical-firing survey** (folded in below). **Parked, not scheduled** — gated on evidence (see "How the evidence accrues"). Method-kernel (`spec/core.md` §4.1.4) if ever pursued → anneal-dev + kernel-independent verify. NOT urgent.

## The observation (anecdotal, n=few)
Once the convergence cycle's **intent-falsification** pass comes up clean, the **mechanical** falsification pass has (anecdotally) held **first-pass** every time. Before intent-falsification existed, the mechanical pass often needed several passes. Operator's question: does mechanical still earn its cost, or could it fold / scope down?

## SETTLED — do NOT fold mechanical into intent
The two passes attack **different objects** and sit on **opposite sides of the bind/surface line** (`core.md` §3.1):
- **Intent** attacks *design ↔ requirements* (does the design serve its intent?). It is a **pure-judgment surfacer** — `core.md` §4.1.4: its per-R# line "is free-form and can be vacuously satisfied, so it does **not** mechanically force soundness."
- **Mechanical** attacks *each decision's basis ↔ the corpus* (is the evidence true/complete?). Its verdict is **orchestrator-computed** from re-checkable search results — "no subagent judgment" — an **un-fakeable bind**.

Folding mechanical into intent would collapse the one binding leg into a surfacer — the exact surfacer-sold-as-bind overclaim the campaign-① sweep exists to eliminate. **Rejected.**

**Why mechanical holds first-pass post-intent (not redundancy):** the basis rule (§3.2) forces every `[VERIFIED]` decision's basis to be a re-runnable search at *decision-time*; intent runs *first* and its D-deltas re-ground the affected bases (skipping mechanical that cycle); so by the time intent is clean the bases are already grounded → mechanical re-runs and holds. Mechanical holding is the convergence *converging* (the upstream disciplines working), not mechanical being idle — and you can't know it holds until you run it (dropping it = assuming the conclusion).

## OPEN — the two genuine questions
1. **Mechanical-convergence vs verify's citation re-check.** Verify (§4.3 / §3.2:187-190) ALSO re-opens every citation. The convergence mechanical pass and verify's re-check both re-run the bases. Is convergence-mechanical redundant with verify? Tentative answer: **no — it's shift-left** (catches a basis flaw *before* implement = cheap, vs verify's post-implement loopback = expensive). But the overlap is real and worth a proper look. (This is the actual overlap — NOT with intent.)
2. **Cost-scoping refinement.** Could the mechanical pass re-run only the bases that **changed** since the last cycle (or that intent didn't already route as `mechanical-falsification-candidate`), preserving the bind while cutting the fresh-context-dispatch cost? The spec already does a little of this (an intent-delta skips mechanical that cycle). A delta-scoped mechanical pass is the Pareto candidate.

## How the evidence accrues (no dedicated absence-watch — that would be cost-gating)
Per the validation-watch README, watching "mechanical never catches anything across N runs → fold" is the named cost-gating anti-pattern (absence-threshold). Instead:
- **The dispositive positive signal** (n=1, keep): a run where the mechanical pass **catches a post-intent-clean basis flaw** intent missed → proves mechanical's independent bind value → the OPEN questions narrow to cost-scoping (#2) only, fold-vs-verify (#1) closed toward keep. The existing **post-run-review attribution** Q already tags per-finding what surfaced it — that data accrues naturally; no new instrument needed.
- The cost angle (#2) composes with `anneal-reliability-measurement` (token-first metrics) — if pursued, measure the mechanical pass's per-run dispatch cost there.

## Empirical-firing survey (operator-requested 2026-06-15, folded in)
Operator request: survey **past runs** — `.anneal-dev/runs/*.cycle-*.falsification.md` (here) **and**
`../beat-the-books/.clippy/runs/` (clippy's convergence/falsification artifacts — "beat the books one
folder up") — for whether the **mechanical** pass ever produced a **real `falsified` aggregate** (an
entry that flipped `[INVALIDATED]→[PENDING]`), on the hypothesis that if it never fires, intent-
falsification may already be sufficient.

**Framing (binds — do not let the survey become the cost-gating fold-trigger this item already
rejected):** the survey is **INPUT to the two OPEN questions**, NOT an absence-watch.
- If the survey finds mechanical **DID** fire (caught a post-intent-clean basis flaw) → that's the
  **dispositive POSITIVE keep signal** named above (n=1 keep) → closes #1 toward keep, narrows to #2.
- If mechanical **never** fired → this is the **absence-threshold cost-gating anti-pattern** (per
  "How the evidence accrues" + the SETTLED section): NOT license to drop. The mechanical pass is the
  INV-5 exclusion keystone (`dev-notes/foundation-invariants/INV-5`); "never fired" is survivorship-
  biased (it may hold *because* the upstream basis-rule/intent disciplines are good — a smoke detector
  that never trips isn't idle). At most it sharpens **cost-scoping #2** (delta-scoped mechanical).
- **Survey method caveat:** the literal token "falsified" is pervasive **noise** — it is the
  `holds-or-falsified` field label on every candidate line. The survey must distinguish a real
  **verdict** (aggregate=`falsified` / a recorded `[INVALIDATED]→[PENDING]` flip / an intent finding
  routed `mechanical-falsification-candidate` that confirmed) from the field-label noise — a careful
  per-artifact read or a precise pattern, not a bare `grep falsified`.

**Seed datapoint (n+1, this run `convergence-machinery-batch` 2026-06-15):** mechanical pass came back
**all-holds** again (cycle-3; intent-clean → mechanical ran → every D-entry held). A quick `grep
falsified` over this repo's artifacts was **inconclusive** (field-label noise; the one real aggregate
verdict caught read "holds. No design decision falsified"). Consistent with the "holds first-pass
post-intent" observation; not yet the dispositive positive signal (no catch), not (per the framing
above) a fold-trigger.

## Relates to
- `proportional-cycle-weight` — lever (A) (skip the convergence cycle) is the SENSITIVE simplification
  this survey could be misread as supporting; the same "you can't know it holds until you run it" +
  INV-5-keystone guard applies. The survey is the empirical input lever (A) would need — but the input
  is necessary-not-sufficient (the keystone + survivorship-bias guards remain).
- `anneal-reliability-measurement` — the cost angle (#2) is a token-efficiency measurement; co-home if #2 is pursued.
- `intent-falsification-soundness-sweep` — same bind-vs-surface family; the "don't fold" conclusion here rests on the same §3.1 distinction the sweep enforces.
- Origin: `campaign3-enforcement-fidelity` run, operator interjection at [READY] (2026-06-05).
