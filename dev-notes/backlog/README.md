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
findings. (Last groomed 2026-06-04 — session-4 research arc added on top; the
framework track below is unchanged from session 3 and still pending.)

### ▶ Where we are + next steps (2026-06-04 session 4 — READ FIRST)

Session 4 executed the **operator-flagged research thread** end-to-end: **four `deep-research`
runs** (placement / design-first-vs-act-first / process-literature / verify-techniques), all
adversarially verified, verdicts + raw reports captured (`dev-notes/research/*.raw.json`; commits
`e2ef6f2` + `4da569d` on `main`, **unpushed**). Headline: **no superior framework found
(kill-switch OFF)**; anneal is **strongly validated** by canonical methodology literature; and
**design-first is unrefuted-but-UNPROVEN** — the deciding experiment has never been run by anyone,
and anneal's instances are the testbed to run it. (Concurrency lesson: 3 runs at once overloaded the
schema-verifier subagents → **run deep-research one at a time.**)

**Run verdicts (detail in each item):**
- `anneal-placement-and-improvement-research` — DONE. Process-discipline layer; **APF = a peer (not
  unique), no superior**; APF deep-read lessons folded.
- `design-first-vs-act-first-research` — DONE. No superior (kill-switch off); design-first
  unrefuted-AND-unproven; act-first dominance ≈ cheap-oracle benchmark artifact.
- `process-literature-for-anneal-research` — DONE. Canonical RE/methodology **validates** anneal
  (basis rule = Zave-Jackson "designation"; complete-state = S,K⊢R; loopback = Platt recycle).
- `verify-techniques-research` — DONE. **Criteria-first verify = standout adoptable**; quorum
  marginal (model-diversity > vote-count).

**⭐ Candidate KERNEL sharpenings surfaced — findings, NOT yet edits; each needs an anneal-dev cycle.**
Two literatures converge on a *"carry rivals → exclude rivals"* posture:
- *Investigate-side:* `multiple-working-hypotheses-investigate-design` (the genuine GAP — resolve the
  internal-rivals-vs-committed-recommendation tension first).
- *Verify-side:* criteria-first verify · exclusion-obligation · falsifiability-gate · different-model
  verifier · decompose judgment claims (across `verify-techniques-research`,
  `multivoter-verify-no-predicate-claims`, `verify-vs-original-requirements`).

