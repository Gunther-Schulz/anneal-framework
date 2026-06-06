# Requirements-anchored brake on additive over-fixing (the additive reflex with no requirement-anchor)

*Keystone vector: actioning an intent-pass surfaced finding (convergence cycle). Generalized
2026-06-06 to a second vector — design-formation — after a same-run, same-root instance (see
"The root is multi-vector"). Filename keeps the keystone-vector slug.*

**Status:** OPEN — framework finding, surfaced by dogfooding 2026-06-06 (during the
`v-entry-is-post-ship-only` run, operator caught it mid-flight). Empirical base **n=2 — two
vectors in one run** (see "The root is multi-vector"); the mechanism is **structural** (the
additive reflex, amplified by an unbounded requirement + the convergence loop), not a one-off slip.
Method-kernel if pursued (`spec/core.md` §4.1.4 intent-falsification routing +
`foundation.md`/`spec/core.md` recommendation discipline + the Bloat lens) → anneal-dev +
kernel-independent verify. **Not urgent**, but interesting — it's a clean instance of a
self-amplifying convergence loop.

## The one-line gap
The convergence cycle's intent-falsification pass routes each finding as either a
**mechanical-falsification candidate** (drives a D-delta) or **pure-judgment**
(`[VERIFIED — surfaced]` — *terminal*, "never blocking the phase, never a loopback,"
`spec/core.md` §4.1.4). In practice the orchestrator **overrides the terminal routing and
actions some surfaced findings as D-deltas** (reopening design). That override is the right
move for a real defect — but it has **no brake**: nothing checks whether the actioned fix
serves an actual **requirement (R#)** or a concern the adversarial pass *generated*. With no
brake, the same override that catches real defects also fires on robustness-preferences
beyond the requirements → **scope inflation (gold-plating)** → the added prose becomes fresh
surface the next convergence cycle attacks → **the loop amplifies instead of converging.**

## The case (this run — full trace)
Run `v-entry-is-post-ship-only` (codify V-entries = post-ship-only; un-implemented gaps →
backlog). Requirements: R1 (noticed gap stays a backlog item), R2 (V-entry role unambiguous,
no cross-doc contradiction), R3 (existing register stays correctly classified).

Every defect across the convergence cycles was routed `[VERIFIED — surfaced]` by the
fresh-context subagent; the orchestrator actioned each:

| Cycle | Finding | Actioned? | Right call? | Why |
|---|---|---|---|---|
| 4 | WATCHING re-framed as "a *choice*" over-narrows; mis-fits class-recurrence (V-30) + rule-residual (V-31) entries | yes (reopen D2) | **✓ correct** | design **failed R3** (entries mis-classified) — a real requirement failure |
| 6 | exclusion's "decided-against" **collides** with the WATCHING def's "accepted residual" | yes (reopen D2) | **✓ correct** | design **failed R2** (internal contradiction) — real requirement failure |
| 7 | *(the over-fix)* added an **inlined discriminator clause** to pre-empt "a filer reading only the README might confuse accepted-residual with noticed-gap" | yes (added prose) | **✗ gold-plating** | R1 **and** R3 were **already served** (cycle 6 said so). The fix served a concern **no requirement asked for** — "make it filer-proof," a hardening *beyond* R1. |
| 8 | the cycle-7 discriminator **misattributes to practice 8** a rule it doesn't state (practice 8 routes a form-in-hand classifiable fix to *commit-now*, not backlog) + umbrella-granularity asymmetry | reverted (removed the clause) | ✓ (by removal) | the cycle-8 findings were **defects in the cycle-7 over-addition** — nitpicks on prose that shouldn't have existed |

So: cycles 4 & 6 = the pass earning its keep; cycle 7 = the miss; cycle 8 = the cost of the
miss (two extra cycles + two opus dispatches spent attacking a clause that had to be removed).
Reading practice 8 in full afterward confirmed its "Entry hygiene" (`development-process.md`
`:310-315`) **already** routes a noticed gap out of validation-watch — so the discriminator was
re-teaching a rule that already existed elsewhere, the textbook gold-plating shape.

## The root is multi-vector — it hits every additive moment (operator-observed 2026-06-06)
The cycle-7 discriminator was **not** the run's only additive over-fix. At **implement**,
applying skill-craft discipline (`anti-patterns.md` Additive-reflex + Edit-as-Pareto) caught a
SECOND instance — same root, different vector:

- **Vector 1 — surfaced-finding-action (cycle 7, the case above):** an intent-pass
  `[VERIFIED — surfaced]` finding actioned into an addition past the requirements.
- **Vector 2 — design-formation (D4, caught at implement):** a design decision *formed*
  additively at cycle 1 — "R2 names practice 8, so add a cross-confirm sentence to practice 8" —
  though practice 8 ALREADY embodied the principle (Entry-hygiene `:310-315` + not-a-deferral-
  journal `:296-308`). **No surfaced finding triggered it**; the reflex fired at design-formation.
  R2 does not fail without it → gold-plating (cross-file fragmentation). Dropped at implement
  (operator agreed 2026-06-06).

So the root — **the additive reflex with no requirement-anchor** — is not convergence-specific;
it fires wherever the AI forms or revises rule-text. The two vectors map to two fixes already in
this item:
- Vector 1 → the **keystone** (evidence-bearing ACTIONED-surfaced gate).
- Vector 2 → **reinforcer #3** (tie the Bloat lens to the requirements record). **D4 is direct
  evidence:** the cycle-1 standardized Bloat pass PASSED D4 because it asked "is this
  load-bearing?" (D4's "cross-confirm" rationale reads load-bearing) — not "is this load-bearing
  *to a failing requirement*?" (R2 already held). A requirements-tied Bloat lens flags D4 at
  design-time, before it ever locks.

## Why THIS run churned so much — the amplifier (operator asked: "how does all this happen?")
9 cycles for a small wording fix is anomalous. The amplifier: **an unbounded requirement has no
natural terminal.** R2 — "the V-entry role is **unambiguous**" — is a goal you can always push
further (more airtight, more cross-confirmed, more filer-proof). A *mechanism* requirement ("the
gate blocks X") terminates — it blocks X or it doesn't. A *clarity* requirement ("unambiguous,"
"robust," "clear") does not. So the additive reflex runs unchecked: each cycle finds another
"could be clearer" and adds; each addition becomes the next cycle's attack surface (convergence-
loop amplification). The named ambiguity (WATCHING reads pre-ship) was resolved by **cycle 5**;
cycles 6–8 chased the unbounded tail.

