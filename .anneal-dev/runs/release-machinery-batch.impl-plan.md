# release-machinery-batch — impl plan

**1 dispatch unit** (multi-file, sequential). Disjointness basis: the only unit — runs in place against
the operator's work product under the Integrity check. Touched containers: this repo only.

## Unit 1 — the two fixes + the comment work + the F6 filing (D1, D2, D3, D4)
- **Dependencies:** first (sole unit). **Parallelism:** sequential.
- **Files:** `hooks/commit-msg` (D1, D3), `development-process.md` (D2), `dev-notes/backlog/commit-msg-hook-kernel-source-overmatch.md` (D4, new).
- **D1 — `hooks/commit-msg` RULE_CORPUS_PATTERN (`:39-44`):** (i) remove `\.claude-plugin/.+|plugin/\.claude-plugin/.+`;
  (ii) narrow `instance-template/.+\.md` → `instance-template/spec/.+\.md`. Keep all other terms.
- **D3 — `hooks/commit-msg` comments:** (a) docstring `:6-8` — qualify "instance-template/" → "instance-template/spec/";
  (b) merge-relocation comment `:34-38` — drop `.claude-plugin` from the "anneal-dev's rule-corpus lives at
  `{spec,plugin/skills,.claude-plugin}`" list (it's packaging, not rule-corpus); (c) a brief note at
  RULE_CORPUS_PATTERN that packaging manifests (`.claude-plugin/*`) + instance-template housekeeping are exempt
  per the instantiation-guide carve-out.
- **D2 — `development-process.md` release loop step 5 (`:798-819`):** add a new subsection (alongside Brevity +
  Coherence-audit-handoff), e.g. **"Release commit from checkpoints."**: when a run's work lands across N (possibly
  non-contiguous) `anneal-checkpoint:` commits, the release commit is a FINAL commit carrying the Step-4 discharge
  that re-touches the run's primary RULE-CORPUS file (so `hooks/commit-msg`'s corpus-gate fires and validates the
  discharge) — not a squash (needs interactive rebase, unavailable) and not an amend (messy across a merge). A run
  whose entire work is exempt (packaging/housekeeping only) produces no rule-corpus commit and needs no discharge.
  Cross-reference (don't restate) the "Checkpoint ≠ release-commit" clause (`:60-64`).
- **D4 — new backlog item `dev-notes/backlog/commit-msg-hook-kernel-source-overmatch.md`:** capture F6 — the
  commit-msg KERNEL_SOURCE_PATTERN (`:61-64`) treats development-process.md/instantiation-guide.md/post-run-review.md
  as method-kernel source (requires the Foundation-invariant check line), broader than the spec's method-kernel
  definition (`development-process.md:24-44`: spec/* + foundation.md + anneal-dev/spec/* only). Status [DESIGN];
  relates-to the shipped commit-msg-hook-packaging-overmatch; sibling hook-vs-spec inconsistency.
- **Briefing:** load anneal-dev foundations/tracker/implement; **invoke skill-craft via the Skill tool BEFORE
  editing `development-process.md`** (pre-edit gate fires on it — SPEC_SOURCE; hooks/commit-msg + dev-notes don't
  trigger the gate, but the unit touches development-process.md so the gate must be satisfied this turn). Write-time
  self-check (Lossy-render N/A — not rendered; Missed-dependents — all stale comments at :6-8/:34-38 covered, the
  regex at :39-44; Undefined-shorthand; Over-claimed) + change-set-vs-scope. Do NOT commit.
