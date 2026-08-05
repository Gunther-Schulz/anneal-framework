## V-10. D-track delta as convergence criterion

**Status: WATCHING.**

**Kind: correctness-watch.** The catcher under watch is the convergence-cycle zero-D-track-delta test (`core.md` §4.1.4) gating [READY] — closes on an instance where the D-delta proxy correctly captured materiality (a material change appeared as a D-track delta and held the phase) where, had it escaped the D-track, a real gap would have reached implement or verify.

**Decision (`core.md` §4.1.4).** The convergence cycle test for
[READY] uses **D-track delta = 0** as the mechanical convergence
criterion: a cycle producing no new design decisions and no
amendments to existing ones is "converged." F-track entries
(findings) alone don't count as material — only D-track entries
do, since design decisions are the load-bearing artifact that
implement reads.

**Why uncertain.** D-track delta is a *proxy* for "material" —
operator-named at the design moment. The proxy is mechanical and
artifact-observable (delta the two cycles' D-track), which is the
class-1 mitigation skill-craft prefers. But the question whether
D-delta correctly captures *materiality* — every material change
in the design appears as a D-track entry — is empirical.

Possible misses:
- Findings whose implication for the design is real but doesn't
  trigger a D-track update (the AI judges the finding doesn't
  invalidate any decision but later implementation reveals it
  did).
- Amendments expressed as evidence-only sub-annotations
  (`modules.md` §3.1 basis-only refinement) — these are
  intentionally not new peer-level ledger lines; the convergence
  test would read this as "no D-track delta" even though the
  basis strengthening might be material.

**Production signal to watch.** Post-implement reviews where new
design decisions surface in implement OR verify that should have
been caught in investigate-design, **and** the convergence-test
cycle(s) for that run produced zero D-track deltas. That'd be
evidence the D-delta proxy is missing real materiality. If
observed: the convergence criterion needs broadening — possibly
to include basis-only sub-annotations on already-[VERIFIED]
decisions, or to add an F-track materiality classifier.

Absence-of-recurrence does not close this; only positive
load-bearing evidence per the lifecycle (or refutation evidence
that proxy misses) updates state.

---

