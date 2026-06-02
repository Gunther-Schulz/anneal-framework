# anneal-dev derivation — framework-core flow-back (R1–R4 + owed validation-watch)

**Status:** open — **R1 RESOLVED 2026-06-02** (this cycle, Option B); R2–R4 +
the contract-2 validation-watch entry remain. The framework-**core** questions the anneal-dev pass-2
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

**Triage note (practice 8):** each is a *design question* (is a framework change
warranted?), not yet a fix-in-hand — backlog material, not validation-watch
(none is parked-for-empirical-watching) and not an n=1 commit (no fix form
settled). Decide each on its own micro-cycle.

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

- **R2 — singular "the domain's executable verification."** `core.md` §4.3 +
  `foundation.md` contract 3 frame verification as one runnable artifact
  (pytest / debugger). Corpus-evolution's is a battery of four heterogeneous
  checks (one a fresh-context dispatch, one a human act). Fits via
  "dispatched/run, not asserted," but the singular noun + single-artifact
  examples lean narrower. Question: acknowledge a multi-check battery shape, or
  is the existing generalization sufficient framing?

- **R3 — a human check inside isolated verify.** Battery check (d) is operator
  diff-approval — but verify runs isolated and §1 bounds operator action to
  menu/interjection; the framework doesn't cleanly model a verify-internal check
  that is an operator act rather than a dispatched/program-run one. Minor.
  Question: should the framework name this?

- **R4 — no native runtime-resolution path for `target-dependents`.** The
  runtime-`[CONDITIONAL]` escape (`glossary.md` Coupling shape; `core.md`
  §3.2.2) is scoped to **target-behavior**; **target-dependents** is
  search-dischargeable. A render-resolved paraphrase dependent (a search cannot
  exhibit it) is a target-dependents case with no native runtime path, so
  anneal-dev binds it as an **extension** of the behavior-scoped path
  (pass-2 lens-set Missed-dependents + rationale R4). The contract-1
  de-pollution abstracted the coupling-shape *set* (Finding 5, dissolved) but
  did not give target-dependents this path. **Surfaced by the separate-context
  verify** catching a pass-2 over-claim — the reflexivity review earning its
  keep. Question: give target-dependents a runtime-`[CONDITIONAL]` path
  paralleling target-behavior?

## Also owed (same cycle origin)

- **Contract-2 render-ceremony validation-watch entry** — register a
  `validation-watch` V-N: watch whether the per-cycle re-render + fidelity check
  on the dev-process-as-instance justifies itself, or whether the shared kernel
  changes rarely enough to make it cheap. (Genuine design-uncertainty →
  validation-watch material, unlike R1–R4. Deferred from
  [[framework-dev-as-anneal]] step 4; its own micro-cycle.)

## Relates
[[framework-dev-as-anneal]] (origin), [[contract1-depollution-cluster]]
(R4 is the coupling-shape strain the de-pollution's Finding-5 abstraction
did not fully reach). Each question that lands is a framework-spec edit cycle
(skill-craft gate + separate-context review + step-4 discharge).
