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
arc + a re-prioritization into the 6-tier order below; **re-groomed session 7** — slotted the
session-6/7 spawned items into the tiers, reinstantiation shipped+activated + self-render-urgency
resolved (both archived). 41 open.)

### ▶ Where we are + next steps (2026-06-04 session 7 — READ FIRST)

**Session 7 — `anneal-dev-model-tier-policy` SHIPPED (spec-only, release `3d03d0c`; archived).** The
blanket top-tier **dispatch model-tier floor**: every anneal-dev dispatch runs at the configured top
tier (value `anneal-dev.config/model-tier.md` = opus), downgrading forbidden; floor-not-guarantee
framing. Instance-level per foundation contract 3 (no framework touch — framework stays harness-agnostic,
mechanically confirmed). Its own anneal-dev run (method-kernel edit; kernel-independent verify =
skill-craft self-review + operator soundness on INV-3/F8).

- **Standout result:** the convergence cycle's **intent-falsification pass** (a session-6 addition the
  *running* plugin doesn't even carry yet) caught a real gap the 8 standardized lenses missed — the floor
  was *absent-by-default* in installed-elsewhere projects → drove the **D5 bootstrap flip**. Conformant-success
  for the session-6 intent-falsification work.
- **Soundness residual (operator accepted):** INV-3/F8 — the blanket pin runs verify on the *same tier as
  the actor*, foreclosing the cross-tier model-diversity lever; trade accepted for now (held open in
  `verify-model-diversity`).
- **Spawned:** `anneal-dev-self-render-urgency` (the render-cadence "stale-while-idle" rationale fails for
  the self-governing instance) · `cross-instance-precedent-discipline` (no forcing-function for sibling-instance
  prior art; the clippy precedent was found late). V-29 got an n≥1 data point (register focus = scope-shrink,
  not judgment-shrink).
- **Renamed:** `multivoter-verify-no-predicate-claims` → **`verify-model-diversity`** (multi-voting is DEAD;
  the intent-falsification pass SHIPPED; the live residual is model-diversity-for-verify, which collides with
  the model-tier floor — F8).

**▶ `anneal-dev-reinstantiation` SHIPPED + ACTIVATED (session 7, 2026-06-04).** The full
`instance-reinstantiation` render scoped to anneal-dev *itself*: re-rendered the plugin from the live spec
(intent-falsification pass + mechanical-rename, `[VERIFIED — surfaced]` disposition, requirements record +
coverage check, model-tier floor) across all 5 affected files; **verify PASSED** (separate-context
render-fidelity battery clean); released `02e7ee2` (step-4 discharge) + `5edf6cd`, pushed; `claude plugin
update` → **0.1.3 LIVE** (cache verified carrying the render; `/reload-plugins` swapped it in-session). The
running anneal-dev now carries its own method. Dogfood: the run used the very intent-falsification pass it
was rendering (grounded in live spec, not the stale loaded skill). Spawned:
`anneal-dev-plugin-dangling-anti-patterns-ref` (pre-existing dangling cite, low-sev).

**▶ `anneal-dev-self-render-urgency` RESOLVED + archived (session 7).** Not via faster renders — via
recognizing **re-grounding already does the job**: the project `CLAUDE.md` "Self-hosting" clause now makes
the **live co-located spec the source of truth** (the loaded plugin is a build artifact that may lag; live
spec governs on divergence). Plugin-freshness → **hygiene** on the existing batched cadence; the "urgency"
is gone. Self-hosting-only (a downstream anneal-dev has only its plugin → plugin IS its truth). Release
`e7542eb`. Net new machinery: zero.

**▶ NEXT-UP (DECIDED session 7 — do after a fresh `/clear`): two quick-wins, then open the
intent-falsification sweep fresh.**

