# Clippy — re-render isolation to new vocab + release

**Status:** OPEN, deferred from Cycle a (framework de-pollution, commit
`3a2245b`, 2026-06-01). The framework spec now states implement-isolation as
domain-general guarantees; clippy's instance spec was conformed, but its
PLUGIN render and the release are pending.

## Done (uncommitted in the coding-clippy repo)
- `spec/bindings.md` §Dispatch isolation — intro reframed to "fills the
  isolation slot"; HEAD labelled as the state marker; "main-tree path" →
  "in-place".
- `plugin/skills/clippy/phases/implement.md` — stale source-pointer corrected
  (mechanism per `bindings.md` slot; guarantees per core §4.2).

## Pending
- **Plugin re-render:** `implement.md` still renders the OLD core vocabulary
  — heading `## Main-tree integrity check (sequential/single units)` + "main
  tree" prose. Re-render its isolation section to the framework's new
  **in-place / Integrity check** vocabulary. Behavior is already faithful
  (render-review subagent `a6dd128362a20b41f`) — this is vocabulary alignment,
  not a behavior fix.
- **Release** (development-process release loop step 6): version-bump the
  clippy plugin, commit + push coding-clippy, pull the marketplace clone,
  `claude plugin update`, operator runs `/reload-plugins`.

Relates to [[contract1-depollution-cluster]], [[framework-dev-as-anneal]].
