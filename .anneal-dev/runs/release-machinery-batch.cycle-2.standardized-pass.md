# release-machinery-batch — cycle 2 (convergence) standardized inspection pass

Scope: the cycle-2 re-amendments (D1 extended for instance-template; D2 clarified for exempt-only)
from the intent-falsification findings F8/F9.

- **Bloat** — clean. Both re-amendments carry a named load-bearing delta (D1: the instance-template
  narrowing closes F8; D2: the exempt-only statement closes F9). No restatement added. basis: D1, D2 cycle-2 lines.
- **Fragmentation** — clean. D1's instance-template narrowing and D2's exempt-only carve are new distinctions,
  not copies of an existing rule. basis: D1, D2 cycle-2 lines.
- **Leakage** — clean. Still dev-machinery (hooks/commit-msg code + development-process.md). basis: D1, D2.
- **Missed-dependents** — clean. The instance-template narrowing has no stale comment dependent (the
  merge-relocation comment lists `.claude-plugin`, not instance-template — D3 covers it); D2's exempt-only carve
  changes no other corpus rule. basis: F7 (the only comment dependent) + D1 cycle-2 line.
- **Unenforced-rule** — clean. D2's exempt-only carve is enforced by the hook's existing corpus-gate skip (an
  exempt-only commit is correctly not gated); D1 is the enforcement code. basis: D2 cycle-2 line + hooks/commit-msg:371-375.
- **Undefined-shorthand** — clean. No new coined term. basis: D1, D2.
- **Lossy-render** — out of scope (not rendered). basis: as cycle 1.
- **Over-claimed-verification** — clean; the re-forms sit at [PENDING] (cycle 2) until cycle-3 re-verify — honest.
  basis: F8, F9 + D1/D2 cycle-2 lines.

**Convergence result:** intent-falsification produced D-deltas → mechanical pass skipped (intent-delta). Deltas feed cycle 3.
