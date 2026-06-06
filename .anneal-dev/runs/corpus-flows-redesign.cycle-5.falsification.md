# corpus-flows-redesign — cycle 5 (re-attempt convergence) falsification pass

Dispatched to the fresh-context checker (agent a8093033c655e4c6c, resumed —
valid separate checker: it did NOT produce the re-resolved D2′/D3′). FRESH
candidates, query strings/reads distinct from cycle 4 (new-surface
requirement). Iterated the 5 [VERIFIED] entries at convergence-cycle start:
D1, D2′, D3′, D4, D8.

## D1 — aggregate: HOLDS
- {target-dependents, candidate: `rg -n 'routes? (corpus|the corpus|corpus-evolution)' -g '!dev-notes/**' -g '!.anneal-dev/**' .` (FRESH routing-verb axis), predicate: any-outside-scope:{6 docs + per-instance CLAUDE + glossary/modules}, result: only instantiation-guide.md:435/466 + instance-template/CLAUDE.md:15 — all in-scope, all pointing to development-process.md, holds}

## D2′ — aggregate: HOLDS
- {target-existence, candidate: read instantiation-guide.md 14-37 "spec-first" (FRESH), predicate: expected-match:"before building the plugin", result: "(1) Write the instance spec, (2) Generate the plugin, (3) Verify and validate" + "Spec-first is not optional. Writing and settling the spec before building the plugin" — confirms the pre-channel derivation prefix, holds}
- {target-behavior, candidate: `rg -n 'derivation.{0,40}anneal-dev|deriv.{0,40}(through|run)|domain.fit.{0,40}anneal-dev'` (FRESH contradiction search), predicate: any-match (text folding derivation into the channel / making it a routing path), result: empty — nothing frames derivation as a routing path, holds}

## D3′ — aggregate: HOLDS
- {target-behavior, candidate: executed hooks/skill-craft-pre-edit.py SPEC_SOURCE_PATTERNS (`/spec/.+\.md$`) + hooks/commit-msg RULE_CORPUS_PATTERN (`^spec/.+\.md`) against coding-clippy/spec/{bindings,lenses,glossary}.md, predicate: expected-match: BOTH patterns match an instance spec file (the "still hits the floor" property; non-match falsifies), result: pre-edit matches all three =True (dev-notes draft carved out); commit-msg matches all three =True. Pre-channel spec authoring is in-scope for both hooks where deployed, holds}
- {target-existence, candidate: read spec/README.md ~150 "deliberately resistant to extension" (FRESH), predicate: expected-match:"deliberately resistant to extension", result: present — grounds rejecting fold-§1-5-into-Scope-machinery for a rare bootstrap, holds}
- {target-behavior, candidate: `rg -n 'derivation.{0,40}anneal-dev|author.{0,40}anneal-dev|deriv.{0,40}(through|run)'` (FRESH — does corpus claim derivation MUST run through anneal-dev?), predicate: any-match (a "derivation must route through anneal-dev" claim falsifies pre-channel), result: only spec/README.md:50 matches, about RE-RENDERING (entry-condition 3), not derivation. Nothing contradicts pre-channel placement, holds}
- RESIDUAL (not a falsification): the pre-edit hook's protection of an instance-repo derivation session depends on that instance deploying the hook (core.hooksPath registered in anneal-framework) — the pre-existing F11 / adoption-instance-settlement gap, already recorded+deferred. D3′'s claim is category-membership ("a spec/*.md write is in-scope for the floor"), which holds; it does not assert universal deployment.

## D4 — aggregate: HOLDS
- {target-existence, candidate: `git config core.hooksPath` + `rg 'DENY_REASON =|def deny' hooks/skill-craft-pre-edit.py` + `ls -l` both hooks (FRESH — config + symbol + exec-bit, distinct from cycle-4 content reads), predicate: expected-match:"hooks/" + DENY_REASON + def deny + executable, result: core.hooksPath=hooks/; DENY_REASON line 78; def deny line 230; both -rwxr-xr-x. Block mechanism live, holds}

## D8 — aggregate: HOLDS
- {target-dependents, candidate: `rg -n 'release machinery|release loop|carries the release'` (FRESH axis), predicate: any-match (a competing release-machinery home, not pointing to development-process.md), result: development-process.md is the home (line 36, 512 "## The release loop"); all others (instantiation-guide 436/466, instance-template/CLAUDE 15, spec/README 52, CLAUDE.md 22, commit-msg:5) POINT to it. No competing home, holds}

## Outcome
ALL FIVE HOLD on fresh candidates. Zero falsifications. Convergence cycle
CLEAN — zero D-track deltas this cycle.
