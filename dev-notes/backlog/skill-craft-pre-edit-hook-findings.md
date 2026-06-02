# skill-craft-pre-edit hook — over-broad path match + bypassable + subagent-reliability

**Status:** Finding 1 **DONE** (2026-06-01); Finding 3 **RE-GROUNDED 2026-06-02 → MOOT as a hook bug** (the boundary detector handles the current harness shape correctly — empirical test below); residual reframed to [[anneal-dev-impl-skillcraft-gate]]. Findings 2 + 4 open. Surfaced
2026-06-01 by the anneal-dev pass-1 subagent (which tripped the gate writing
draft spec files and routed around it). The path-narrowing (Finding 1) is done,
so the de-pollution cycles' `spec/*.md` edits gate correctly without
false-positives on `dev-notes/` drafts. The hook change is committed (ad29c27).
Relates to `framework-dev-as-anneal.md`, `contract1-depollution-cluster.md`.

> **Finding 3's "MOOT — boundary detector handles the current harness shape
> correctly" is CONTRADICTED (2026-06-02).** The `framework-spec-cleanup-pipeline`
> run's impl Unit-1 subagent got 5/5 `spec/core.md` Edit denials; reading the hook
> confirmed the subagent-path boundary detection misfires (Skill-result `user`
> events lack `isMeta=True`). The subagent-reliability concern is REAL, not moot —
> tracked now as the dedicated next-up item
> `skill-craft-hook-subagent-dispatch-block.md`, which also carries the
> reconciliation with the archived `impl-skillcraft-gate` "satisfiable from a
> subagent" conclusion.

The hook is `hooks/skill-craft-pre-edit.py` (development-process.md practice 5:
gates Edit/Write to rule-corpus files behind an in-turn skill-craft invocation).

## Findings (ranked)

1. **Over-broad path pattern — DONE (2026-06-01).** The gate matched
   `/spec/.+\.md$`, which caught `dev-notes/derivation-pass1/spec/` — a scratch
   draft, not canonical rule-corpus. Fixed by adding a `NON_CORPUS_PATTERNS`
   exclusion (`/dev-notes/`) checked before corpus classification, so an
   excluded path never gates. Verified: `dev-notes/**/spec/` now passes; canonical
   `anneal-framework/spec/`, instance `coding-clippy/spec/`, and plugin renders
   still gate. Kept minimal — `dev-notes/` is the one concrete non-corpus area
   (its README says "not the spec"); no speculative scratch-dir list (practice 7).
2. **`mv`/`cp` bypass hole (note).** The gate is a PreToolUse hook on Write/Edit;
   it does not gate Bash file moves, so writing to a non-matching path and
   `mv`-ing into place circumvents it (which the pass-1 subagent did). Fully
   closing this is not cheap (can't gate all Bash without heavy friction) —
   record as a known limitation; the real backstop stays release-loop step 4
   (post-edit skill-craft review) + operator approval.
3. **Subagent-context reliability — ROOT-CAUSED 2026-06-02 (fix open).**
   Diagnosed by the anneal-dev step-5 render subagent (`ad0442118fb42bce8`),
   which tripped it again. Root cause: the boundary detector
   (`hooks/skill-craft-pre-edit.py:156-176`) skips Skill-output user events by
   keying on `isMeta is True` (comment `:144-145`). In a **subagent**
   transcript the Skill-tool result is recorded `role=user, isMeta=None,
   origin=None, content=[{type:text}]` — so it is NOT skipped and IS classified
   as the last operator-prompt boundary. Every same-turn skill-craft `Skill`
   `tool_use` therefore lands BEFORE the boundary → the gate can never
   discharge from a subagent. (Main context works because there Skill outputs
   are `isMeta=True` and correctly skipped — why prior main-context spec edits
   gated fine. Hook-source half verified against the file; the `isMeta=None`
   runtime shape is the subagent's transcript replication, not re-confirmed
   from main context.) **Consequence:** subagent-dispatched rule-corpus edits —
   including the framework's own impl-phase dispatch (`core.md` §4.2) — cannot
   satisfy the gate; route via the spawn-fallback (main-context edit, where the
   gate works) or accept the Finding-2 Bash-bypass under the release-loop-step-4
   backstop (the step-5 render did the latter, then ran the separate-context
   verify). **Fix shape (own cycle; the hook is tooling, not rule-corpus, so
   ungated):** skip Skill/tool-result user events regardless of `isMeta`
   (detect the Skill-result / `tool_result` content shape and treat as
   non-prompt), rather than relying on the `isMeta=True` assumption.

   **RE-GROUNDED 2026-06-02 (this session) — does NOT reproduce; MOOT as a hook
   bug.** The root-cause above was flagged "not re-confirmed"; re-confirming
   empirically (dispatched a subagent that invoked skill-craft via the Skill tool,
   then ran the actual `has_skill_craft_invocation_this_turn` against its real
   transcript) → the gate returns **True**. Current harness shape: a Skill *result*
   is a `tool_result` block (`isMeta=None`, correctly NOT a text-prompt) and the
   skill *content* is a separate `isMeta=True` event (correctly skipped); the task
   message is the boundary at index 0. Across four real subagent transcripts: no
   fail-opens, no false-positives, boundary correct every time. The harness
   transcript shape changed since the dogfood, incidentally fixing the
   misclassification — **there is no hook fix to make.** Residual (reframed):
   anneal-dev's impl dispatch loads its references but does not *invoke* skill-craft
   via the Skill tool, so a dispatched rule-corpus edit has no Skill `tool_use` and
   the gate correctly blocks it → [[anneal-dev-impl-skillcraft-gate]].
4. **Spec-origin-trace fires on non-anneal-instance skills (over-match,
   2026-06-02).** The PreToolUse spec-origin-trace demand (practice 5
   "spec-origin grounding for plugin edits") matched a `plugin/skills/*/` edit
   in a **sibling repo** (`bildhauer`), demanding an anneal framework/instance
   spec-origin that cannot apply — bildhauer is a standalone skill, not an
   anneal-rendered plugin. The skill-craft *invocation* gate firing there is
   arguably correct (any skill edit should route through skill-craft); the
   **spec-origin-trace** half is the over-match (same path-scoping class as
   Finding 1). Scope the spec-origin-trace to anneal-instance plugin paths
   (clippy / daneel / … renders), not every `plugin/skills/*/` on disk.
   Surfaced editing bildhauer C6.
