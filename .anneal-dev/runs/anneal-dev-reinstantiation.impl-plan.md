# Impl plan — anneal-dev-reinstantiation

**6 dispatch units, organized PER PLUGIN FILE** (the disjointness axis). Each
unit renders the slice of every design decision that lands in its file, from the
cited live-spec source clause, faithfully (no lossy-render). **Disjointness
basis:** the units partition the touched file set {SKILL.md,
investigate-design.md, verify.md, foundations.md, tracker.md, plugin.json} — no
two units write the same file (`grep`-confirmed per-file scope below). → **all 6
units parallel-eligible** (source is read-only; renders land in disjoint files).
Each subagent invokes **skill-craft before editing** (rule-corpus edit gate,
`bindings.md` Skill-craft invocation) and self-checks its change-set with the
write-time lenses (Lossy-render, Missed-dependents, Undefined-shorthand,
Over-claimed-verification) before returning.

- **U1 — `SKILL.md`** (renders D5 + D6 + the SKILL rename site). first / parallel.
  - D5: model-tier dispatch floor as a dispatch-wide rule near the dispatch
    brief (anchor L71-75); bootstrap "three placeholder files"→"four" +
    `model-tier.md` placeholder block (anchor L290-294). Source:
    `anneal-dev/spec/bindings.md` "Dispatch model tier" (L249-260) +
    "Operator-editable artifacts"/"four placeholder files" (L284-305);
    `anneal-dev.config/model-tier.md`.
  - D6: closed-artifact State summary dual-citation (intent-falsification +
    mechanical falsification artifacts, or recorded skip; anchor L184-187);
    auto-battle mode-keyed text carries `[VERIFIED — surfaced]` beside
    `[VERIFIED — deferred]` (anchor L243-249). Source: `spec/modules.md` §3.1;
    `spec/core.md` §4.1.4 / §5.2.
  - Rename: L186 "falsification-pass" → "mechanical falsification-pass".

- **U2 — `phases/investigate-design.md`** (renders D2 + D4). first / parallel.
  - D2: the convergence cycle gains the **intent-falsification pass** (sequenced
    FIRST; mechanical second; skip-on-intent-delta carve-out); rename
    "falsification pass" → "mechanical falsification pass" across all 35 sites;
    add the intent-falsification **dispatch-brief variant** (carries the
    requirements record as criteria source). Source: `spec/core.md` §4.1.4;
    `spec/modules.md` §3.3 (dispatch brief) + §3.4.1.
  - D4: **requirements-record capture** rule (R1..Rn + verbatim request,
    header-adjacent), placed after the Scope section (mirrors core §4.1 order).
    Source: `spec/core.md` §4.1.

- **U3 — `phases/verify.md`** (renders D4 + D3). first / parallel.
  - D4: "three checks" → "**four checks**"; insert **requirements-coverage** as
    check 2 (per core §4.3 order) incl. the soft verbatim-request leg. Source:
    `spec/core.md` §4.3 (anchor verify.md L32-34/L143).
  - D3: the finding-ledger format example may carry a `[VERIFIED — surfaced]`
    line (forward-compat; the rule "[VERIFIED] without disposition = malformed"
    already covers it). Source: `spec/core.md` §5.1.

- **U4 — `references/foundations.md`** (renders D3 + D4 + D5). first / parallel.
  - D3: disposition enum "three cases" → "**four**" (+ **surfaced**); F-entry
    closure "four paths" → "**five**"; [READY] gate — `[VERIFIED — surfaced]`
    terminal, does not hold the phase. Source: `spec/core.md` §5.1/§5.3/§4.1.1.
  - D4: requirements record in **the model** (task-input, header-adjacent, read
    by isolated verify). Source: `spec/core.md` §4.1.
  - D5: Operator-editable artifacts set three → **four** (+`model-tier.md`);
    name the dispatch model-tier slot. Source: `anneal-dev/spec/bindings.md`
    Operator-editable (anchor foundations.md L444-446).

- **U5 — `references/tracker.md`** (renders D2 + D3 + D4). first / parallel.
  - D2: rename "The falsification-pass artifact" → "**The mechanical
    falsification-pass artifact**" + the **skip carve-out**; ADD "**The
    intent-falsification-pass artifact**" section (per-R# attack line + per-finding
    route line); persistence — add `.cycle-<N>.intent-falsification.md`. Source:
    `spec/modules.md` §3.4/§3.4.1; `anneal-dev/spec/persistence.md`.
  - D3: disposition enum "addressed / non-issue / deferred" → +**surfaced**.
    Source: `spec/core.md` §5.1.
  - D4: requirements record persisted header-adjacent (Persistence section).
    Source: `spec/core.md` §4.1; `spec/modules.md` §3.1.

- **U6 — `.claude-plugin/plugin.json`** (renders D8). first / parallel.
  - Version `0.1.2` → `0.1.3`. (Trivial; no skill-craft gate — not a skill file.)

## Sequencing
All 6 units are first/parallel (file-disjoint). No dependency ordering. Verify
(separate-context render-fidelity battery) is the safety net for R2.
