# framework-gap-receipt — impl plan

Derived from the locked design (D1–D11). **1 dispatch unit**, run-level **sequential**
(single file → no parallelism). Disjointness basis: the entire change lands in ONE file
(`development-process.md`); a single in-place unit has no concurrency to make disjoint, so it
runs against the operator's work product **in place** under the Integrity check (not separate-copy).

## Unit 1 — Add practice 13 + update the intro enumeration (development-process.md)
- **Dependencies:** first (no predecessor).
- **Parallelism:** sequential (sole unit; same-file edits).
- **Implements:** D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11 (the whole design — one coherent practice).
- **Scope (development-process.md):**
  - (a) **Insert practice 13 "Periodic framework-gap receipt"** after practice 12 (`development-process.md:486-555`),
    before "## The release loop" (`:556`). Content from the locked design:
    - Defining sentence for "framework-gap receipt" (D10, define-in-place — no glossary entry).
    - **Invocation (D2):** operator-invoked, optional, at the framework-review cadence; NOT a mechanical/per-run
      trigger; not a per-run obligation.
    - **Mechanism (D3):** an evidence-bearing **by-class tally** over an instance's persisted falsification-pass
      records (primary source — clippy `.passes.md`; anneal-dev `.falsification.md` + `.intent-falsification.md`;
      instance-defined locator, examples only) — per class: count + cited located instances + recurrence flag.
      The tracker's existing status-history is consulted ONLY for the [VERIFIED]-position pairing (D8), never the
      bare flip. Class-LABEL = a weak artifact (judgment), stability via the separate checker (D6).
    - **Pass-type split as router by landed type (D4):** §3.4 mechanical `falsified` line (enumerable →
      lens-or-re-sequence) vs §3.4.1 `[VERIFIED — surfaced]` residual (→ framework-gap, almost never a lens);
      intent-routed-mechanical reconciled via the cross-artifact join.
    - **Routing discriminator + SG3 (D5):** look-FOR → lens; STRUCTURE-of-looking → framework; else → neither
      (default). Recurrence → re-sequence/strengthen EXISTING structure by default; a new lens needs
      novelty+generality, justification forced (guards Additive-reflex / lens-crowding).
    - **The four safeguards (D8/SG1, D6/SG2, D5/SG3, D2+D3/SG4)** stated load-bearing; SG4 reconciliation
      (reads existing run-records, adds no per-run field).
    - **Operator-binds, surface-only (D6):** AI first-judges each routing (cited discriminator-test + evidence),
      operator second-judges at review; routing NEVER auto-applied. **Dispatch to fresh context (D9).**
    - **Caught-side scope (D7):** routes only what a falsification pass (mechanical OR intent) caught; missed
      side → cross-reference `self-review-missed-side` (the per-run missed-side review). No register dependency.
    - **Practice-8 classification:** structural enforcement (the evidence-bearing tally + the SG3 forced
      justification) + the operator-binds surface (mirrors practices 10/11/12).
  - (b) **Update the intro machinery-enumeration (D11)** at `development-process.md:66-68` — add the
    framework-gap receipt alongside "the coherence-audit cadence" (its structural sibling).
- **Honors contracts:** Leakage (instance-locator generic); Bloat (cross-reference practice 11 / additive-reflex
  / lens-crowding rather than restate); Undefined-shorthand (single defining sentence); Integrate-don't-insert
  (placement after practice 12, weight proportional).
- **Briefing:** load anneal-dev `references/foundations.md` + `references/tracker.md` + `phases/implement.md`;
  **invoke skill-craft via the Skill tool BEFORE the edit** (practice 5 gate); write-time self-check against the
  design using the write-time lenses (Lossy-render N/A — not rendered; Missed-dependents — the intro enumeration;
  Undefined-shorthand; Over-claimed-verification) + change-set-vs-listed-scope; return the fixed-shape ledger.
