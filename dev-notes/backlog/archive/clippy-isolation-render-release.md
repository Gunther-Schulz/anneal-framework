# Clippy — re-render to new framework vocab + release

**Status:** **DONE — shipped clippy v0.9.94 (coding-clippy `56414d6`),
2026-06-02.** All three pending parts landed: implement.md isolation re-render
(in-place / Integrity check), tracker.md §5.2 (contract surface / realization
output), and release (commit + push + marketplace pull + `claude plugin
update`; operator `/reload-plugins` to activate). Step-4 render-fidelity PASS via
subagents `af5f269d1cc9a646f` + `af6207c67e8d1be71`; the practice-4 audit caught +
fixed intra-repo dependent `SKILL.md:65` and spun out [[daneel-cycle-b-sync]]
(daneel's §5.2 is still stale on the Cycle-b vocab). The a+b render (isolation +
design-shape vocab) did NOT touch clippy's intricate *falsification* render, so
it was the small, low-risk catch-up intended. Cycle c-safe (which cleans the
falsification machinery) still gets its own *focused* c-only clippy-sync — the
delicate falsification re-render stays isolated, not batched into a big a+b+c
sync.

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
- **§5.2 body-shape re-render (Cycle b):** `references/tracker.md:126-140` carries
  the OLD code-flavored §5.2 design-decision shape **verbatim** (not a binding) —
  re-render against the abstracted §5.2 (clippy's element kind → contract surface =
  signature/types; realization output = body). Behavior faithful (subagent
  `ac0a56455ed827c25`); vocabulary/derivation alignment.
- **Release** (development-process release loop step 6): version-bump the
  clippy plugin, commit + push coding-clippy, pull the marketplace clone,
  `claude plugin update`, operator runs `/reload-plugins`.

Relates to [[contract1-depollution-cluster]], [[framework-dev-as-anneal]].
