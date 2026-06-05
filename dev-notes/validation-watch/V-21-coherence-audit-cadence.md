## V-21. Periodic coherence-audit cadence — is N=5 the right cycle threshold?

**Status: WATCHING.**

**Kind: quality-watch.** The fix is a calibration of an existing cadence number (practice-12 N=5 → adjusted), not a catcher — so it closes on a *produced-clean* instance: an audit cycle whose finding-density sits between the too-low and too-high boundaries where the old N would have mis-paced (see README closing rule). (Borderline fit: a pacing-calibration is neither a pure catcher nor an output-form change; quality-watch is the better of the two kinds.)

**Decision (`development-process.md` practice 12; commit pending).**
The mechanical trigger for periodic coherence audits fires every
**N=5 cycles** closed since the last `Coherence-audit-handoff:`
marker. The mechanical SHAPE (cycle-count threshold + git-log
observable + handoff marker) is fixed; the threshold NUMBER (5)
is initial calibration.

**Why uncertain.** The choice of 5 rests on a single empirical
data point: the D.1 → D.1-revalidation cluster ran roughly 6
cycles (D.1 / D.3 / D.2 / D.4 / G / H) between audit and
revalidation, and that interval "felt about right" — drift was
detectable, fixes were tractable, and the audit's set-level
findings cleanly mapped to per-cycle fixes. Whether 5 generalizes
across other corpora, other phases of an instance's lifecycle, or
other operators' cadences is the open question. Too low → audit
overhead dominates productive cycles; too high → drift accumulates
past tractable batch size.

**Production signal to watch.** Either of two shapes, observed at
n=1:
- **Too-low signal.** Three consecutive cycle-N audits return PASS
  (zero substantive findings) — the cadence runs faster than
  drift accumulates. Sharpen N upward (e.g., 7, 10).
- **Too-high signal.** A cycle-N audit returns blocking findings
  that the audit-deltas strategy traces to >50% of the audited
  scope, AND the operator reports the fix-cycle batch felt
  unwieldy. Sharpen N downward (e.g., 3, 4).

Closing criterion (WATCHING → FIX-SHIPPED): observed n=1 of
either signal; ship the N adjustment to practice 12. FIX-SHIPPED
→ RESOLVED on first subsequent audit-cycle where the new N
produces a non-trivial finding density (between the too-low and
too-high boundaries above).

Per `development-process.md` practice 8, this V-N is legitimate:
the fix-shape (mechanical cycle-count) IS shipped; only the
NUMBER is open. Calibration uncertainty, not classifiable-fix
deferral.

---

