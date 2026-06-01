# Backlog — carry-forward items for the anneal-framework project

The persistence system for things to remember across sessions. **The
folder IS the index:** each open item is one file here, so `ls` shows
the live backlog. Done items move to `archive/`.

## Convention (the process)

- **Relate before add — never blindly append.** Check a new item against
  the existing ones *first*: does it **fold into** one (same canonical
  referent → merge, don't duplicate)? Does it **inform** existing items,
  or do they **inform** it (→ revise the affected ones)? The backlog is a
  corpus too — it fragments if you just append. This is the
  coherence-audit's merge discipline applied to the backlog itself, and
  the same "relate-before-add" the anti-decay effort generalizes
  corpus-wide. FB-5 is the cautionary tale: a principle that fragmented
  across homes before anyone consolidated it.
- **One item per file.** Name `fb-N-<slug>.md` for findings, or
  `<slug>.md` for anything else to carry forward. Each file is either
  self-contained or a short stub pointing to a bigger dedicated doc.
- **Each item states:** what it is, status, where the detail lives (if
  elsewhere), and the next action.
- **When an item ships / closes:** `git mv` its file into `archive/`.
  The folder root is the live backlog; `archive/` is history.
- **Memory:** one pointer ([[project-framework-backlog]]) auto-loads and
  says "read `dev-notes/backlog/`." Update it only when the *structure*
  changes, not per item.
- **Big efforts** keep their own dedicated dev-note (too large for one
  backlog file); they're listed below as pointers, not duplicated here.

## Open findings (files in this folder)

- `fb-1-surface-non-task-observations.md` — no channel for what the
  agent notices outside the task (code observations + protocol-tensions).
- `fb-2-verify-vs-original-requirements.md` — verify checks the locked
  design, not the original ask.
- `fb-3-cite-glossary-not-section-numbers.md` — instance specs cite
  framework §-numbers, not glossary terms.
- `fb-4-clippy-greenfield-tolerance.md` — clippy's `verify` (and likely
  other bindings) assume existing code; instance-level greenfield
  hardening, low-priority.
- `fb-5-verified-integrity-consolidation.md` — consolidate the
  "[VERIFIED] claims more than was checked" family (Cycle 3 static +
  V-25 un-run + new sample-bias face) under one umbrella principle; a
  consolidation cycle.

## Deferred / in-flight efforts (detail in their own docs)

- **Anti-decay forcing functions** (skill-craft + dev-process —
  **foundational, recommended first**) → stop corpus structural decay
  (bloat / fragmentation / leakage) by forcing the anti-decay disciplines
  per-cycle. Outputs: SKILL.md de-bloat, FB-5 consolidation, a thorough
  coherence-audit. → `../anti-decay-forcing-functions.md`
- **Contract-1 de-pollution cluster** (3 cycles — high-value, adjacent to
  the audit above) → `../contract1-depollution-cluster.md`
- **Cycle 2.5 — bindings.md slot-collapse** → deferred to the planner
  derivation → `../clippy-run-findings-dispatch-coupling.md` +
  `../planner-instance-exploration.md` finding 3
- **Coherence-audit deep-sweep** (§4.4 / §5.1 / mode mechanics not yet
  swept) → `../clippy-run-findings-dispatch-coupling.md`
- **Planner instance build** → `../planner-instance-exploration.md`
