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

- `framework-dev-as-anneal.md` — **the active effort; decision LOCKED**
  (reframed-A, 2026-06-01): make framework-dev a real anneal instance. Pass-1
  forward-derivation **DONE**. **De-pollution Cycles a + b DONE** (commits
  `3a2245b` + `8bf4d47`); **resume at Cycle c (Leak 3, §4.1.4) in
  `contract1-depollution-cluster.md`**, before finalizing the instance.
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
- `skill-craft-pre-edit-hook-findings.md` — the practice-5 gate hook matches
  `/spec/.+\.md$` (over-broad: catches `dev-notes/**/spec/`), is `mv`-bypassable,
  and may not register subagent skill-craft invocations. Narrow the path before
  the de-pollution cycles.
- `generalize-sharpening-skill.md` — the sharpening family (`sharpen` /
  `decision-design-sharpening` / `pre-implementation-sharpening`) is still
  PBS-coupled, never extracted like `coherence-audit`. Cross-repo tooling
  extraction; low-priority. Relates to `framework-dev-as-anneal.md`.
- `dev-process-validation-watch-path.md` — **trivial, not pressing.**
  `development-process.md:453` cites `spec/validation-watch.md`; the file is at
  `dev-notes/validation-watch.md` (one site). One-token fix; own micro-cycle or
  fold into the next dev-process edit.
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

### Instance render-settlement (parked — framework's downstream tail, not a rival)

Fix lands in the clippy/daneel render, not the core; *owed by* framework edits.
Parked while those instances are idle (drift cost ~0), so they batch behind
framework work by design — **but only for vocab-debt; see the vocab-vs-semantic
caveat in `clippy-render-resync.md`.**

- `clippy-render-resync.md` — **PARKED** (clippy idle). The clippy render-debt
  owed for c-safe (+ future T1/T2), batched into one render pass to do when
  clippy returns to active use. Re-entry procedure recorded in the file.
- `daneel-cycle-b-sync.md` — **not pressing.** Practice-4 cross-repo dependent
  surfaced by the clippy a+b sync: daneel's §5.2 is still stale on the Cycle-b
  vocab ("implementation outputs" vs "realization output"). A separate daneel
  render-sync cycle; sequence after the contract1 work unless pulled forward.
  (clippy's render-sync shipped → `archive/clippy-isolation-render-release.md`.)

### Genuinely instance-level (behind framework)

Fix lands in the instance, and the file argues it must *not* become a framework
change — framework-izing would re-leak the corpus-state distinction the
de-pollution cluster just removed (contract-1).

- `clippy-greenfield-tolerance.md` — clippy's `verify` (and likely other
  bindings) assume existing code; instance-level greenfield hardening,
  low-priority.
