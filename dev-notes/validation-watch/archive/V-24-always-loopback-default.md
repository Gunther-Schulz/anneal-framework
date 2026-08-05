## V-24. Always-loopback default — does the elimination of inline-fix in implement reduce judgment-failures empirically, and does loopback overhead become a real burden?

**Status: FIX-SHIPPED (2026-05-28, commit e2c0776).**

**Kind: correctness-watch.** The shipped always-loopback rule's residual fix is a forcing function (dispatch-boundary check halting out-of-scope diff lines) — a catcher — so it closes on a *caught* instance: a run where an inline-edit that would have produced the partial-state-commit failure is halted and routed through loopback, counterfactual shown (see README closing rule).

**Decision (`core.md` §4.2; commit e2c0776).** The impl-phase
rule for handling new findings is replaced: any actioned
finding routes through loopback to investigate-design; any
non-actioned finding routes through [VERIFIED — deferred] with
explicit trigger condition. Inline-fix is eliminated as a path.
Local-clarification-and-continue is eliminated. The pre-
classification 4-criteria judgment (major-new-scope vs local)
that prior D.2 cycle mechanically anchored is removed entirely
— the criteria are no longer needed because the decision they
gated is no longer made.

**Why uncertain.** The change supersedes D.2 (mechanical
anchoring of the 4 criteria) per the pre-compact 09:53Z
decision that compaction lost. The trade-off is empirically
unmeasured: eliminating the judgment-call removes a known
failure mode (operator-session evidence: AI confidently
misclassified an F-entry as "inline-safe" producing scope-creep
and tracker drift) but introduces loopback overhead on every
actioned finding, including ones that are genuinely small.
Whether the net effect is positive depends on observed
frequency of (a) prior judgment-failures, (b) loopback cycles
that prove unproductive (re-design adds nothing because the
finding was actually small).

**Production signal to watch.** Either of two shapes, observed
at n=1:
- **Loopback-overhead signal.** Three consecutive runs where
  an actioned finding loops back through investigate-design and
  the loopback cycle produces zero D-track delta (the design
  was already correct; the finding could have been addressed
  without re-design). This indicates the always-loopback default
  over-corrects.
- **Judgment-failure-recurrence signal.** A run where, despite
  the always-loopback rule, the AI inline-edits to address a
  finding (rule violation) AND the violation produces the
  partial-state-commit failure shape the rule was designed to
  prevent. This indicates the rule isn't being honored
  structurally — needs a forcing function.

Closing criterion (WATCHING → FIX-SHIPPED):
- On loopback-overhead signal: reintroduce a narrow inline-fix
  path with mechanical pre-conditions (e.g., the D.2 4-criteria
  could be reinstated as gate, but only on findings where the
  basis is observably zero-scope-impact).
- On judgment-failure-recurrence signal: add a forcing function
  (e.g., dispatch-boundary check halting commits that introduce
  diff lines outside the unit's listed scope; routes through
  loopback automatically).

Per `development-process.md` practice 8, this V-N is legitimate:
the fix-shape (always-loopback rule) IS shipped; what's open is
whether the trade-off (eliminate judgment, accept loopback
overhead) holds empirically. Calibration uncertainty on the
mechanism's cost-benefit, not classifiable-fix deferral.

**Historical context.** Cycle D.2 (commit 95a1dc5; clippy
v0.9.82) shipped the opposite approach — mechanical anchoring
of the 4 major-new-scope criteria. That cycle was based on the
compaction summary which had lost the operator's pre-compact
09:53Z approval of the always-loopback rule. D.2's anchoring
becomes superseded by this cycle: the criteria it anchored are
removed because the decision they gated is no longer made.

