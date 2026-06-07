# f0-render-conventions — cycle 2 standardized-pass

In scope this cycle = lenses the cycle's design work touched (the isolation.md scaffold design D2,
the README amendment D3, the glossary sharpening D4).

- **Missed-dependents** — CLEAN (grounded): D3 amends the README slot-list — sole enumeration at
  `:25-48` (run: `grep 'spec/.*\.md' instance-template/README.md`); D4 amends Basis/Completeness —
  no file cites `glossary.md Basis`/`Completeness` (run: `grep -rn` across specs+guide → 0). Both
  additive, dependents enumerated and empty/sole. basis: F7 run-searches, D3/D4 sub-annotations.
- **Undefined-shorthand** — RESOLVED by D4: the four NEEDS terms (located read, construct-taken-whole,
  executable verification, wrap-tolerant search) get a glossary definition; the discriminator excluded
  the self-evident/covered terms. basis: F7.
- **Fragmentation** — CLEAN: D4 defines concisely + retains the `core.md §3.2` pointer (the full rule
  stays single-homed in core.md); D2's isolation.md points at `core.md §4.2.3` rather than restating
  the isolation rule. No second canonical home created. basis: D4 body (gloss+pointer), D2 body
  (header→core.md), `glossary.md:53-54` (existing "specified in core.md §3.2" pattern).
- **Bloat** — CLEAN: D4 chose define-in-place over 4 new headwords (anti-Additive-reflex); D2's
  isolation.md is load-bearing — its file-presence is the producer-independent signal the slot exists
  (`instantiation-guide.md:404-408`). No non-load-bearing scope added by the designs. basis: D4
  considered-line, located read `:404-408`.
- **Leakage** — CLEAN (design commits to domain-general): D2's isolation.md is modeled on the
  domain-general persistence.md placeholder (no language/tool concretion); re-attested on the drafted
  prose at impl self-check. basis: `instance-template/spec/persistence.md` (domain-general).
- **Unenforced-rule** — CLEAN: the "file for every slot" claim is enforced by file-presence
  (`:404-408`); D2 makes the artifact exist, satisfying it — no enforcement prose needed. basis:
  located read `:400-408`.
- **Lossy-render / Over-claimed-verification** — CLEAN: D4 is additive (list→define), no enforcement
  strength softened; D2 renders no rule (placeholder). The [VERIFIED] tags on D2/D3/D4 carry
  true-unit bases (run searches for the amendment completeness claims). basis: D2/D3/D4 bases.

No load-bearing finding open. All cycle-2 design decisions [VERIFIED]. Next: the convergence cycle
(intent-falsification + mechanical falsification, fresh-context dispatch) required before [READY].
