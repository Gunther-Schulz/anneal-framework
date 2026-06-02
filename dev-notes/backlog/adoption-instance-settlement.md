# Adoption instance-settlement — re-point instance CLAUDE.md seed blocks

**Status:** OPEN (parked behind the instances, per the render-settlement policy) —
filed 2026-06-02 by [[dev-process-adoption]]. Instance render-settlement, not
framework-core.

The adoption re-pointed the **seed** of the instance CLAUDE.md "rendered, not
authored" block (`instantiation-guide.md` §6 + `instance-template/CLAUDE.md`) to the
two-regime / anneal-dev model. The **already-rendered** instances still carry the old
"the procedure is `development-process.md`" seed and need re-pointing:

- **clippy** (`coding-clippy/CLAUDE.md:15`) + **daneel** (`daneel/CLAUDE.md:15`) —
  the seeded block; straightforward re-point to the new seed text.
- **campaign-craft** — **stale + no local source repo**: `CLAUDE.md:16-17` cites the
  obsolete `diligence-framework` name + the single-spec model; only the marketplace
  clone exists (`~/.claude/plugins/marketplaces/campaign-craft`). Locate/clone the
  source repo first, then a larger re-point (name + spec-model + seed).

The practice-1 **triage** citations in the rendered instance `post-run-review.md`
files are **unaffected** — the triage stayed in P1 (Decision 1 reversed), so those
still resolve. Only the CLAUDE.md seed block is owed.

Park-safe while instances idle (drift cost low — the old seed still resolves to a
file). Relates to [[clippy-render-resync]] (batch when clippy re-activates),
[[dev-process-adoption]].
