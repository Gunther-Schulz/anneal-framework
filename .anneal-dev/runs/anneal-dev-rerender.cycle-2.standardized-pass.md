# Standardized-pass — cycle 2 (convergence cycle) — NOT clean (D1 falsified)

New surfaces investigated this cycle (convergence new-surface requirement):
- Surface A — current `spec/core.md §5.3` (915-922, the post-cleanup thin [READY] bridge) +
  the `bf32f9c` cleanup delta (the §5.3 collapse) — new reads, not in cycle 1.
- Surface B — render `foundations.md:391-404` + `tracker.md:213-226` ([READY] sections) read
  against their source — new reads.
- Surface C — independent de-dup-mirror re-derivation (investigate-design.md cite vs tracker.md
  closed-set ownership) + the firewall alternate-form/flatten census.

Lenses:
- **Over-claimed-verification** — **FINDING (F5)**. Cycle-1's F2 rested on the audit (secondary
  source) and asserted "foundations.md [READY] already the post-D4 thin-bridge shape." The
  fresh-context falsification + orchestrator direct read FALSIFIED that: foundations.md:391-404
  (and tracker.md:213-226) carry the OLD full §5.3 restatement; current §5.3 is thin. The
  secondary-source claim was taken too far in cycle 1; this cycle corrects it. — basis: cycle-2
  falsification D1; direct reads (foundations.md:393-404, core.md:915-922, tracker.md:213-226).
- **Missed-dependents** — **FINDING (F5, same)**. The §5.3 collapse (cleanup D4) is a spec change
  whose render dependents (the [READY]-relationship sections in foundations.md + tracker.md) were
  not enumerated in D1's change-set. Reopens D1. — basis: cycle-2 falsification.
- **Lossy-render** — CLEAN (re-confirmed). The 5 re-points + 3 strips remain non-softening; the
  newly-found [READY] divergence is the opposite of lossy (the render is MORE than the thin source).
- Firewall completeness + de-dup mirror — independently re-confirmed by the falsification (the 5
  hits hold; the de-dup mirror holds). — basis: cycle-2 falsification D1 (firewall candidate holds).

Convergence cycle 2 is NOT clean — D1 falsified (one content divergence missed). Re-formation in
cycle 3; fresh convergence in cycle 4.
