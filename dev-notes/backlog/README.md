# Backlog — open items for the anneal-framework project

The carry-across-sessions list of framework work. **The folder IS the
index:** every open item is one file here, so `ls` shows the live backlog.
Closed items move to `archive/`.

## Convention (the process)

- **Relate before add — never blindly append.** Check a new item against
  the existing ones *first*: does it **fold into** one (same canonical
  referent → merge, don't duplicate)? Does it **inform** existing items, or
  do they **inform** it (→ revise the affected ones)? The backlog is a
  corpus too — it fragments if you just append. This is the coherence-audit's
  merge discipline applied to the backlog itself. The verified-integrity
  consolidation is the cautionary tale: a principle that fragmented across
  homes before anyone consolidated it.
- **One file per item, one naming scheme: `<slug>.md`.** Name it for what the
  item *is* (a stable identity), not its type. There's no finding/effort
  prefix — that split is a size/stage difference, not a kind, and stage
  changes (a finding grows into a designed effort) without the file's
  identity changing.
- **Status lives in the file, not the name.** Each item's first lines state
  what it is, its status/stage, where deeper detail lives, and the next
  action. A small item is a short file; a big one (with its own design
  surface) is a long file — same folder, same scheme.
- **When an item ships / closes:** `git mv` it into `archive/`. The folder
  root is the live backlog; `archive/` is history.
- **Memory:** one pointer ([[project-framework-backlog]]) auto-loads and says
  "read `dev-notes/backlog/`." Update it only when the *structure* changes,
  not per item.

## Open items (`ls` = this list)

**Sorted by where the fix lands — framework-core leads; instance work follows.**
An item's group is set by *where its fix lands*, not where it was noticed: a
framework gap surfaced during a clippy run is framework work; a render owed to
clippy/daneel after a framework edit is instance-settlement — framework's
downstream tail, not a rival workstream. (Filenames stay as the item's stable
identity per the convention above; this framework/instance axis is a *category*,
so it lives here in the index, not in the names.)

### Framework-core (leads)

- `framework-spec-cleanup.md` — **THE NEXT MAJOR EFFORT (2026-06-02).** Re-derive
  the chaotic `core.md` (978 ln) cleanly: **re-derive-and-reconcile** (top-down from
  primitives → compare → reconcile), driven through anneal-dev (drive +
  kernel-independent verify) — **NOT** incremental patching. **Mapping pass DONE**
  (coherence-audit `ac1856832b8712fda`; debt-checklist in the item). **Next run:
  re-derive `core.md`'s phase pipeline (§4) from primitives.** Method-kernel;
  FOUNDATIONAL; multi-session.
- `framework-dev-as-anneal.md` — **the active effort; decision LOCKED**
  (reframed-A, 2026-06-01): make framework-dev a real anneal instance.
  **Steps 1–5 DONE (2026-06-02).** Build + validate complete: pass-1/2 derivation
  → core de-pollution → skeleton render (`anneal-dev` repo `abf5290`,
  separate-context verify + skill-craft review PASS) → **step-5 dogfood PASSED**
  (drove `daneel-cycle-b-sync` through anneal-dev end-to-end, verify [PASSED],
  shipped daneel `d85cff3`). **anneal-dev runs as a real instance.** **Adoption
  IMPLEMENTED 2026-06-02** (→ `dev-process-adoption.md`) — shadow-copy method
  retired surgically; bootstrap rule refined to *drive, don't self-certify*.
  Package DONE (`anneal-dev-packaging.md`: anneal-dev `0.1.1` installed + active).
  **Next major effort → `framework-spec-cleanup.md`.** V-27 has its n=1
  ceremony-cost seed; four flow-back questions resolved →
  `archive/anneal-dev-framework-flowback.md`.
- `dev-process-adoption.md` — **IMPLEMENTED + COMMITTED 2026-06-02 (B1, surgical; `19dc1d8`).** Retired `development-process.md`'s shadow-copy *method* (reframed to
  "everything runs through anneal-dev"; only P2 + the three-levels prose thinned —
  the rest is genuine framework-dev machinery that stayed). Bootstrap rule refined
  to *drive, don't self-certify*; Decision-1 reversed (triage stays in P1). Spawned
  `anneal-dev-packaging.md` + `adoption-instance-settlement.md`; elevated
  `skill-craft-pre-edit-hook-findings.md` Finding 3.
