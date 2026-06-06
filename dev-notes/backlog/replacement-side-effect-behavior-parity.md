# Replacement behavioral-parity must name SIDE-EFFECTS (invisible to reference-search)

**Status:** OPEN — surfaced 2026-06-06 by a clippy Unit-5 retrospective (other session, carried
in by the operator). Empirical n=1 (production side-effect drop). **Adherence-failure-driven, but
the recurrence-reducing fix is a framework sharpening** (the failure mode is structural search-
blindness, not laziness — see below). Framework-level (`spec/core.md` §3.2.2 + the Coupled-change /
Missed-dependents lens in `anneal-dev/spec/lens-set.md`), rendered to instances → anneal-dev cycle
+ kernel-independent verify if pursued.

## The failure (clippy Unit 5)
A replacement deleted the runner classes and routed through a new `TicketCoordinator`. The
**Coupled-change lens fired** and tracked the *structural* coupling (schema + wiring + runner
deletion as a coupled set). But the **behavioral-parity enumeration** — what behaviors the deleted
runners *produced* that the successor must preserve — was never done. The runners made 4
`notify_autobet_placed` calls (live + dry paths); these were **silently dropped** on deletion.

## Why the rule already covers it (adherence failure, not a missing rule)
`core.md §3.2.2`: a replacement's basis must account for "references to, **load-bearing behaviors
of**, AND non-reference structural dependents" + "an explicit enumeration of **behaviors preserved
or dropped**." A produced notification is a load-bearing behavior of the deleted code → the rule
requires it enumerated. It wasn't → adherence failure on the behavior-enumeration clause.

## The real failure-mode (why "try harder" won't fix it) — and the sharpening
The basis has two legs: a **re-runnable search** (references + dependents — mechanical, grep-able)
AND a **behavior enumeration** (preserved/dropped — a *reading* task). A **side-effect** (a
Telegram post, a log line, an external call, an emit) produced *inside* the deleted code is
**invisible to the reference-search**: grep finds *who calls* the target, not *what the target
does*. So the model, having completed the visible leg (the search), defaults to "behaviors ≈ what
the search surfaced" and skips the side-effects the search can't reach. "Try harder to adhere"
doesn't close a *structural* blindness.

**The fix is the exact sibling of the shipped `structural-change-dependent-enumeration`** (campaign
②, now `core.md §3.2.2:235-244`): that sharpened the **dependents** clause to NAME the
non-reference-findable dependent forms (location-hardcoders, producer/consumer). This sharpens the
**behaviors** clause to NAME the non-reference-findable **behavior forms** — side-effects
(notifications, logging, external/network calls, queue emits, file writes that aren't return
values) produced *inside* the replaced code — and the **method**: enumerate by **reading the
deleted code's method bodies**, not grepping its callers. Candidate edit sites: `core.md §3.2.2`
(the behavior-enumeration clause names the side-effect form + the read-the-bodies method) + the
**Coupled-change / Missed-dependents lens** (`anneal-dev/spec/lens-set.md`; fire the side-effect
enumeration when the coupled set includes a deletion/replacement). Edit-as-Pareto: extends an
existing clause to name a search-blind form (mirrors the campaign-② precedent), no new rule.

## Adherence solutions (operator-pushed 2026-06-06) — mechanical > structural > safety-net
The above names the search-blind FORM; this is what makes the behavioral-parity leg actually
FIRE. The root adherence failure: the behavior-enumeration is a **judgment leg with a weak
artifact** ("behaviors: X preserved, Y dropped" — a claim, vacuously satisfiable) sitting next
to a **strong mechanical leg** (the reference-search); the model finishes the strong leg and
self-attests the weak one. Per the evidence-bearing-artifact rule ("a rule whose adherence can't
be read off an artifact isn't enforced"), give the behavior-leg an un-fakeable artifact:

1. **Mechanical — grep the RIGHT target (strongest; the key insight).** Side-effects aren't truly
   invisible — the search was aimed at the wrong thing. The reference-search greps *who calls* the
   deleted code (callers); the side-effect enumeration must grep the **deleted code's own method
   bodies** for **side-effect-producing calls** (external/network calls, notifications, logging,
   emits, non-return writes). Same tool, right target. Converts "read the bodies" (judgment) into
   "grep the bodies for side-effect signatures" (mechanical floor) + the un-fakeable artifact (the
   body-grep + each effect's disposition). **This supersedes the candidate-fix's "read the bodies"
   phrasing above.**
2. **Force it in the convergence mechanical-falsification pass (the teeth).** A `target-behavior`
   candidate per deleted/replaced unit: grep its body for side-effect calls; for each, search the
   successor for the preserved effect — **a side-effect with no successor = falsified**
   (orchestrator-computed, no self-attest). Fires structurally at convergence, not on the model
   remembering the leg.
3. **Sharpen the existing gate.** §3.2.2 already blocks [VERIFIED] without "behaviors preserved or
   dropped"; sharpen it to **require the side-effect-enumeration artifact specifically** (located
   body-reads + per-effect disposition) so the completeness claim cannot be satisfied by the
   reference-search alone (the Unit-5 conflation).
4. **Safety net (weakest).** A verify-time "deleted code's side-effects have successors" check —
   what the clippy retrospective was (manual, after-the-fact). Only if 1–3 insufficient.

**Headline:** the adherence fix is NOT "read more carefully" (judgment) — it's "grep the bodies,
not the callers" (mechanical) + the convergence falsification candidate. Caveat: the body-grep
catches *known* side-effect signatures (a mechanical floor); a *novel* side-effect API still needs
judgment — so (1) is a strong floor, not a complete elimination (same reducible-not-eliminable
ceiling as `design-decision-implication-depth-gaps`).

## V-watch vs backlog (dogfood note, 2026-06-06)
The operator floated a V-watch. Per the just-shipped `v-entry-is-post-ship-only` rule (V-entries
are **post-ship effect-watches** on a shipped fix/choice; a not-yet-implemented gap is a backlog
item), this is a **backlog item**, not a V-watch. A V-watch becomes appropriate *after* the
sharpening ships — to watch whether it reduces side-effect-drop recurrence (its catcher: a future
replacement that drops a side-effect the read-the-bodies enumeration would have caught).

## Relates to
- `structural-change-dependent-enumeration` (**archived — shipped** at `core.md §3.2.2:235-244`):
  the **dependents-clause sibling**; this is the same sharpening move on the **behaviors clause**.
  The decisive precedent — it confirms "name the search-blind form + the method" is the
  framework-level treatment, not an adherence nag.
- `behavior-change-test-impact-enumeration` (archived — shipped): a different class (test-assertion
  breakage from behavior *changes*), not side-effect *dropping* from replacements.
- `design-decision-implication-depth-gaps`: same "saw the fact (the deleted code), didn't connect
  it (to the parity obligation)" reasoning-depth shape — a candidate 4th class there, but homed
  separately because it has the distinct search-blindness mechanism + a clean sibling-of-shipped fix.
- `instance-domain-invariant-register`: the broader clippy cross-unit-invariant family; a "every
  observable side-effect of replaced code has a preserved-or-explicitly-dropped successor" is an
  invariant-shaped statement.
- Origin: clippy Unit-5 replacement retrospective (other session, operator 2026-06-06).
