# anneal-dev derivation — framework-core flow-back (R1–R4 + owed validation-watch)

**Status:** **CLOSED 2026-06-02** — R1–R4 all resolved; the contract-2 ceremony
cost filed as **V-27** (WATCHING, `dev-notes/validation-watch.md`). Archived
record. The framework-**core** questions the anneal-dev pass-2
derivation surfaced (`framework-dev-as-anneal` step 4, 2026-06-02). These are
**framework-kernel** decisions: per the bootstrap rule, the anneal-dev instance
never governs its own foundation, so each is decided framework-layer with
independent review — NOT inside the instance build. Spawned by
[[framework-dev-as-anneal]]; full evidence in
`dev-notes/derivation-pass2/spec/derivation-rationale.md` (Residual strains +
Framework-layer questions). This is the "~10-20% architectural flow-back" the
effort anticipated: forward-deriving the instance is how the framework gets
tested for its own domain, and these are where the fixed method still strained
*after* the contract-1 de-pollution.

**Triage note (practice 8):** each was a *design question* (is a framework change
warranted?) — decided on its own micro-cycle. **Outcome:** R1 + R4 → framework
fixes shipped; R2 + R3 → no framework change (the framework already handles them);
contract-2 → genuine uncertainty, filed as V-27 (WATCHING). Two of four needed a
kernel change; the other two dissolved on grounding — the forward-derivation's
value was as much in what it ruled OUT as in what it fixed.

## The four questions

- **R1 — §5.2(b) design-decision body-shape for prose work products. RESOLVED
  2026-06-02 (Option B).** Root cause: a code-shaped discriminator — "contract
  surface = what's observable from outside the element" assumes the element hides
  its internals, which only code reliably does; for prose nothing is hidden, so
  the test failed to separate contract from realization. **Fix:** abstracted to a
  coupling-based test — contract surface = "what a dependent would break if it
  silently changed"; realization = "the content nothing outside depends on"
  (`core.md` §5.2(b) + `glossary.md` Contract surface + target-existence), with
  the contract/realization line now explicitly the instance's binding. The prose
  case resolves cleanly (a rule's enforcement strength is on its contract surface
  because dependents rely on it). Separate-context self-review `a594164` PASS.
  **Subsumed** the prior standalone open item "design-decision body-shape vs
  verdicts" (D-track verdicts are the same §5.2(b) surface). Instance render-debt
  → [[clippy-render-resync]] + [[daneel-cycle-b-sync]].

- **R2 — singular "the domain's executable verification." RESOLVED 2026-06-02 —
  no framework change.** `core.md` §4.3 says "the domain's executable verification
  is run and its output shown" — appropriately abstract (a *collective*; the
  instance binds however many checks) and carries NO program examples. The
  pytest/debugger examples live only in `foundation.md` contract 3, explicitly as
  **instance-binding-scope** illustrations. anneal-dev bound a four-check battery
  without the framework blocking it (`derivation-pass2` bindings Verification
  battery) — the abstraction held (n=1). The singular noun reads as collective,
  not single-artifact-forcing; adding "one or more checks" would be Additive-reflex
  for a non-problem. Closed.

- **R3 — a human check inside isolated verify. RESOLVED 2026-06-02 — no framework
  change.** Operator diff-approval is not a verify-internal check: it's the §1(a)
  **menu-selection at a closed-artifact presentation** (post-verify [PASSED]) /
  the release-loop commit gate. The framework already separates verify (isolated,
  dispatched checks → [PASSED]) from operator approval (`core.md` §1(a)).
  anneal-dev minorly mis-grouped operator approval under its verify battery as
  check (d) — an instance presentation point, not a framework gap; noted for
  anneal-dev's next touch (it is the operator gate, not a dispatched check). Closed.

- **R4 — runtime-resolution for a search-unsurfaceable dependent. RESOLVED
  2026-06-02 — the premise was wrong; no mechanism was missing.** Grounding
  `core.md` §3.2.2 showed it already covers this: "a preserved-behavior claim …
  the behavior resolves at runtime through **a dependent the reference-search
  does not surface** … → [CONDITIONAL], basis exercised by executable
  verification." A render-resolved paraphrase is exactly that — the rule's
  behavior resolving through an unsurfaced dependent — so it routes the **native**
  target-behavior runtime path, NOT a target-dependents extension. (The pass-2
  "extension" framing, and the step-4 verify that prompted it, were both misled
  by the glossary presenting "dependents = search / behavior = runtime" as a
  clean split.) **Fix:** a glossary bridge sentence on the target-dependents
  bullet documenting the route + a mechanical-trigger guard against the "merely
  unfound → [CONDITIONAL]" dodge (`glossary.md` Coupling shape). No new
  mechanism. Separate-context review `aa72bc8` PASS-with-fixes (applied);
  corrected pass-2 framing (lens-set + rationale). Instance render-debt →
  [[clippy-render-resync]].

## Also owed (same cycle origin)

- **Contract-2 render-ceremony — FILED as V-27 (WATCHING) 2026-06-02.**
  Registered in `dev-notes/validation-watch.md` V-27: watch whether the per-cycle
  re-render + fidelity check on the dev-process-as-instance justifies itself once
  anneal-dev is operational, or whether the shared kernel changes rarely enough to
  make it cheap. (Genuine design-uncertainty → validation-watch, unlike R1–R4.
  Settles empirically at step 5 dogfood + promotion.)

## Relates
[[framework-dev-as-anneal]] (origin), [[contract1-depollution-cluster]]
(R4 is the coupling-shape strain the de-pollution's Finding-5 abstraction
did not fully reach). Each question that lands is a framework-spec edit cycle
(skill-craft gate + separate-context review + step-4 discharge).
