# commit-msg hook over-matches packaging manifests (+ disagrees with the pre-edit hook)

**Status:** [READY] — small hook-consistency finding, surfaced at the `corpus-flows-redesign`
C1b release (2026-06-03). Methodology-correctness → operator-judged. Not blocking.

## What
The `commit-msg` hook's `RULE_CORPUS_PATTERN` includes `\.claude-plugin/.+` and
`plugin/\.claude-plugin/.+` — so a commit touching `marketplace.json` or `plugin.json`
(plugin **packaging** manifests) is treated as a rule-corpus commit and **requires a Step-4
discharge artifact**. But packaging files are explicitly **exempt** per the instantiation-guide
carve-out ("Plugin packaging files — README.md, plugin.json, CLAUDE.md and similar repo-local
files — are exempt; packaging is repo-local, not rendered from spec"). So the hook over-matches:
it gates packaging that has no rendered-rule content + no spec origin.

Encountered at C1b: committing anneal-framework's root `.claude-plugin/marketplace.json` required
`git commit --no-verify` (packaging — discharge genuinely N/A). The bypass was legitimate, but it
shouldn't have been needed.

## Also: the two hooks DISAGREE
The **pre-edit** hook (`skill-craft-pre-edit.py`) EXEMPTS `.claude-plugin/*` (its patterns are
PLUGIN_RENDER `plugin/skills/*` + SPEC_SOURCE `spec/*.md` etc. — packaging manifests match neither,
so they pass). The **commit-msg** hook GATES `.claude-plugin/*`. Same packaging file: allowed at
edit-time, gated at commit-time. Inconsistent.

## Candidate fix
Align the commit-msg `RULE_CORPUS_PATTERN` with the packaging carve-out + the pre-edit hook:
gate `plugin/skills/*` renders + `spec/*`/dev-process/etc. spec sources, but EXEMPT packaging
manifests (`marketplace.json`, `plugin.json`) — they carry no rendered rule + no spec origin.
(Keep gating `plugin/skills/*` content.)

## Relates to
- `skill-craft-pre-edit-hook-findings.md` — sibling hook-findings item (that one is the PRE-EDIT
  hook: Bash-bypass + spec-origin over-match; this is the COMMIT-MSG hook + the inter-hook
  inconsistency).
- `hooks/commit-msg` (RULE_CORPUS_PATTERN), `hooks/skill-craft-pre-edit.py`,
  `instantiation-guide.md` (the packaging carve-out) — edit sites.
- Surfaced by `corpus-flows-redesign` C1b. Dev-machinery finding → anneal-dev + kernel-independent verify.
