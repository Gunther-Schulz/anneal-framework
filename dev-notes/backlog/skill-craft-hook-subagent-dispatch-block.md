# skill-craft pre-edit hook blocks subagent-dispatched spec edits

**Status:** OPEN — **operator-flagged NEXT-UP (2026-06-02).** Surfaced as an
impl-phase loopback finding (F10) during the `framework-spec-cleanup-pipeline`
anneal-dev run (the §4 re-derivation): the impl Unit-1 subagent could not land
any edit. **Mechanical/dispatch blocker, not a spec problem** — the §4 design was
[VERIFIED]/clean; the run continued via spawn-fallback (orchestrator edits
in-context). Fix lands in `hooks/skill-craft-pre-edit.py` (machinery, NOT
rule-corpus → not itself skill-craft-gated).

## The finding (grounded)

`hooks/skill-craft-pre-edit.py` denies every `Edit`/`Write` to `spec/*` (and the
other gated corpus paths) **when the edit comes from a dispatched subagent**.
Effect: subagent `af60f2dc239967b6b` got 5/5 denials on `spec/core.md`, every
skill-craft-invocation pattern, clean `git status --porcelain spec/core.md`
throughout.

**Mechanism (orchestrator-confirmed by reading the hook, lines 155–208).** The
gate finds the last operator-prompt boundary by scanning `user` events and
*skipping* those with `isMeta is True` (line 162) or `origin` set (line 164),
then scans forward for a skill-craft `Skill` `tool_use`. In the subagent /
sidechain path, the skill-craft Skill **result** arrives as a text-bearing
`user` event **without** `isMeta=True`, so the hook mis-reads it as a fresh
operator-prompt boundary, moves `last_prompt_idx` *past* the preceding Skill
`tool_use`, and the forward scan finds nothing → deny. The main-session path
works because its Skill results carry `isMeta=True` (so they're skipped, and the
real boundary + the Skill invocation are seen).

## Impact

anneal-dev's **subagent-dispatch impl model is blocked for every `spec/*`
(method-kernel) edit** — not just one unit. Until fixed, method-kernel impl must
use the **spawn-fallback** (orchestrator implements in-context), which waives the
impl-isolation guarantee (backstopped by the isolated verify + the kernel-
independent review). Corpus-evolution edits to `plugin/skills/*/` from a subagent
hit the same gate and the same block.

## Contradiction to reconcile (do NOT skip)

The archived `archive/anneal-dev-impl-skillcraft-gate.md` concluded **"the gate
IS satisfiable from a subagent"** (and was the first method-kernel self-hosting
anneal-dev run, anneal-dev `ee9e2e6`). This finding **empirically contradicts**
that. Two hypotheses to test:
- (a) the harness transcript shape **changed since 2026-06-02** (the `isMeta`
  flag on subagent Skill-result `user` events), so a once-working gate regressed; or
- (b) the prior conclusion **never actually landed a subagent `spec/*` edit** — it
  may have verified the dispatch-*brief* change (the brief now instructs skill-craft
  invocation) without proving a subagent edit clears the hook, or used the
  spawn-fallback. If (b), the archived item's conclusion was wrong and its "DONE"
  needs re-opening.
Resolve by checking the `ee9e2e6` run's actual edit path (subagent vs main-session)
before deciding whether this is a regression or a never-true claim.

## Fix direction (candidate — not locked; design at full discipline)

The boundary detection must not treat a subagent-path Skill/tool-result `user`
event as an operator prompt. Options (weigh at design time):
1. **Structural boundary detection** — when locating the last operator prompt,
   skip text-bearing `user` events that are tool/skill *results* (detect by
   structure — e.g. content carries a tool_result/skill-output shape — not solely
   by the `isMeta` flag the subagent path omits). Most robust; hook-local.
2. Have the harness flag subagent Skill-result `user` events `isMeta=True` (parity
   with the main path) — not hook-local; depends on harness behavior we don't own.
3. Per-transcript heuristic when the hook runs against a subagent transcript.
Option 1 is the thorough, self-contained fix; it also wants a regression guard
(a test exercising a synthetic subagent-shaped transcript).

## Relates to
- `skill-craft-pre-edit-hook-findings.md` — same hook (Findings 1 done / 2 Bash-bypass / 4 spec-origin over-match open); this is a distinct failure mode (subagent-path false-block, not gating-scope).
- `archive/anneal-dev-impl-skillcraft-gate.md` — the contradicted "gate IS satisfiable from a subagent" conclusion.
- `framework-spec-cleanup.md` — the run that surfaced this (its impl is proceeding via spawn-fallback).
