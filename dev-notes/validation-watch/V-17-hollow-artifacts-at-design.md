## V-17. HOLLOW artifacts at design — basis-rule + executable-verify residual

**Status: WATCHING.**

**Kind: correctness-watch.** The anticipated fix is a catcher (a Substantive-artifact lens, a basis-rule substance sub-edge, or a pre-verify check) firing at design-time, not a form-change — so it closes on a *caught* instance: a Clippy [ISSUES FOUND] tracing to a HOLLOW artifact named as a target without a behavioral claim, where a design-time catcher would have caught at [READY] what executable-verify caught at impl (see README closing rule).

**Decision (no dedicated mechanism shipped).** The framework
does not ship a dedicated catcher for "design decision names an
artifact as a binding/wiring target, the artifact exists at the
named location, but the artifact is a stub or wired-but-data-
disconnected." Existing partial coverage:

- Basis rule's embedded-claim edge (`core.md` §3.2) — catches
  HOLLOW when the design decision makes any claim about the
  artifact's current behavior (the observable fact at the cited
  range — e.g., terminal statement, return type — exposes
  stub-shape)
- Basis rule's true-unit basis (`core.md` §3.2) — a claim about
  a construct's behavior requires a citation to the construct's
  visible close paired with an observable fact about it
- Executable-verification artifact (`core.md` §4.3) — a stub or
  wired-but-disconnected artifact fails the project's test/build
  suite when the implementation exercises the wiring chain

**Why uncertain.** The residual class: design decisions that
NAME an artifact as a binding/wiring/target without making any
embedded claim about its substance (e.g., "add toggle bound to
`userSettings.darkMode`" without claiming anything about
darkMode's current downstream wiring). Basis rule doesn't fire
on substance; executable-verify catches it at impl, but by then
a full cycle's design has locked targeting a hollow artifact —
a wasted cycle. Whether this class produces observable Clippy
incidents (vs. being caught upstream by basis rule's claim-about-
behavior edge, or downstream cheaply by executable-verify) is
empirical. The GSD framework's verifier (gsd-verifier.md) ships
this as a four-level artifact taxonomy (exists/substantive/wired/
data-flows); whether it earns its place in Clippy's lens set is
unverified at n=0.

**Production signal to watch.** Any Clippy [ISSUES FOUND] traceable
to a HOLLOW artifact whose design decision named it as a target
WITHOUT making behavioral claims about it — where executable-verify
caught at impl-time what a design-time lens would have caught at
[READY]. **n>=1** of this specific shape (basis rule didn't fire,
executable-verify did, full cycle's worth of design landed on a
hollow target) earns a structural fix. The fix form depends on
the shape: a Substantive-artifact lens, a basis-rule sub-edge
(target-naming carries an implicit substance claim), or a pre-
verify check are the candidates.

Per `development-process.md` practice 8, this V-N is legitimate
(Y not classifiable upfront — fix form depends on the specific
shape that surfaces), not deferral-journal. The proposing context
was a cross-framework comparison with GSD's verifier, not an
observed Clippy incident.

---

