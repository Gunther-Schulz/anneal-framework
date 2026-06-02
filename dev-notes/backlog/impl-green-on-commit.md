# Impl commit semantics — "committed on completion" vs "green on commit"

**Status:** OPEN — finding (cross-session clippy run, 2026-06-02; surfaced in a
"what's mandated vs ad-hoc" exchange). Minor / spec-silence. Relates to
[[clippy-run-findings-dispatch-coupling]] (V-8 dispatch self-check) and the verify
phase's executable verification.

**Gap.** `core.md` §4.2 / clippy `implement.md` say a unit is **"committed on
completion"** but do **not** say the commit must be **green** (project test / lint
/ type suite passing). The orchestrator fills the silence by *habit* — it ad-hoc
runs pytest/ruff/mypy before the impl commit — so whether impl must pre-validate
is **unspecified**, left to the agent. Distinct from the **dispatch self-check**
(§4.2 "Self-check at dispatch boundary" / V-8), which applies the standardized
**lenses** to the diff but is not an **executable** green-gate; and distinct from
[[behavior-change-test-impact-enumeration]] (which is about *which* tests a
decision must enumerate).

**Why it's low-priority but real.** The agent judged its ad-hoc gate benign —
"verify re-runs it anyway," so a red impl commit gets caught at the verify phase
regardless. The cost of the silence is only that a red commit can land *between*
impl and verify (bisect noise, a non-green per-unit checkpoint that the
resume-from-tracker discipline assumes is clean). The fix is a **spec-clarity**
decision, not a new mechanism.

**Decision to make.** Either (a) **mandate green-on-commit** — the impl unit's
commit must pass the project's executable verification before it lands (each
per-unit checkpoint is green; matches the orchestrator's current habit); or
(b) **explicitly leave it to verify** — state that impl commits are *not* required
green and the verify phase is the sole executable gate (removes the ad-hoc habit's
implicit status). Pick one and state it; the current silence is the only defect.

**Level.** Framework (§4.2 implement commit semantics) + clippy render. Renders to
all instances (the green-gate's binding — what "the suite" is — is the instance's
executable-verification slot).