1. **Quick-wins first** (close items, keep velocity): `anneal-dev-plugin-dangling-anti-patterns-ref`
   (one-line render fix — qualify the dangling `references/anti-patterns.md` cite as skill-craft's) +
   `validation-watch-entry-retrofit` (mechanical: active V-entries gain the watch-kind / catcher fields).
2. **Then `intent-falsification-soundness-sweep` — bounded FIRST PASS.** The retrospective audit of the
   enforcement floor (the prospective half — every future run carries the intent-falsification pass —
   shipped + went live this session). Risk-ordered first slice: the **3 hooks** (`commit-msg` discharge,
   `anneal-dev-run-gate`, `skill-craft-pre-edit`) + the **step-4 discharge machinery** — exactly where the
   n=1 seed (B1/B2: self-dischargeable enforcement + overclaimed gate) lived. Method per target:
   fresh-context, criteria-first intent-falsification — state the mechanism's intent, then attack whether
   it actually *binds* (self-dischargeable / overclaimed / operator-detection-dependent / false-comfort).
   **Single check, not multi-vote.** The sweep is an AUDIT → dispatch the passes directly (NOT an
   anneal-dev run); output = a triaged **fix-queue**; each confirmed finding then becomes its own
   anneal-dev cycle. Cap the pass; log what's left unswept. **Why ahead of F0:** it audits the floor every
   run leans on (incl. this session's); F0 only unblocks the idle tier-5 re-render. (F0 render-conventions
   — `instance-template-slot-scaffolding`, `glossary-binding-table-interface-completeness` — stay
   tier-2-next after.)

*(Session 6 history below.)*

### ▶ Where we are + next steps (2026-06-04 session 6 — superseded; history)

**Session 6 — two method-kernel anneal-dev runs SHIPPED (both spec-only; instance renders deferred to
the batch). The foundation-self-certification arc + its dogfooding consequence.**

1. **`foundation-invariants-register`** (release `35cc329`; item `foundation-self-certification-machinery`
   archived) — the anchor-gated **foundation-invariants register** (`dev-notes/foundation-invariants/`: 5
   externally-anchored kernel invariants + README) + the per-touched-invariant focusing artifact wired into
   the method-kernel-edit verify (`development-process.md` §2 / step-4) + the `Invariant-change-ratified`
   protection (`hooks/commit-msg`). Surfacer, not certifier; operator stays irreducible. Watch **V-29**
   (focus-payoff, WATCHING).
2. **`intent-falsification-convergence-pass`** (shipped this commit) — the **intent-falsification pass**
   (judgment-class design-vs-intent soundness check) in core anneal's convergence cycle (`core.md` §4.1.4) +
   the new **`[VERIFIED — surfaced]`** finding disposition + the artifact (`modules.md` §3.4.1) + glossary
   terms + persistence binding. A pure SURFACER (operator-irreducible for kernel edits; never self-certifies).
   **Validated by 4 recursive-dogfooding rounds — the pass run on its own design caught + fixed B/F/S-class
   soundness flaws** (the session's standout result).

**▶ NEXT-UP (operator-chosen, after /clear): `anneal-dev-model-tier-policy`.** anneal-dev work always uses
the top model tier (never cost-downgraded) — rule in `anneal-dev/spec`, value in `anneal-dev.config`. Its own
anneal-dev run (method-kernel edit). Self-contained: design sketch + home + relate in the item.

**Spawned this session (dogfooding + operator probes):** `framework-blindspot-class-analysis` (tier 6) ·
`intent-falsification-soundness-sweep` · `canonical-scenario-regression-suite` ·
`deferred-finding-owed-artifact-forcing-function` · `verify-model-diversity` reframed (the
intent-falsification kernel-candidate — now SHIPPED prospectively as run 2) · `loopback-root-cause-triage`
n≥4. Render-debt: both runs queue into `instance-reinstantiation`.

*(Session 5 history below.)*

### ▶ Where we are + next steps (2026-06-04 session 5 — superseded; history)

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

**▶ NEXT (operator-chosen, 2026-06-04): `foundation-self-certification-machinery`.** Lighten the
operator's soundness role on kernel edits (catch known-invariant breaks mechanically; the operator stays
irreducible). See that item's **"NEXT-UP" section** — start by settling the design forks WITH the operator
(decide-ahead), THEN run anneal-dev. (It edits `development-process.md` → the run-gate hook will require an
active run, so they compose.)

**Also open (from this session):**
- **Run B — `core-md-bloat-measure-then-cut`** (the deferred core/modules consolidation half: core↔modules §4.1.4/§3.4 dedup + glossary-indexes-core-bodies).
- **The render batch — `instance-reinstantiation`** now queues **3** source-deltas (the 3 runs above) for the clippy/daneel re-render.
- **`validation-watch-entry-retrofit`** (lazy: the 26 active V-entries gain the new kind/catcher fields).
- The **render-cadence policy** (framework runs ship spec-only) + the **interactive auto-cycle affordance** (`auto-battle-cadence-mode`, design resolved, not built).

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
  verifier · decompose judgment claims (across `verify-model-diversity`,
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
- **F7 — enforcement-fidelity gaps (session-6/7 dogfood):** `basis-recorded-query-fidelity` (the
  recorded basis-query isn't mechanically enforced, only conclusion-correctness is; n=1) ·
  `deferred-finding-owed-artifact-forcing-function` (a finding deferred to a to-be-authored
  validation-watch entry *owes* that entry; nothing forces it to exist) ·
  `validation-watch-entry-retrofit` (mechanical: the active V-entries gain the new watch-kind /
  catcher fields — a quick-win).

### 3 ▸ CLIPPY FIXES — instance-level corrections (root-at-clippy)
Sparse on purpose: most clippy-surfaced findings are framework-root (→ tier 2, fix-at-source).
- `clippy-greenfield-tolerance` — clippy `verify` assumes existing code; greenfield hardening.
- `anneal-dev-plugin-dangling-anti-patterns-ref` — anneal-dev's `tracker.md` render cites a dangling
  `references/anti-patterns.md` (skill-craft's); pre-existing, low-sev, one-line fix that rides the
  next anneal-dev render.

### 4 ▸ FRAMEWORK CHANGES — new disciplines / larger kernel additions (each = an anneal-dev cycle)
- **The convergent "carry rivals → exclude rivals" sharpenings** (from the literature runs; two
  independent sources point the same way):
  - *investigate-side* `multiple-working-hypotheses-investigate-design` — the genuine GAP; resolve the
    internal-rivals-vs-committed-recommendation tension first.
  - *verify-side* `verify-model-diversity` (reframed: model-diversity, not vote-count)
    + the criteria-first / exclusion-obligation / falsifiability-gate / different-model sharpenings
    (partly captured in `verify-vs-original-requirements`, tier 2 — the *fix* and the *change*
    converge; sequence them together).
- **anneal-dev method:** `anneal-dev-rerender-changeset-by-source-delta` ·
  `anneal-dev-extension-render-gate` (downgraded — D4 answered the core question) ·
  `anneal-dev-impl-skillcraft-gate` (NEW 2026-06-04 — dispatch *loads* but doesn't *invoke*
  skill-craft → the pre-edit gate blocks dispatched rule-corpus edits).
- **mode-mechanics / disciplines:** `auto-battle-cadence-mode` (interactive "auto-cycle to [READY],
  halt at the phase gate" affordance — direction resolved, not built; the thing we did by hand this
  session) · `cross-instance-precedent-discipline` (candidate — a forcing-function to check sibling
  instances for prior art; evaluate "earns a lens" vs "just investigate harder" first).

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
- **Framework blind-spot class analysis (high interest — generalizes the intent-falsification
  discovery):** `framework-blindspot-class-analysis` — proactively enumerate the CLASSES of
  verification blind spot the framework may have (one — judgment-class soundness — was just found
  by accident; others likely). Must use EXTERNAL lenses (the framework can't introspect its own
  blind spots — Gödel). Output feeds tier-4 changes + `intent-falsification-soundness-sweep`.
- **Retrospective audits (high-leverage; each generates a fix-queue, not a single edit):**
  `intent-falsification-soundness-sweep` — audit *already-shipped* enforcement (the `hooks/`, the
  step-4 discharge, the self-classified "structural enforcement" rules) for the self-certifying-form
  blind spot the intent-falsification pass was built to catch. The prospective half is DONE (every
  future run now carries the pass, live as of session 7); this is the retrospective cleanup. n=1 seed
  caught a 2-for-1 the mechanical pass confirmed clean past. **Strong candidate to promote out of
  tier 6** — it audits the floor every run leans on. · `canonical-scenario-regression-suite`
  (executable verification *for the method itself* — a regression net so a spec change can't silently
  break a known-good scenario).
- **Exploratory (no rush):** `impl-dispatch-workflow-substrate` · `anneal-adhoc-use-and-graduation` ·
  `planner-instance-exploration` (new instance) · `generalize-sharpening-skill` (cross-repo tooling).
