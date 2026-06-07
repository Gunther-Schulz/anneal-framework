# clippy-reinstantiation — cycle 6 mechanical falsification-pass artifact

**Per-artifact header — cited this-cycle intent-clean verdict:** `cycle-6.intent-falsification.md` = CLEAN (no `mechanical-falsification-candidate`). Pass constructed from that verdict (`modules.md §3.4`).

Fresh-context subagent (opus) declared candidate+predicate+result; **orchestrator computed holds-or-falsified** (coverage check, `core.md §4.1.4`). One line per [VERIFIED] entry + [CONDITIONAL] technical-shapes.

## Per-entry (orchestrator-computed verdicts)
- **D1'** — `{target-existence: source-delta 28 commits extant (F5), expected-match, holds}` · `{target-dependents: full instance sweep `rg validation-watch\.md spec/ plugin/` → 5 sites incl **spec/README.md:27** OUTSIDE the 10-target scope, any-outside-scope:<10 targets>, **FALSIFIED**}` → **aggregate: FALSIFIED.**
- **D4** — `{target-existence: core.md:813-820 run-state exclusion + d0f479a downstream-bind-off, expected-match, holds}` → holds.
- **D5** — `{target-existence: core.md :163 'strong surfacer'/:156 'BINDS when'/:222 provenance/:261 co-producer/:275 'emits rather than returns'/:318 §3.2.3/:22 mechanism, expected-match, holds}` · `{target-dependents: coupling-rename 7 sites all in D6'/D9, any-outside-scope, holds}` → holds.
- **D6'** — `{target-existence: core.md:392 requirements record/:485 intent pass/:525 exemption, expected-match, holds}` · `{target-dependents: V-N strip — 3 breadcrumbs all in D6'(:144,255)/D14'(:209), any-outside-scope, holds}` → holds.
- **D7** — `{target-existence: core.md:903 loopback triage/:919 checkpoint/:813 run-state excl, expected-match, holds}` → holds.
- **D8** — `{target-existence: core.md:981 requirements-coverage/:971 design-completeness audit/:1006 de-prioritization, expected-match, holds}` → holds.
- **D9** — `{target-existence: core.md:629 surfaced/:1078 deferred-(c) + modules.md:440 intent artifact/:345 header/:187 considered, expected-match, holds}` · `{target-dependents: coupling-rename 7 sites in D9/D6', holds}` → holds.
- **D10'** — `{target-existence: core.md:261/:275/:279 co-producer+emitted + glossary:98-135, expected-match, holds}` · `{target-dependents: lens-set §-cites exactly :10,:75,:204, any-outside-scope, holds}` → holds.
- **D11** — `{target-existence: lenses.md is render of lens-set.md (CLAUDE.md:22), expected-match, holds}` → holds.
- **D12'** — `{target-existence: bindings table + run-state provisioning extant, expected-match, holds}` · `{target-dependents: bindings §-cites exactly :45,50,60,148,153,173 (6), any-outside-scope, holds}` → holds.
- **D13** — `{target-existence: post-run-review.md:163 Q7 walk/WATCHING/FIX-SHIPPED/folder, expected-match, holds}` · `{target-dependents: dependents of D13's TARGET (post-run-review.md) — :162 vw path in scope; spec/README.md:27 is NOT a dependent of post-run-review.md (it belongs to scope-completeness D1'), any-outside-scope:<post-run-review.md>, holds}` → **aggregate: holds** (orchestrator correction: subagent over-attributed the whole-instance vw sweep to D13; re-computed against D13's actual target → holds).
- **D14'** — `{target-existence: modules.md:51-53 convergence-cycle status, expected-match, holds}` · `{target-dependents: SKILL.md:209 V-9+vw-path = the STRIP site, no other SKILL V-N, any-outside-scope, holds}` → holds.
- **D16** — `{target-existence: instantiation-guide.md:188-191 firewall check + render-verify-runs-it, expected-match, holds}` · `{target-dependents: 14 §-cites across 6 active files all in D1' targets (archived docs out of scope), any-outside-scope, holds}` → holds.
- **D2** [CONDITIONAL, technical only] — `{target-existence: wc -w SKILL.md = 2579 (matches F4), expected-match, holds}` → holds.
- **D15** [CONDITIONAL, technical only] — `{target-existence: wc -w tracker 3015/investigate-design 2364/implement 1988 (match F13), expected-match, holds}` → holds.

## Verdict
**1 entry falsified: D1' (scope completeness).** All 16 other entries hold (every cited source clause extant; coupling-rename / V-N strip / firewall conversions fully enumerated within converting decisions). D1' flips [INVALIDATED]→[PENDING] (`core.md §5.2`) → re-formed as D1'' (scope = 11 targets, +`spec/README.md`) + new D17 (repoint its vw path). Cycle 6 NOT zero-delta → another convergence cycle.

## Loopback root-cause triage (`core.md §4.2.7`)
Root: **adherence-class (this run's investigation), NOT a framework spec gap nor a clippy render gap.** F8's enumeration grep was scoped to `plugin/skills/clippy/` only, excluding the co-located `spec/` dir — the true-unit-basis error `core.md §3.2.1` names ("a search narrowed by where members are assumed to live"). Disposition: noted (no source fix); the mechanical falsification pass is the designed catcher and caught it. The corrected un-narrowed whole-repo sweep (orchestrator-run) re-establishes D1'' completeness. basis: the falsified D1' target-dependents line above.
