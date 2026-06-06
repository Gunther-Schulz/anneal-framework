# campaign2-completeness-rigor — impl plan (at [READY])

Dispatch units derived from the locked design. **All units touch `spec/core.md` (one file) across different sections → intra-file integration hazard → SEQUENTIAL** (§4.2.1: a unit whose disjointness is not search-established is sequential; same-file section edits are not search-established-disjoint for concurrent integration). Run-level: 5 units, all sequential. Each unit's secondary-file touches (modules.md / lens-set.md / glossary.md) ride with the unit.

- **U1 [D1, D1.1, D2.1, D8-cross-file]** — `core.md` §3.2.2 (dependent-class generalization + behavior-change test-impact sub-clause) + `anneal-dev/spec/lens-set.md` Missed-dependents (path-hardcoder + producer↔consumer forms, mapped to existing coupling shapes) + `spec/glossary.md` (Coupling-shape subclass note + cross-file term entries). first; sequential.
- **U2 [D3]** — `core.md` §4.1.4 (narrow the [CONDITIONAL]/[AUTO-ACCEPTED] exemption to the assumption shape) + `modules.md` §3.4 (candidate-set extends to conditional entries' technical shapes). after U1; sequential (shares core.md).
- **U3 [D4.1]** — `core.md` §4.1 Design step (during-formation rival-carrying) + `modules.md` §3.1 (`considered` required-where-genuine-rivals). after U2; sequential.
- **U4 [D5, D5.1, D8-triage-home]** — `core.md` §4.2.7 + §4.3 + §4.1.4 (standard in-loop root-cause triage; actor = orchestrator on loopback-receipt). after U3; sequential (shares §4.1.4 with U2).
- **U5 [D6]** — `core.md` §4.2.8 (green-on-commit at the checkpoint). after U4; sequential.

**D7** (render deferral) is not an impl unit — it queues the source-delta to campaign ⑥ render-debt post-verify.

**Green-on-commit (D6) self-application note:** per D6, each unit's checkpoint must pass the project's executable verification before landing. For this spec corpus the executable verification = the kernel-independent verify battery (render-fidelity / coherence / skill-quality) at the verify phase; per-unit checkpoint green = the unit's edits leave the corpus parseable + the run-gate/commit-msg hooks pass. (The spec corpus has no unit-test suite; the green-gate binds to the hook + structural checks.)
