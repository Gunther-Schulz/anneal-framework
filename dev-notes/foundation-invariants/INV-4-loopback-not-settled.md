## INV-4. Loopback — not-yet-excluded = not-yet-settled

**Invariant.** A phase returns to an earlier one until the concern is
settled; a conclusion is rechecked rather than taken as final, because
enumeration of the alternatives is never complete.

**Kernel home.** `spec/core.md` §4.1.4 (the convergence-cycle requirement:
the loop continues until a convergence cycle is observed clean) + the
loopback machinery (§6, §5.1, §4.2.7 — a phase raises a loopback the
orchestrator honors rather than proceeding).

**External anchor.** Platt, "Strong Inference," Science 146(3642):347–353
(1964) — the recycle step. The four-step procedure ends in step (1'):
recycle and refine the remaining possibilities. "Any conclusion that is not
an exclusion is insecure and must be rechecked," so not-yet-excluded must
be treated as not-yet-settled. Quine-Duhem under-determination sharpens
this: a single crucial experiment is logically inconclusive (an apparent
falsification cannot say whether the central or an auxiliary hypothesis is
to blame), and complete enumeration of alternatives is impossible for
open-ended problems — so refutation never fully settles a question. The
discredited Strong-Inference promise (one decisive falsification settles a
question) is rejected; the recheck discipline it leaves is the anchor.

**Research.** `dev-notes/research/process-literature-deep-research-2026-06-03.raw.json`
findings [4], [7].
