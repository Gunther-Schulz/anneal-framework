# clippy-reinstantiation — impl plan

11 dispatch units = the 11 render targets (D1'' scope). Each unit: a subagent loads the **live co-located method** (self-hosting — `anneal-framework/spec/*`, not the lagging plugin) + the cited source sections + reads the current target + faithfully re-renders + **invokes skill-craft before the edit** (rule-corpus edit, project `CLAUDE.md`) + self-checks (Lossy-render, Missed-dependents, Undefined-shorthand, Over-claimed-verification) + commits green (per-unit checkpoint, §4.2.8). Cross-cutting carried by every unit: **D3'** (citation-firewall — convert this file's framework §-cites to glossary terms) + **D4** run-state binding (U5/U10) + **D15** budget (no de-bloat of U4/U5/U7; flagged only).

**Run-level:** 10 units parallel-eligible + 1 dependency (U2←U1). **Disjointness basis:** the 11 targets are pairwise-distinct file paths (D1'' enumerates 11 distinct paths; `find` inventory cycle-6 confirms distinctness); concurrent edits to distinct files in the one container (coding-clippy) don't clash. Integration per the integrity check (§4.2.4); run-state dir N/A (coding-clippy is the work product, anneal-dev run-state lives in anneal-framework).

| Unit | Target | Decision(s) | Depends | Parallel |
|---|---|---|---|---|
| U1 | `coding-clippy/spec/lens-set.md` | D10' (co-producer/emitted-effect + firewall) | first | parallel w/ U3–U11 |
| U2 | `…/plugin/skills/clippy/references/lenses.md` | D11 (render from U1) | **after U1** | sequential after U1 |
| U3 | `…/references/foundations.md` | D5 (§3.1 relabel + §3.2.1 provenance + §3.2.2 full + Purpose/Mechanism + firewall) | first | parallel |
| U4 | `…/phases/investigate-design.md` | D6' (requirements record + intent pass + L1 + coupling-rename + V-5 strip + firewall) | first | parallel |
| U5 | `…/phases/implement.md` | D7 (loopback triage + green-checkpoint + run-state excl + firewall) | first | parallel |
| U6 | `…/phases/verify.md` | D8 (requirements-coverage + loopback triage) | first | parallel |
| U7 | `…/references/tracker.md` | D9 (surfaced + deferred-(c) + intent artifact + intent-clean header + considered + coupling-rename) | first | parallel |
| U8 | `…/references/post-run-review.md` | D13 (vw folder + Q7 lifecycle walk + firewall) | first | parallel |
| U9 | `…/SKILL.md` | D14' (convergence status + V-9 strip + firewall) + D2 (de-bloat ≤~2000w, skill-craft-gated) | first | parallel |
| U10 | `coding-clippy/spec/bindings.md` | D12' (firewall §→glossary + run-state binding D4) | first | parallel |
| U11 | `coding-clippy/spec/README.md` | D17 (vw path repoint) | first | parallel |

After all units: this run's **render-fidelity verify** (isolated subagent) — clause-by-clause vs source per file + the **D16 firewall coherence check** (`rg '(core|modules)\.md[^\n]{0,4}§'` over clippy instance specs + rendered files → empty) + clippy's own structural integrity (skill-craft form on SKILL.md).
