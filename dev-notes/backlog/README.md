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

Three parts: the **READ-FIRST block** (current state + next decisions), the **▶ Campaign map**
(the execution view — what runs together as one anneal-dev cycle, in what order), and **the
ordered backlog** (6 tiers, batched by theme — retained for per-item detail + the
fix-before-change rationale). `ls` is the full index. (Last groomed 2026-06-04 — session-4 research
arc + a re-prioritization into the 6-tier order below; re-groomed session 7 — slotted the
session-6/7 spawned items into the tiers, reinstantiation shipped+activated + self-render-urgency
resolved; **session 8 (2026-06-05)** — the two quick-wins + V-15 archived, the sweep ran both passes
+ keystone Move-1 partially shipped, items filed (`method-kernel-soundness-verdict-locus`,
`foundation-register-intent-falsification-anchors`; *continued:* `convergence-sequencing-enforcement`
after the convergence-pass sequencing gap + skill-craft v1.0.58 L3 fix + L1 `f74b145` shipped;
*then-continued:* `ready-machinery-self-attestation` (promoted from sweep) + `instance-domain-invariant-register`
(new architectural surface from a cross-session clippy-bug analysis) + V-30 watch (form-not-binding
class-recurrence) filed, + `instance-reinstantiation` extended with a capability-by-instance matrix
+ clippy semantic-render call-out; **then** `anneal-dev-evaluation-discipline` filed —
render skill-craft v1.0.61's Tier 1/2 (triggering + behaviour-delta signature) into
anneal-dev-the-plugin; **and** Option-C re-tiering: `canonical-scenario-regression-suite`
promoted tier 6 → tier 4 (per-edit method-level Tier-2 measurement); proof-thread items
stay in tier 6 with the v1.0.61 framing note; **then Move 1 of the session-strategy plan executed**:
tier-6 archive sweep — `impl-dispatch-workflow-substrate` archived (work-of-deciding already done),
`framework-blindspot-class-analysis` promoted tier 6 → tier 4 (empirically validated by this session's
dispatch-witness manifest discovery); **and** Move-2 of `intent-falsification-soundness-sweep` broadened
from tactical FQ-patch to "dispatch-witness manifest as §3.1 first-class instrument" framing — same
backlog count, sharper item); **then the session-strategy re-assessment landed the ▶ Campaign map** —
the 44 items grouped into **6 coherent drain campaigns + 1 deferred + a meta bucket** (the rate fix:
drain clusters as one cycle each, not one item at a time — see ▶ Campaign map below), and
`proportional-cycle-weight` filed (⑦ stub; no-silent-deferral); **then campaign ② SHIPPED**
(run `campaign2-completeness-rigor`, spec-only release) — 5 items archived, `verify-model-diversity`
dropped-but-open (fork ε), V-31 watch filed, render-debt queued to ⑥. 40 open.)

### ▶ Campaign map (2026-06-05 — the execution view; READ FIRST)

The rate fix: **stop draining one item per cycle.** The 45 open items group into **6 coherent drain
campaigns** (each = one anneal-dev cycle, weight called per-item in-loop) + **1 deferred** + a **meta
bucket** (handled deliberately, never campaign-drained). This is the master ordering; the 6-tier
section below is retained for per-item detail + the fix-before-change rationale. Folder stays flat —
a campaign is a *view*, not item identity, so no per-campaign folders; `ls` is still the index.

**Order:** ~~②~~ ✅ → ③ → ⑤ → ④a → ④b → ①-light → ①-heavy → ⑥ (last; gated). ⑦ practiced-not-run throughout.
**(② SHIPPED 2026-06-05 — next up: ③.)**

- **① Sweep finish — soundness & binding** *(active workstream; split by weight)*
  - *light (drain):* `intent-falsification-soundness-sweep` Move-1 tail (honest-relabel; the parked
    run `move1-tail-honest-relabel`) + Moves 3/4/5 · `convergence-sequencing-enforcement` (rides ⑥)
  - *heavy (deliberate — the dispatch-witness manifest, re-scoped on its OWN merits, not the rate push):*
    manifest = sweep Move-2 · `method-kernel-soundness-verdict-locus` · `ready-machinery-self-attestation`
    · `foundation-register-intent-falsification-anchors`
