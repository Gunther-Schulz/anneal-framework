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

## Open items

Two parts: the **READ-FIRST block** (current state + next decisions) and **the ordered backlog**
(6 tiers, batched by theme). `ls` is the full index. (Last groomed 2026-06-04 — session-4 research
arc + a re-prioritization into the 6-tier order below; in the same grooming: 4 research runs
archived, the re-render bundle merged into `instance-reinstantiation`. 32 open.)

### ▶ Where we are + next steps (2026-06-04 session 5 — READ FIRST)

**Session 5 — three method-kernel anneal-dev runs SHIPPED (all spec-only; instance renders deferred to
the batch) + a new enforcement hook. Dogfooding validated: runs 2 & 3 came out of using anneal-dev on
itself.**

1. **`verify-vs-original-requirements`** (release `1d93e58`) — verify now checks the locked design's
   coverage of a captured **requirements record** (intent-correct channel beside planned-vs-actual).
   Honest residual V-28 (never-captured requirement), WATCHING.
2. **`kernel-consolidation-batch`** (release `e6abcc8` + folder `d008afe`) — `validation-watch.md` → a
   **folder** (file-per-entry + README + `archive/`); the 3 misfiled glossary terms relocated; the
   render/spec/adherence-gap triage consolidated to one home (practice 1); "edit cycle" disambiguated.
3. **`validation-watch-lifecycle-fix`** (release `78be6e8` + `0aa04e3`) — the **opportunity-exercised**
   closing rule (a watch closes when the failure's *opportunity* arose and the fix handled it — caught,
   or produced-clean; pure non-occurrence never closes), the **correctness-watch / quality-watch** split,
   n=1 justified, and the **archive-check** (recurrence/regression net + n=1 safety hatch).

**New: `hooks/anneal-dev-run-gate.py` (project-local `.claude/settings.json`).** Blocks Edit/Write to the
kernel source (`spec/*.md`, `foundation.md`, `development-process.md`, `post-run-review.md`,
`instantiation-guide.md`, `anneal-dev/spec/*`) unless an anneal-dev run is `IN-PROGRESS` — i.e. **spec
work must go through anneal-dev** (now enforced at edit-time, not just at commit). Bypass:
`touch .anneal-dev/allow-adhoc-kernel-edit` (15-min self-healing TTL, non-silent). **Needs operator
approval (project hook) to activate next session.**

**Open / next (from this session):**
- **Run B — `core-md-bloat-measure-then-cut`** (the deferred core/modules consolidation half: core↔modules §4.1.4/§3.4 dedup + glossary-indexes-core-bodies).
- **The render batch — `instance-reinstantiation`** now queues **3** source-deltas (the 3 runs above) for the clippy/daneel re-render.
- **`validation-watch-entry-retrofit`** (lazy: the 26 active V-entries gain the new kind/catcher fields).
- **`foundation-self-certification-machinery`** (the soundness-machinery idea) + the **render-cadence policy** (framework runs ship spec-only) + the **interactive auto-cycle affordance** (`auto-battle-cadence-mode`, design resolved, not built).

**Session 4 (prior — the operator-flagged research thread):**

Session 4 executed the **operator-flagged research thread** end-to-end: **four `deep-research`
runs** (placement / design-first-vs-act-first / process-literature / verify-techniques), all
adversarially verified, verdicts + raw reports captured (`dev-notes/research/*.raw.json`; commits
`e2ef6f2` + `4da569d` on `main`). Headline: **no superior framework found (kill-switch OFF)**;
anneal is **strongly validated** by canonical methodology literature; and **design-first is
unrefuted-but-UNPROVEN** — the deciding experiment has never been run by anyone, and anneal's
instances are the testbed to run it. (Concurrency lesson: 3 runs at once overloaded the
schema-verifier subagents → **run deep-research one at a time.**) The 4 run-items are **archived**
(verdicts summarized below; raw in `dev-notes/research/`).

**Run verdicts (now in `archive/`):**
- placement — Process-discipline layer; **APF = a peer (not unique), no superior**; APF lessons folded.
- design-first-vs-act-first — No superior (kill-switch off); design-first unrefuted-AND-unproven;
  act-first dominance ≈ cheap-oracle benchmark artifact.
- process-literature — Canonical RE/methodology **validates** anneal (basis rule = Zave-Jackson
  "designation"; complete-state = S,K⊢R; loopback = Platt recycle).
- verify-techniques — **Criteria-first verify = standout adoptable**; quorum marginal
  (model-diversity > vote-count).

**⭐ Candidate KERNEL sharpenings surfaced — findings, NOT yet edits; each needs an anneal-dev cycle.**
Two literatures converge on a *"carry rivals → exclude rivals"* posture (see tier 4 + the F1 verify
batch):
- *Investigate-side:* `multiple-working-hypotheses-investigate-design` (the genuine GAP — resolve the
  internal-rivals-vs-committed-recommendation tension first).
- *Verify-side:* criteria-first verify · exclusion-obligation · falsifiability-gate · different-model
  verifier · decompose judgment claims (across `multivoter-verify-no-predicate-claims`,
  `verify-vs-original-requirements`).

