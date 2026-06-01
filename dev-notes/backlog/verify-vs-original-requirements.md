# FB-2. Verify checks the locked design, not the original task requirements

**Status:** open finding — needs a practice-9 design surface. Detail + steelman: `planner-instance-exploration.md` finding 5. Memory: [[project-verify-requirements-coverage-gap]].

**Gap.** A requirement dropped at investigate-design escapes: verify
checks work-vs-locked-design + standardized lenses + executable
verification, none of which re-derive against the *original ask*. The
design-completeness audit catches *undesigned work* (scope creep), not a
*missing requirement* (no work element to flag). Only catch today is the
operator at [READY] — which the framework explicitly disclaims
(no-operator-detection principle). So requirement-coverage has no
structural verifier.

**Design fork:** a per-task **requirements artifact** verify checks
against, **and/or** recurring-requirement **lenses** (e.g. a
data-integrity lens for the btb instance — operator-raised angle). Verify
is the stronger spot (an isolated context could catch a working-context-
dropped requirement, *if* requirements are in its artifacts).

**Level:** framework (fix at source per practice 1 → renders to all
instances).
