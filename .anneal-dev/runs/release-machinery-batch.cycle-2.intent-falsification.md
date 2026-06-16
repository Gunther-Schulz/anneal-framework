# release-machinery-batch — cycle 2 (convergence) intent-falsification pass

Fresh-context subagent (opus), criteria-first. Subagent agent-id: a524ac5e42553dd01.
All R1–R3 served; 3 surfaced findings; orchestrator actions 2 as D-deltas (practice-4 class
completion + D2 completeness), 1 confirms F6 separable.

## Per-R# attack lines
- {R1, serves D1+D3, refutation: `find . -path '*/.claude-plugin/*' -type f` → only marketplace.json +
  plugin.json (JSON manifests, no rule); post-D1 pattern test → both commit-gated=False. outcome: **served**}
- {R2, serves D1, refutation: before/after pattern test — before: packaging commit-gated=True/edit-gated=False
  (disagree, confirms F2); after D1: both False (agree). pre-edit genuinely exempts .claude-plugin. outcome:
  **served (for packaging) + Finding-1 (a NON-packaging sibling disagreement surfaced)**}
- {R3, serves D2, refutation: traced hooks/commit-msg main() (:357 skip, :371 corpus-gate, :382 validate) —
  a final release commit (non-checkpoint first line) re-touching a rule-corpus file → is_corpus=True →
  validate_discharge fires; topology-independent (final commit on top, no rewrite of N checkpoints) → handles
  non-contiguous + merge (squash needs interactive rebase=unavailable; amend messy across merge). step 5
  (development-process.md:798-802) currently has no formation clause. outcome: **served + Finding-2 (OR-branch residual)**}

## Per-finding lines (orchestrator disposition)
- {Finding-1: `instance-template/CLAUDE.md` + `instance-template/README.md` are commit-gated
  (RULE_CORPUS_PATTERN `instance-template/.+\.md`) but NOT pre-edit-gated — the exact edit-vs-commit
  disagreement R2 names, on repo-local housekeeping the SAME carve-out exempts (instantiation-guide.md:491-492
  "the READMEs … and the like — repo-local"; development-process.md practice-5 lists CLAUDE.md as exempt).
  `instance-template/spec/*.md` IS correctly gated by both (genuine spec source). criterion: R2, refutation:
  `ls instance-template/` (CLAUDE.md + README.md + spec/) + Python pattern tests, route: [VERIFIED — surfaced]}
  → **ORCH: actioned as D-delta (extend D1)** — practice-4 class completion: the over-match CLASS is
  packaging/housekeeping, not just `.claude-plugin`; narrow `instance-template/.+\.md` → `instance-template/spec/.+\.md`
  (gate spec placeholders, exempt CLAUDE/README), aligning with the carve-out + the pre-edit hook.
- {Finding-2: D2's "re-touch the primary file OR a rule-corpus marker" has a residual — if a run's ENTIRE diff
  is now-exempt (packaging-only / README-only), no rule-corpus file exists to re-touch → final commit touches
  only exempt files → hook skips (:373-375) → discharge unvalidated. criterion: R3, refutation: post-D1 a
  final commit touching only .claude-plugin/marketplace.json → commit-gated=False → main returns 0 without
  validate_discharge, route: [VERIFIED — surfaced]} → **ORCH: actioned as D-delta (clarify D2)** — the clean
  reading: an exempt-only commit is BY DEFINITION not rule-corpus → correctly needs no discharge (the skip is
  right, not a gap). D2 states: the final discharge commit re-touches the run's primary **rule-corpus** file;
  a run whose work is entirely exempt produces no rule-corpus commit and needs no discharge. Closes by stating.
  (Note the D1↔D2 coherence touchpoint the subagent flagged: D1 enlarges the exempt set, slightly widening
  this case — the clarification covers it.)
- {Finding-3: F6 (KERNEL_SOURCE_PATTERN over-match) genuinely separable — Python test: KERNEL_SOURCE_PATTERN
  matches development-process.md/instantiation-guide.md, NEVER .claude-plugin → does not bear on R1/R2.
  criterion: scope-coherence, route: [VERIFIED — surfaced]} → **ORCH: confirms D4** (file F6 separately). Clean.

## Convergence status
**NOT clean — orchestrator actioned 2 D-deltas (D1 extended for instance-template; D2 clarified for exempt-only).**
Mechanical pass **skipped: intent-delta this cycle.** D1↔D2 cohere (both the discharge-gate surface). Deltas
feed cycle 3.
