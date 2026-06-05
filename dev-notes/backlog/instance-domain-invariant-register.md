# Instance-domain-invariant register — locked cross-run primitives the instance evolves against

**Status:** OPEN — filed 2026-06-05 after a cross-session analysis of clippy's
silent-correctness bug class (other-session investigation; carried in by the operator).
Anneal-framework architectural addition: the work-product analogue of anneal's own
foundation-invariants register, scoped to the **instance's domain corpus** (clippy → code;
daneel → debugging artifacts; bauleitplan → German planning docs; campaign-craft →
marketing artifacts). Composes with the intent-falsification pass (the rendered attack
mechanism); the register would be one of its anchor sources.

## The gap
Three anchor layers currently exist in anneal-framework:

1. **Anneal's own kernel invariants** (`dev-notes/foundation-invariants/`) — INV-3
   verify-isolation, INV-5 exclusion-via-named-falsifier, etc. Locks the *framework*.
2. **Per-run requirements record** (`core.md §4.1`) — locks intent for *one run*.
3. **Glossary + closed sets** — locks vocabulary across the spec.

**Missing:** a **cross-run, instance-scoped** register that locks the **work-product
corpus's** load-bearing primitives — the invariants every future anneal-dev cycle in that
instance must derive from. For clippy (corpus = code), this would be primitives like:
- canonical identity ("a bet is identified by these 9 fields")
- producer-for-every-consumer ("every consumer of a value-class has a real producer for
  that class")
- closed-set membership ("MarketType is exactly {moneyline, spread, total, team_total};
  adding a value triggers sweep across every branch/serializer/consumer")
- cross-unit contracts ("the announce path reads from `autobet_bets`; a parallel
  `paper_bets` table requires the announce path updated")

For other instances, the slot is general — each instance fills it with its own domain
primitives. The slot itself is framework-level.

## Why the gap matters (empirical evidence)
Clippy's investigation sweeps surfaced 4 silent-correctness bugs of the
**load-bearing-dependency-without-producer-independent-re-derivable-artifact** class
(V-30 catalog, class (i)+(iv) at the work-product layer):
- Replay (Unit 7) verified green but no score producer existed; tests supplied fixture
  scores → gap invisible at unit-test time.
- Freshness gate's attribute-match selected the wrong market for `team_total`.
- `signal_id` was complete for original markets but went lossy when `team_total` arrived.
- Alert dedup checks `autobet_bets` but a later unit put bets in `autobet_paper_bets`.

Each unit's design was **correct on its own terms**. Clippy's basis-falsification (the
analogue of anneal's mechanical pass) couldn't catch them — the bug was not in the unit's
basis. **Intent-falsification IS the missing axis** — but its current anchor is the
*per-run* requirements record, not a *cross-run* domain invariant. A locked register
would be the cross-run anchor intent-falsification attacks against.

## Fix direction (design seed, not the locked design)
A register slot (instance-scoped; framework provides the slot, the instance fills it),
plus discipline + rendered attack mechanism:

**Register shape (per-invariant entry):**
- **Name** — the locked primitive (e.g., "canonical-bet-identity").
- **Locked statement** — the invariant in precise form (the 9 fields, the closed set,
  the contract).
- **Basis** — how the lock was established: search-established (corpus-wide enumeration)
  / data-grounded (real prod data confirming the closed set) / etc. — per the basis rule
  (`core.md §3.2`).
- **Forcing function** — what change-class triggers re-verification of the invariant
  (e.g., "adding a `MarketType` value" → sweep every branch/serializer/consumer).

**Discipline:**
- Every anneal-dev cycle in the instance reads the register at investigate-design.
- The intent-falsification pass attacks the locked design against the register's
  invariants in addition to the requirements record.
- The forcing-function class catches **enum-extension / new-dimension** consequences
  cross-corpus (one of clippy's bug shapes).

**Open questions for the cycle:**
- Slot location: extend `instantiation-guide.md §5` Operator-editable-artifacts with a
  fifth slot, or as an instance-internal `dev-notes/instance-invariants/` mirror of
  anneal-framework's own register? (The latter parallels the existing structure cleanly.)
- Composition with intent-falsification: extend the pass's criteria source from
  "requirements record" to "requirements record ∪ instance-domain-invariant register"?
  Or fire a sibling pass per invariant?
- Discoverability: how an instance authors the register at first-run + grows it as new
  invariants are recognized (clippy's `canonical-bet-identity` was **discovered**
  during sweeps, not pre-declared; the register needs an entry-on-discovery discipline).
- Composition with the foundation-invariants register's **anchor requirement** — the
  framework register requires an *external* anchor (Platt, Panickssery, etc.) to gate
  membership; should the instance-domain register require an analogous external anchor
  (e.g., a domain-data observation, a published spec, a regulatory text), or is the
  cross-run lock itself the gate? (Likely the latter — instance-domain primitives are
  by definition domain-specific.)

## Relates to
- `cross-instance-precedent-discipline` — distinct concern (precedent discovery in
  sibling instances; this is invariant-locking *within* an instance), but composes (a
  sibling instance's locked register is precedent for a new instance's first authoring).
- `framework-blindspot-class-analysis` — this is one specific blind-spot class the
  register addresses; the broader analytical work surfaces siblings.
- `instance-reinstantiation` — the register slot needs rendering into instances when
  shipped; the capability matrix (added today) tracks it.
- V-30 (`form-not-binding-class-recurrence`) — the empirical watch this register's
  effectiveness rolls into.
- `intent-falsification-soundness-sweep` — the per-run anchor (requirements record) the
  cross-run register supplements; sweep machinery composes cleanly.
- `design-decision-implication-depth-gaps` — **the complementary half of the same clippy
  retrospective.** This register homes the *out-of-scope / inherited / uncharted-surface*
  class (paper-mode idempotency, `signal_id` identity, overtime period-drop — cross-unit
  invariants never locked); that item homes the *within-scope reasoning-depth-at-design-lock*
  class (period-blind settlement, txn-hold, dead-write). Overlapping evidence (Unit 7,
  `signal_id`); together they cover the retrospective's 6 production bugs. The register is
  the stronger answer to the inherited-surface class than the analysis's "inherited-surface
  audit pass" candidate — lock the primitive once, every unit derives from it.

## Surfacing context (other-session note, 2026-06-05, key excerpts)
> "Lock cross-unit domain primitives as first-class invariants. The deepest prevention:
> the lossy-identity class is impossible if 'the canonical bet-identity' is a locked
> primitive every unit derives from. Clippy locks per-unit design + checks broken-basis
> within a run; it has no notion of a shared invariant a new unit must verify against."
>
> "The load-bearing prerequisite is the **anchor**, not the boot. With no 'complete
> identity' / 'producer-for-every-consumer' / 'recompute≈detect' anchor, both observation
> and ad-hoc review default to 'looks fine' (pattern-matching). The anchor is what
> converts 'looks fine' into a checkable claim a sweep can attack."

Full carry of the other-session analysis is in the operator's transcript of session
2026-06-05; the load-bearing analytical claims are reproduced above.
