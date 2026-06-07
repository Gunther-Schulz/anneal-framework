# Run: clippy-write-side-boundary

- **Status:** PASSED (verify [ISSUES FOUND] → F1 fixed → operator-waived re-verify, proportionate for a cosmetic whitespace fix)
- **Phase:** verify
- **Mode:** interactive
- **Task summary:** Close the clippy write-side boundary gap (F29) — a producer emitting a non-authoritative value on a branch into an overwriting merge sink, clobbering a more-authoritative stored value — in clippy's lens set (`coding-clippy/spec/lens-set.md` → re-render `references/lenses.md`).

## Requirements record
**Operator verbatim:** "file but also lets handle it now" (re the beat-the-books Unit-31 F29 loopback transcript). Brief: `dev-notes/backlog/clippy-write-side-boundary-gap.md`.
- **R1** — Clippy's lens set catches the F29 write-side class (non-authoritative branch value written into an overwriting merge sink, clobbering a more-authoritative stored value) at **design/standardized-pass** time, not impl-review.
- **R2** — Faithful render: `lens-set.md` (source) → `references/lenses.md`, enforcement/form preserved.
- **R3** — **Additive-reflex respected**: the fix names what it REDUCES; prefer extend/scope-sharpen over a new lens unless a distinct axis is confirmed.
- **R4** — Acceptance: render-fidelity verify + skill-craft form + citation-firewall clean.