- **② Verify / impl / investigate rigor — ✅ SHIPPED 2026-06-05** (run `campaign2-completeness-rigor`,
  spec-only release; 5 items archived: `structural-change-dependent-enumeration` (D1/D1.1) ·
  `behavior-change-test-impact-enumeration` (D2.1) · `multiple-working-hypotheses-investigate-design` (D4.1) ·
  `loopback-root-cause-triage` (D5) · `impl-green-on-commit` (D6). `verify-model-diversity` **dropped-not-shipped**
  per fork ε — stays open (held option). Residuals: F-R4b closed; F-R5a → V-31 watch. Render-debt → ⑥.)
- **③ Under-enforced disciplines → structural + core de-dup:** `completeness-search-enforcement` ·
  `verified-integrity-consolidation` · `surface-non-task-observations` · `basis-recorded-query-fidelity`
  · `deferred-finding-owed-artifact-forcing-function` · `core-md-bloat-measure-then-cut`
- **④a Dispatch / parallel-isolation:** `dispatch-brief-one-source-of-truth` · `worktree-isolation-and-integration`
- **④b Release machinery + hooks:** `release-commit-formation-from-checkpoints` ·
  `commit-msg-hook-packaging-overmatch` · `instructional-files-streamline` ·
  `skill-craft-soft-load-pointer-discriminator`
- **⑤ anneal-dev method & evaluation:** `anneal-dev-rerender-changeset-by-source-delta` ·
  `anneal-dev-extension-render-gate` · `anneal-dev-impl-skillcraft-gate` · `anneal-dev-evaluation-discipline`
  · `canonical-scenario-regression-suite`
- **⑥ Render conventions + the big re-render** *(LAST — gated; batches the accumulated spec deltas from
  ①–⑤):* `instance-template-slot-scaffolding` · `glossary-binding-table-interface-completeness` ·
  `instance-reinstantiation` (umbrella) · `instance-domain-invariant-register` · `clippy-greenfield-tolerance`
  · *auto-closers fall out here:* `framework-spec-cleanup`, `contract1-depollution-cluster`,
  `clippy-run-findings-dispatch-coupling`
- **⑦ Rate machinery — DEFERRED (practice first, formalize only if proven):** `auto-battle-cadence-mode` ·
  `cross-instance-precedent-discipline` · `proportional-cycle-weight` (thin stub). Not run as a cycle; the
  *practice* (operator calls cycle-weight + auto-battles non-kernel items) runs throughout.
- **Meta / proof-thread / exploratory (deliberate, never campaign-drained):**
  `anneal-empirical-validation-experiment` · `anneal-reliability-measurement` ·
  `framework-blindspot-class-analysis` · `anneal-adhoc-use-and-graduation` · `planner-instance-exploration`
  · `generalize-sharpening-skill`

**Coverage:** all 45 items placed (44 prior + `proportional-cycle-weight`); campaign ② SHIPPED 2026-06-05
(5 archived) → **40 open**. Nothing dropped.

### ▶ Where we are + next steps (2026-06-05 session 8 — READ FIRST)

**⏵ Session 8 *continued* (2026-06-05, later) — sequencing-enforcement gap found + skill-craft L3 fix
shipped; L1 anneal-dev fix in progress; the Move-1-tail run PARKED.** While running the Move-1 tail
(FQ-5 hook relabel + dev-process:438), the orchestrator ran the convergence cycle's two falsification
passes **in parallel** instead of sequenced (intent-first, mechanical-only-if-clean — `core.md §4.1.4`);
the **operator caught it**. Root-caused across levels → new item **`convergence-sequencing-enforcement`**:
- **L3 (skill-craft) SHIPPED v1.0.58** (`9771523`, pin 1.0.57→1.0.58 installed): the missing authoring
  discipline for conditionally-dependent *independently-dispatchable* steps (encode the dependency in the
  dependent's input + cite it) + the enforcement-register **salience** fix (proportionality elevated to the
  Layer-2 intro; new "Scope precedes default" principle; 12th review-checklist item "Salience / reading order").
