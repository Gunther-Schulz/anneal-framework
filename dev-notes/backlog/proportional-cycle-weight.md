# Proportional cycle weight — right-size anneal-dev ceremony to the change

**What it is:** a candidate method-kernel discipline — run a *light* anneal-dev
cycle (single investigation pass, no convergence cycle, one verify) for changes
that are small / cosmetic / behavior-preserving / grab-bag, reserving full
ceremony (convergence + intent+mechanical falsification + isolated verify) for
method-kernel + load-bearing semantic edits.

**Status / stage:** [PARKED] DEFERRED — campaign ⑦ (rate machinery). **Practice now,
formalize only if proven** — now **n=2 evidenced** (2026-06-06 v-entry lever (A);
2026-06-07 clippy-write-side lever (B), below), so the "proven" bar is closer. The
*practice* is already available: the operator calls cycle-weight per item in-loop
when draining a campaign. This item is the *formalization* (a spec change making the
light path + lean-brief a documented default) — run it as its own anneal-dev cycle
when ⑦ is un-deferred.

**The soundness hazard (why it's not a free win):** this is the cousin of the
**carry-forward optimization removed by D7** (`f74b145`, the sweep's L1) — that
one was the WRONG simplification because it let a pass skip re-verification on
its own say-so. Proportional weight is only sound with a **non-circular certifier
of "light"**: the operator (or a non-producing checker) classifies the change's
weight, NOT the same pass that wants to skip ceremony. If the AI self-certifies
"behavior-preserving" to drop falsification, that's the exact circularity D7
closed. Encode the classifier as operator-in-loop (or an external check), never
self-attested.

**Empirical evidence (n=1, 2026-06-06 — the "proven" the deferred status waited for):**
the `v-entry-is-post-ship-only` run — a **non-method-kernel, small doc-clarification**
(re-word one state def + one exclusion sentence + a Vocab pointer) — got the **full**
ceremony: **3 convergence intent-falsification dispatches** (cycles 4/6/8) + an isolated
verify, across **10 cycles** for a ~3-edit change. Two findings:
1. **The cost was the convergence ceremony, not verify** — 3 opus dispatches vs verify's 1.
   A *light* cycle (no convergence, one verify) would have cut ~3 dispatches and kept the
   irreducible independent check. (The operator's instinct "skip verify?" aimed at the wrong
   target — verify stays; convergence is the lever.)
2. **The heavy ceremony GENERATED churn, not just cost** — each convergence cycle invited
   additive over-fixing (the gold-plating in `convergence-surfaced-finding-action-brake`);
   cycles 6–8 chased an unbounded "unambiguous" requirement's tail. A light cycle would have
   *avoided* the churn by never opening the convergence loop. So proportional weight is not
   only a cost win — for a small/non-kernel change it removes a churn *source*.
   The operator flagged the disproportion **twice** in-run (overthinking in convergence; verify
   weight) — the signal the light path was warranted and not taken.

**Two distinct levers (clarified 2026-06-07):** proportional weight has *two* knobs, not one —
- **(A) skip the convergence cycle** for a light change (the n=1 finding above — avoid opening the
  intent+mechanical loop at all). Home: method-kernel ([READY]/convergence requirement, `core.md §4.1.4`).
- **(B) lean the dispatch BRIEF** — even when falsification/verify *do* run, scope the brief to the **diff +
  its source clause + the relevant method section**, NOT "load the whole method." Home: the **dispatch-brief
  schema** (`modules.md §3.3`) + the falsification-brief template (`investigate-design.md`) + verify's brief
  (`verify.md`). (A) cuts dispatch *count*; (B) cuts each dispatch's *fixed cost*.

**⚠ Lever (A) is SENSITIVE — operator flagged 2026-06-07, unsure whether to pursue it at all.** Reason: skipping
the convergence cycle = **removing the framework's primary independence mechanism** (the fresh-context falsification
that catches the blind spot the producer shared) — on a **"light" classification that can be wrong**. In direct
tension with the framework's own "independence is the lever" tenet (`framework-intent-vision-statement`). The two
datapoints **conflict on (A)**, which is itself the hazard:
- **n=1 (v-entry)** — convergence only *churned* (gold-plating, no real catch) → favored skipping.
- **n=2 (clippy-write-side, THIS run)** — the change *looked* light (one lens), yet the convergence cycle **caught a
  real defect**: the cycle-2 intent pass found D2's render target was wrong (F-b — would have shipped the wrong
  lenses.md lines) AND surfaced the extend-vs-new crux. **Skipping convergence here would have shipped a defect.**
- ∴ the value of convergence on a "light" change is **unpredictable** — you cannot tell ahead of time whether it
  will churn (waste) or catch (save). That unpredictability + the **cost asymmetry** (a skipped-convergence *shipped
  defect* ≫ a wasted-ceremony) is why (A) is doubtful. **Lever (B) carries NO such hazard** — it keeps the
  independent check, only leaning the brief. **Recommendation: pursue (B); HOLD (A)** — do not adopt it without a
  hard non-circular "light" certifier AND acceptance that some real catches will be missed; quite possibly **don't
  do (A)** and just take (B). (The "light" classifier is the same circularity-risk the D7 precedent closed.)

