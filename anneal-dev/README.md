# anneal-dev

**Anneal applied to evolving the rule-corpus itself** — the *corpus-evolution*
instance of the [anneal-framework](https://github.com/Gunther-Schulz/anneal-framework).

Just as `coding-clippy` is "anneal applied to coding" and `daneel` is "anneal
applied to debugging," **anneal-dev is "anneal applied to evolving the
spec-and-skill files that define an AI methodology and its tools."** It exists to
replace the hand-maintained shadow copy of the method
(`anneal-framework/development-process.md`) with a real, rendered instance — so the
process we use to develop the framework *is* the framework, not a drifting copy.

## Status

**Skeleton — followed-in-context, not yet packaged for install.** Rendered from the
settled spec (`spec/`) on 2026-06-02 and validated by a first dogfood run (a daneel
render-sync), per the anneal-framework `framework-dev-as-anneal` effort, step 5
(bootstrap PASSED: anneal-dev ran investigate-design → implement → verify end-to-end
as a real instance). Not yet registered in a marketplace; the **adoption** phase
(promote anneal-dev to the actual dev-process, reconcile `development-process.md`,
package for install) is the next step.

## Layout

- `spec/` — the instance's slot specs (bindings, lens set, persistence, extensions,
  lens-supplement, presentation): the corpus-evolution binding of the framework's
  open slots.
- `plugin/skills/anneal-dev/` — the rendered runnable skill: `SKILL.md`
  (orchestrator), `phases/` (investigate-design / implement / verify),
  `references/` (foundations, tracker, lenses).
- `derivation-rationale.md` — derivation commentary (how the spec was derived from
  the cleaned framework core; scar-tissue-dissolved map + residual strains).

The **method itself** (phases, tracker, status-state machine, basis rule, isolation,
orchestrator) lives in the [anneal-framework](https://github.com/Gunther-Schulz/anneal-framework)
spec; this repo binds it to the corpus-evolution domain.
