# clippy-write-side-boundary — cycle 2 intent-falsification artifact

Fresh-context subagent (opus), criteria-first. Method grounded in live core.md §4.1.4 + modules.md §3.4.1.

## Per-R# attack lines
- `{R1, attempted-refutation: D1 write-side question vs F29 shape — direct match on all 3 elements (overwriting merge sink / producer non-authoritative branch incl unauthored callers / clobbers more-authoritative value), outcome: served}`
- `{R2, attempted-refutation: checked D2's cited render target — `references/lenses.md:130-151` does not resolve; actual render `plugin/skills/clippy/references/lenses.md`, Silent-substitution at :167-187, :130-151 = Thorough-fix/Target-locality, outcome: FINDING (F-b)}`
- `{R3, attempted-refutation: extend-vs-new Pareto check — extend reduces (one lens/principle) IFF read+write are one question; attacked hard (F-a), outcome: FINDING (F-a)}`
- `{R4, attempted-refutation: acceptance triad — skill-craft one-coherent-question deferred to impl w/ no recorded design-time PASS criterion; the crux (F-a) is what skill-craft must adjudicate, outcome: FINDING (F-a)}`

## Per-finding lines
- `{F-b, criterion-attacked: R2, refutation: find -name lenses.md → single hit plugin/skills/clippy/references/lenses.md; :167-187 = Silent-substitution, :130-151 = Thorough-fix/Target-locality, route: mechanical-falsification-candidate}` → flips D2 (target-existence: cited render location wrong).
- `{F-a (CRUX), criterion-attacked: R3+R4, refutation: D1 write-side question (clobber/destroy, fix=COALESCE/gate, fire-site=write/producer) vs read-side (propagate, fix=surface, fire-site=read/consumer) — disjoint fire-sites/harm/fix under a shared abstraction; BUT read-side lens already carries 5 heterogeneous sub-shapes under one question, so write-clobber-as-one-more-shape is in-form. Defensible-as-extend, contestable — skill-craft+operator call, route: [VERIFIED — surfaced]}` → RESOLVED by operator (bidirectional = core tenet → extend confirmed).
- `{F-c, criterion-attacked: R1 (catch the CLASS), refutation: D1 exemplars lean SQL-merge; class is broader (cache last-writer-wins, idempotent-PUT/object-store, dict assignment, ORM save() nulling unset cols); keep the question mechanism-general w/ SQL as exemplar, route: [VERIFIED — surfaced]}` → fold into D1.
- `{F-d, criterion-attacked: R3 (fragmentation), refutation: D1 scope-adds "producer branch at referenced-but-unauthored call site" — same site-class Branch-coverage ranges over; different questions (is-branch-evidenced vs does-its-value-clobber-on-write); acceptable, keep distinct in render, route: [VERIFIED — surfaced]}` → render note.

## Verdict
NOT clean: 1 mechanical (F-b, holds phase) + 3 surfaced (F-a crux, F-c, F-d). Intent produced a D-delta → mechanical pass SKIPPED cycle 2. Actions: F-b → correct D2 basis; F-c → fold mechanism-generality into D1; F-a → operator-ratified (bidirectional core tenet); F-d → render note. → not converged, cycle 3 re-converge.
