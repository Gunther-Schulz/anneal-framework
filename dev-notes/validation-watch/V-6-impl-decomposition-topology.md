## V-6. Implementation decomposition + impl-phase subagent topology

**Status: WATCHING.**

**Decision (`core.md` §4.2, §6; `modules.md` §3.3).** The impl phase
opens with an impl plan: dispatch units derived from the locked
design, dependency-ordered, parallel-eligibility marked with a
search-established disjointness basis. Dispatch to subagents is the
default when the plan has two or more units; a single-unit plan is
implemented in the working context. The orchestrator owns the tracker
append; subagents return state. A subagent surfacing any actioned
finding triggers a loopback to investigate-design, with other in-flight
parallel subagents halted. Per-unit commits are the checkpoint
discipline that makes resume-from-tracker reliable.

**Why uncertain.** Design completed on n=1 evidence (Unit 5, mid-impl
session-budget exhaustion, 2026-05-23). Ship-fast applied: a
reversible spec change with a real post-analysis hook (this entry),
preferred over withholding for more runs of the unsupported old
protocol. Several calls rest on analogy to verify rather than direct
evidence — that the impl-subagent brief shape mirroring verify will
be artifact-sufficient, that the loopback-from-impl-subagent pattern
works the same as verify's [ISSUES FOUND] return, that one-writer
tracker append remains workable when parallel subagents return state
in short intervals. The ≥2-unit dispatch threshold is a judgment call
balancing verify-isolation symmetry against mechanism-creep on
trivial impls.

**Production signal to watch.** (1) Whether impl-plan production at
implement-start works smoothly — is the dispatch-unit grouping
intuitive from the locked design, is parallel-eligibility usefully
identifiable, does the artifact feel useful or ceremonial. Difficulty
here is also a downstream signal on [READY] quality (V-5): a tracker
[READY]'d but not yielding a well-formed impl plan suggests the
design was incomplete. (2) Whether parallel dispatch actually
parallelizes cleanly in practice (Unit 6 candidate, may not exercise
it to full extent) — tracker write integration, return-state
handling, no race-on-merge surprises. (3) Whether the
loopback-across-boundary protocol fires correctly — subagent halts at
the right moments (not too liberal, not too conservative);
orchestrator's halt-other-subagents works without lost work. (4)
Whether per-unit commits become natural cadence or chafe (too coarse
/ too fine). (5) Whether verify's task remains tractable when reading
code from multiple impl subagents.

**First signal (2026-05-23).** A real instance run hit mid-impl
session-budget exhaustion with ad-hoc per-slice commit + resume
recommendation. Decomposition was clean; resume-from-tracker observed
working in practice. Instance-specific detail (findings, slice
numbers, commit references) lives in the instance's run tracker
(`.clippy/runs/`), not here. Lessons abstracted into the protocol
changes named in subsequent V-N entries.

---