- `contract1-depollution-cluster.md` — de-code-ify domain leaks in the agnostic
  core. **COMPLETE (2026-06-02):** full sweep a/b/c-safe/T1/T2+T3 (`3a2245b` …
  `c634ebf`) + a whole-corpus coherence-audit (handoff `a3a2adda5508d9cdf`,
  2 findings fixed `8bfa20b`). Core is now domain-independent at the mechanism
  level. **Deferred (not blocking):** c-parked completeness (V-26) + parked
  clippy render-debt ([[clippy-render-resync]]). **Head →
  `framework-dev-as-anneal` step 4.** (Keep open until V-26 + render-debt close.)
- `verified-integrity-consolidation.md` — consolidate the "[VERIFIED] claims
  more than was checked" family (Cycle 3 static + V-25 un-run + sample-bias)
  under one umbrella principle; a consolidation cycle.
- `surface-non-task-observations.md` — no channel for what the agent notices
  outside the task (code observations + protocol tensions).
- `verify-vs-original-requirements.md` — verify checks the locked design, not
  the original ask.
- `cite-glossary-not-section-numbers.md` — instance specs cite framework
  §-numbers, not glossary terms.
- `instance-template-slot-scaffolding.md` — Cycle-a finding: the
  instance-template doesn't scaffold placeholder sections for the mechanism
  slots (persistence, isolation), despite the guide's "placeholder per slot"
  claim. Slot-as-file vs slot-as-section to settle.
- `skill-craft-pre-edit-hook-findings.md` — the practice-5 gate hook. Finding 1
  (over-broad path) DONE; **Finding 3 RE-GROUNDED 2026-06-02 → MOOT as a hook bug**
  (re-confirmed empirically: the gate IS satisfiable from a subagent; the harness
  transcript shape changed; residual reframed → `anneal-dev-impl-skillcraft-gate.md`);
  Findings 2 (Bash-bypass) + 4 (spec-origin over-match) open.
- `harness-tool-runstate-unsourced.md` — step-5 finding: the rendered instance
  `SKILL.md` (clippy + anneal-dev, verbatim) tells the AI not to use harness
  task-tools for run-state, but that half has no spec origin (contract-2 drift).
  Corpus-wide; lean fix = an instantiation-guide render-time note.
