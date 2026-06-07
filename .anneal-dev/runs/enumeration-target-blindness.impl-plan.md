# Impl plan — enumeration-target-blindness

Derived from the locked design (D1–D5, D7; D6 [CONDITIONAL]→[AUTO-ACCEPTED] at [READY]).
3 dispatch units. Run-level: Unit 1 sequential-first; Units 2 ∥ 3 parallel after Unit 1.
Spec-only release (instance/plugin renders are render-debt → `instance-reinstantiation`).

## Unit 1 — core.md (the canonical rule) — FIRST
Files: `spec/core.md` only.
- **§3.2.2 behaviors clause** (D3): extend `core.md:255-257` ("explicit enumeration of
  behaviors preserved or dropped") to name the **emitted-effect** form (a behavior the
  replaced artifact emits rather than returns — produced within its body, invisible to a
  reference-search) + the **method** (read the replaced artifact's body for effect-producing
  operations, not a reference-search of its callers) + the target-behavior falsification
  candidate (each emitted effect must have a successor; absence = falsified). Domain-general;
  do NOT coin "side-effect" (collision with §5.2(d), F9).
- **§3.2.2 dependents clause** (D4): extend `core.md:246-254` (two non-reference renderings)
  with a THIRD — the **co-producer**: when the amended artifact produces a value written to
  a shared site consumed by equality, enumerate every producer/writer of that site (method:
  search the site's writers, not the amended symbol's references); target-dependents
  candidate (a co-producer whose format diverges = falsified). MUST carry **(i) inline
  closed-set licensing** — the dependency resolves through the shared sink's format contract,
  mirroring the producer↔consumer inline licensing at `core.md:252-253` — and **(ii)
  target-role disambiguation** (target-as-consumer → enumerate its producer; target-as-
  producer → enumerate sibling producers of the shared sink).
- **§3.2.2 consolidation framing** (D5): present both under the shared principle — aim the
  enumeration at the right target (the body; the site's writers) — Edit-as-Pareto, no new
  section; keep the block cognitively palatable (NEW-1 / brevity discipline).
- **§5.2(e)** (D7): replace the leg-list paraphrase at `core.md:1123-1124` ("references +
  behaviors preserved/dropped") with a §3.2.2 pointer ("the §3.2.2 completeness enumeration").
- Briefed: load `foundations.md` + `tracker.md` + `phases/implement.md`; invoke skill-craft
  before the edit; write-time self-check (Lossy-render / Missed-dependents / Undefined-
  shorthand / Over-claimed-verification + change-set-vs-scope).

## Unit 2 — glossary.md Coupling-shape rendering — after Unit 1, ∥ Unit 3
Files: `spec/glossary.md` only.
- Add the **co-producer** as a third non-content-reference **target-dependents** rendering
  at `glossary.md:112-122` (beside path-hardcoder + producer↔consumer), pointer to §3.2.2,
  carrying the target-role disambiguation (D5). No fourth shape.

## Unit 3 — lens-set.md Missed-dependents form-list — after Unit 1, ∥ Unit 2
Files: `anneal-dev/spec/lens-set.md` only.
- Extend the seven-form list at `lens-set.md:106-119` to **eight** (add co-producer) +
  update "all seven"→"all eight … render the existing closed set (no fourth shape)" + a note
  that the behaviors leg's emitted-effect enumeration reads the replaced body (D5).

## Disjointness basis (Units 2 ∥ 3)
Unit 2 touches only `spec/glossary.md`; Unit 3 only `anneal-dev/spec/lens-set.md` — disjoint
files, no shared edit target (search-established). Both depend on Unit 1's realized §3.2.2
phrasing (they render it), so both sequence AFTER Unit 1; they are parallel to each other.
