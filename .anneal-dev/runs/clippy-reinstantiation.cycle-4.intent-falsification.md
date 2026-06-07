# clippy-reinstantiation — cycle 4 intent-falsification-pass artifact

Fresh-context subagent (opus), criteria-first. Dispatched per live `core.md §4.1.4`; artifact shape per `modules.md §3.4.1`.

## Criteria derived from R1–R5 (before reading the design)
- R1 delta-completeness: every framework spec delta postdating clippy's 2026-06-02 render carried by some decision.
- R2 faithfulness: render preserves source enforcement/completeness/enums AND does not render source-DELETED content.
- R3 coherence: instance sources + rendered files coherent with deltas; citation-firewall (glossary terms, not §-numbers).
- R4 separate-context verify: clause-by-clause render-fidelity in an independent context.
- R5 budget: clippy within skill-craft budget; over-budget surfaces flagged across the file set.

## Per-R# attack lines
- `{R1, attempted-refutation: git log since 2026-06-02 10:01 of spec/foundation/anneal-dev-spec/post-run-review (29 commits, 21 kernel-touching) mapped each to a decision; checked a6ce126's 6 sub-items, f74b145, 432e618, 1d93e58, bf32f9c via bodies+diffs, outcome: SERVED — every delta maps; all 8 plugin files + 2 instance sources covered}`
- `{R2, attempted-refutation: compared repoint decisions vs live source at rendered-from site — git show bf32f9c -- spec/core.md (V-5 removed from §4.1.2) + e453678 (glossary zero V-N), outcome: FINDING (F-INT-1)}`
- `{R3, attempted-refutation: read both instance sources; D10 co-producer/emitted vs glossary.md:98-135 + core.md:269-289; bindings.md §-number load vs b56f7d8 firewall scope, outcome: FINDING (F-INT-1 firewall + F-INT-3)}`
- `{R4, attempted-refutation: each D5-D14 carries "render-fidelity verify clean clause-by-clause" acceptance; foundation.md:21-30 contract 2, outcome: SERVED}`
- `{R5, attempted-refutation: wc -w sweep all 8 plugin files (tracker.md=3015, investigate-design.md=2364, SKILL.md=2579, implement.md=1988) vs which decisions ADD content vs flag budget (only D2/D14 flag SKILL.md), outcome: FINDING (F-INT-2)}`

## Per-finding lines (all route [VERIFIED — surfaced]; zero mechanical-falsification-candidate)
- `{finding: F-INT-1 — D6/D14 commit to REPOINT the validation-watch V-5/V-9 breadcrumb sites (investigate-design.md:144,255-256; SKILL.md:209), but the framework DELETED those V-N breadcrumbs from its own source — faithful render is a STRIP, not a path-repoint; a repointed "V-5 in validation-watch/" cites content the live spec no longer carries + crosses framework-private provenance into a downstream plugin. D13's post-run-review.md:162 repoint is correctly distinguished (its source legitimately references the folder for the Q7 walk). criterion-attacked: R2+R3. refutation: git show bf32f9c -- spec/core.md (-(V-5)); git show -s e453678 (glossary zero V-N); grep V-[0-9]+ plugin/skills/clippy/ → 3 surviving breadcrumbs. route: [VERIFIED — surfaced]}`
- `{finding: F-INT-2 — R5 budget flagged for SKILL.md only (D2/D14/F4 used single-file wc -w SKILL.md), but the re-render adds semantic content to three already-large files: tracker.md (3015, via D9), investigate-design.md (2364, via D6), implement.md (1988, via D7). criterion-attacked: R5. refutation: wc -w sweep. route: [VERIFIED — surfaced]}`
- `{finding: F-INT-3 (minor) — bindings.md carries ~15 core.md/modules.md §-number citations; firewall convention b56f7d8 ("an instance references … never section numbers") covers instance sources, but D3 scopes to "rendered plugin files" and D12 folds it under vague "citation touch-ups". criterion-attacked: R3. refutation: grep 'core.md §|modules.md §' coding-clippy/spec/bindings.md → ~15; git show b56f7d8. route: [VERIFIED — surfaced]}`

## Verdict
3/5 R# served clean (R1, R4); 2 produced findings (R2/R3, R5); all 3 findings route [VERIFIED — surfaced] (pure judgment). No coupling-shape falsification of any [VERIFIED] D-entry's technical basis — every D5-D14 located read accurate, scope complete. Per the subagent the pass is "intent-clean" (no mechanical-falsification-candidate). **Working-context disposition: the 3 surfaced findings are clear design improvements → ACTIONED as D-deltas (D6'/D12'/D14'/D15), so the design is amended this cycle and not converged.**
