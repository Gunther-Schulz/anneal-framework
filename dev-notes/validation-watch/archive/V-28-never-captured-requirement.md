## V-28. Never-captured-requirement residual — does capture-at-design + the soft verbatim backstop hold in practice?

**Status: FIX-SHIPPED (2026-06-04, commit 1d93e58).**

**Kind: correctness-watch.** The shipped requirements-coverage check is a catcher; its residual fix (a harder record-vs-request gate or capture-time elicitation discipline) is also a catcher — so it closes on a *caught* instance: a never-enumerated requirement the operator genuinely asked for that the strengthened gate flags before it ships, where the soft verbatim backstop would have missed it (see README closing rule).

**Decision (`core.md` §4.1 requirements record + §4.3 requirements-coverage
check; shipped `1d93e58`, 2026-06-04, run `verify-vs-original-requirements`).**
The fix closes the gap where a requirement dropped at investigate-design escaped
verify: investigate-design captures the original requirements as a
header-adjacent tracked record (enumerated R1..Rn + the operator's verbatim
request), and verify checks the locked design's coverage of each — uncovered →
finding → [ISSUES FOUND]. The primary leg (record → coverage) is
evidence-bearing; a second, soft-judgment leg checks the enumeration against the
captured verbatim request.

**Why uncertain (the shipped residual, run finding F5 [VERIFIED — deferred]).**
The coverage check can only catch a requirement that **made it into the record**.
A requirement **never captured** — absent from the enumeration AND missed by the
soft record-vs-request judgment (no mechanical predicate) — still escapes; the
isolated verify "needs nothing from the run's conversation", so it cannot
re-derive the original ask from the raw conversation. The verbatim-request
capture reduces this but does not eliminate it. Whether the residual actually
bites — vs. capture-at-design + the soft backstop being sufficient in practice —
is not judgeable ahead of operation.

**Production signal to watch (n≥1).** A real run where a requirement the operator
genuinely asked for is **never enumerated** into the record AND slips past the
soft verbatim-request check AND ships unaddressed (the deferred-trigger the run
recorded). That is the evidence a stronger capture-completeness mechanism is
warranted (a harder record-vs-request gate, or an elicitation discipline at
capture). Conversely, a long stretch with no such escape is evidence the soft
backstop suffices.

Per `development-process.md` practice 8, this V-N is legitimate: genuine
uncertainty about whether the shipped design's known residual matters in
practice, to settle empirically — not deferral of a classifiable fix (the harder
mechanism is not in hand; it is a soft-judgment problem whose stricter-gate cost
is unjustified absent evidence the residual bites).