- **L1 (anneal-dev kernel) SHIPPED `f74b145`** (run `l1-convergence-pass-sequencing`, operator step-4-approved):
  `core.md §4.1.4` + `modules.md §3.3/§3.4` — mechanical pass's input carries this-cycle's intent-clean verdict
  + artifact cites it + coverage-check clause (v) rejects a mismatch + prose names the structural bind. **The
  convergence cycle's own intent pass caught a carry-forward legitimacy hole → D7 removed the carry-forward
  optimization** (intent runs every convergence cycle). Render-follow queued to `instance-reinstantiation` (ALL
  instances; not behavior-preserving). `convergence-sequencing-enforcement` now L3+L1 shipped (archives when the
  render batch carries L1's delta).
- **⏸ PARKED — the `move1-tail-honest-relabel` anneal-dev run** (tracker `IN-PROGRESS`, `.anneal-dev/runs/`).
  Stopped mid-investigate-design at **cycle 2**: design locked (D1-D4 [VERIFIED] — FQ-5 hook PASS-line relabel
  + dev-process:438 "un-fakeable evidence" relabel + defer-FQ-B), convergence cycle NOT yet run. **Resume:**
  re-invoke anneal-dev (resumes from the tracker); only the convergence cycle → [READY] → implement → verify
  remain. No timeline set. (Tail of the sweep's Root-Move-1, beside the shipped keystone `819e84e`.)

**Session 8 — the `intent-falsification-soundness-sweep` RAN (both passes) + its keystone Root-Move-1
PARTIALLY SHIPPED.** The session-7 NEXT-UP executed end-to-end: the two quick-wins, then the sweep, then
the first fix.

1. **Two quick-wins SHIPPED + archived.** `anneal-dev-plugin-dangling-anti-patterns-ref` (one-line render
   fix, `26ac662`) — and its **step-4 discharge became the live seed probe** that opened the sweep
   (`1ae472f`). `validation-watch-entry-retrofit` (`5c187ee`) — the active V-entries gained
   watch-kind/catcher fields; **V-15 archived** in the same pass.
2. **`intent-falsification-soundness-sweep` — FIRST + SECOND PASS DONE (8 targets; `cd75248` + `1023f5a`).**
   First pass: the 3 hooks (commit-msg / run-gate / skill-craft-pre-edit) + step-4 design. Second: the
   structural-enforcement practices + the **§3.1 keystone** + the falsification machinery + the
   intent-falsification pass *itself* (the recursion). **Convergent verdict:** enforcement certifies **form**
   (a string is present), not **binding** (the verification happened) — BUT the **foundation is SOUND**
   (operator-irreducible gate + strong-surfacers); the defect is **localized OVERCLAIM** (surfacers sold as
   binding gates). The ~25 granular FQs **reduce to 5 root moves** (in the item). **⚠ Self-catch:** the sweep
   found **V-26's archival *earlier this session* was a circular error** (spec-closure can't certify
   spec-correctness) → **reversed; V-26 restored WATCHING.** Only **scope-item-2** (shipped run artifacts)
   remains unswept.
3. **Root-Move-1 (THE KEYSTONE) — PARTIALLY SHIPPED `819e84e`.** The honest **bind-vs-surface relabel**:
   `spec/core.md` §3.1 (producer-independence bind test + F-B operator-detection fence) +
   `development-process.md` practices 10/11/12 + step-4 + `glossary.md` + `foundation.md` +
   `instantiation-guide.md`. A method-kernel anneal-dev run (`move1-s3.1-honest-relabel`), operator
   step-4-approved; render-follow queued to the render-debt batch (D7). **Still in Move-1 scope, NOT yet done**
   (separate sites/cycles, noted in the item): the commit-msg hook's green-✓ output relabel (FQ-5) · the
   falsification "holds" labels (FQ-B·pass7) · the `development-process.md:438` "un-fakeable evidence"
   reconcile (`c5adcbb`).

**Spawned this session:** `method-kernel-soundness-verdict-locus` (NEW — the [READY]-vs-step-4 split: *which*
operator soundness verdict binds *where* for a kernel edit; surfaced by running move-1, finding F-B) ·
`foundation-register-intent-falsification-anchors` (NEW — external-anchor source-map for the register). New
sweep target logged: the **[READY] / fresh-session-implementability machinery** (the readiness verdict is
orchestrator-self-attested; move-1's cycle-2 self-PASS under-detected, the fresh-context convergence cycle
caught the real refinements). `auto-battle-cadence-mode` got **dogfood datapoint 2** — the move-1 run was
driven by "auto-cycle until (n)", validating the (b) affordance (halt-at-[READY], menu-persistence, mid-cycle
interjection all held).

*(2026-06-05: the items below are folded into the ▶ Campaign map above — sweep = campaign ①, F0/tier-5 =
⑥, etc. Ordering now lives in the map; these blocks are retained for per-item detail.)*

**▶ NEXT-UP (the sweep is now the active workstream): finish Root-Move-1's residual sites, then Root-Moves 2–5
(each its own anneal-dev cycle; the queue lives in `intent-falsification-soundness-sweep`).**
1. **Close Move-1's tail** — FQ-5 (commit-msg green-✓ relabel) + FQ-B·pass7 (falsification "holds" labels) +
   dev-process:438 — all the same honest-relabel concept, deferred from `819e84e` to avoid widening that
   release.
2. **Then Root-Moves 2–5.** **Move-2 [ARCHITECTURAL FORK] dispatch provenance** — the one lever that converts
   surfacers→binding; **needs the operator's "bind-harder vs honest-relabel" decision + a harness-capability
   check** (can it witness spawns?) before it runs. **Move-3** carry-every-caveat-to-its-point-of-use.
   **Move-4** cheap external checks (verdict-form parsing FQ-1 / mechanical-N/A validation FQ-2). **Move-5**
   falsification-enum completeness (**the root of the V-26 reversal**). Plus the **Bash-bypass
   reconsideration** (promote from "accepted" — it nullifies every hook fix).

*(Session 7 history below.)*

### ▶ Where we are + next steps (2026-06-04 session 7 — superseded; history)

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
**(2026-06-05: the ▶ Campaign map above is now the execution grouping — these tiers are retained for
per-item detail + the fix-before-change / framework-before-clippy rationale, which the campaigns respect.)**

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
- **method evaluation (per-edit discipline; renders skill-craft v1.0.61's Tier 2 at the method level):**
  `canonical-scenario-regression-suite` — promoted from tier 6 2026-06-05. Executable verification
  *for the method itself*: a regression net so a spec change can't silently break a known-good
  scenario. Per-edit cadence (every spec change runs it) — Tier-2-shaped behaviour-delta signature
  measurement at the method level, sibling to `anneal-dev-evaluation-discipline` (which renders
  Tier 1/2 at the **plugin** level). Composes with V-30 closing rule (provides the empirical
  per-edit input the watch tracks).
- **blind-spot enumeration (proactive, not by-accident):**
  `framework-blindspot-class-analysis` — promoted from tier 6 2026-06-05.
  Empirically validated this session: the dispatch-witness manifest discovery (sweep
  Move-2, broadened to a §3.1 first-class instrument) is exactly one such blind-spot
  class found by accident — confirming the item's premise that enumeration-instead-of-
  accident is right. Must use EXTERNAL lenses (framework can't introspect its own
  blind spots — Gödel). Output feeds tier-4 changes + `intent-falsification-soundness-sweep`.
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
  framework/clippy fix/change. Promote if you want to act.)* **2026-06-05 framing update** (per
  skill-craft v1.0.61's evaluation discipline + the C-option re-tiering decision): these are
  **Tier-3 isolated-grade shape** at the framework level — one-shot validation that anneal-the-method
  is itself sound, distinct from the per-edit regression net (`canonical-scenario-regression-suite`,
  now in tier 4). Kept here as proof-thread items, not under-valued. Compose with V-30
  (`form-not-binding-class-recurrence`): the A/B's outcome would be one of V-30's data points.
- (*`framework-blindspot-class-analysis` was previously listed here; **promoted to tier 4** 2026-06-05
  — empirically validated by this session's dispatch-witness discovery; the item's premise that
  enumeration-instead-of-accident is right is now confirmed. See tier 4.*)
- **Retrospective audits (high-leverage; each generates a fix-queue, not a single edit):**
  `intent-falsification-soundness-sweep` — audit *already-shipped* enforcement (the `hooks/`, the
  step-4 discharge, the self-classified "structural enforcement" rules) for the self-certifying-form
  blind spot the intent-falsification pass was built to catch. The prospective half is DONE (every
  future run now carries the pass, live as of session 7); this is the retrospective cleanup. n=1 seed
  caught a 2-for-1 the mechanical pass confirmed clean past. **Strong candidate to promote out of
  tier 6** — it audits the floor every run leans on. (*`canonical-scenario-regression-suite` was
  previously listed here; **promoted to tier 4** 2026-06-05 — per-edit cadence + Tier-2-shaped
  measurement discipline. See tier 4.*)
- **Exploratory (no rush):** `anneal-adhoc-use-and-graduation` · `planner-instance-exploration`
  (new instance) · `generalize-sharpening-skill` (cross-repo tooling).
  (*`impl-dispatch-workflow-substrate` was previously listed here; **archived 2026-06-05** — its own
  status was already "no change recommended now; captured so it isn't re-derived"; the work-of-deciding
  was done. Decision preserved in `archive/`.*)
