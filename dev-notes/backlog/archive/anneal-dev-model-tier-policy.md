# anneal-dev model-tier policy — sensitive corpus-evolution work always uses the top tier

**Status:** OPEN — **▶ NEXT-UP (operator-chosen 2026-06-04):** the next item once the
intent-falsification-convergence-pass run ships. Operator-raised 2026-06-04 (during that run).
Its own anneal-dev method change (edits `anneal-dev/spec` → a method-kernel edit → own run + the
kernel-independent verify). NOT folded into the intent-falsification run (one-scope-per-cycle).

## The idea
anneal-dev work (corpus-evolution / method-kernel edits) is too sensitive to cost-optimize the
model tier: its blast radius is the whole framework + every instance, and the work is judgment-heavy
(the intent-falsification run took 3 blocking dogfooding rounds on subtle soundness). So **every
anneal-dev subagent dispatch (investigate / falsification / intent-falsification / implement / verify)
uses the TOP / most-capable model tier, never cost-downgraded.** Instances keep the framework default
(per-task choice — Sonnet where a task is cheap-and-safe).

## Design (for the run)
- **Rule (in `anneal-dev/spec`, e.g. bindings.md):** anneal-dev dispatches use the configured top
  tier; cost-downgrading an anneal-dev dispatch is forbidden. Blanket (all dispatch kinds) — not
  per-dispatch "is this one sensitive?" judgment (that judgment is itself error-prone). Classifiable:
  mechanical (every dispatch's model = the config'd tier; observable on the dispatch).
- **Value (in `anneal-dev.config`):** the actual model name (`opus` today), operator-editable. KEEP
  THE MODEL NAME OUT OF THE SPEC PROSE — the framework spec is harness-agnostic (names no models/tools);
  a literal model name is leakage + a staleness trap (names change). Rule in spec, value in config.
- **Floor, not guarantee (honest framing for the rule's prose):** top-tier avoids *handicapping*
  sensitive judgment; it is NOT a substitute for the structural robustness that actually catches
  errors (fresh-context verify, the dogfooding/falsification passes, the operator). Frame as "don't
  run sensitive work on a weak model," not "a strong model makes it safe."

## Note
In practice, anneal-dev dispatches already inherit the session model (Opus this session), so the rule
mainly formalizes a FLOOR — it bites when the session model is lower, or to forbid a cost-downgrade on
an individual dispatch. Cost (all-top-tier across anneal-dev's many dispatches) is real but
operator-owned (sensitivity > cost is the operator's ratified call).

## Relates to
- `anneal-dev.config/` (the operator-editable home — already holds lenses.md / extensions.enabled).
- The dispatch mechanics (`development-process.md` practice 3 / `anneal-dev/spec/bindings.md`).
- The Agent-tool model param (harness): default inherits the session model; this rule pins a floor.
