# anneal-dev Specification

anneal-dev is the Anneal framework instantiated for
**corpus-evolution** — evolving the rule-corpus (the spec-and-skill
files that define an AI methodology and its tools). The framework's
method — phases, tracker, status-state machine, basis rule,
evidence-bearing-artifact rule, modes, orchestrator — is specified
in the `anneal-framework` repo (`spec/`). That spec is
domain-general; this document set binds it to the corpus-evolution
domain.

This `spec/` folder carries the slots the framework leaves to the
instance. Per `anneal-framework/instantiation-guide.md` §2 the slot
set is **closed**: an instance fills declared slots, does not invent
new ones.

**Required:**

- `bindings.md` — domain bindings (incl. the verification battery
  and the isolation-slot binding)
- `persistence.md` — run-artifact persistence mechanism
- `lens-set.md` — the standardized lens set (8 lenses, Path 1)

**Required-mechanism (declare the mechanism even when no items
declared yet):**

- `extensions.md` — lifecycle-extension enable mechanism (+ one
  declared extension)
- `lens-supplement.md` — lens-supplement mechanism

**Optional:**

- `presentation.md` — kept; records the deliberate framework-default
  presentation (no persona, no flourish)

`derivation-rationale.md` (this directory, beside `spec/`) carries
the §1 fit verdict, the lens-set path, the judgment calls, the
**scar-tissue-dissolved** map (what pass-1 worked around that the
cleaned core now natively supports), and the **residual strains**
that survive the de-pollution. It is derivation commentary, not a
render-consumed slot.

## Conventions

The framework spec's conventions apply unchanged — the
fixed-decision rule, the prescription discipline, the entry
conventions, the operational/analytic term distinction
(`anneal-framework/spec/README.md`).
