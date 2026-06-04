## V-15. Standardized-pass lens noise on methodology-design tasks — collapse or accept?

**Status: WATCHING.**

**Decision (`core.md` §4.1.1 + `modules.md` §3.2).** Each cycle's
standardized inspection pass emits a line per lens whose scope
the cycle touched — a finding, cited-clean reason, or
out-of-scope reason. The lens set is accounted for whole once,
at [READY]. The current spec does not differentiate cycle
categories; every cycle's pass emits the per-lens enumeration.

**Why uncertain.** Unit 16 (a methodology-design task that
produced no code) generated 3 cycles × 12 lenses = 36 lens-lines,
of which ~24 were "cited-clean (re-attest)" or "out of scope
this cycle." For tasks that don't touch code (audit-only,
methodology-design, framework-design), most lenses are
perpetually out-of-scope or trivially clean; the protocol forces
rote per-lens lining anyway. Cost is small per-line but
cumulative across cycles.

Possible spec sharpening (deferred pending recurrence):

- *Form 1 — cycle-category enum*: classify cycles as
  `code-change | refactor-only | methodology-design | audit-only`,
  with per-category default lens-scope. Out-of-scope lenses
  batch-collapse to a single line per cycle.
- *Form 2 — batch out-of-scope*: keep per-lens lining but allow
  a "batch out-of-scope: [list] — cited reason: [reason]" line
  covering multiple lenses. AI still enumerates which, just
  doesn't write a per-lens line.

At n=1 (Unit 16) the categories are not stable; shipping Form 1
risks premature codification. Form 2 is incremental but adds
protocol surface without strong evidence the savings justify.
Defer; watch.

**Production signal to watch.** Future runs where ≥50% of
lens-lines collapse to "cited-clean re-attest" or "out-of-scope"
across 3+ cycles. If recurrent across 3+ runs with consistent
shape (same categorical pattern), Form 1 earns its place. If
the lens-noise pattern is one-off (only methodology-design
runs), Form 2 may be sufficient.

**Closing criterion (WATCHING → RESOLVED via sharpening).** One
run shows ≥50% cited-clean-re-attest or out-of-scope lens-lines
in a recognizable categorical pattern (code-change /
refactor-only / methodology-design / audit-only). Ship Form 1 or
Form 2 per the observed shape.

**Alternative closure (WATCHING → INVALIDATED).** One run shows
the lens-noise pattern was one-off (specific to its categorical
context) and does not generalize. Accept current per-lens lining
as design intent.

---