**Brake refinement this yields:** for an unbounded (clarity-class) requirement, "served" must be
defined as **the *named* ambiguity resolved** — the specific contradiction/gap that motivated the
requirement — NOT "no conceivable reader could misread." Without that pin, the requirements-anchor
test ("does this serve a *failing* requirement?") is itself un-terminating for clarity requirements,
because such a requirement is never definitively "served." This pin is what the keystone + reinforcers
need to bite on a clarity requirement.

## The discriminator the orchestrator was missing
The tell that separates a *correct* action from gold-plating:

> **Action a surfaced finding only if it shows the design FAILS a requirement R# (cite which,
> and how it fails). If it merely proposes hardening BEYOND the requirements, record it
> terminal-surfaced and move on.**

Applied to the case: cycles 4/6 cite a failing R# (R3 / R2). Cycle 7 cites none — R1/R3 were
already served; the subagent *framed* it "criterion-attacked: R1," but R1 wasn't *failing*, it
was being *inflated* into "and make it impossible for any reader to mis-apply." That framing —
**an in-scope requirement stretched into an out-of-scope robustness goal** — is the exact shape
the brake must catch.

## Candidate fix (keystone + two reinforcers — design sketch, not locked)
1. **Keystone — make "ACTIONED-surfaced" evidence-bearing.** Today the orchestrator's
   action-a-surfaced-finding move is an ad-hoc tracker tag (`[VERIFIED — surfaced → ACTIONED]`,
   cycles 2/4/6) with **no required basis**. Formalize it: actioning a surfaced finding into a
   D-delta requires a cited **{R# it fails, how it fails}** artifact. A surfaced finding with no
   citable R#-failure **cannot** be actioned — it stays terminal (recorded for the operator's
   review). This converts a silent improvisation into an evidence-bearing gate, in the spirit of
   the rest of the kernel (a move with no producible artifact isn't enforced). Home:
   `spec/core.md` §4.1.4 (the intent-pass per-finding routing) + the finding-state enum in
   `foundation.md`/`spec/core.md` (Finding states — give "surfaced→actioned" a basis requirement,
   or add it as a sanctioned third route distinct from the two current ones).
2. **Reinforcer — thorough-fix scope is a ceiling, not only a floor.** The recommendation
   discipline ("addresses the situation at its **actual scope**, not pre-clipped on cost")
   is read as a *floor* (don't do less). It is silent that actual-scope is also a *ceiling*
   (don't do more). The thorough-fix default biases toward *adding*; nothing symmetric guards
   over-adding. Sharpen: actual-scope binds both ways; a fix exceeding the requirement's scope
   is as malformed as one clipped below it.
3. **Reinforcer — tie the Bloat lens to the requirements record.** The Bloat lens asks "is this
   load-bearing?" — defeated here by a *manufactured* load-bearing rationale (the filer concern).
   Sharpen the question to "is this load-bearing **to a requirement (R#) or a locked decision** —
   not to a self-generated concern?" That re-anchors the lens to the requirements record the
   intent pass already attacks against.

## Why standalone (relate-before-add)
- `convergence-mechanical-pass-value` — **distinct.** That item is about whether the *mechanical*
  pass earns its cost (settled: don't fold mechanical into intent). This item is about the
  orchestrator's *action decision* on the **intent** pass's surfaced findings. Same convergence
  cycle, opposite end. Cross-ref, no fold.
- `intent-falsification-soundness-sweep` — **same bind-vs-surface family.** The sweep eliminates
  "surfacer sold as bind"; this is the converse failure on the *consumer* side — a surfacer
  (terminal by design) treated as an *actionable mandate* with no anchor. Co-relevant.
- `framework-blindspot-class-analysis` / `post-run-review-failure-class-register` — this is a
  named failure class ("convergence scope-inflation via actioned-surfaced-finding-without-
  requirement-anchor") → a candidate register entry the post-run self-review could probe.
- `post-run-review-nonsensical-cycle-probe` — the **detective, general** counterpart to this
  **preventive, single-shape** brake (operator-clarified 2026-06-06: post-review should catch
  **any** nonsensical cycle). This brake stops the known shape in-run; that probe catches what the
  brake doesn't, post-run.
- `design-decision-implication-depth-gaps` — **instructive contrast, not the same.** That class
  is *under*-connecting ("saw the fact, didn't connect it to the decision"). This is
  *over*-connecting ("connected a non-requirement concern to the design"). Same "reasoning-depth
  at design-lock" family, opposite direction — worth noting together when either is worked.
- Origin: `v-entry-is-post-ship-only` run, operator interjection mid-convergence (2026-06-06),
  recorded in that run's `.cycle-6` / `.cycle-8` intent-falsification artifacts.

## Next action
Not scheduled. When picked up: it's a tier-4 framework-change / campaign-① (sweep — soundness &
binding) cycle — design the keystone gate first (decide: basis-on-the-ACTIONED-tag vs a sanctioned
third route), then the two reinforcers ride it. Composes with the sweep's surfacer-vs-bind theme.
