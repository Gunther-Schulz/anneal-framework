## V-4. Standardized pass — in-scope per cycle, whole set at [READY]

**Status: WATCHING.**

**Kind: correctness-watch.** The catcher under watch is the [READY] whole-set lens accounting (`core.md` §4.1.1, `modules.md` §3.2) that replaced per-cycle whole-set attestation — closes on an instance where it caught a lens-catchable concern (or a silently-dropped lens) at [READY], before implement, that the dropped per-cycle attestation would otherwise have surfaced earlier.

**Decision (`core.md` §4.1, `modules.md` §3.2).** Each cycle's
standardized inspection pass emits a line only for the lenses in
scope that cycle; an out-of-scope lens is not lined. The set is
accounted for whole once, at [READY] — every lens applied in the
cycle(s) where its scope was touched, or cited out of scope for the
run. Per-cycle application of in-scope lenses is unchanged.

**Why uncertain.** Earlier the pass accounted for every lens every
cycle, in-scope and out. The every-cycle out-of-scope accounting was
identified as grind, and the fixed ten-row grid as competing with
ad-hoc investigation for attention; the change drops the per-cycle
whole-set attestation and moves omission-visibility to [READY]-time.
It rests on a single run's evidence (Unit-3/Unit-4 — ad-hoc
investigation found the load-bearing defects, and most per-cycle lens
lines recorded what was already in scope). The lower-risk variant was
chosen: per-cycle application of in-scope lenses stays a forcing
function, and the soft-priming variant — priming only, no per-cycle
attestation — was not adopted. One run is still thin evidence for a
cycle-structure change.

**Production signal to watch.** Whether a concern a lens would catch,
that per-cycle attestation surfaced earlier, now slips — caught later
at the [READY] whole-set accounting (acceptable, still before
implement) or past it entirely (not acceptable). And whether the
[READY] accounting reliably catches a lens silently dropped from a
cycle's scope. If lens-catchable concerns routinely reach implement,
the per-cycle whole-set attestation earned its cost and should
return.

---

