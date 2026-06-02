# Daneel — re-render §5.2 to Cycle-b vocab (+ verify a/other drift)

**Status:** OPEN — surfaced 2026-06-02 by the practice-4 cross-repo
dependent audit during the clippy a+b sync ([[clippy-isolation-render-release]]).
Daneel is the debugging instance; it renders the same framework §5.2
contract clippy does, and Cycle b's render catch-up was only scoped to
clippy. Parallel to clippy's render-sync, one instance over.

## Confirmed drift
- **§5.2 body-shape (Cycle b) — STALE.** `daneel/plugin/skills/daneel/references/tracker.md`
  is half-migrated: `:104` already uses "contract surface", but `:112`
  still carries the OLD brevity vocab "…are **implementation outputs**"
  instead of the framework's defined term **realization output**
  (`anneal-framework/spec/core.md` §5.2 + glossary *Contract surface* /
  *realization output*). Same state clippy's `tracker.md` was in before
  this sync. Behavior likely faithful (verbatim-stale, as clippy's was);
  vocabulary alignment.
- **§5.2 contract-surface discriminator (R1) — DEFINITION changed 2026-06-02.**
  Beyond the vocab staleness above, the `Contract surface` definition itself was
  abstracted (code-shaped "observable from outside" → coupling-based "what a
  dependent would break if it silently changed"; `anneal-framework/spec/core.md`
  §5.2(b) + glossary). Daneel's render of §5.2(b) / any contract-surface gloss
  inherits this; fold into the same daneel render-sync. See
  [[anneal-dev-framework-flowback]] R1.

## To verify before scoping the cycle
- **Cycle a (§4.2 isolation) — likely N/A for daneel.** A grep found NO
  "Main-tree integrity check" / "integrity check" in daneel's plugin or
  spec — debugging may render no parallel-worktree isolation mechanism
  (in-place only). Confirm: does daneel render §4.2 isolation at all? If
  not, no Cycle-a drift; if yes under different headings, check the
  in-place / Integrity check vocab too.
- **Other a/b vocab.** A focused render-fidelity diff of daneel's tracker
  / phases against the abstracted core (a+b) — the same separate-context
  check this clippy sync ran — is the real scope-setter.

## Next action
A daneel render-sync cycle (own skill-craft gate + spec-origin traces +
separate-context render-fidelity check + release), not folded into the
clippy sync. Sequence after the locked contract1 work (clippy a+b →
Cycle c-safe → c-only sync) unless the operator pulls it forward.

Relates to [[clippy-isolation-render-release]] (the sibling render-sync),
[[contract1-depollution-cluster]] (Cycle b is the source contract change).
