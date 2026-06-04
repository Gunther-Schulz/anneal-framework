# FB-2. Verify checks the locked design, not the original task requirements

**✅ SHIPPED + CLOSED 2026-06-04 — spec-only release `1d93e58` on `main`.** The anneal-dev run
completed: design locked + [VERIFIED] → implement (re-shaped spec-only per the render-cadence policy)
→ verify **[PASSED]** (isolated) + method-kernel kernel-independent review (skill-craft form-review
clean + operator soundness "sound, ship — as close as we can get") + operator commit approval. The
kernel edit (`core.md` §4.1 requirements-record capture + verbatim-request; §4.3 requirements-coverage
check incl. the soft record-vs-request leg; `glossary` 2 entries) shipped. **Instance renders
(U2/U3/U4) DEFERRED** to the batch re-render — queued in `instance-reinstantiation` Render-debt queue
(source-delta = `1d93e58`). **Honest residual shipped (F5, deferred):** catches
captured-but-uncovered, not never-captured; deferred-trigger = a real run observing a never-captured
escape. Run state (gitignored, local): `.anneal-dev/runs/verify-vs-original-requirements.md` (Status
PASSED). Archived per backlog convention.

**Status:** open finding — needs a practice-9 design surface. Detail + steelman: `planner-instance-exploration.md` finding 5. Memory: [[project-verify-requirements-coverage-gap]].
**✅ AUDIT-CONFIRMED** (coherence-audit `ac39b6ab6d5d929cd`, 2026-06-04, L9-b): the audit independently
traced this gap (`core.md:686`, `:708-720`) — verify frames on the *locked design*; neither a
design-side nor a verify-side check tests against the *original ask*. Ranked the **one finding with a
real correctness consequence**. Fix is this item's anneal-dev cycle (F1).

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

**External corroboration (APF deep-read, 2026-06-03).** APF (arXiv 2602.19065)
independently splits verification into two **mandatory** channels: **Callback** =
*fact* verification (did the world change as specified — ≈ anneal's
verify-vs-locked-design) and **Confirm** = *value* verification (does that confirmed
fact align with the original intent, approved by a separate actor — ≈ *this* gap). APF
treats Confirm as a first-class, always-present obligation, not an operator-only catch.
Reframes the fix: make verify a **two-part obligation (fact-correct AND intent-correct)**,
not a single design-conformance check. Source: `anneal-placement-and-improvement-research.md`
APF deep-read + `dev-notes/research/anneal-placement-deep-research-2026-06-03.raw.json`.

**Level:** framework (fix at source per practice 1 → renders to all
instances).
