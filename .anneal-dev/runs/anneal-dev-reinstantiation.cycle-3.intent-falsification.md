# Intent-falsification-pass artifact — anneal-dev-reinstantiation, cycle 3

Fresh-context subagent (agentId a4747be325863c5d7). Criteria-first attack on
whether the locked design (D1–D8) serves the requirements record (R1–R4).

## Criteria derived (criteria-first, before reading D1–D8)
- R1 → every session-5/6/7 delta with a plugin home appears in the render; the
  named additions present; nothing plugin-homed silently excluded.
- R2 → no lossy render; fidelity verified clause-by-clause in a separate context
  (a verify-phase obligation).
- R3 → a committed (tracked) decision exists on the carve-out, not an open
  question.
- R4 → the running cache matches the verified render.

## Per-R# attack lines
- `{R1, attack: git diff --stat d9033ee HEAD (10 files) ∩ plugin render-site
  greps (foundation-invariants/validation-watch/Q7 = zero plugin occurrences;
  verify.md "three checks" L32/34 confirms D4 target), every plugin-homed delta
  maps D2–D6, every exclusion dev-notes/maintainer-side, served}`
- `{R2, attack: R2 + verify.md:32-57 (clause-by-clause fidelity = battery
  check-(a), separate-context) — a verify-phase obligation, correctly not closed
  at convergence, served}`
- `{R3, attack: self-render-urgency.md:24-36 (candidate-fix = practice-8 classify
  of a policy edit) vs D7 (committed defer) — committed decision per core §1/§5.2,
  served}`
- `{R4, attack: known_marketplaces.json (github source) + installed_plugins.json
  (cache built from github clone) — R4 unmeetable by local cache write; D8 records
  it operator-gated, finding (F-a)}`

## Per-finding lines
- `{F-a: R4 not achieved within the run (terminates at verified render + version
  bump; reinstall = downstream github-release + operator push), criterion: R4,
  refutation: installed_plugins.json installPath cache/.../0.1.2 + known_marketplaces
  source=github, route: [VERIFIED — surfaced]}` — honest residual, not a defect
  (the design correctly does NOT auto-push). No coupling-shape reduction (D8's
  github-coupling basis is correct).
- `{F-b: R3 "settled" holds only as a recorded defer while the carve-out policy
  stays an OPEN backlog item, criterion: R3, refutation: self-render-urgency.md:3
  (Status: OPEN) + D7 ("Keep that item OPEN"), route: [VERIFIED — surfaced]}` —
  R3's own wording ("whether to land now or resolve immediate-only") is answered
  by D7's defer-decision; intent-depth has no runnable adjudication.

## Routing summary
Zero `mechanical-falsification-candidate` findings → **zero intent-delta** → the
mechanical falsification pass runs this cycle (not skipped). Both findings route
`[VERIFIED — surfaced]`, terminal, do not hold the phase.

## Bottom line
The design serves its intent. Scope (D1) misses no session-5/6/7 delta R1 demands.
Nothing must change. The one judgment the operator's soundness pass should weigh:
whether R4's "reinstalled / running cache matches its own method" is *met* by a run
that stops at verified-render + version-bump and hands activation to an
operator-authorized release — "met" vs "made ready." The pass feeds that judgment;
it does not make it.
