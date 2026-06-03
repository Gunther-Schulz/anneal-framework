# FB-3. Instance specs should cite framework glossary terms, not section-numbers

**Status:** RESOLVED 2026-06-03 — settled via the `cite-glossary-not-section-numbers`
anneal-dev run (merged `b56f7d8`): the §-number firewall rule (`instantiation-guide.md`
§3) + its grep-check + 3 glossary headwords (evidence-bearing-artifact rule / standardized-pass
findings artifact / post-run review) + the glossary-as-instance-facing-interface naming
(`spec/README.md`). Run tracker: `.anneal-dev/runs/cite-glossary-not-section-numbers.md`.
The caveat's binding-table-completeness residual spun off to
`glossary-binding-table-interface-completeness.md`. Archived.

Original detail: `planner-instance-exploration.md` finding 4. (Sibling of the slot-collapse fork; both informed by the planner derivation.)

**Gap.** Instance specs (clippy) reference framework **section numbers**
(`core.md §3.2`, `§4.1.4`) and re-explain internal mechanisms — brittle
coupling to framework layout. The clean rule: instance specs cite
framework **glossary terms** (locked, stable vocabulary), never section
numbers — the glossary is the **instance-facing interface** (it owns the
term→section mapping, so instances decouple from layout churn while
keeping traceability: the term *is* the trace).

**Caveat:** the glossary isn't a *complete* instance-facing contract
today (the bindings table binds terms — e.g. "executable verification" —
that aren't full glossary entries). Making it complete is real work;
scoping it is part of what the planner derivation exposes.
