# Citation-firewall coherence-check regex is not wrap-tolerant

**▶ SHIPPED + ARCHIVED 2026-06-16 — `103e2e7` (main, pushed).** Via anneal-dev (run
`firewall-regex-wrap-tolerance`, auto-battle). The firewall regex at instantiation-guide.md:189 →
wrap-tolerant `rg -U '(core|modules)\.md[^A-Za-z0-9]{0,12}§'` (catches the newline-split §-cite the
old single-line regex missed; empirically validated — wrap caught, zero prose false positives; bound
criterion stated). Render-debt queued for instances. verify [PASSED] isolated (loopback on a self-stale
line-ref → content anchor → delta-verify; step-4 self-review caught + fixed the naked `{0,12}` bound).

**Status:** SHIPPED (was [READY]) — spawned by the `clippy-reinstantiation` run (2026-06-07). Method/kernel robustness; low-sev but real.

## The gap

The citation-firewall coherence check (`instantiation-guide.md` §, "the render-verify runs `rg '(core|modules)\.md[^\n]{0,4}§'` over the instance specs + rendered files → empty") uses a **single-line** regex. It **misses a §-citation split across a newline** (e.g. `` modules.md` `` at end of line, `§2.2` at start of next) — exactly the residual that escaped the clippy re-render's firewall passes and was caught only by a subagent's *manual* Missed-dependents flag (run `clippy-reinstantiation`, finding "B": `lens-set.md:5` line-wrapped `modules.md §2.2`).

## Why it matters

The firewall check is named as an acceptance gate (R3/R4 in the clippy run; the D16 verify-acceptance). A check that misses wrap-split cites gives false-clean — a downstream instance render could carry an un-firewalled §-cite the check passes over. Prose wraps; the basis rule's own true-unit guidance is **wrap-tolerant** ("newline-flattened input, because prose wraps across lines and a multi-word pattern can split mid-match", `core.md §3.2`/`glossary.md` Completeness claim) — the firewall check should match that discipline.

## Next action

Make the firewall coherence-check regex wrap-tolerant where it's specified (`instantiation-guide.md` + any instance render-verify that renders it) — e.g. `rg -U '(core|modules)\.md[\s]*§'` (multiline/dotall, whitespace-flexible) or a newline-flattened pre-pass. Small kernel/method edit; runs through anneal-dev.

## Relates to
- `clippy-reinstantiation` run (the catch) · the firewall convention (`b56f7d8` / `cite-glossary-not-section-numbers`).
