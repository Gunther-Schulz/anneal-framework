# Backlog status-queryability — cluster/campaign reasoning is stale-prone or expensive

**Status:** [PARTIAL] — process/hygiene gap, surfaced 2026-06-15 (during `convergence-machinery-batch`,
operator-raised). Dev-notes hygiene (NOT method-kernel) → a dev-process tweak, not an anneal-dev cycle.
**Gated on need:** earns its place IF coherent-cluster batching becomes routine (see Trigger). NOT urgent.
**ADOPTED + applied 2026-06-15:** the greppable token ([READY]/[DESIGN]/[PARKED]/[GATED]/[PARTIAL]) is now
documented in the README convention and applied across all open items (this pass). The "earns-its-place-if-routine"
gate resolved YES — the marginal cost is ~zero (a format on the status-line first-word you already edit). Residual:
the self-audit is a documented grep recipe; a pre-commit hook is a future option, not built (would be over-building now).

## The phenomenon
An item's **real status** (open-and-ready vs parked vs gated vs partially-shipped vs deferred-pending-
evidence) lives in **free-form prose** after a only-mostly-consistent leading token. Grep over all items:
the opening token is `OPEN` ×52 but also `open` ×4, `L3`, `RAN`, `SECOND`, `DECIDED`, `design`; and
`proportional-cycle-weight` uses a different `**Status / stage:**` label. The *resolution* state is in the
prose, not the token — e.g. `convergence-sequencing-enforcement` opens "L3 … SHIPPED … L1 … SHIPPED"
(effectively done; greps as neither OPEN nor SHIPPED); `convergence-mechanical-pass-value` greps as `OPEN`
but is `PARKED, gated on evidence`.

**Consequence:** "which items are open AND ship-ready AND cluster coherently" cannot be answered by a grep —
it requires reading each candidate item's prose (expensive, N-file reads) or trusting the hand-maintained
**campaign map** (`README.md` ▶ Campaign map), which **drifts stale** because status lives in the item files,
not synced to the map. Concrete near-miss this run: a proposed convergence-cluster batch rested on **recalled**
statuses that were stale (most convergence items had shipped/parked); caught by grounding, but the catch was
**willed** (re-read the files), not structural.

**Empirical (2026-06-15 full grounding sweep):** a body-grounded sweep of all 70 open items (5 subagents)
found **~14 (20%) materially mis-stated** — 5–6 shipped-stale (still in `backlog/` after their fix shipped,
incl. a same-slug `backlog/`↔`archive/` conflict on `anneal-dev-impl-skillcraft-gate`) + ~8 partials whose
`OPEN` status-line oversells a mostly-shipped body. Reading bodies was the only way to catch them; the
leading token did not. Cost-of-absence: three consecutive batch-cluster picks (⑤, the ③ pair) failed on
stale/heterogeneous state a greppable status-token would have surfaced in one query.

## Why it matters now (the trigger)
`proportional-cycle-weight`'s coherence-batch finding (n=1, 2026-06-15) makes **"identify a coherent
ship-ready cluster"** a **first-class, recurring** operation — every aggressive-batch planning step does
cluster-level reasoning over live status. That raises the value of cheap, drift-free cluster-queryability
from "nice" to "load-bearing for the batching workflow." Absent batching, the practice-5 discipline suffices;
with routine batching, the willed form leaks at exactly the step batching depends on.

## Relation to existing discipline (it's partly covered — in the leaky form)
Practice 5 (`development-process.md` "Ground before asserting — never assert current state from memory; verify
against the live source") **already** mandates re-checking live status before asserting. So the *discipline*
exists; the gap is its **enforcement strength**: it's **willed** (the AI must remember to re-read N files),
which by the framework's own "willed = leaks / structural > willed" reasoning is the weaker form. The fix is
to make grounding **cheap** (structural) rather than rely on willed re-checking.

## Candidate fix (LEAN — make grounding cheap, don't build tooling)
A **greppable status-state token convention**: `**Status:** <STATE> — <free prose>` where `<STATE>` is a
small closed enum — **OPEN / SHIPPED / PARKED / GATED / DEFERRED / PARTIAL**. Then "what's batch-ready" is one
grep over the source of truth (`grep -l "Status:.* OPEN" *.md`), no per-file prose-read, no separate index.
The drifting campaign-map's **status role consolidates** into the live files (the map becomes a *derived/checked*
cluster view, not a hand-maintained status mirror) — a **Pareto consolidation**, not an addition.

**Proportionality / no-ship test (practice 7 + 9e):** it adds a per-item maintenance discipline (keep the token
current) — weigh that. The no-ship alternative is the status quo (practice-5 willed re-check), which is fine
while batching is rare. The item ships **only if** batching becomes routine (then the token earns its place by
making the recurring cluster-query cheap + drift-free). Keep it a **convention + maybe a grep helper**, NOT an
index file or tooling build (that would re-introduce a drifting second source).

## Relates to
- `proportional-cycle-weight` (Coherence-batch economics) — the **trigger**; batching makes cluster-query first-class.
- `README.md` ▶ Campaign map + the backlog README convention ("status lives in the file, not the name; ls is the
  index") — this **sharpens** that convention (status in file + greppable token) and backs the drifting map with
  a queryable source.
- `development-process.md` practice 5 (ground before asserting) — the willed discipline this would structuralize.
- `instance-reinstantiation.md` render-debt queue + capability-by-instance matrix — precedents of queryable
  sub-indexes for a specific concern (the pattern this generalizes to item-status).
- Origin: operator, 2026-06-15 — "is this a phenomenon of the protocol itself? maybe needs improvement?"
