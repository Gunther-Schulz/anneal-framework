# Impl plan — harness-tool-runstate-unsourced

**1 dispatch unit**, single container (`anneal-framework`), sequential/single → in-place
under the Integrity check. Touches rule-corpus (`instantiation-guide.md`) → the dispatched
subagent invokes skill-craft before editing. **STAGED-ONLY (no commit)** — applying prior-run
F9/D7: the commit-msg discharge hook makes a pre-verify rule-corpus checkpoint commit
impossible; the orchestrator commits once post-verify with the discharge.

State marker (HEAD before dispatch): `b398227dfd7ed6fdeb02bf5b3f07f2807f56c1fd` on branch
`harness-tool-runstate-unsourced`.

## Unit U1 — the harness-disambiguation render-time note (implements D3 within D1's scope)
- **Implements:** D3 (the note). D1 = scope; D2 = home decision (guide-not-spec).
- **Container:** `anneal-framework` (1).
- **Element scope:** `instantiation-guide.md` ONLY — add a harness-general render-time note near
  the §2 run-artifact-persistence slot (~:84-92), without renumbering sections.
- **Contract scope (locked contract honored):** D3 — the note states (harness-GENERAL, naming NO
  specific tool): when the target harness provides ambient task/run-state-tracking tools, the
  rendered protocol states run-state lives in the instance persistence mechanism (source of truth,
  core.md §6 + the persistence slot), not those tools (which may serve harness-level work outside
  the protocol). This sources the existing rendered SKILL.md blocks. Leakage discipline: no tool
  name in the guide note.
- **Out of scope:** the 4 instance SKILL.md blocks (= Phase B re-render); any spec/foundation edit
  (D2 ruled out option a).
- **Persistence:** STAGED only; orchestrator commits post-verify with discharge.
