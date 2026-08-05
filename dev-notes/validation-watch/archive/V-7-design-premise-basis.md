## V-7. Design-decision premise basis — paths, filenames, completeness counts

**Status: FIX-SHIPPED (2026-05-24, commit c5e7ad9).** Downgraded
from RESOLVED 2026-05-25 per the new lifecycle: a fix shipped to
spec is FIX-SHIPPED, not RESOLVED, until a post-run review
identifies a load-bearing instance of the mitigation. The
structural fix is in spec; positive evidence of the fix actively
catching a finding that would have escaped pre-fix has not yet
been recorded.

**Kind: correctness-watch.** The fix is a catcher (the Target-locality lens + the §3.2.1 embedded-claims basis requirement + the [READY] judgment), not a form-change — so it closes on a *caught* instance where one of them caught a path/filename/completeness-count claim that the pre-fix protocol would have let slip into [READY] (see README closing rule).

**Closing criterion (FIX-SHIPPED → RESOLVED).** A post-run review
identifies a run where the §3.2 embedded-claims sharpening or the
Target-locality lens was load-bearing — caught a path / filename /
count claim that the pre-fix protocol would have allowed to slip
into [READY].

**Original observation preserved below for audit trail.**

---

This entry's "if recurrent X, then sharpen the rule" framing was
itself the cost-gating-as-epistemic-humility shape that
`development-process.md` practice 8 ("Validation-watch is not a
deferral journal") now rejects. The proposed sharpening
classified as a **structural enforcement** fix (§3.2 sub-clause
that an embedded design-decision premise carries the basis-rule
requirement separately from the surrounding statement), so it
earned its place at n=1 rather than waiting for recurrence.

**Resolution.** Commit c5e7ad9 sharpened §3.2 with the embedded-
claims principle: "claims embedded within larger statements —
implicit premises in target-naming decisions, cited rules or
prior decisions, completeness counts asserted as facts. Each
embedded claim carries the basis-rule requirement *separately*
from the surrounding statement." Plus the Target-locality lens
(Clippy v0.9.9, DANEEL v0.2.1) is the standardized-inspection
catcher. The class now has a write-time catcher (§3.2 sharpening),
a gate-time catcher (§4.1 [READY] judgment), and a
standardized-inspection-time catcher (Target-locality lens).

**Original observation preserved below for audit trail.**

---

**Decision (`core.md` §3.2).** The basis rule requires every
load-bearing claim and every design premise to carry a named basis.
Applied uniformly: findings cite evidence, design decisions cite
basis. The rule's text did not separately enumerate paths,
filenames, or completeness counts embedded within design
decisions — these were covered by "every design premise" generally
*at the time of this entry's writing* (pre-c5e7ad9).

**Why uncertain (at time of writing).** A real-run incident
(coding-clippy unit-10 file-split refactor, 2026-05-24) surfaced
a class of [READY] escape where the rule was loaded but unevenly
applied: design-decision premises that name a path/filename
("move X to **new file** `overtime_settlement_persistence.py`")
have an implicit completeness claim — "no existing nearby module
is suitable" — that got less rigorous basis-rule application
than explicit findings did. Cycle 2 declared [READY] with this
claim ungrounded; cycle 3 surfaced the existing
`services/autobet/overtime_settlement.py` module that would have
been the natural home, requiring D3 to be re-formed. Same shape
on cross-reference completeness: cycle 2 listed 3 sites, cycle 3
found 7.

The fresh-session implementability test (`core.md` §4.1) PASSED
at cycle 2 — a fresh session reading the tracker would have
implemented the design *as specified*, never surfacing a new
design decision. The test catches **clear-but-incomplete**
designs; it did not catch **clear-but-wrong-target** designs
where the implementation lands cleanly but in the wrong
location. (Now caught by the §3.2 embedded-claims sharpening +
Target-locality lens.)

---

