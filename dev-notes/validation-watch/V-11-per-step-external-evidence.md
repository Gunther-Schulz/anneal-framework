## V-11. §4.1.2 per-step external evidence — independence from §4.1.4 convergence cycle

**Status: WATCHING.**

**Kind: correctness-watch.** The fix is a catcher (§4.1.2's per-implementer-step external-evidence artifact at [READY]), not a form-change — so it closes on a *caught* instance: a run where §4.1.2 surfaces a decision-to-step translation gap that §4.1.4's convergence cycle did not (see README closing rule).

**Decision (`core.md` §4.1.2, §4.1.4).** V-5's false-[READY] failure
shape was closed in commit e18bca1 with two layered mitigations:
§4.1.2 requires per-implementer-step external evidence (file:line /
grep) in the [READY] artifact, and §4.1.4 requires a convergence
cycle producing zero D-track deltas. §4.1.4 fires after §4.1.2
produces PASSED.

**Why uncertain.** Both shipped in the same commit and have not been
separately validated. The unit-14 continuation (the first run under
the new protocol) showed §4.1.4 paying for itself — cycles 5–7
surfaced material findings (production performance bug, cycle-1
basis-rule violation in F31/F32, pattern catches) before convergence
at cycle 8. But every catch was an investigation-pass finding, not
an implementer-walkthrough artifact. §4.1.2 fires at [READY] *after*
§4.1.4 — by which point the investigation has already surfaced the
gaps.

The failure shape §4.1.2 specifically targets — *design decisions
that look complete but don't cash out to clear implementer steps*
(translation gap) — is distinct from §4.1.4's target shape
(incomplete investigation, missed surfaces). Plausible: a decision
whose surfaces are settled but whose per-step implementer
walkthrough exposes a gap not visible as a new investigation
surface. Not yet observed in the field.

In unit-14, §4.1.2 was delivered in *cheap variant* — paraphrased
prior tracker citations rather than re-read source — which is
recall-pool-equivalent and doesn't independently validate against
§4.1.4. The §4.1.2 sharpening (commit [pending]) closes the cheap
loophole by inheriting §3.2's basis form (citation + observable
fact for a read; executable query with output for a search — see
V-13 below for the verbatim-content drop) — cheap can no longer
satisfy structurally. Independence vs §4.1.4 becomes
testable with strict-by-construction data on next runs.

**Production signal to watch.** A run where §4.1.2's per-step
external-evidence artifact catches a citation failure (file:line
mismatch, decision-to-step translation gap) that §4.1.4's
convergence cycle did not catch. If observed: §4.1.2 is
independently load-bearing.

The contrary signal: one run where §4.1.4's convergence cycle
produces non-zero D-track deltas (catches) and §4.1.2 runs clean
on the resulting tracker. In that case, §4.1.2 is redundancy
candidate; the spec-change shape is designed at observation time
per practice 8.

**Closing criterion (WATCHING → RESOLVED).** A post-run review
identifies a run where §4.1.2 surfaced a translation-gap catch
§4.1.4's convergence cycle did not. One observed instance is
sufficient.

Alternative closure (WATCHING → INVALIDATED): one run where
§4.1.4's convergence cycle produced non-zero D-track deltas and
§4.1.2 ran clean on the resulting tracker.

---