**Empirical evidence (n=2, 2026-06-07 — the lean-brief lever (B)):** the `clippy-write-side-boundary` run — a
**one-lens instance edit** (extend Silent-substitution-at-boundary bidirectional) — spent **~4 subagents ×
~50–77k tokens**, the isolated verify alone **~68k** for a one-line-class change. Diagnosis:
- **Fixed cost dominates, not change-size** — a fresh isolated context (the independence requirement) re-loads
  the method + work-product from zero every dispatch; a 1-line and a 100-line edit pay nearly the same toll.
- **Triage = mostly adherence + a self-hosting wrinkle, with a real spec-gap tail:** the brief template does NOT
  mandate "load the full method" — the orchestrator over-briefed (adherence), aggravated by self-hosting (it
  pointed the subagent at the live `core.md` ~17k because the plugin lags, vs the lean *rendered* method files a
  normal run loads). The genuine **spec gap**: nothing *structurally forces* proportional brief-scoping — it's
  left to orchestrator discretion = **willed = leaks** (the loaded-but-inert class). "I'll lean it next time" is
  itself the willed-not-structural anti-pattern this whole family targets → encode it, don't resolve to it.
- **Independence tension (the (B) soundness hazard, cousin of the (A) certifier-of-light hazard above):** lean
  the brief **while preserving the fresh-context independent re-derivation** — too thin (just the diff) and the
  falsification/verify subagent *rubber-stamps* instead of catching the blind spot the producer shared. The rule
  is "scope proportional to the change, independence preserved," not "always thin."

## Coherence-batch economics — n=1, 2026-06-15 (`convergence-machinery-batch`)
A **sibling lever** to (A)/(B): not "how heavy a cycle for one change" but **how many items per cycle.**
The `convergence-machinery-batch` run drained TWO coherent backlog items (#2 `intent-falsification-
coverage-binding` + #3 `investigation-pass-lens-priming`, both §4.1.4 convergence machinery) in ONE cycle.
**Finding: the token savings come from COHERENCE, not count** — the fixed per-cycle costs (one grounding,
one convergence, one verify, one skill-craft self-review) amortize across items sharing the same machinery;
unrelated items share none of it. Estimate (**NOT a measured A/B**): ~one full cycle-overhead saved vs two
separate runs.

**The ceiling (do NOT read this as "batch more"):** a finding in ANY batched item re-converges the WHOLE
batch (this run: an intent-pass R2 seam in D3 → re-converge both items) and a fresh-context verify has
finite budget → past some size it churns or dilutes (the "too thin → rubber-stamp" failure at batch scale).
A coherent batch has a **sweet spot**, not a maximum. The lever licenses **"batch the largest *coherent*
cluster"** (= the campaign-map unit, `dev-notes/backlog/README.md` ▶ Campaign map), NOT "batch more items."
This empirically supports the campaign-map thesis (drain a coherent campaign as one cycle).

**Correction (2026-06-15 full grounding sweep):** the earlier impression that clean coherent
comparable-weight clusters are *rare* was a **status-line-picking artifact** — picking candidate clusters
from status-lines/titles (⑤, the ③ pair) kept hitting heterogeneous or stale items. A body-grounded sweep
of all 70 open items found **≥3 clean comparable-weight open-ready light pairs** (core-structural:
`core-md-bloat-measure-then-cut` + `verify-disposition-citation-reopen-explicit-leg`; release/hooks;
render-conventions). So aggressive batching is **more available than reactive picking suggested** — the
bottleneck was queryability (`backlog-status-queryability`), not scarcity.

**Measure it next:** n=1 + an estimate. Pair the next aggressive coherent batch with the token-measurement
(`measurement-harness-mve`) for a real number, and watch specifically for the churn/dilution ceiling.

**Isolation is NOT a proportional-weight lever (F9 lesson, same run).** When this run's skill-craft
self-review surfaced a behavior-preserving wording fix (F9), the orchestrator first delta-checked it
**in-context** (doer=checker) on a proportionality rationale — then the operator flagged it. Verify
isolation is **unconditional** (`core.md` §4.3 / INV-3), and a *delta* verify is still a verify → it must
run in a separate context. Leaning the BRIEF (lever B) is the safe economy; dropping the INDEPENDENT check
— even for a "trivial" fix — is the sensitive lever-(A) shape. Re-ran isolated: [F9 CLOSED — clean], no harm,
but the lesson binds: **proportional weight scopes the brief, never the independence.**

**Relates to:** `auto-battle-cadence-mode` (sibling ⑦ mode-mechanic — cadence vs
weight; distinct concerns) · `convergence-surfaced-finding-action-brake` (complementary:
the brake prevents gold-plating *within* a convergence cycle; proportional-weight *avoids*
the convergence cycle for a light change — two levers on the same 2026-06-06 churn) · the
framework's existing behavior-preserving classification (verify already uses delta-vs-fresh
re-verify — extend that *forward* to right-size the whole cycle) · D7 carry-forward removal
(the negative precedent; the soundness hazard above is its cousin).

**Next action:** none until campaign ⑦ is un-deferred. When it is: settle the
"who certifies light, non-circularly" fork WITH the operator (decide-ahead),
then run anneal-dev.

**Filed:** 2026-06-05 (session-strategy campaign map — captured the
proportional-weight idea raised during the rate re-assessment so it isn't lost;
no-silent-deferral).
