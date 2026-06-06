# Provenance-at-handoff — candidate clippy lens (a value's assumed semantics ≠ its producer's)

**Status:** OPEN — candidate clippy lens, surfaced empirically 2026-06-06 (session 11) by the
beat-the-books real-codebase review A/B (`anneal-empirical-validation-experiment.md` VERDICT).
Routing: **clippy instance** lens (coding-flavored), per the `design-decision-implication-depth-gaps`
precedent; the underlying principle is the framework **basis rule** (root), so this is a
*lens that operationalizes the basis rule at value-handoff seams*, not new doctrine.

## The bug class
A value crosses a producer→consumer boundary, and the consumer's assumption about *what the value
is* — its provider, perspective, value-domain, identity — does **not** match what the producer
actually sets. The field name, variable name, and/or docstring typically **assert the consumer's
(wrong) assumption**, so reading the consumer in isolation looks fine.

Four distinct bugs in the beat-the-books replay-settlement review were all this one class:
- **market_id** — `re_score` matches `leg['market_id']` against `reference_provider.market_id`
  (Pinnacle); the leg's id is the *betting* provider's (EV+ `ev_plus.py:338`). Variable even named
  `pinnacle_market_id`; docstring asserts Pinnacle. → never matches → every pick aborts. (Latent:
  tests hardcode the Pinnacle id; replay never ran on real data.)
- **handicap sign** — consumer assumes picked-team perspective; broker stores HOME perspective.
- **team_qualifier crash** — consumer requires HOME/AWAY; broker sets `None` for spreads.
- **closing_lines CLV** — same `team_qualifier` mismatch in the backfill matcher.

## The lens (candidate)
> **Provenance-at-handoff** — for each value a function consumes where correctness depends on *what
> the value means* (an id, a provider, a perspective, a unit, a value-domain), trace it to where it
> is *produced* and verify the producer's actual semantics match the consumer's assumption.
> **Distrust the field name, the variable name, and the docstring** — ground the meaning in where the
> value is set. A mismatch is a bug.
> *Trigger (mechanical):* a value consumed by the unit-under-review whose semantics are load-bearing
> and whose producer is a different module/provider. *Evaluation (judgment):* do producer and
> consumer agree on the referent?

## Finding-rate evidence (3 arms × 5, same task) — this lens is *specifically* load-bearing
The 3-arm ×5 comparison **isolates this lens**: generic anneal discipline does NOT catch the provenance
class — only the explicit "trace each value to its producer" does.

| bug (this class) | act-first (none) | vanilla-anneal (generic disc.) | adhoc (+ trace-to-producer) |
|---|---|---|---|
| market_id | 2/5 | **2/5** | **5/5** |
| closing_lines | 2/5 | **2/5** | **5/5** |

**Vanilla anneal is no better than act-first here (both 2/5); only the explicit provenance discipline
lifts it to 5/5.** So this lens earns its keep — it catches a class that *plain thoroughness misses*.
Contrast the sibling **dimension-completeness** lens (for the **period** bug): that one turned out
**redundant with generic thoroughness** — vanilla catches period **3/5 without it**, *more* than adhoc's
2/5. So of the two candidate lenses, **provenance-at-handoff (this one) is the stronger bet; the
completeness lens is the weaker** (plain "verify each kind" already gets period). Bounds: n=5 (wide CIs);
single-pass (understates anneal — cycles would compound); the clippy/heavy-machinery arm was run
single-pass so heavy-vs-lean is untested.

## Lens vs. general-discipline (the open question — mirrors depth-gaps' open Q)
What actually *caught* market_id (the adhoc arm) was the **general** basis-rule + trace-to-producer
discipline, not a specific lens trigger. So the fix is one of:
- **(a)** add this specific lens (a mechanical trigger at value-handoff seams), or
- **(b)** raise the *salience/adherence* of the existing basis rule for **value-provenance claims**
  (treat a name/docstring's assertion of a value's meaning as a claim requiring grounding at the
  producer) — no new lens, a sharpening.
Likely both: (b) is the root principle; (a) is the mechanical fire-point. Decide which when the cycle
runs. NB: lenses are *additive to scope* (they don't narrow the review surface — the prior framework
position holds); whether a salient lens-set degrades the open-ended general pass *in practice* is an
**untested** hypothesis (would need clippy×5 vs adhoc×5), not a finding.

## Relates to
- `design-decision-implication-depth-gaps.md` — **sibling class catalog.** That item homes Class 1
  (dropped *dimension* = period) + Class 2 (execution-context). This is a distinct class (wrong
  *provenance* of a present value). Could be **merged in as a 4th class** if the maintainer prefers
  one catalog; kept separate here because it has its own session-11 empirical backing.
- `anneal-empirical-validation-experiment.md` — the empirical source (the real-codebase A/B + the
  act-first ×5 finding-rate data live in its VERDICT section).
- the **clippy** instance (`coding-clippy/spec/lens-set.md` or wherever the lens-set lives) — the edit target.
- `clippy-greenfield-tolerance.md` — sibling clippy-lens-quality item.
