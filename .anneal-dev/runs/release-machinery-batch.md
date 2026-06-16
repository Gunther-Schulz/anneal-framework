# Run: release-machinery-batch

- **Status:** PASSED — **SHIPPED `b8f53df` (main, pushed 2026-06-16).** 2 items archived (commit-msg-hook-packaging-overmatch, release-commit-formation-from-checkpoints); commit-msg-hook-kernel-source-overmatch spawned+filed; README NEXT-UP advanced (open 63 → 62). (verify [PASSED] isolated a75cc0a9 — 9/9 gate, 5/5 exempt; operator: "ship".) Batch-economics datapoint: batching shares investigation, not convergence cost (run logged in README NEXT-UP #4).
- **Phase:** verify (investigate-design reached [READY] at cycle 6; auto-battle → proceed; no operator-soundness gate — corpus-evolution + code, no anneal-dev/spec touch)
- **Mode:** auto-battle
- **[READY] (cycle 6):** convergence CLEAN — intent carried-forward CLEAN (`.cycle-4.intent-falsification.md`; the 1 docstring finding closed behavior-preservingly) + mechanical ALL-HOLDS (`.cycle-6.falsification.md`, D1-D4 hold) + zero cycle-6 D-deltas. **Fresh-session implementability: PASSED** — per-step evidence: D1 (the regex fix) → `hooks/commit-msg:39-44` (RULE_CORPUS_PATTERN, the 2 `.claude-plugin` terms + `instance-template/.+\.md`); D2 (step-5 clause) → `development-process.md:798-819` (step 5, no formation clause — the insertion site) + `:60-64` (Checkpoint ≠ release-commit, cross-ref); D3 (comments) → `hooks/commit-msg:6-8` (docstring) + `:34-38` (merge-relocation) + `:39` (pattern note site); D4 (file F6) → a new `dev-notes/backlog/commit-msg-hook-kernel-source-overmatch.md`. All steps cite located reads. **Batch-economics datapoint:** this "light pair" still required cycles 1→6 (3 convergence-style passes finding F8/F9/F10 — instance-template sibling, exempt-only residual, stale docstring); the convergence machinery ran at full weight regardless of item size — batching did NOT reduce per-cycle convergence cost (noted for post-run).
- **Task:** Batch two [READY] commit/release-machinery items (the deferred batch-economics
  measurement — body-confirmed clean, coherent pair): (1) `commit-msg-hook-packaging-overmatch`
  — the commit-msg hook's RULE_CORPUS_PATTERN over-matches packaging manifests (exempt per the
  instantiation-guide carve-out) + disagrees with the pre-edit hook; (2)
  `release-commit-formation-from-checkpoints` — the release loop doesn't specify how the
  discharge-bearing release commit is formed from N checkpoints (resolution: "final discharge
  commit, hook-validated"). **Batch-economics datapoint:** track whether batching these two in
  one cycle is more economical than two separate runs.

## Requirements record (R1..Rn — the goal, separated from any proposed solution)

**Operator verbatim request:** "lets do next up" (remote-control) → resolved (backlog README
session-15 NEXT-UP #4, the deferred batch-economics measurement) to body-confirming + running a
clean comparable-weight light pair: `commit-msg-hook-packaging-overmatch` +
`release-commit-formation-from-checkpoints`. Auto-battle requested.

- **R1** — A commit touching ONLY packaging manifests (`.claude-plugin/marketplace.json`,
  `.claude-plugin/plugin.json`, and the like) does NOT require a Step-4 discharge artifact — they
  are exempt per the instantiation-guide carve-out (repo-local packaging, not rendered from spec).
- **R2** — The commit-msg hook's rule-corpus gating AGREES with the pre-edit hook on packaging
  manifests (both exempt `.claude-plugin/*`) — no file allowed-at-edit-time / gated-at-commit-time.
- **R3** — The release loop specifies HOW the discharge-bearing release commit is formed when the
  run's work spans N (possibly non-contiguous) `anneal-checkpoint:` commits, given no interactive
  rebase in-env — such that the Step-4 discharge is reliably hook-validated, not merely body-recorded.

---

## F-track (findings)

- **F1** [VERIFIED — non-issue] The commit-msg `RULE_CORPUS_PATTERN` over-matches packaging: it
  includes `\.claude-plugin/.+` and `plugin/\.claude-plugin/.+`, so a commit touching
  `marketplace.json`/`plugin.json` is treated as rule-corpus and requires a discharge. basis: located
  read `hooks/commit-msg:39-44` (the pattern). → grounds D1.
- **F2** [VERIFIED — non-issue] The pre-edit hook gates ONLY `plugin/skills/*` (PLUGIN_RENDER) +
  `spec/*` (SPEC_SOURCE) — it does NOT gate `.claude-plugin/*` → packaging passes the pre-edit hook
  but is gated by commit-msg = inconsistent (allowed at edit-time, gated at commit-time). basis:
  located read `hooks/skill-craft-pre-edit.py:44-52` (PLUGIN_RENDER_PATTERNS + SPEC_SOURCE_PATTERNS,
  no `.claude-plugin`). → grounds D1, R2.
- **F3** [VERIFIED — non-issue] The packaging carve-out is canonical: "The plugin's packaging — this
  file, the READMEs, `plugin.json`, and the like — is repo-local" (exempt). basis: located read
  `instantiation-guide.md:491-492`. → grounds D1, R1.
- **F4** [VERIFIED — non-issue] The checkpoint convention (`anneal-checkpoint:` prefix; checkpoint ≠
  release-commit) lives in `anneal-dev/spec/persistence.md:71-75` (kernel) + `development-process.md`
  ("Checkpoint ≠ release-commit"). The RELEASE-commit *formation* is a release-loop concern
  (development-process.md step 5), downstream of the checkpoints → scopable to development-process.md
  (corpus-evolution), leaving anneal-dev/spec UNTOUCHED. basis: located read
  `anneal-dev/spec/persistence.md:71-75` + `development-process.md:60-64` (Checkpoint ≠ release-commit).
  → grounds D2, the no-kernel-touch claim.
- **F5** [VERIFIED — non-issue] The env has no interactive rebase (squash-on-release unavailable); the
  `corpus-flows-redesign` run hit non-contiguous checkpoints split by a merge → amend-last is messier
  across a merge. So the "final discharge commit" resolution is the general one. basis: item
  `release-commit-formation-from-checkpoints.md:16-21,28-33` (the env constraint + the 3 options). → grounds D2.
- **F6** [VERIFIED — surfaced] (out-of-scope finding, will FILE) The commit-msg hook's
  `KERNEL_SOURCE_PATTERN` (`hooks/commit-msg:61-64`) treats `development-process.md`,
  `instantiation-guide.md`, `post-run-review.md` as method-kernel SOURCE (requires the Foundation-invariant
  check line), broader than the spec's method-kernel definition (`development-process.md:24-44`: kernel =
  `spec/*`, `foundation.md`, `anneal-dev/spec/*`; "anything else is corpus-evolution"). A genuine hook-vs-spec
  inconsistency, sibling of item (1) — but resolving it (is development-process.md method-kernel?) is a
  heavier methodology decision. basis: located read `hooks/commit-msg:61-64` (KERNEL_SOURCE_PATTERN) vs
  `development-process.md:24-44` (method-kernel definition). disposition: surfaced → file backlog item
  `commit-msg-hook-kernel-source-overmatch`; NOT fixed in this batch.

- **F7** [VERIFIED — addressed] (Missed-dependents, cycle 1) Removing `.claude-plugin` from
  RULE_CORPUS_PATTERN leaves a stale dependent: the merge-relocation comment at `hooks/commit-msg:34-38`
  lists `.claude-plugin` among where "anneal-dev's rule-corpus lives" — but `.claude-plugin/` is packaging
  (plugin manifests), not rule-corpus. No commit-msg test dependent exists (only `hooks/test_skill_craft_pre_edit.py`
  tests the pre-edit hook). `anneal-dev/spec/persistence.md:73` is already consistent with D2 (checkpoint ≠
  release-commit, no formation claim) → D2 needs no kernel touch. basis: search
  `grep -rniE 'claude-plugin|RULE_CORPUS_PATTERN' development-process.md instantiation-guide.md hooks/ spec/ anneal-dev/spec/`
  → only `hooks/commit-msg:36` (the comment) + :157 (usage); `release loop step 5` search → persistence.md:73 +
  development-process.md:60-64 (both consistent). disposition addressed-by → D1/D3 (the edit updates the comment).
- **F8** [PENDING] (cycle 2 intent-falsification, practice-4 class completion) `instance-template/CLAUDE.md` +
  `instance-template/README.md` reproduce the SAME over-match: commit-gated by `instance-template/.+\.md`,
  NOT pre-edit-gated, and repo-local housekeeping the SAME carve-out exempts (CLAUDE.md/README.md exempt per
  instantiation-guide:491-492 + development-process.md practice 5). `instance-template/spec/*.md` is genuine
  spec source (gated correctly by both). The over-match CLASS is packaging/housekeeping, not just `.claude-plugin`
  (practice 4: fix the class). basis: `ls instance-template/` (CLAUDE.md + README.md + spec/) + pre-edit-vs-commit
  pattern test. drives D1 extension (narrow `instance-template/.+\.md` to `instance-template/spec/.+\.md`).
  holds phase until D1 re-[VERIFIED].
- **F9** [PENDING] (cycle 2 intent-falsification, D2 completeness) D2's "re-touch the primary file" has a
  residual: a run whose ENTIRE diff is now-exempt (packaging-only) has no rule-corpus file to re-touch, so the
  final commit skips the hook and the discharge goes unvalidated. Clean reading: an exempt-only commit is by
  definition not rule-corpus, so it correctly needs no discharge. basis: hooks/commit-msg:371-375 (corpus-gate
  skip) + the post-D1 exempt-set. drives D2 clarification (re-touch the primary RULE-CORPUS file; an exempt-only
  run needs no discharge). holds phase until D2 re-[VERIFIED].
- **F10** [PENDING] (cycle 4 intent-falsification, Missed-dependents of the narrowing's own dependent) D1(ii)'s
  `instance-template/.+\.md` → `instance-template/spec/.+\.md` narrowing left the commit-msg DOCSTRING stale:
  `hooks/commit-msg:6-8` lists "instance-template/" (unqualified) as a detected rule-corpus dir, but only
  instance-template/spec/ is now gated. F7's search (`claude-plugin|RULE_CORPUS_PATTERN`) couldn't catch line 8;
  same staleness class D3 fixes at lines 34-38. basis: located read hooks/commit-msg:6-8 + `grep -rn instance-template hooks/`
  → :8 (docstring) + :42 (regex). drives D3 extension (update docstring 6-8). Behavior-preserving (comment-only).
  holds phase until D3 re-[VERIFIED].

---

## D-track (design decisions)

- **D1** [VERIFIED] **Item-1 fix: drop the packaging over-match from RULE_CORPUS_PATTERN.** Remove
  `\.claude-plugin/.+|plugin/\.claude-plugin/.+` from the commit-msg `RULE_CORPUS_PATTERN`
  (`hooks/commit-msg:43`), exempting packaging manifests (aligns with the carve-out F3 + the pre-edit
  hook F2). Keep gating `plugin/skills/.+\.md` (rendered skills), `spec/.+\.md`, `development-process.md`,
  `post-run-review.md`, `instantiation-guide.md`, `foundation.md`, `instance-template/.+\.md`. (a) target:
  `hooks/commit-msg` RULE_CORPUS_PATTERN regex; (b) shape: delete the 2 `.claude-plugin` alternatives;
  (c) accept: a commit touching only `.claude-plugin/*.json` requires no discharge; plugin/skills/* +
  spec sources still gated; (d) failure modes: a gap only if `.claude-plugin/` carried rendered-rule
  content — it carries JSON manifests only (no rule, no spec origin), so no gap; (e) basis: F1, F2, F3.
- **D2** [VERIFIED] **Item-2 fix: specify final-discharge-commit release formation in the release loop.**
  In `development-process.md` release loop step 5, specify: when an anneal-dev run's work lands across N
  (possibly non-contiguous) `anneal-checkpoint:` commits, the **release commit is a FINAL commit** carrying
  the Step-4 discharge that touches a rule-corpus file (re-touch the run's primary changed file, or a
  rule-corpus marker) so `hooks/commit-msg` validates the discharge — NOT a squash (needs interactive
  rebase, unavailable) and NOT an amend of the last checkpoint (messier across a merge). The
  `anneal-checkpoint:` commits remain as resume points (hook-skipped). (a) target: development-process.md
  release loop step 5; (b) shape: a new clause in step 5 specifying the final-discharge-commit formation;
  (c) accept: the release loop names how the discharge-bearing commit forms from checkpoints + why
  hook-validated; (d) failure modes: the final commit must touch a rule-corpus file or the hook won't fire
  — the clause states re-touch-the-primary-file; (e) basis: F4, F5. Scoped to development-process.md
  (corpus-evolution); anneal-dev/spec NOT touched (F4).
  considered: amend-last-checkpoint (rejected: messier across a merge, F5); squash-on-release (rejected:
  needs interactive rebase, unavailable in-env, F5).
- **D3** [VERIFIED] **Hook-comment note (item-1 clarity).** Add a brief comment at the
  `RULE_CORPUS_PATTERN` in `hooks/commit-msg` noting packaging manifests (`.claude-plugin/*`) are exempt
  per the instantiation-guide carve-out (so the pattern's intent + the deliberate non-gating is legible).
  (a) target: `hooks/commit-msg` comment above RULE_CORPUS_PATTERN; (b) shape: 1-2 line comment; (c) accept:
  the exemption rationale is documented at the pattern; (d) failure modes: none; (e) basis: F3 (the carve-out).
- **D3** [VERIFIED] (extended cycle 1 per F7) **Hook-comment work (item-1 clarity + stale-comment fix).**
  In addition to noting packaging is exempt per the carve-out at RULE_CORPUS_PATTERN: **fix the stale
  merge-relocation comment at `hooks/commit-msg:34-38`** which lists `.claude-plugin` among where
  "anneal-dev's rule-corpus lives" — `.claude-plugin/` is packaging (plugin manifests), not rule-corpus, so
  remove it from that list (or annotate packaging-exempt) so the comment matches the corrected pattern.
  basis: F3, F7.
- **D4** [VERIFIED] **File the surfaced third finding.** File F6 (the KERNEL_SOURCE_PATTERN-vs-spec
  method-kernel discrepancy) as a new backlog item `commit-msg-hook-kernel-source-overmatch` (sibling of
  the shipped item-1); NOT fixed in this batch (heavier methodology decision — is development-process.md
  method-kernel?). (a) target: a new dev-notes/backlog item; (b) shape: a [DESIGN] backlog item capturing
  F6; (c) accept: the finding is filed (no-silent-deferral); (d) failure modes: none; (e) basis: F6.

### Cycle-2 convergence D-deltas (flip [VERIFIED] to [INVALIDATED] to [PENDING]; re-formed below)

- **D1** [PENDING] (extended cycle 2 per F8; was [VERIFIED] cycle 1) **Item-1 fix: drop the packaging/housekeeping
  over-match CLASS from RULE_CORPUS_PATTERN.** (i) Remove `\.claude-plugin/.+|plugin/\.claude-plugin/.+`
  (packaging manifests). (ii) **Narrow `instance-template/.+\.md` to `instance-template/spec/.+\.md`** — gate the
  genuine spec-slot placeholders, exempt `instance-template/CLAUDE.md` + `README.md` (repo-local housekeeping,
  carve-out-exempt, F8). Keep gating `plugin/skills/.+\.md`, `spec/.+\.md`, `development-process.md`,
  `post-run-review.md`, `instantiation-guide.md`, `foundation.md`. (a) target: hooks/commit-msg RULE_CORPUS_PATTERN;
  (b) shape: delete the 2 `.claude-plugin` alternatives + narrow the instance-template term; (c) accept: a commit
  touching only packaging/housekeeping (`.claude-plugin/*`, `instance-template/CLAUDE.md|README.md`) needs no
  discharge; spec placeholders + renders + spec sources still gated; both hooks agree (R2); (d) failure modes: a
  gap only if these dirs carried rendered-rule content — manifests + housekeeping only, no rule/spec origin, so
  no gap; (e) basis: F1, F2, F3, F8.
- **D2** [PENDING] (clarified cycle 2 per F9; was [VERIFIED] cycle 1) **Item-2 fix: final-discharge-commit
  release formation (exempt-only case stated).** In development-process.md release loop step 5: when a run's work
  lands across N (possibly non-contiguous) `anneal-checkpoint:` commits, the **release commit is a FINAL commit**
  carrying the Step-4 discharge that **re-touches the run's primary RULE-CORPUS file** (so hooks/commit-msg's
  corpus-gate fires and validates the discharge) — NOT a squash (needs interactive rebase, unavailable) and NOT
  an amend (messier across a merge). A run whose ENTIRE work is exempt (packaging/housekeeping only) produces no
  rule-corpus commit and **correctly needs no discharge** (the hook's skip is right, not a gap — F9). The
  `anneal-checkpoint:` commits remain resume points (hook-skipped). (a) target: development-process.md release
  loop step 5; (b) shape: a new clause specifying the final-discharge-commit formation + the exempt-only case;
  (c) accept: step 5 names how the discharge-bearing commit forms from checkpoints, why hook-validated, and the
  exempt-only carve; (d) failure modes: closed — the "primary rule-corpus file" wording + the exempt-only
  statement remove the F9 residual; (e) basis: F4, F5, F9. Scoped to development-process.md (corpus-evolution);
  anneal-dev/spec NOT touched.
  considered: amend-last-checkpoint (rejected: messy across a merge, F5); squash-on-release (rejected: needs
  interactive rebase, unavailable, F5).

### Cycle-3 re-verification (working context locks the cycle-2 deltas; broken-basis check clean — D3/D4 unaffected)

- **D1** [VERIFIED] (cycle 3) Re-formed resolution sound: drops the `.claude-plugin` packaging terms + narrows `instance-template/.+\.md` to `instance-template/spec/.+\.md` — closes F8 (practice-4 class completion). basis: as D1 cycle-2 line.
- **D2** [VERIFIED] (cycle 3) Re-formed resolution sound: final discharge commit re-touches the primary RULE-CORPUS file; exempt-only run needs no discharge — closes F9. basis: as D2 cycle-2 line.
- **F8** [VERIFIED — addressed] (cycle 3) addressed by D1 extension (narrow instance-template gating). basis: D1 [VERIFIED] cycle 3.
- **F9** [VERIFIED — addressed] (cycle 3) addressed by D2 clarification (primary rule-corpus file + exempt-only carve). basis: D2 [VERIFIED] cycle 3.

### Cycle-4/5 — D3 docstring extension + re-verify

- **D3** [VERIFIED] (extended cycle 4 per F10; re-verified cycle 5) **Hook-comment work — now also the docstring.**
  In addition to the RULE_CORPUS_PATTERN carve-out note (cycle 1) + the lines 34-38 merge-relocation comment fix
  (F7): **update the docstring at `hooks/commit-msg:6-8`** — qualify "instance-template/" → "instance-template/spec/"
  so the hook's self-documentation matches the narrowed regex (D1(ii)). basis: F10. (Behavior-preserving comment work.)
- **F10** [VERIFIED — addressed] (cycle 5) addressed by D3 docstring extension. basis: D3 [VERIFIED] cycle 5.
- **F11** [VERIFIED — addressed] (release step-4 skill-craft self-review, subagent a9b4d9feb30083efb; notable, fix-now)
  D2's "primary changed rule-corpus file" was naked-judgment + too narrow (the commit-msg hook fires on ANY in-diff
  rule-corpus path). Fixed at development-process.md:825 → "any rule-corpus file the run changed". basis: anti-patterns.md Naked-judgment.
- **F12** [VERIFIED — addressed] (release step-4 skill-craft self-review; nit, fix-now) D2's "entire work is exempt
  (packaging/housekeeping only)" was a judgment label; step 4 states the mechanical N/A condition observably. Fixed at
  development-process.md:831 → "final diff contains no rule-corpus file". Both behavior-preserving (naked-judgment → mechanical)
  → delta-verify: findings closed, the clause + the 1 keep-as-is (WHY-parentheticals) unchanged, AST still OK → clean.
