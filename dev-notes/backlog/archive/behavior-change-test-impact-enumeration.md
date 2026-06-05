# Behavior-changing decision → executable test-impact enumeration

**Status:** OPEN — finding (cross-session clippy run, 2026-06-02; "dry-mode paper
bankroll" unit). A **sibling** of [[clippy-run-findings-dispatch-coupling]]
Finding 3 (design-phase static-blind to behavioral coupling, shipped Cycle F3)
that the shipped fix does **not** cover. Also a face of
[[verified-integrity-consolidation]].

**Gap.** A design decision that **changes an observable / computed behavior** has
a third coupled surface beyond code-callers (consumer-enumeration) and downstream
behavior (lenses): **existing tests that assert the *old* behavior.** These are
**invisible to a symbol-grep** — a test may assert a *derived value* (e.g. `9.98`)
while calling a higher-level entry point, never mentioning the changed symbol.
n=1: D2 changed dry-mode bankroll (probe-value → config-value); an existing test
asserting the derived `9.98` broke, and a grep on the changed symbol would never
find it. The Finding-3 shipped clause covers **subtype-construction** behavioral
coupling; **test-assertion breakage from a behavior change is the sibling it
doesn't cover** (confirmed in the dump's own analysis).

**Fix shape (primary).** Extend the Replacement/amendment apparatus: a decision
that changes an observable/computed behavior carries an **implicit completeness
claim** that existing tests asserting the prior behavior are enumerated — and
because a test can assert a *derived* value without referencing the symbol, the
enumeration is **executable, not search-based**: run the relevant suite against a
spike of the change; the failing tests *are* the enumerated set; their
expected-value updates **enter the locked design scope** (listed old→new). This
moves the test-update into the locked design (the impl subagent transcribes,
doesn't judge) — no impl-time surprise, no loopback ambiguity. Same discipline
Clippy already trusts (executable verification), just **earlier** (design, not
final verify).

**Fix shape (secondary, lower-confidence).** A narrow "design-entailed change"
carve-out to always-loopback: a diff touching an out-of-scope identifier is *not*
a loopback **iff** the subagent cites the specific [VERIFIED] decision that
**mechanically entails** the change (e.g. `99.98 = 100.0 − 0.01 − 0.01`, from D2)
and verify re-derives the entailment; any new judgment → loopback. Reintroduces a
sliver of the judgment always-loopback removes — belt-and-suspenders if the
primary ships.

**Level.** Framework (§ Replacement / §3.2 / §4.2 always-loopback + impl-plan) +
clippy render. Relates to [[clippy-run-findings-dispatch-coupling]] Finding 3,
[[verified-integrity-consolidation]] (incomplete-evidence face).
