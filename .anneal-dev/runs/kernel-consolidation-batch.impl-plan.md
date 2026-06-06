# Impl plan — kernel-consolidation-batch

Units from the locked design (D1–D5; D7 deferred to Run B). **One container** (anneal-framework repo) —
no cross-repo parallelism. Two units, **sequential** (U2's reference updates + B's glossary removal depend
on U1's folder + README home existing).

- **U1 — validation-watch → folder** (dev-notes; NOT rule-corpus → no skill-craft gate, still dispatched).
  Restructure `dev-notes/validation-watch.md` → `dev-notes/validation-watch/`: `README.md` = the current
  preamble verbatim (purpose / n=1 / Entry lifecycle) **+ the B home** (canonical definitions of Production
  signal / Watch-entry lifecycle states / Load-bearing instance, which the preamble already carries);
  `V-N-<slug>.md` ×28 (one per entry, number = stable key); `archive/` with V-5 (the one RESOLVED) moved in.
  Add the archival convention to the README (RESOLVED → `git mv` to archive/, no stub). **First.** Scope:
  `dev-notes/validation-watch/` only. Contract: the folder structure + the B definitional home.
- **U2 — kernel reference + glossary/dev-process consolidation** (rule-corpus → **skill-craft gate**). After U1.
  - **validation-watch refs (D2):** file→folder at `development-process.md:99,:496`, `post-run-review.md:3,:165,:222`,
    `spec/glossary.md` (the validation-watch source-cites :376,:381,:382,:392,:396), `spec/README.md:64,:98`, `CLAUDE.md:61`.
  - **B (D4):** remove the 3 misfiled terms from `spec/glossary.md:374-403`; add a one-line pointer to the
    validation-watch home.
  - **A (D3):** `spec/glossary.md:456-467` → brief per-gap gloss + "full machinery: `development-process.md` practice 1";
    `spec/modules.md §4.5 :461-470` → drop the re-listed definitions, keep the practice-1 cross-ref.
  - **C (D5):** `development-process.md:177` edit-cycle definition stays canonical (sharpen to a clear gloss if
    needed); `spec/glossary.md:144` **Cycle** entry gains the one-line "edit cycle" disambiguation.
  Scope: `spec/glossary.md`, `spec/modules.md`, `development-process.md`, `post-run-review.md`, `spec/README.md`, `CLAUDE.md`. **No `core.md`.**

**Disjointness:** none needed — sequential (single container, U2 depends on U1). U1 is dev-notes-only; U2 is the
rule-corpus edit.

**Method-kernel note:** U2 touches `spec/glossary.md` + `development-process.md` → verify adds the
kernel-independent review (skill-craft form + operator soundness). U2 invokes skill-craft before its edit.

**Spec-only:** the clippy/daneel instance renders (F1 INSTANCE refs + the triage/term render dependents)
DEFER to the batch re-render (`instance-reinstantiation` Render-debt queue).