**The proof path (operator's "prove me right or wrong"):** `anneal-empirical-validation-experiment`
(v0 — falsifiable design-first-vs-act-first A/B on instances, expensive-verification regime) +
`anneal-reliability-measurement` (token-first + grounding-ratio metrics).

**Next decisions (operator's call):**
1. **Pursue one kernel sharpening via anneal-dev** — *criteria-first verify* is lowest-cost /
   highest-confidence (peer-reviewed; attacks rubber-stamping; convergent across two runs).
2. **Design the MVE experiment** (`anneal-empirical-validation-experiment`).
3. **Resume the framework track** (unchanged, session-3 block below) — coherence-audit (cadence-due)
   → re-renders.
4. **Push** the two unpushed commits when ready.

### Where we are + ordered next steps (2026-06-03 session 3 — prior handoff; framework track still pending)

Session 3 landed the **keystone `corpus-flows-redesign`** anneal-dev run (verify PASSED +
operator-soundness PASSED; release-record `4e77837`; **archived**). It decided AND implemented
the redesign: **one channel (anneal-dev), three entry-conditions** — new-instantiation
(derivation = a PRE-CHANNEL design step) / dev-on-anneal / re-render (= the render-tail, never
separate); the **anneal-dev↔anneal-framework MERGE** (anneal-dev now co-located at
`anneal-framework/anneal-dev/`, subtree-add `d5ae00d`, clean 0.1.2 carried); enforcement = a
structural floor (the two hooks, **no new routing gate**, D4); canonical routing home =
`development-process.md` (D8); a new-user **bootstrapping anchor** in README (D11). Folded items
resolved: `anneal-dev-impl-checkpoint-vs-discharge-hook` (→ D7/D12, archived);
`anneal-dev-extension-render-gate` (→ D4 answered the question; **downgraded-open** on a residual).
Run ledger: `.anneal-dev/runs/corpus-flows-redesign.md` (gitignored).

**Dogfooding yield — 5 method-kernel findings filed (for future anneal-dev runs):**
`structural-change-dependent-enumeration` (**n=2, highest-leverage**: Missed-dependents misses
non-content-reference dependent classes + the `[CONDITIONAL]`-falsification-exemption — the
shared root of BOTH this run's loopbacks), `loopback-root-cause-triage` (bake the root-cause
triage in vs operator-prompt), `release-commit-formation-from-checkpoints`,
`instructional-files-streamline` (operator-raised clarity pass), `commit-msg-hook-packaging-overmatch`
(the commit-msg hook gates packaging manifests + disagrees with the pre-edit hook).

**Release — ✅ DONE + verified live (all on remote).** anneal-framework `main` pushed to origin.
**C1b install re-pointed**: anneal-framework is now the marketplace host (root manifest →
`./anneal-dev/plugin`); the install switched to `anneal-dev@anneal-framework` → the merged clean
0.1.2 (D12 present; firewall-clean — 0 framework §-citations vs the old 0.1.1's 5); old
`@anneal-dev` install + marketplace removed; `/reload-plugins` confirmed the running session
resolved the merged render — **F7 fully resolved**. **C1c**: standalone `anneal-dev` repo
tombstoned (pushed) + **archived** on GitHub (read-only). Cosmetic leftover only: the orphaned
`~/.claude/plugins/cache/anneal-dev/anneal-dev/0.1.1` dir (harmless, prunable).

**Ordered next steps:**
1. **`instance-template-slot-scaffolding`** — the last Phase-A convention; now unblocked (the
   redesign settled instantiation routing — derivation is pre-channel, guided by
   instantiation-guide + the template).
2. **Domain-instance re-renders** (Phase B `instance-reinstantiation`): clippy (heavy — de-bloat +
   render-resync) → daneel → campaign-craft → bauleitplan. anneal-dev's own render is now merged-in;
   drivable through the merged anneal-dev + the source-delta method. Idle (drift ~0) → low urgency.
3. **Phase C — method-findings campaign** (coherence-audit-driven): folds in the 5 NEW findings
   above (structural-change-dependent + loopback-root-cause-triage are the high-value method-kernel
   fixes) alongside the prior C-cluster.
4. **Phase D** — instance-level / exploratory. Lowest priority.

**Ordering note (decide at pickup):** a **coherence-audit is cadence-due** (practice 12 + session-3's
heavy cycle count) and is the home for the framework-spec **bloat/tightness** question — `core.md`
(~7.2k words / 976 lines) is the weight; the call was **no de-bloat *rewrite*** (anneal-dev is clean
spec-rendered lineage), **measure-then-cut via the audit's Bloat lens** instead, aimed at the shared
framework spec. Strong case to **elevate the coherence-audit ahead of the re-renders** (clean the
corpus before re-rendering instances *from* it — the same "settle conventions before renders" logic
that ordered the phases). vs. the as-ordered `instance-template-slot-scaffolding` first.

**Operator-flagged research thread — ✅ EXECUTED in session 4 (2026-06-04); see the READ-FIRST block
at top.** Four deep-research runs done, verdicts captured; the measurement leg continues via
`anneal-reliability-measurement` + `anneal-empirical-validation-experiment`.

### Near-done — stay open only for a live residual

- `framework-spec-cleanup` — the core.md §4 re-derivation + S3; **audit debt fully
  discharged** (runs 1+2, merged). Archives when its render-tail (`instance-reinstantiation`) lands.
- `contract1-depollution-cluster` — de-pollution complete; held open only on V-26
  (validation-watch) + the parked clippy render-debt.

### ⭐ STRATEGY — ✅ DONE (session 3, archived)

- `corpus-flows-redesign` — **DONE** (release-record `4e77837`; archived to `archive/`).
  Decided + implemented: one channel (anneal-dev), three entry-conditions; the
  anneal-dev↔anneal-framework merge; enforcement floor; canonical routing home; bootstrapping
  anchor. See the READ-FIRST block above. The renders below (Phase B) are now unblocked.

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

**Session-4 additions (literature-backed candidate kernel sharpenings — fold into this campaign):**
the verify-side cluster (criteria-first verify · exclusion-obligation · falsifiability-gate ·
different-model verifier · decompose judgment claims — across `verify-techniques-research`,
`multivoter-verify-no-predicate-claims`, `verify-vs-original-requirements`) + the investigate-side
`multiple-working-hypotheses-investigate-design`. See the READ-FIRST block for the convergence.

These are small spec/method fixes. **Recommended approach (operator-preferred 2026-06-03): one
coherence-audit-driven campaign.** Run a **coherence audit** (practice 12 — and it's *due-ish*
anyway: cycles have accumulated since the last handoff `ac1856832b8712fda`) over the corpus to
surface fresh drift, and **fold the known findings below into that same cleanup**, resolved by
theme — one audit + a few themed anneal-dev runs, instead of picking items off one at a time.
**Caveat (still true):** the audit is a *floor not a gate*, the batching is a cost-saver not a
requirement — every item below is its own file (`ls` shows them), workable individually, in any
order, earlier than any audit if you want. The themes (the run-groupings within the campaign):

- **C1 — verify/impl discipline** (gaps in what verify/impl must check; all touch `core.md` §4.2/§4.3 + `development-process.md`): `verify-vs-original-requirements`, `behavior-change-test-impact-enumeration`, `impl-green-on-commit`.
- **C2 — dispatch / parallel-isolation mechanics** (the impl dispatch + worktree path): `dispatch-brief-one-source-of-truth`, `worktree-isolation-and-integration`.
- **C3 — under-enforced / fragmented disciplines** (soft-rule → structural; consolidate): `completeness-search-enforcement` (decide the open question first), `verified-integrity-consolidation`.
- **C4 — skill-craft / gate-hook small fixes**: `skill-craft-soft-load-pointer-discriminator` (skill-craft canonical), `skill-craft-pre-edit-hook-findings` (Findings 2 Bash-bypass + 4 spec-origin over-match).
- **Standalone:** `surface-non-task-observations` (a new channel — small, its own thing).
- **Feeds the strategy, not its own run:** `anneal-dev-extension-render-gate` — the "does a mechanical re-render warrant the skill-craft gate?" question is answered *within* `corpus-flows-redesign` (#3 enforcement); `anneal-dev-impl-checkpoint-vs-discharge-hook` (NEW 2026-06-03) — anneal-dev's impl-Checkpoint per-unit-commit vs the dev-process rule-corpus discharge hook, reconciled within the same redesign (#3 enforcement).

### Phase D — instance-level / exploratory (no rush)

- `impl-dispatch-workflow-substrate` — (NEW session 4) could clippy's impl-dispatch run on the
  Workflow substrate? Verdict: not the whole run; defensible for the impl phase only; no change now.
- `anneal-adhoc-use-and-graduation` — (NEW session 4) ad-hoc anneal use + graduation to an instance;
  codify in the guide before building any skill.
- `glossary-binding-table-interface-completeness` — (NEW 2026-06-03, the FB-3 residual) make the
  glossary cover the binding-table left-column technical terms too; not a re-render blocker.
- `clippy-greenfield-tolerance` — clippy's `verify` assumes existing code; instance-level greenfield hardening.
- `clippy-run-findings-dispatch-coupling` — open clippy-surfaced cycles (Cycle 2.5 + the coherence-audit deep-sweep of §4.4 / §5.1 / mode mechanics).
- `planner-instance-exploration` — build the planner instance + its framework findings (holds the `bindings.md` slot-collapse fork).
- `generalize-sharpening-skill` — extract the sharpening family (PBS-coupled) like `coherence-audit` was; cross-repo, low-priority.
