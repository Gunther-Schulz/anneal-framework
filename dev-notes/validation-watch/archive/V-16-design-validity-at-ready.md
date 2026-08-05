## V-16. Design-validity/coherence at [READY] — gap?

**Status: WATCHING.**

**Kind: correctness-watch.** The anticipated fix is a catcher (a coherence/validity check or lens for the specific incoherence shape that surfaces, per the Unit-4 §5.2 precedent), not a form-change — so it closes on a *caught* instance: a [READY] design later found incoherent or invalid where a design-time catcher would have caught it at [READY] (see README closing rule).

**Decision (no dedicated mechanism shipped).** The framework
does not ship a dedicated design-validity/coherence audit at
[READY]. Existing partial coverage:

- Per-decision basis rule (`core.md` §3.2) — each decision
  evidence-grounded
- Convergence cycle (`core.md` §4.1.4) — zero D-track deltas
  required for [READY]
- Standardized lens set (`modules.md` §2) — per-decision checks
- Fresh-session implementability test (`core.md` §4.1.2) —
  whole-design re-derivability indirectly tests coherence
- Verify's planned-vs-actual (`core.md` §4.3) — diff-vs-design
  + design-completeness audit (catches material ad-hoc decisions
  in impl-phase)
- Q4 ad-hoc additions in post-run review (debug-only) —
  historical catch of cross-decision detection gaps (Unit-4
  F18 → v0.8.2 §5.2 sharpening)

**Why uncertain.** Generic design-validity/coherence is
naked-judgment-shaped: no observable artifact-form forces
"these decisions hang together" or "this design actually solves
the request." Specific coherence shapes (e.g., pairwise
cross-decision detection per Unit-4) ARE structural-enforcement-
shaped and have been addressed per-incident. Open question: is
there a CLASS of coherence/validity failure beyond what
per-decision + fresh-session + verify + Q4 mechanisms catch?

**Production signal to watch.** Any [READY] design later found
internally incoherent (contradictions between decisions) or
invalid (the locked design wouldn't actually solve the
operator's request) — surfacing via verify [ISSUES FOUND],
implement-loopback, post-run review Q-set, or operator's
free-form override at presentation. The shape of the
incoherence is the analytical handle; per Unit-4 §5.2 evidence,
specific shapes get specific structural fixes, not a generic
coherence audit. **One observed shape** earns its specific
structural fix at n=1; a second distinct shape (different cause,
different fix) under the new spec would suggest a class-level
mechanism is warranted instead of per-shape sharpening.

Per `development-process.md` practice 8, this V-N is legitimate
(Y not classifiable upfront — fix form depends on the specific
shape that surfaces), not deferral-journal.

---

