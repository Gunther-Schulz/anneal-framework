# Per-loopback / falsification-failure root-cause triage (failures as framework-gap signals)

**Status:** OPEN — framework finding, operator-raised 2026-06-03, strongly
evidenced by THIS session (F16 + VF1, n=2). Methodology-correctness →
**operator is the kernel-independent judge.** Idea, not yet a design.

## The idea
On a **falsification-failure** (a [VERIFIED] decision falsified at the convergence
cycle) or a **verify [ISSUES FOUND]** (a loopback), make it a STANDARD in-loop
step to **triage the failure's root cause** — does it point to an instance-render
gap, a framework-spec gap, or an adherence gap (practice 1's three-way sort)?
Root at instance/framework level → surface as a finding (fix in-run if reachable;
else surface for a corpus-evolution run). Adherence → noted, no source fix.
Rendered into every instance (every instance's loops self-triage).

## Why it's correct (not gold-plating)
This session's root-cause analyses (F16 → the Missed-dependents blind spot; VF1 →
the same + the [CONDITIONAL] exemption) happened ONLY because the operator
prompted "investigate the gap" after each loopback. **That reliance on the
operator to ask is the operator-detection anti-pattern the framework's own
foundations forbid** (`foundations.md`/`core.md`: "where an artifact's enforcement
would otherwise require operator-detection, the enforcement form is malformed —
AI discipline or a fresh-context checker carries it"). Baking the triage in closes
that hole. Concretely: a per-loopback triage would have auto-surfaced exactly the
two framework gaps we found by hand, at the loopback moment — n=2 this session.

It is **practice 1 ("fix at the source") applied to the run's OWN loopbacks** —
currently practice 1 covers deviations found *running* an instance (empirical),
not the run's *internal* falsification/verify failures. This extends it.

## The push-back (must sort, not cry wolf)
NOT every loopback is a framework gap — some are this-run adherence misses (no
spec defect). A check that ASSUMED every loopback = framework gap would
manufacture false gaps and bloat the backlog. The value is in the SORT (practice
1's render/spec/adherence triage); the check is "triage the root," not "log a gap."

## Design sketch (for the actual pass)
- **PLACEMENT FORK (the key open question — resolve when taken up).** Operator's
  first-thought (2026-06-03): put the check in **post-run-review / self-review**
  (the retrospective machinery). Weigh against the alternative:
  - *Post-run / retrospective* (operator's lean) — analyze the run's loopbacks
    after verify PASSED. Fits the existing post-run-review home; but it is
    currently OPTIONAL + operator-invoked + after-the-fact.
  - *In-loop / per-failure* — triage at the moment each falsification/verify
    failure fires (forces the analysis; catches the root while fresh; not
    operator-dependent).
  - *Both (compose)* — in-loop catches + forces; post-run sweeps for what in-loop
    missed. Likely the answer, IF they don't duplicate.
  The deciding criterion is the no-operator-detection principle: the optional/
  operator-invoked post-run path alone re-introduces the very operator-detection
  reliance this finding is trying to remove — so a standard (non-optional) firing
  is needed wherever it lands.
- **Home (if in-loop):** framework spec (`spec/core.md` — the loopback +
  verify-[ISSUES FOUND] mechanics, + the convergence-cycle falsification
  mechanics in `investigate-design`), rendered into each instance.
- **Home (if retrospective):** `post-run-review.md` (the Q-set), made non-optional
  for the loopback-root-cause question — rendered into each instance's
  `references/post-run-review.md`.
- **Artifact:** a triage line per failure — root level (render/spec/adherence) +
  basis + disposition (fix-in-run / surface-for-corpus-evolution / adherence-noted).
  Structural-enforcement candidate (the triage artifact is the un-fakeable check).
- **Cross-level surfacing:** an instance (e.g. clippy) that loops back and triages
  a FRAMEWORK-root cannot fix it (that's corpus-evolution) — it SURFACES it (per
  skill-craft Layer 5 reflexivity: notice + surface, don't fix cross-level).

## Relates to
- `structural-change-dependent-enumeration.md` — that is a SPECIFIC gap (n=2);
  this check is the META-mechanism that would have surfaced it automatically.
- `post-run-review.md` (spec) — the OPTIONAL, post-run, operator-invoked
  retrospective Q-set. This idea is the IN-LOOP, STANDARD, per-failure complement
  (catch the root when it surfaces, not only in an optional post-run pass). Check
  for overlap at design — the two should compose, not duplicate.
- `surface-non-task-observations.md` — sibling surfacing-channel item.
- `development-process.md` practice 1 (the triage shape this extends).
- Method-kernel finding (touches `spec/*`) → anneal-dev + kernel-independent verify.
