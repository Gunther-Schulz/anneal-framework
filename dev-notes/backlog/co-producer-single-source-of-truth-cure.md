# Single-source-of-truth cure for co-produced shared-key values (the structural fix, not the enumeration)

**Status:** OPEN — filed 2026-06-07 as the discharge of decision **D6** of the
`enumeration-target-blindness` anneal-dev run (tracker
`.anneal-dev/runs/enumeration-target-blindness.md`, D6/D6'). That run sharpened
`core.md §3.2.2` to **enumerate** co-producers of a shared equality-compared sink (the
completeness-claim teeth). D6 deliberately **excluded the structural cure** from §3.2.2 —
the basis rule governs enumeration-completeness, not refactoring prescription — and
promised to file it separately. This is that item. (Filing it discharges the run's
no-silent-deferral obligation; the intent-falsification pass flagged that an unfiled
promise re-creates the very Refactor-#58 deferral that enabled the original bug —
`enumeration-target-blindness.cycle-4` NEW-2 / INT-5.)

## The cure (design-quality heuristic, NOT a completeness rule)
When a logical value is **produced by two+ independently-named functions that must emit
byte-identical output** because a downstream consumer compares them by equality (a DB
column, a dedup key, a JOIN/`EXISTS`/index predicate, a wire field), parity-by-discipline
is a **standing liability**. The cure: prefer **single source of truth** — collapse to one
producer, or have one producer **read the other's stored output**, so format parity is
**structural, not willed**. The lens should flag a *known duplicated producer of a shared
equality-compared sink* as **debt**.

## Why it is distinct from the shipped §3.2.2 enumeration
- `§3.2.2` (shipped via `enumeration-target-blindness`) makes a *change* that touches a
  shared-sink producer **enumerate the sink's other writers + confirm format parity** —
  it catches the drift *at the moment of an edit*. That is a completeness-of-basis rule.
- **This item** is the *standing* fix: even with perfect enumeration each edit, two
  parallel producers held in parity by discipline will eventually drift; the structural
  cure removes the duplication so there is nothing to keep in parity. Enumeration is the
  detector; single-source-of-truth is the cure. Different contract (a design/refactor
  heuristic), so it does not belong in the §3.2.2 basis clause (D6 rationale).

## Origin evidence (the bug the cure would have prevented)
`co-producer-format-parity.md`: the `signal_id` dedup key was built by **two** functions
(`build_signal_id` 7→10 components; `_build_autobet_signal_id` still 7) → `EXISTS` never
matched → already-bet opportunities re-alert indefinitely. The duplication was *enabled* by
**Refactor #58** deferring the "delete the twin, collapse to one builder" cutover
indefinitely (`signal_id.py:29-31` documents the plan — *"becomes the only signal_id
builder"* — it never happened). The cure flags exactly that deferred-collapse as debt.

## Routing
A **clippy instance** lens / anti-pattern (coding-flavored: duplicated builders of a shared
key), design-quality class — NOT a framework basis rule. Sibling of `co-producer-format-parity`
(the enumeration half, now in `§3.2.2`). Land it in the clippy lens-set re-render (tier ⑥),
beside the `co-producer` enumeration form the §3.2.2 sharpening renders.

## Relates to
- `co-producer-format-parity` — **the enumeration sibling** (now shipped to `§3.2.2` via
  `enumeration-target-blindness`); this is the structural-cure half D6 split out.
- `deferred-removal-cross-run-obligation-ledger` — the **orthogonal** forcing-function axis
  (a cross-run obligation to DELETE a deferred twin); Refactor #58 is the shared root, but
  that item tracks the *removal-obligation* mechanism, this one the *single-producer design
  preference*. Cross-link, keep separate.
- `framework-blindspot-class-analysis` / `replacement-side-effect-behavior-parity` — the
  blind-spot cluster; this is the design-quality (not search-blindness) member.
- `instance-reinstantiation` — render-debt umbrella (lands in the clippy re-render).
