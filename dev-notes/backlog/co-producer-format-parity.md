# Co-producer parity for a shared-format key (consumer-enumeration is consumer-shaped — it misses CO-PRODUCERS)

**Status:** OPEN — surfaced 2026-06-07 by a beat-the-books production bug + a clippy run-tracker
archaeology (operator-driven). Empirical n=1, rich (the divergence + the exact lens-slip are both
quotable from the `.clippy/runs/` history). **Adherence-failure-driven, but the recurrence-reducing
fix is a framework/clippy sharpening** (the failure mode is structural search-blindness, not
laziness). Routing: a **clippy instance** lens (coding-flavored: "the same value is built by two
functions"); the underlying principle is the framework **Consumer-enumeration / basis rule** (root) —
so a *lens that operationalizes consumer-enumeration over CO-PRODUCERS of a shared-format key*, not
new doctrine. Sibling-routing of `provenance-at-handoff-lens` and `replacement-side-effect-behavior-parity`.

## The bug class
A logical value is **produced by two (or more) independently-named functions** that must emit
**byte-identical** strings because the value is later **compared for equality** at a shared sink (a
DB column, a dedup key, a JOIN/`EXISTS` predicate, a wire field). One producer's format is changed;
the other is not. Neither producer references the other, so a symbol-grep on the changed function
finds only its own call site (clean), and a token-grep on the *value name* sees the second producer's
module only as a **consumer** of the value — never as a co-producer bound by a format-parity
contract. The equality silently never holds.

## The failure (clippy / beat-the-books, confirmed)
`signal_id` is the autobet dedup key, built by **two** functions:
- `build_signal_id` (`services/autobet_pipeline/signal_id.py:169`) — the runner writes
  `autobet_bets`/`autobet_opportunities` with this. **Unit 26 (D2) extended it 7→10 components**
  (added `game_id_safe`, `tq`, `variant`) to fix real same-team/rematch collisions.
- `_build_autobet_signal_id` (`services/analysis/value_betting_pipeline.py:245`) — the Telegram EV+
  announce-suppress builds its key with this. **Still 7 components.**

The already-bet suppress (`get_announce_state_with_bet_check`) runs `EXISTS(autobet_bets WHERE
signal_id = <7-comp>)` against the stored `<10-comp>` → **never matches → already-bet opportunities
re-alert every cycle, indefinitely.** Prod-confirmed: `EXISTS(bet)` is FALSE for *every* announce-log
key; both example games re-alerted the same day while their bets sat under the longer keys. Blast
radius = **all** autobet signals since Unit 26 shipped.

## Why the rule already covers it (adherence failure, not a missing rule) — and where it slipped
Consumer-enumeration / the basis rule's true-unit basis require enumerating everything a contract
change touches. Unit 26's Coupled-change pass **did** surface `telegram_notifier.py` via
`grep -rn "signal_id"` — and reasoned it away (`...passes.md:15`, ratified as tracker `F18`):
> *"signal_id is an **opaque key** used in lookups/JOINs/indexing, never **parsed by position**. No
> consumer extracts sub-fields. Clean."*

That is the **right test for the wrong threat model.** It asked *"does any **consumer** parse
sub-fields?"* (no → safe — correct for a single-producer key). The actual risk was a second
**producer** whose output must byte-equal the changed one. A grep keyed on the token `signal_id`
cannot connect *"the string this function returns"* to *"the string the other function returns";* the
coupling lives in the **equality requirement between two functions' return values**, reachable by a
grep on neither name. The side-effect note sealed it (`tracker:78`): *"new signal_ids differ from
existing DB values → new rows coexist with old"* — framed as **old-rows-vs-new-rows within one
writer** (harmless, age out), not **reader-format ≠ writer-format across two builders** (fatal).

## The real failure-mode + the sharpening
This is the **co-producer sibling** of the shipped `structural-change-dependent-enumeration`
(`core.md §3.2.2`, which named non-reference-findable **dependent** forms incl. "producer/consumer")
and of `replacement-side-effect-behavior-parity` (grep the bodies, not the callers). The shared
meta-shape: **enumeration keyed on X misses Y because Y is unreachable by an X-grep.** Here X = the
changed producer's symbol / the value's token; Y = the **other producer** of the same shared-format
value.

- **Name the search-blind form.** When a change alters the **format/shape** of a value written to a
  **shared, equality-compared sink** (DB column, dedup key, JOIN/`EXISTS`/index predicate, wire
  field), the completeness obligation is to enumerate every **function that PRODUCES a value for
  that sink** — not only consumers of it.
- **Mechanical fire-point (the teeth, mirrors the side-effect-parity item's "grep the right
  target").** Don't grep the changed symbol; grep the **sink** for its writers: every site that
  `INSERT`/`UPDATE`s the column, sets the field, or builds the key. Each writer is a co-producer;
  for each, confirm its format matches post-change. Un-fakeable artifact = the writer-set + each
  one's format disposition.
- **Convergence falsification candidate.** For a shared-format key compared by equality: a
  `target-shape` candidate per co-producer — do all producers emit the same component structure?
  A producer whose format differs from the changed one = **falsified** (orchestrator-computed, no
  self-attest).
- **Structural cure (strongest — and the actual fix here).** Two parallel producers kept in parity
  by *discipline* are a standing liability; prefer **single source of truth**. The signal_id bug was
  *enabled* by Refactor #58 deferring the "delete the twin, collapse to one builder" cutover
  indefinitely (`signal_id.py:29-31` documents the plan: *"becomes the only signal_id builder"* —
  it never happened). The lens should flag a *known duplicated producer* as debt; the fix collapses
  to one producer (or has one read the other's stored output) so parity is structural, not willed.

## The near-miss (why "try harder" won't fix it)
**Unit 24 (D4)** sat **directly on the failing reader** and read its SQL line-by-line, yet missed it:
its `F6` inspected the signal_id format but validated only the **shared `_<provider>` suffix**
(identical in 7- and 10-comp) — the matching suffix masked the diverging prefix — then *extended the
broken `EXISTS` to `autobet_paper_bets` on the same mismatched key*, propagating the defect. A model
*looking right at the format* still missed a component-count divergence because it checked the
invariant tail. Structural blindness, not inattention.

## V-watch vs backlog (dogfood note)
Per `v-entry-is-post-ship-only`: this is a **backlog item** (a not-yet-implemented gap), not a
V-watch. A V-watch becomes appropriate *after* the sharpening ships — to watch whether the
co-producer enumeration reduces shared-key-format-drift recurrence (catcher: a future format change
to a shared, equality-compared key that leaves a second producer un-updated).

## Relates to
- `replacement-side-effect-behavior-parity` — **closest sibling** (same "enumeration aimed at the
  wrong target / grep the sink not the symbol" meta-shape + the same "name the search-blind form +
  the mechanical fire-point + a convergence candidate" treatment). Distinct trigger: that fires on a
  **delete/replace** (behaviors of removed code); this fires on a **format change to a shared key
  with multiple producers** (no deletion). If the maintainer prefers one item, these two could
  consolidate into a "**enumeration-target-blindness** (callers vs bodies vs co-producers)" cluster —
  kept separate here for the distinct trigger surface.
- `structural-change-dependent-enumeration` (**archived — shipped**, `core.md §3.2.2`): the
  dependents-clause precedent that already named "producer/consumer" as a search-blind form; this is
  the **co-producer parity** sub-case made explicit + given a mechanical fire-point.
- `provenance-at-handoff-lens` — sibling producer-grounding family, but **producer↔consumer
  semantics** (a value's meaning) vs this item's **producer↔producer format** (a key's shape). Same
  "distrust the name/docstring, ground at the producer" instinct, different seam.
- `framework-blindspot-class-analysis` (+ `design-decision-implication-depth-gaps`) — a new datapoint
  for the blind-spot-class catalog: *"saw the consumer (the grep surfaced telegram_notifier), didn't
  connect it as a co-producer."* Same reasoning-depth shape; homed separately for the distinct
  search-blindness mechanism + a clean sibling-of-shipped fix.
- `clippy-greenfield-tolerance` — sibling clippy-lens-quality item.
- Origin: beat-the-books `signal_id` 7-vs-10 dedup divergence (Unit 26 introduced; Unit 24 near-miss;
  Refactor #58 deferred the collapse) — traced through `.clippy/runs/` by the operator 2026-06-07.