**The proof path (operator's "prove me right or wrong"):** `anneal-empirical-validation-experiment`
(v0 — falsifiable design-first-vs-act-first A/B on instances, expensive-verification regime) +
`anneal-reliability-measurement` (token-first + grounding-ratio metrics). In tier 6 *only* because
they're meta (not framework/clippy fix/change) — high interest, not low value.

**Next decisions (operator's call):**
1. **Pursue one kernel sharpening via anneal-dev** — *criteria-first verify* is lowest-cost /
   highest-confidence (peer-reviewed; attacks rubber-stamping; convergent across two runs).
2. **Design the MVE experiment** (`anneal-empirical-validation-experiment`).
3. **Resume the framework track** (tiers 2 + 5 below) — the coherence-audit-driven framework fixes,
   then the re-render.

**⚙ Render-cadence policy (operator-decided 2026-06-04).** Framework-change anneal-dev runs (tiers
2 + 4) ship **spec-only** — they edit the kernel and do **NOT** render into instances per-run. Renders
batch **once** into tier-5 `instance-reinstantiation`, which now carries a **render-debt queue**: each
spec-only run appends its source-delta there, and the batch renders the accumulated delta into every
instance in one pass (method: `anneal-dev-rerender-changeset-by-source-delta`). This operationalizes
the tier rationale below ("*or you render twice*") at the **run** level — and matches the framework's
own decoupled model (`render-and-open-diff` fires post-verify, never inside a spec-change run's verify).
First applicant: the `verify-vs-original-requirements` run **SHIPPED 2026-06-04** (spec-only release
`1d93e58`, archived); its per-instance renders (U2/U3/U4) deferred to the batch (queued in
`instance-reinstantiation`). Instances stay transiently stale — tracked, low-urgency while idle (drift ~0).

### Session history (context, not work)

- **Session 3 (2026-06-03):** landed the keystone `corpus-flows-redesign` (one channel = anneal-dev;
  three entry-conditions; the anneal-dev↔anneal-framework merge; enforcement floor) + the live
  release (F7 resolved). Archived (release-record `4e77837`). Surfaced 5 method-kernel findings (now
  in the framework tiers below). **The old Phase A–D structure is superseded by the tiers below.**
- Phase-A render-conventions already DONE + archived: `harness-tool-runstate-unsourced` (`8b8a4ac`),
  `cite-glossary-not-section-numbers` (`b56f7d8`).

## The ordered backlog (2026-06-04 re-prioritization)

Order = **near-done → framework fixes → clippy fixes → framework changes → clippy changes → rest.**
Rationale: finish the almost-done; then *fix* (close gaps in existing behavior) before *change* (add
new); and **framework before clippy at each tier** — clippy renders *from* the framework, so fix /
change at the source first (practice 1) or you render twice. Level = **root (fix-at-source)**, not
where it surfaced. Within tiers, items are **batched by theme** (resolve a batch in one campaign/run,
not one-at-a-time). `ls` remains the full index; every item is workable individually, in any order.

### 1 ▸ NEAR-DONE
**Finish-now:** none open. (`skill-craft-pre-edit-hook-findings` **CLOSED + archived 2026-06-04** —
F4 hook spec-origin reminder scoped to anneal-instance renders [sibling-`spec/` detection, verified];
F2 `mv`/`cp` Bash-bypass accepted as a known limitation; F3 residual filed →
`anneal-dev-impl-skillcraft-gate`, now in tier 4.)

**Auto-closing — NO action; each archives when its dependency lands (do not try to "work" these):**
- `framework-spec-cleanup` → archives when `instance-reinstantiation` (tier 5) lands.
- `contract1-depollution-cluster` → archives when validation-watch **V-26** resolves (needs a built
  non-code instance) + the parked render-debt (now folded into `instance-reinstantiation`).
- `clippy-run-findings-dispatch-coupling` → archives when the coherence-audit deep-sweep (tier 2 —
  §4.4 / §5.1 / mode mechanics) lands + Cycle 2.5 (deferred into `planner-instance-exploration`).
  (NOTE: the 2026-06-04 cadence audit was kernel-wide / on-demand-fleshing — it did NOT target this
  specific §4.4/§5.1/mode-mechanics deep-sweep; this tail remains open.)

### 2 ▸ FRAMEWORK FIXES — close gaps in the existing kernel / dev-process (root-at-framework)
**Vehicle: the coherence-audit-driven campaign — audit ✅ RAN 2026-06-04** (handoff
`ac39b6ab6d5d929cd`; cadence baseline reset from `ac1856832b8712fda`). Verdict: kernel structurally
sound, keystone coherent, no domain-leakage; load-bearing-lens (1+8+9) finding count = 5. Findings
captured → the F-batches below (F1 confirmations) + the new `kernel-consolidation-glossary-hygiene`
(cluster: triage-3-homes · dev-terms-in-glossary · "edit cycle" gloss · `core.md` §4=52% bloat with 2
measured movable points). The **`core.md` bloat question** is now *measured* (no de-bloat rewrite —
the 2 movable points live in that item). Fixes are separate anneal-dev cycles (the audit was the
floor). **F0 render-conventions gate the tier-5 re-renders — do them first.**
- **F0 — render-convention (gate tier 5):** `instance-template-slot-scaffolding` (settle slot-as-file
  vs slot-as-section, then fix guide/template) · `glossary-binding-table-interface-completeness`.
- **F1 — verify/impl discipline gaps** (`core.md` §4.2/§4.3 + `development-process.md`):
  `verify-vs-original-requirements` (✅ **SHIPPED 2026-06-04**, spec-only `1d93e58`, archived — render
  debt queued in `instance-reinstantiation`) · `behavior-change-test-impact-enumeration` ·
  `impl-green-on-commit` (✅ audit-confirmed spec-silent L7-a).
- **F2 — structural / dependency enumeration** (dogfooding-surfaced; highest-leverage):
  `structural-change-dependent-enumeration` (n=2) · `loopback-root-cause-triage`.
- **F3 — under-enforced / fragmented disciplines** (soft-rule → structural; consolidate):
  `completeness-search-enforcement` (decide its open question first) · `verified-integrity-consolidation`
  · `surface-non-task-observations`. **✅ SHIPPED 2026-06-04** (run `kernel-consolidation-batch`, release
  `e6abcc8`/`d008afe`): `validation-watch-entry-archival` (validation-watch → folder, archived) +
  `kernel-consolidation-glossary-hygiene` A/B/C (triage-one-home, glossary-vocab relocate, edit-cycle
  disambiguation, archived). **Remaining:** `core-md-bloat-measure-then-cut` (Run B — the core/modules
  half of the consolidation, split out; core.md §4.1.4↔modules §3.4 dedup + glossary-indexes-core-bodies).
- **F4 — dispatch / parallel-isolation mechanics** (root framework §4.2 + render; surfaced via clippy):
  `dispatch-brief-one-source-of-truth` · `worktree-isolation-and-integration` (mixed-level: also
  harness; placed here as fix-at-source).
- **F5 — dev-process / release machinery:** `release-commit-formation-from-checkpoints` ·
  `commit-msg-hook-packaging-overmatch` · `instructional-files-streamline`.
- **F6 — skill-craft / hooks:** `skill-craft-soft-load-pointer-discriminator` (+ the hook-findings
  residual in tier 1).

### 3 ▸ CLIPPY FIXES — instance-level corrections (root-at-clippy)
Sparse on purpose: most clippy-surfaced findings are framework-root (→ tier 2, fix-at-source).
- `clippy-greenfield-tolerance` — clippy `verify` assumes existing code; greenfield hardening.

### 4 ▸ FRAMEWORK CHANGES — new disciplines / larger kernel additions (each = an anneal-dev cycle)
- **The convergent "carry rivals → exclude rivals" sharpenings** (from the literature runs; two
  independent sources point the same way):
  - *investigate-side* `multiple-working-hypotheses-investigate-design` — the genuine GAP; resolve the
    internal-rivals-vs-committed-recommendation tension first.
  - *verify-side* `multivoter-verify-no-predicate-claims` (reframed: model-diversity, not vote-count)
    + the criteria-first / exclusion-obligation / falsifiability-gate / different-model sharpenings
    (partly captured in `verify-vs-original-requirements`, tier 2 — the *fix* and the *change*
    converge; sequence them together).
- **anneal-dev method:** `anneal-dev-rerender-changeset-by-source-delta` ·
  `anneal-dev-extension-render-gate` (downgraded — D4 answered the core question) ·
  `anneal-dev-impl-skillcraft-gate` (NEW 2026-06-04 — dispatch *loads* but doesn't *invoke*
  skill-craft → the pre-edit gate blocks dispatched rule-corpus edits).

### 5 ▸ CLIPPY / INSTANCE CHANGES — the big re-render (gated by F0 above)
- `instance-reinstantiation` — **umbrella** (now incl. the 3 folded bundles: render-resync, SKILL.md
  de-bloat, CLAUDE.md seed re-point): re-render the cleaned spec into the instances via anneal-dev
  (anneal-dev DONE → clippy [heavy] → daneel → campaign-craft → bauleitplan), de-bloating the
  legacy-bloated ones, render-fidelity-verified. Idle instances (drift ~0) → low urgency.

### 6 ▸ REST — meta / exploratory / new-instance (doesn't fit the fix/change axis)
- **Operator-flagged proof thread (high interest, NOT low value):**
  `anneal-empirical-validation-experiment` (v0 — the falsifiable design-first-vs-act-first A/B) +
  `anneal-reliability-measurement` (token-first + grounding-ratio). *(Mild disagreement with "rest":
  these are your "prove me right or wrong" thread — here only because they're meta, not
  framework/clippy fix/change. Promote if you want to act.)*
- **Exploratory (no rush):** `impl-dispatch-workflow-substrate` · `anneal-adhoc-use-and-graduation` ·
  `planner-instance-exploration` (new instance) · `generalize-sharpening-skill` (cross-repo tooling).
