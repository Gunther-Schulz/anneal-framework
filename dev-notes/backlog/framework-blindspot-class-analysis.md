# Framework blind-spot class analysis — proactively enumerate the classes of verification blind spot the framework may have

**Status:** OPEN — operator-raised 2026-06-04, generalizing the
`foundation-invariants-register` run's intent-falsification discovery. **Meta/analytical**
(produces candidate framework changes; not itself a change). High interest. The analysis is
OF the framework → acting on its findings = method-kernel edits through anneal-dev.

## The trigger
The intent-falsification experiment found a **whole class** of verification blind spot — the
framework's mechanical checks (falsification pass, lenses, hooks) are structurally blind to
**judgment-class soundness flaws** (self-certifying enforcement, overclaimed gates) — and it
found it **by accident** (an operator-proposed experiment), not by design. One class surfaced
by accident is strong evidence **others exist, undiscovered.** Rather than trip over them
one-at-a-time, enumerate the *classes* proactively.

## The hard constraint (why this can't be pure introspection — same theme as the register)
A framework cannot see its own blind spots by looking inward: the analysis runs in the
framework's own context and inherits the framework's blind spots — by definition it cannot see
what it cannot see (Gödel; the same reason the kernel can't self-certify its foundation). So
this analysis **must be grounded OUTSIDE the framework** — external lenses: the
process/methodology literature (the `dev-notes/research/` runs are precedent), other
disciplines' failure taxonomies, adversarial fresh-context attack, and the operator. An
introspective "what might we be missing?" pass is the malformed form.

## Method sketch (for the actual pass)
For each check the framework runs — mechanical falsification pass (`core.md` §4.1.4), the
standardized lenses, the basis rule, the [READY] gate, render-fidelity, the hooks, the
operator-soundness leg — name the **class of flaw it is structurally blind to** (what could be
wrong while this check reports clean), then probe each candidate class with an external lens.
The output is a **taxonomy of candidate blind-spot classes**, each carrying a
structural-invisibility argument + (ideally) an instance.

## Candidate seed classes (to confirm/refute, not assume)
- **Judgment-class soundness** — FOUND (the intent-falsification class; mechanical checks see
  form, not whether form binds). Already being acted on (the fix + the sweep).
- **Absence / never-stated** — you cannot verify against a requirement/rule that was never
  written (the V-28 never-captured-requirement shape). What classes of "the missing thing"
  are invisible to every check that operates on what's present?
- **Emergent / cross-rule** — each rule sound, the SET unsound. Partly `coherence-audit`'s
  domain — confirm what it covers and what still escapes.
- **Temporal / edit-sequence** — sound at each single edit, broken by a sequence of edits no
  single per-edit check sees (related to the periodic-coherence-audit cadence).
- **Gaming / letter-vs-spirit** — a rule satisfiable in form while its intent is violated; the
  evidence-bearing-artifact discipline targets this but may not close it.
- **Operator's own blind spots** — the framework leans on the operator as the irreducible
  soundness judge; what catches an operator who is confidently wrong? (the deepest residual).

## Push-back (sort, don't cry wolf)
NOT every imaginable failure is a structural blind-spot class. The value is the **sort**: a
genuine class is one **all** current checks provably can't see, argued structurally, ideally
with an instance — not a hypothetical. A pass that manufactures speculative classes bloats the
backlog and is itself a false-comfort artifact ("we enumerated the blind spots" when we
listed guesses). Mirror `loopback-root-cause-triage`'s discipline: the artifact is the
*argued* class + disposition, not a wish-list.

## Output
A taxonomy of confirmed candidate classes; each confirmed class → its own fix/sweep
(method-kernel edit or audit). NOT a mandate to fix all — the analysis surfaces and prioritizes.

## Relates to
- `intent-falsification-soundness-sweep` — the RETROSPECTIVE sweep for the ONE class found;
  this is the PROSPECTIVE enumeration of ALL classes (the sweep is acting on one output).
- `multivoter-verify-no-predicate-claims` — the FIX for the found class (judgment-soundness).
- `loopback-root-cause-triage` — REACTIVE (failures-as-gap-signals, per loopback); this is
  PROACTIVE (enumerate before they fire). Compose.
- `coherence-audit` — one known class (set-level drift) already has a tool; a data point for
  "which classes are already covered."
- the `dev-notes/research/` deep-research runs — the external-lens precedent (and a possible
  vehicle: a deep-research run on methodology failure taxonomies).
- `foundation-invariants-register` — the external-grounding theme (you can't self-certify /
  self-introspect the foundation); origin of the trigger.