**Proposed solution (the transcript's):** "add a 12th lens `Destructive-merge-at-write`." Investigated as a premise, not locked — re-scoped to the Pareto option (D1) per R3.

---
## F-track
- **F1 [VERIFIED]** Silent-substitution-at-boundary is strictly READ-side, so F29's write-side falls through; Branch-coverage's offending branch is at an un-authored caller (out of authored scope); the co-producer/emitted-effect forms are different shapes (co-producers disagreeing / replacement-preserved effects, not one writer clobbering a prior write). basis: `coding-clippy/spec/lens-set.md:159` ("at every cross-boundary **read**") + `:173` (scope "cross-boundary data **read**") — located read, observable fact: the lens Question + Scope are read-only.

## D-track
- **D1 [VERIFIED]** **Extend `Silent-substitution-at-boundary` to BIDIRECTIONAL** (not a new lens). The lens's principle — *a non-authoritative value silently treated as authoritative* — and its direction-neutral name already span both directions; add the **write side**: at every cross-boundary **write into an overwriting merge sink** (`UPSERT … DO UPDATE SET col = EXCLUDED.col`, put/replace), does the producer emit a non-authoritative value (NULL/default/empty/stale) on **any** branch — including failure/empty branches at call sites the decision references but doesn't author — such that the merge **clobbers a more-authoritative stored value**? Fix shapes: value-preserving merge (`COALESCE(EXCLUDED.col, existing.col)`) or gate the write to the authoritative branch. **Scope addition:** fires at the merge/write site AND at every producer branch supplying the written value, incl referenced-but-unauthored call sites (this folds in the Branch-coverage scope-sharpen — no separate Branch-coverage edit). **Additive-reflex (R3):** REDUCES vs the proposed 12th lens — one existing lens extended, one principle, the read+write mirror unified; names what it cuts (a parallel new lens). basis: `lens-set.md:157-178` (the read-side lens to extend) + F1 + the §3.2.2 emitted-effect/co-producer already present (`:42-99`, distinct shapes → no overlap, so this is the genuinely-missing axis, not a dup). (b) shape: amend the lens's Question + Scope as a delta. (e) skill-craft fires at impl (the lens-form / one-coherent-question check) per `CLAUDE.md` Rule-corpus edits + the dispatch brief.
- **D2 [VERIFIED]** **Re-render `references/lenses.md`** Silent-substitution-at-boundary entry from the D1-edited `lens-set.md` (lenses.md renders FROM lens-set.md). Dependency: after D1. Acceptance: render-fidelity vs the edited source; firewall clean. basis: clippy `CLAUDE.md` (lens set lives in spec/, renders into plugin files); `references/lenses.md:130-151` is the current render of the read-only lens.

### Cycle 2 (convergence — intent-falsification; NOT clean)
- **F-b [VERIFIED — addressed by D2']** D2's render-target basis is wrong: cited `references/lenses.md:130-151`, but the Silent-substitution entry is at `plugin/skills/clippy/references/lenses.md:167-187` (`:130-151` = Thorough-fix/Target-locality) — stale pre-re-render line numbers. basis (cycle-2 intent artifact): `find coding-clippy -name lenses.md` → single hit; located read :167-187 = Silent-substitution (observable fact: cited range resolves to the wrong entry).
- **F-a [VERIFIED — surfaced → operator-ratified]** The one-coherent-question crux: bidirectional Silent-substitution (read=substitute-propagates / write=clobber-destroys differ in harm/fix/fire-site) risks overloading — defensible-as-extend (the lens already governs 5 heterogeneous sub-shapes under one question) but contestable. basis: D1 write-side Q vs `lens-set.md:159-172` read-side Q+sub-shapes. **RESOLVED:** operator declared bidirectionality a **core tenet** (2026-06-07) → extend (not a separate lens) confirmed; spawns the follow-up `bidirectional-lens-audit`.
- **F-c [VERIFIED — surfaced → ACTIONED: amends D1]** D1's write-side exemplars lean SQL-merge; the class is broader (cache last-writer-wins, idempotent-PUT/object-store, dict/map assignment, ORM `save()` nulling unset cols). Keep the question mechanism-general, SQL as one exemplar. basis: `clippy-write-side-boundary.md:22` (D1 exemplar set SQL-only).
- **F-d [VERIFIED — surfaced]** Scope-overlap with Branch-coverage (both range over the producer-branch-at-unauthored-caller site; distinct questions: is-branch-evidenced vs does-its-value-clobber-on-write) — acceptable; keep distinct in the render. basis: `lens-set.md:107-114` (Branch-coverage) vs D1 scope addition.
- **Mechanical falsification pass: SKIPPED cycle 2** — intent produced a D-delta (D2 basis falsified → D2'; D1 amended → D1' per F-c); mechanical would be stale (L1 intent-delta skip, `core.md §4.1.4`). Runs next cycle.

### Cycle 2 — design amendments
- **D1 [INVALIDATED]** (cycle 2) amended per F-c.
- **D1' [VERIFIED]** As D1, plus: the write-side question is **mechanism-general** — an *overwriting write into a stored sink* (SQL `UPSERT DO UPDATE`/`= EXCLUDED`, object-store/idempotent PUT, cache last-writer-wins set, in-memory dict/map assignment, ORM `save()`/`update()` that nulls unset columns), SQL as ONE exemplar, not the trigger. Render keeps it direction-and-mechanism-general (F-c) and question-distinct from Branch-coverage over the shared call-site scope (F-d). basis: F-c + F-d.
- **D2 [INVALIDATED]** (cycle 2) basis falsified by F-b.
- **D2' [VERIFIED]** As D2, corrected render target: `plugin/skills/clippy/references/lenses.md:167-187` (the Silent-substitution-at-boundary entry). basis: F-b's located read.

### Cycle 3 (CONVERGENCE — both passes clean) → [READY]
- **Convergence CLEAN:** intent-falsification CLEAN (`cycle-3.intent-falsification.md`, R1–R4 served, zero findings) + mechanical ALL-HOLD (`cycle-3.falsification.md`, D1'/D2' aggregate `holds`; target-existence + target-dependents; target-behavior [CONDITIONAL]/verify-discharged) + **zero D-track deltas**. Standardized pass vacuous-clean (no design delta this cycle).
- **[READY] supporting facts:** all findings terminal (F1 [VERIFIED]; F-a/F-c/F-d [VERIFIED — surfaced]; F-b [VERIFIED — addressed]); D1'/D2' [VERIFIED]; standardized set accounted for (cycles 1–3).
- **Fresh-session implementability: PASSED** — U1 extends the lens located at `lens-set.md:157-178` (confirmed read-only, cycle-3 mechanical) with the D1' write-side delta; U2 re-renders `lenses.md:167-187` (confirmed the Silent-substitution entry); the write-clobber axis is absent from the set (`rg` empty) so "extend" is grounded. Realization (lens prose) at impl.
- **Impl plan:** `clippy-write-side-boundary.impl-plan.md` — 2 units, sequential (U2←U1): U1 edit `spec/lens-set.md` (skill-craft-gated), U2 re-render `references/lenses.md`.

### implement + verify
- **U1 + U2 SHIPPED** (uncommitted working tree): Silent-substitution-at-boundary extended bidirectional in `coding-clippy/spec/lens-set.md` (U1, skill-craft PASS — one-coherent-question confirmed, Edit-as-Pareto, distinct from Branch-coverage) + re-rendered into `references/lenses.md` (U2, skill-craft PASS). Firewall clean both files.
- **VERIFY: [ISSUES FOUND] → resolved.** Isolated verify (opus): planned-vs-actual + R1–R4 + lenses all hold; ONE LOW finding **F1** (render line-wrap split `referenced-but-unauthored` → CommonMark mid-token space — a Lossy-render divergence).
- **F1 [VERIFIED — addressed]** Rewrapped: the token now sits intact on one line (`lens-set.md:197`, `references/lenses.md:205`); `rg 'referenced-but-$'` → none; firewall clean; only the 2 lens files changed. **Delta-verify WAIVED by operator** (proportionate — cosmetic whitespace, mechanically confirmed; "don't run verify again if that's all there was"). basis: `rg -n 'referenced-but-unauthored'` → 1 intact match per file + `git diff --stat` (2 files).
- **Cost note (operator-flagged):** the verify subagent used ~68k tokens for a one-lens change — fixed cost (fresh isolated context re-loads the full method `core.md`~17k + files), not change-size cost; aggravated by a fat brief (loaded full method vs just the changed entry+source+diff). Across the cycle: ~4 subagents × ~50–77k for a one-lens edit → a concrete `proportional-cycle-weight` datapoint (lean the falsification/verify briefs for small edits; lighter cycle weight).
- **RELEASE:** PENDING operator — `coding-clippy` 0.9.95→0.9.96 (commit the 2 lens files + version bump + push + `claude plugin update`). Surfaced, not auto-released.
