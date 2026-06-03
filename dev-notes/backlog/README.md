# Backlog — open items for the anneal-framework project

The carry-across-sessions list of framework work. **The folder IS the
index:** every open item is one file here, so `ls` shows the live backlog.
Closed items move to `archive/`. Per-item detail lives in each file; this
README is the **ordered** view (what to do, in what order).

## Convention (the process)

- **Relate before add — never blindly append.** Check a new item against
  the existing ones *first*: does it **fold into** one (same canonical
  referent → merge, don't duplicate)? Does it **inform** existing items, or
  do they **inform** it (→ revise the affected ones)? The backlog is a
  corpus too — it fragments if you just append.
- **One file per item, one naming scheme: `<slug>.md`.** Name it for what the
  item *is* (a stable identity), not its type or status.
- **Status lives in the file, not the name.** Each item's first lines state
  what it is, its status/stage, where deeper detail lives, and the next action.
- **When an item ships / closes:** `git mv` it into `archive/`.
- **Memory:** one pointer ([[project-framework-backlog]]) auto-loads and says
  "read `dev-notes/backlog/`." Update it only when the *structure* changes.

## Open items — ordered by execution

One ordered list (replaces the old category grouping). **Phases reflect
dependency order**, not priority within a phase. The arc: settle the *system*
→ settle the render *conventions* → do the *renders* → mop up independent
findings. (Last groomed 2026-06-03, after the spec-cleanup campaign merged to
`main`.)

### Near-done — stay open only for a live residual

- `framework-spec-cleanup` — the core.md §4 re-derivation + S3; **audit debt fully
  discharged** (runs 1+2, merged). Archives when its render-tail (`instance-reinstantiation`) lands.
- `contract1-depollution-cluster` — de-pollution complete; held open only on V-26
  (validation-watch) + the parked clippy render-debt.

### ⭐ STRATEGY — the next major effort (governs Phases A+B; its own fresh session)

- `corpus-flows-redesign` — **re-think all three corpus-work flows into one clear,
  contained system:** (1) fresh instantiation, (2) re-render existing instances,
  (3) dev on anneal itself — all routed through **anneal-dev** as the enforced
  de-facto channel; **includes the `anneal-dev`↔`anneal-framework` repo-merge
  question.** Decide this *before* the renders below — it sets how they're driven.

### Phase A — render-CONVENTION fixes (the rules; settle before re-rendering, or re-render twice)

- ✅ `harness-tool-runstate-unsourced` — **DONE** (merged `8b8a4ac`, 2026-06-03): a harness-general
  render-time note in instantiation-guide §2 sources the "not the harness's task-tools" disambiguation
  (decision: guide not spec — spec stays harness-clean). Archived. The 4 SKILL.md blocks re-render
  faithfully from it in Phase B.
- ✅ `cite-glossary-not-section-numbers` — **DONE** (merged `b56f7d8`, 2026-06-03): the
  §-number firewall rule + grep-check + 3 glossary headwords + glossary-as-interface naming.
  Archived. Residual (the binding-table interface completion) spun off, not a re-render blocker →
  `glossary-binding-table-interface-completeness` (Phase D / no-rush).
- `instance-template-slot-scaffolding` — the template doesn't scaffold the mechanism-slot
  placeholders; settle slot-as-file vs slot-as-section, then fix the guide/template.

### Phase B — re-instantiation (the big multi-run effort; anneal-dev first)

- `instance-reinstantiation` — **umbrella:** re-render the cleaned spec into the instances
  via anneal-dev (**anneal-dev first** → clippy → daneel → campaign-craft → bauleitplan),
  de-bloating the legacy-bloated ones with a from-scratch rewrite, render-fidelity-verified. Bundles:
  - `clippy-render-resync` — clippy's parked de-pollution vocab debt (c-safe/T1/T2/R1/R4; pre-dates §4).
  - `clippy-skill-de-bloat` — clippy `SKILL.md` structural fresh-rewrite (the "2nd anneal-dev dogfood").
  - `adoption-instance-settlement` — re-point each instance's CLAUDE.md seed; campaign-craft needs its source repo located first.

### Phase C — independent method findings, in THEMED BATCHES (not 11 separate runs)

These are small spec/method fixes. **Recommended approach (operator-preferred 2026-06-03): one
coherence-audit-driven campaign.** Run a **coherence audit** (practice 12 — and it's *due-ish*
anyway: cycles have accumulated since the last handoff `ac1856832b8712fda`) over the corpus to
surface fresh drift, and **fold the known findings below into that same cleanup**, resolved by
theme — one audit + a few themed anneal-dev runs, instead of picking items off one at a time.
**Caveat (still true):** the audit is a *floor not a gate*, the batching is a cost-saver not a
requirement — every item below is its own file (`ls` shows them), workable individually, in any
order, earlier than any audit if you want. The themes (the run-groupings within the campaign):

- **C1 — verify/impl discipline** (gaps in what verify/impl must check; all touch `core.md` §4.2/§4.3 + `development-process.md`): `verify-vs-original-requirements`, `behavior-change-test-impact-enumeration`, `impl-green-on-commit`.
- **C2 — dispatch / parallel-isolation mechanics** (the impl dispatch + worktree path): `dispatch-brief-one-source-of-truth`, `worktree-isolation-and-integration`, `anneal-dev-impl-checkpoint-vs-discharge-hook` (NEW 2026-06-03 — impl-Checkpoint mandates a per-unit commit, but the rule-corpus discharge hook needs verify+operator first; surfaced by the cite-glossary run).
- **C3 — under-enforced / fragmented disciplines** (soft-rule → structural; consolidate): `completeness-search-enforcement` (decide the open question first), `verified-integrity-consolidation`.
- **C4 — skill-craft / gate-hook small fixes**: `skill-craft-soft-load-pointer-discriminator` (skill-craft canonical), `skill-craft-pre-edit-hook-findings` (Findings 2 Bash-bypass + 4 spec-origin over-match).
- **Standalone:** `surface-non-task-observations` (a new channel — small, its own thing).
- **Feeds the strategy, not its own run:** `anneal-dev-extension-render-gate` — the "does a mechanical re-render warrant the skill-craft gate?" question is answered *within* `corpus-flows-redesign` (#3 enforcement).

### Phase D — instance-level / exploratory (no rush)

- `glossary-binding-table-interface-completeness` — (NEW 2026-06-03, the FB-3 residual) make the
  glossary cover the binding-table left-column technical terms too; not a re-render blocker.
- `clippy-greenfield-tolerance` — clippy's `verify` assumes existing code; instance-level greenfield hardening.
- `clippy-run-findings-dispatch-coupling` — open clippy-surfaced cycles (Cycle 2.5 + the coherence-audit deep-sweep of §4.4 / §5.1 / mode mechanics).
- `planner-instance-exploration` — build the planner instance + its framework findings (holds the `bindings.md` slot-collapse fork).
- `generalize-sharpening-skill` — extract the sharpening family (PBS-coupled) like `coherence-audit` was; cross-repo, low-priority.
