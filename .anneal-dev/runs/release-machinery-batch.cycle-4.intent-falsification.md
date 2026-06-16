# release-machinery-batch — cycle 4 (convergence re-attempt) intent-falsification pass

Fresh-context subagent (opus), criteria-first, re-attack. Subagent agent-id: ac5847075ce4e23e0.
R1–R3 all SERVED, prior cycle-2 fixes hold (no gap from the instance-template narrowing). ONE
actionable finding (a stale docstring — the narrowing's own un-enumerated dependent).

## Per-R# attack lines (all served)
- {R1, serves D1(i)+D3, refutation: post-D1 pattern test over `.claude-plugin/*.json` + `anneal-dev/.claude-plugin/plugin.json`
  → all commit-gated=False; carve-out verbatim instantiation-guide.md:491-492. outcome: **served**}
- {R2, serves D1(i)+D1(ii), refutation: pre-edit verdict (abs-path form) vs post-D1 commit-msg verdict over
  {instance-template/CLAUDE.md, README.md, spec/*, .claude-plugin/*, anneal-dev/spec/*, plugin/skills/*,
  development-process.md} → AGREE on every path; pre-edit's `/spec/.+\.md$` gates instance-template/spec/* (incl.
  spec/README.md), the narrowed commit-msg term gates exactly the same set; both exempt CLAUDE.md/README.md.
  `find instance-template -type f` → only top-level .md are CLAUDE.md + README.md (exempt); everything else under
  spec/ (genuine source). NO third category → no gap. outcome: **served**}
- {R3, serves D2, refutation: read step 5 (development-process.md:798-810 — no formation clause exists yet, D2
  fills a real gap) + origin (release-commit-formation-from-checkpoints.md:1-31, the merge-non-contiguity + body-only
  record); re-touch primary rule-corpus file → discharge-required=True; exempt-only → False; checkpoint-prefix →
  False. The exempt-only carve keys re-touch to the PRIMARY RULE-CORPUS file, so a should-discharge run cannot slip
  through. outcome: **served**}

## Per-finding line (orchestrator disposition)
- {finding: D1(ii)'s narrowing makes the commit-msg DOCSTRING stale — `hooks/commit-msg:6-8` lists
  "instance-template/" (unqualified) as a detected rule-corpus directory, but post-D1 only instance-template/spec/
  is gated. No D-entry covers it: D3 scoped the RULE_CORPUS_PATTERN comment + the lines 34-38 merge-relocation
  comment (F7), and F7's search `grep -rniE 'claude-plugin|RULE_CORPUS_PATTERN'` can't catch line 8 (contains
  neither token); F8 drove the narrowing via a pattern test, not a docstring sweep. Same staleness class D3 already
  fixes at lines 34-38. criterion: R2/Missed-dependents, refutation: located read hooks/commit-msg:6-8 + grep -rn
  'instance-template' hooks/ → :8 (docstring) + :42 (regex), route: [VERIFIED — surfaced] (a doc-comment drift, no
  coupling-shape falsification — the regex is correct), ACTIONABLE} → **ORCH: actioned as D-delta (extend D3)** —
  update the docstring at line 6-8 to qualify "instance-template/" → "instance-template/spec/", same Missed-dependents
  discharge D3 applies at 34-38. **Behavior-preserving (comment-only)** → intent result carries forward after the fix.

## Convergence status
**NOT clean — orchestrator actioned 1 D-delta (D3 extended for the docstring at 6-8).** The fix is
behavior-preserving (comment-only) → the cycle-4 intent result carries forward; cycle-6 convergence runs the
mechanical pass over D1-D4 (no intent re-dispatch needed). Mechanical pass skipped THIS cycle (intent-delta).
