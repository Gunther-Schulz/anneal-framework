# Clippy write-side boundary gap (F29 — destructive merge clobbers an authoritative value)

**Status:** OPEN — occurrence-grounded, surfaced 2026-06-07 by a clippy **Unit-31 run on beat-the-books**
(on clippy v0.9.95 — i.e. *with* the just-shipped §3.2.2 emitted-effect/co-producer lenses, and it still
fell through). Clippy **instance** lens-set concern (coding-domain), NOT framework/-dev. Caught at impl-review,
not design.

## The occurrence (F29)
An `UPSERT … DO UPDATE SET col = EXCLUDED.col` **clobbers a prior authoritative stored value** with a
NULL/default the producer emits on its **failure/empty branch**. The bad value's branch lived at a call site
the locked decision (D5) *referenced but did not author*, and the `DO UPDATE` clause itself doesn't branch —
so it was outside the standardized-pass scope when `= EXCLUDED` was locked. Result: data loss, caught only at
impl-review.

## Why it fell through the current lens set
- **Silent-substitution-at-boundary** guards the **read** side (missing input → surfaced failure vs silent
  default) — F29 is its exact **write-side mirror**, uncovered.
- **Branch-coverage** is closest but the offending branch is at an un-authored caller → out of the locked
  decision's standardized-pass scope.
- **Coupled-change / Consumer-enumeration** (incl. the new co-producer / emitted-effect forms) cover
  *co-producers disagreeing* + *emitted-effects across a replacement* — not *one writer's merge clobbering its
  own prior write with a non-authoritative value*.

## The OPEN design-Q (resolve in the cycle, do NOT pre-commit to "new lens")
The transcript proposed a **12th lens** (`Destructive-merge-at-write`). Apply the **additive-reflex** check
(skill-craft: name what the edit *reduces*) before adding one. The genuine alternatives:
- **(a) Extend `Silent-substitution-at-boundary` to bidirectional** — same principle (a non-authoritative value
  silently standing in for an authoritative one), two directions: read-in / write-out-merge-clobber. One lens
  covers both → Pareto. *(Candidate-preferred — name reduces, not adds.)*
- **(b) Scope-sharpen** `Branch-coverage` + `emitted-effect` to reach **the producer's branches at call sites
  the decision references but doesn't author** (the actual scope hole the root-cause names).
- **(c) New lens** (the transcript's `Destructive-merge-at-write`) — only if the *destructive-merge / clobber-a-
  more-authoritative-value* harm is genuinely a distinct axis (a)+(b) can't carry.
Likely answer: some mix of (a)+(b); (c) only if skill-craft confirms a distinct axis.

## Sub-note (weaker; check before acting)
The transcript's secondary "re-attack a fix's own failure branches in the falsification brief" — it half-retracts
it, and it overlaps the **§3.2.2 behavior-CHANGE** clause shipped this session (a fix *is* a behavior change →
completeness claim over its branches). Check whether §3.2.2 already covers it before any framework brief-edit.
If it generalizes, that piece is **framework/-dev** (falsification dispatch-brief), not clippy.

## Channel
- **Tactical (other session, beat-the-books):** a `clippy.config/lenses.md` project-supplement is additive-only /
  low-risk → fine to guard the running Unit-31; removable once core ships.
- **Core:** clippy `spec/lens-set.md` → re-render `references/lenses.md` → release, via an anneal-dev clippy cycle
  (skill-craft-gated). **Do NOT hand-edit the cached plugin** (`…/plugins/cache/coding-clippy/0.9.95/…`).

## Relates to
- `coding-clippy/spec/lens-set.md` (Silent-substitution-at-boundary, Branch-coverage) · the §3.2.2 emitted-effect/
  co-producer work shipped 2026-06-07 (`clippy-reinstantiation`) · `forcing-function-dose-discriminator` (force/
  surface/build) · origin: beat-the-books Unit-31 F29.
