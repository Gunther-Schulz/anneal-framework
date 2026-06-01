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

- `surface-non-task-observations.md` — no channel for what the agent notices
  outside the task (code observations + protocol tensions).
- `verify-vs-original-requirements.md` — verify checks the locked design, not
  the original ask.
- `cite-glossary-not-section-numbers.md` — instance specs cite framework
  §-numbers, not glossary terms.
- `clippy-greenfield-tolerance.md` — clippy's `verify` (and likely other
  bindings) assume existing code; instance-level greenfield hardening,
  low-priority.
- `verified-integrity-consolidation.md` — consolidate the "[VERIFIED] claims
  more than was checked" family (Cycle 3 static + V-25 un-run + sample-bias)
  under one umbrella principle; a consolidation cycle.
- `framework-dev-as-anneal.md` — **foundational, recommended first.**
  `development-process.md` is already a *shadow-anneal*; make framework-dev a
  real anneal instance so the rigor + anti-decay forcing-functions come
  built-in (bolt-on anti-decay is the fallback). First dogfooding outputs:
  SKILL.md de-bloat, the consolidation above, the coherence-audit.
- `contract1-depollution-cluster.md` — de-code-ify 3 domain leaks in the
  agnostic core (§5.2b / §4.2 / §4.1.4); a 3-cycle cluster, high-value,
  adjacent to the coherence-audit.
- `planner-instance-exploration.md` — the planner instance build + the
  framework findings (1–5) seeding several items above; also holds the
  **Cycle 2.5 bindings.md slot-collapse** fork (deferred to the planner
  derivation, finding 3).
- `clippy-run-findings-dispatch-coupling.md` — the azuro dispatch/coupling
  record: shipped Cycles 1–3 + G (clippy ≤v0.9.93); **still open:** Cycle 2.5
  (above) + the **coherence-audit deep-sweep** (§4.4 / §5.1 / mode mechanics
  not yet swept). Archives whole when those close.
- `generalize-sharpening-skill.md` — the sharpening family (`sharpen` /
  `decision-design-sharpening` / `pre-implementation-sharpening`) is still
  PBS-coupled, never extracted like `coherence-audit`. Cross-repo tooling
  extraction; low-priority. Relates to `framework-dev-as-anneal.md`.
- `skill-craft-pre-edit-hook-findings.md` — the practice-5 gate hook matches
  `/spec/.+\.md$` (over-broad: catches `dev-notes/**/spec/`), is `mv`-bypassable,
  and may not register subagent skill-craft invocations. Narrow the path before
  the de-pollution cycles.