- `skill-craft-soft-load-pointer-discriminator.md` — small skill-craft canonical
  edit: the Soft-load-pointer anti-pattern doesn't discriminate a provenance
  citation (inline content) from a load-bearing pointer → a false-positive blocking
  in the step-5 review. Add the discriminator. Path-1 grounded (OBSERVATIONS #26).
- `generalize-sharpening-skill.md` — the sharpening family (`sharpen` /
  `decision-design-sharpening` / `pre-implementation-sharpening`) is still
  PBS-coupled, never extracted like `coherence-audit`. Cross-repo tooling
  extraction; low-priority. Relates to `framework-dev-as-anneal.md`.
- `anneal-dev-packaging.md` — **DONE 2026-06-02** — installed `anneal-dev@anneal-dev`
  `0.1.1` (installed + **activated** via `/reload-plugins`; bumped from 0.1.0 by the
  impl-skillcraft-gate fix). Fully done.
- `archive/anneal-dev-impl-skillcraft-gate.md` — **DONE 2026-06-02** — shipped via
  the first method-kernel self-hosting anneal-dev run (anneal-dev `ee9e2e6`, verify
  [PASSED]); the convergence falsification caught a missed 3rd render + the
  spawn-fallback edit path, both fixed.
- `planner-instance-exploration.md` — the planner instance build + the
  framework findings (1–5) seeding several items above; also holds the
  **Cycle 2.5 bindings.md slot-collapse** fork (deferred to the planner
  derivation, finding 3).
- `clippy-run-findings-dispatch-coupling.md` — **framework/instance findings
  surfaced *via* a clippy run** (azuro dispatch/coupling; clippy was the source,
  the fixes are mostly framework-level): shipped Cycles 1–3 + G (clippy
  ≤v0.9.93); **still open:** Cycle 2.5 (above) + the **coherence-audit
  deep-sweep** (§4.4 / §5.1 / mode mechanics not yet swept). Open cycles are
  classified per-level. Archives whole when those close.

**Cross-session dump triage (2026-06-02).** Git/dispatch findings from the tail
of a saved other-session clippy dump. Already-handled, not re-filed:
always-dispatch-impl = Cycle G above; fabricated-tracker-tags = V-25; sort-null
incomplete-evidence = [[verified-integrity-consolidation]]. New items:

- `worktree-isolation-and-integration.md` — parallel-worktree path: relocate the
  worktree out of operator's main (escape hazard), verify the unit fully landed
  after cherry-pick, fail-loud on a stale worktree base.
- `dispatch-brief-one-source-of-truth.md` — "reference by letter" is
  unenforceable for a context-less spawned agent; ship dedicated subagent types /
  template / minimal bootstrap pointer.
- `behavior-change-test-impact-enumeration.md` — a behavior-changing decision must
  *executably* enumerate existing tests asserting the old behavior (grep-blind
  sibling of dispatch-coupling Finding 3).
- `impl-green-on-commit.md` — spec is silent on whether the impl commit must be
  green ("committed on completion" ≠ "green on commit"); orchestrator fills it by
  habit. Pick: mandate green-on-commit, or explicitly leave it to verify.

### Instance render-settlement (parked — framework's downstream tail, not a rival)

Fix lands in the clippy/daneel render, not the core; *owed by* framework edits.
Parked while those instances are idle (drift cost ~0), so they batch behind
framework work by design — **but only for vocab-debt; see the vocab-vs-semantic
caveat in `clippy-render-resync.md`.**

- `clippy-render-resync.md` — **PARKED** (clippy idle). The clippy render-debt
  owed for c-safe (+ future T1/T2), batched into one render pass to do when
  clippy returns to active use. Re-entry procedure recorded in the file.
- `adoption-instance-settlement.md` — **PARKED** (instances idle). Re-point the
  instance CLAUDE.md "rendered, not authored" seed blocks (clippy / daneel /
  campaign-craft) from "the procedure is `development-process.md`" to the
  anneal-dev model. campaign-craft also needs its source repo located (stale
  `diligence-framework` name; only the marketplace clone exists). Filed by adoption.
- `clippy-skill-de-bloat.md` — de-bloat clippy's `SKILL.md` (over the word budget;
  named in the `framework-dev-as-anneal` locked decision). *Structural* de-bloat,
  not vocab-debt — but clippy-local, so park-safe while clippy is idle. Candidate
  **2nd anneal-dev dogfood** (larger change → better V-27 datapoint), which would
  re-activate clippy and bundle `clippy-render-resync`. Not pressing.
- `daneel-cycle-b-sync.md` — **CLOSED 2026-06-02 → `archive/`.** Shipped daneel
  `d85cff3` (§5.2 vocab sync `implementation outputs`→`realization output`) as the
  step-5 anneal-dev dogfood; R1 resolved to a no-op. (clippy's render-sync shipped
  → `archive/clippy-isolation-render-release.md`.)

### Genuinely instance-level (behind framework)

Fix lands in the instance, and the file argues it must *not* become a framework
change — framework-izing would re-leak the corpus-state distinction the
de-pollution cluster just removed (contract-1).

- `clippy-greenfield-tolerance.md` — clippy's `verify` (and likely other
  bindings) assume existing code; instance-level greenfield hardening,
  low-priority.
