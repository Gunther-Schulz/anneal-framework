## V-9. Verify-terminal loopback destination and auto-battle convergence

**Status: WATCHING.**

**Decision (`core.md` §4.3, §6; `modules.md` §1.2).** Verify [ISSUES
FOUND] returns the run to investigate-design — the single locus for
fix resolution. The fix runs through the full procedure
(investigate-design → implement → verify); no in-place shortcut at
verify-terminal in either mode. In auto-battle, loopback is
automatic, with a convergence exception: a verify finding whose
evidence field explicitly cross-references an existing
[AUTO-ACCEPTED] design decision by tracker ID does not trigger
loopback; the run completes with the finding noted as a re-surfacing
alongside the original [AUTO-ACCEPTED] tag, for the operator's
post-run review.

**Why uncertain.** Two judgment calls. (1) Always-loopback to
investigate-design as the single re-entry point — no fix-in-implement
shortcut, no operator-accept-as-followup option at verify-terminal in
interactive — was chosen to unify with implement-loopback (§4.2)
and [INVALIDATED] reopening (§5), and to deny the silent-
accept-by-close pathway observed at n=1 (unit-12 F43/F47, closed as
"scope-proportional gaps" without explicit operator decision — a
deferral-shape resolution the basis rule §3.2 rejects). The cost is
overhead on verify findings that could in principle be addressed in
implement directly; the rationale is that "trivially fixable" is
itself a judgment that belongs in design, not at verify-terminal.
(2) The [AUTO-ACCEPTED]-re-surfacing exception prevents auto-battle
non-convergence on findings the AI already chose to defer at
investigate-design. Originally a naked judgment ("the same gap, now
observed in the work"); sharpened post-n=1 to a mechanical criterion
— the finding's evidence field must cross-reference the
[AUTO-ACCEPTED] decision by tracker ID for the exception to apply.
The remaining uncertainty: whether the verify subagent reliably
*recognizes* when to construct the cross-reference, since a missed
recognition produces a false-new-gap finding which triggers loopback
(conservative; over-loops rather than under-converges).

**Production signal to watch.** (a) Whether always-loopback in
interactive feels right vs heavy for trivial verify findings; whether
operators routinely use free-form override to scope-out a finding
rather than re-investigate. (b) Whether the verify subagent reliably
recognizes when an [AUTO-ACCEPTED] cross-reference applies — under-
recognition produces false-new-gap findings which over-loop
(conservative). Over-recognition is structurally prevented by the
cross-reference-by-tracker-ID criterion (no cross-reference → no
exception). (c) Whether auto-battle converges under the rule in
practice — no observed infinite verify-loopback loops. (d) Whether
the close-with-re-surfacing-notation creates useful post-run review
material or noise.

---

