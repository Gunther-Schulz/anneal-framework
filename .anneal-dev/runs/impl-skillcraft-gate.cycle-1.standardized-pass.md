# impl-skillcraft-gate — cycle 1 standardized inspection pass

Change-set under design: a dispatch-brief binding (spec/bindings.md) + amendments to 2 renders (implement.md §a, SKILL.md:71). In-scope lenses:

- **Bloat** → clean. basis: D2 — the binding carries one load-bearing rule (invoke skill-craft before edits) + cross-refs; no restatement/hedge/narration committed.
- **Fragmentation** → clean. basis: D2's committed cross-ref shape — `development-process.md` practice 5 already states the operator-session gate; the anneal-dev binding is the subagent-dispatch sibling (different context) and cross-references practice 5 + skill-craft rather than restating, so the corpus holds one canonical gate-statement, not two drifting copies.
- **Leakage** → clean (N/A by level). basis: lens Scope — Leakage fires only on domain-general files; the binding lands in `anneal-dev/spec` (a domain-specific instance file), where domain-specific content is in-scope.
- **Missed-dependents** → clean. basis: D1's `rg` — the dispatch-brief load-instructions render to exactly implement.md:170-174 + SKILL.md:71; no paraphrased restatement elsewhere.
- **Unenforced-rule** → clean. basis: the rule's enforcement IS the pre-edit hook (`skill-craft-pre-edit.py`) — a subagent editing without invoking skill-craft is visibly blocked; the gate is the un-fakeable artifact.
- **Undefined-shorthand** → clean. basis: the binding uses established terms (skill-craft, rule-corpus edit, Skill tool, dispatch); no new coined shorthand.

Out of scope this cycle (applied at impl write-time + verify): **Lossy-render** (no source-rule render committed yet), **Over-claimed-verification** (no verification claim recorded yet).
