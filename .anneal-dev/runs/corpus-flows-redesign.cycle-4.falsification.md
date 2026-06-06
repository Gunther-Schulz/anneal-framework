# corpus-flows-redesign — cycle 4 (convergence) falsification pass

Dispatched to a fresh-context subagent (agent a8093033c655e4c6c), isolated
from the working context. Iterated the 5 [VERIFIED] D-entries at the
convergence cycle's start: D1, D2, D3, D4, D8. ([CONDITIONAL] D5/D6/D7 not
textually falsified — their assumptions discharge at verify.)
Orchestrator computed holds-or-falsified by applying each predicate to the
subagent's cited result.

## D1 — SCOPE completeness — aggregate: HOLDS
- {target-dependents, candidate: `rg -l 'anneal-dev' -g '*.md' -g '!dev-notes/**' -g '!.anneal-dev/**' .`, predicate: any-outside-scope:{6 docs + per-instance CLAUDE + glossary.md + modules.md}, result: only adds anneal-dev.config/{lenses,README}.md — operator-config placeholders mentioning the tool name, encoding no routing rule, holds}
- {target-dependents, candidate: `rg -ln 're.render' -g '!dev-notes/**' -g '!.anneal-dev/**' .`, predicate: any-outside-scope:{6 docs + glossary.md + modules.md}, result: glossary/modules = the designated re-render method-definition; extensions.enabled = operator-config toggle, holds}
- {target-dependents, candidate: `rg -ln 'three paths|corpus.work|run through|route.{0,30}anneal-dev|through anneal-dev' …`, predicate: any-outside-scope, result: core.md = anneal-dev internal phase machinery; hooks = carve-out comment; post-run-review = practice-1 ref; foundation/template-README = zero. None is the routing-contract, holds}

## D2 — one channel, three entry-conditions; re-render = render-tail — aggregate: HOLDS
- {target-existence, candidate: read phases/verify.md 58-67, predicate: expected-match:"Render-fidelity (separate-context)", result: present (clause-by-clause vs source, isolated), holds}
- {target-existence, candidate: read anneal-dev/spec/extensions.md 26-44, predicate: expected-match:"render-and-open-diff", result: present (on-verify-PASSED re-render), holds}
- {target-behavior, candidate: read extensions.md 32-33, predicate: expected-match:"verified D-entries whose targets are rendered plugin clauses", result: present, holds}

## D3 — instantiation DERIVATION ACT fits investigate-design — aggregate: FALSIFIED
- {target-behavior, candidate: read phases/investigate-design.md 3-5 + SKILL.md 8, predicate: expected-match:"produce a locked design", result: present BUT SKILL.md frames anneal-dev as editing "the rules a rule-corpus encodes"; examples all edit-ops, holds}
- {target-behavior, candidate: read investigate-design.md 88-104 (Scope) + core.md 285, predicate: expected-match: scope machinery admitting greenfield authoring, result: Scope presupposes "the contract being changed" + "every intended target's dependents" — an EXISTING corpus; greenfield instance-derivation has no pre-existing contract-spots; tracker "new element" path only partially rescues. Expected pattern (admits-greenfield) ABSENT → **falsified**}
- {target-existence, candidate: `rg 'deriv.{0,40}investigate.design|instantiation.{0,30}anneal-dev'` + read instantiation-guide.md 6 + §6 430-440, predicate: expected-match: corpus text placing §1-5 derivation inside the channel, result: NONE; §6 places derivation BEFORE/OUTSIDE the channel ("the domain-specific work is done. From here … run through anneal-dev"). Expected pattern ABSENT → **falsified**}
- **aggregate: FALSIFIED** (2 of 3 candidates falsified). D3's literal basis holds, but the claim outruns it: anneal-dev's Scope machinery presupposes existing-contract+dependents, which greenfield derivation lacks, and the current corpus boundary (§6) places derivation outside the channel. D3 flips [VERIFIED]→[INVALIDATED]→[PENDING].

## D4 — no new gate; guarantees already hook-gated — aggregate: HOLDS
- {target-existence, candidate: read hooks/skill-craft-pre-edit.py 281-296, predicate: expected-match:"deny(DENY_REASON)", result: present — actively denies plugin/spec edits lacking same-turn skill-craft, holds}
- {target-existence, candidate: read hooks/commit-msg 99-233 + REQUIRED_CHECKS 38-46, predicate: expected-match:"Commit blocked" + the 7 checks + spec-origin, result: present — exit-1 block; all four D4-named guarantees in REQUIRED_CHECKS, holds}
- {target-behavior, candidate: read development-process.md 540-645 + commit-msg RULE_CORPUS_PATTERN 25-30, predicate: expected-match: a load-bearing render/edit guarantee escaping BOTH hooks + step-4, result: full parity hook↔discharge; carve-outs (README/CLAUDE) are routing-prose not render-fidelity targets; no escapee, holds}

## D8 — canonical home = development-process.md — aggregate: HOLDS
- {target-dependents, candidate: `rg -n 'home of|machinery home|canonical home|is the home' …`, predicate: any-match (competing home outside development-process.md), result: only README.md:101 DESCRIBING dev-process as the home (reinforces); dev-process:308-310 unrelated. No competing claim, holds}
- {target-dependents, candidate: `rg -n 'run through the.{0,5}anneal-dev|routes? corpus' -g '!development-process.md' …`, predicate: any-match (independent restatement NOT pointing to dev-process), result: instantiation-guide/spec-README/template-CLAUDE/README all restate but POINT to development-process.md as the home. No contradiction, holds}
- note (orchestrator): anneal-framework/CLAUDE.md 11-22 is a fuller working restatement than a "one-line pointer" (but defers to dev-process); D8's "one-line pointer" framing slightly under-describes it — fold into D8's implement detail, not a falsification.

## Outcome
4/5 hold (D1, D2, D4, D8). D3 FALSIFIED → reopened [PENDING]. Cascade: D3's
reopening breaks D2's "derivation folded by D3" sub-clause and D6's "reframe
as channel input." D-track delta in the convergence cycle → NOT [READY]; the
loop continues (re-resolve D2/D3/D6, then re-attempt convergence).
