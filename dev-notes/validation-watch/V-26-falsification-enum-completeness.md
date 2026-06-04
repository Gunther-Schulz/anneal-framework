## V-26. Falsification closed-enum domain-completeness — are 3 coupling shapes / 3 predicate types enough across domains?

**Status: WATCHING.**

**Decision (`core.md` §4.1.4, `glossary.md` Coupling shape /
Falsification predicate, `modules.md` §3.4).** Cycle c-safe (2026-06-02)
de-code-ified the falsification machinery: the coupling shapes
(target-existence / target-dependents / target-behavior) and the
predicate types (`any-match` / `any-outside-scope` / `expected-match`)
are now stated domain-generally, with the concrete evidence form
instance-bound. Both stay **closed enums**. The accepted residual: if a
real non-code domain needs a 4th coupling shape or predicate type, that
is a framework amendment — the contract-1 (domain-pollution) failure
recreated one level up — accepted as the correct trade against a
premature open/extensible enum built for domains that do not yet exist.

**Why uncertain.** Whether 3 coupling shapes and 3 predicate types are
domain-*complete* cannot be settled without a non-code instance actually
exercising the falsification pass. Closing the enum is the non-premature
move (no extensibility for hypothetical domains, practice 7); opening it
now would be the over-build. But the completeness claim itself is
unverifiable today — the earlier "3 types are logically complete" framing
was retracted as overclaim. The honest frame is current-best-closed,
amend-if-a-real-domain-proves-a-4th-needed.

**Production signal to watch (n=1).** The first non-code instance's
falsification pass hits a basis-coupling or falsifying-rule it cannot
express with the closed set — forced to mis-tag a candidate's shape,
mis-fit a predicate, or amend the spec. That warrants reconsidering
closed-vs-open. **Specific watch:** `target-dependents` in a non-code
domain includes a **paraphrased restatement** invisible to verbatim
search (e.g. a rendered plugin clause) — which may have no existing
evidence-binding; the one place the "no new binding" abstraction could
break. [Update 2026-06-02 — R4 (`dev-notes/backlog/archive/anneal-dev-framework-flowback.md`):
this sub-case DOES have a binding — a render-resolved paraphrase is the
**target-behavior** runtime [CONDITIONAL] path (the rule's behavior
resolving through an unsurfaced dependent, `core.md` §3.2.2), now
documented at `glossary.md` Coupling shape. The broader watch — a
genuinely new 4th coupling shape / predicate type for a non-code domain
— remains open.]

**n=1 (seed).** None yet — no non-code instance has run falsification.
The anneal-dev / planner derivations (`framework-dev-as-anneal`,
`planner-instance-exploration`) are the eventual tests; the Pass-1
anneal-dev draft already flagged the paraphrase-drift dependent as a
concrete case the old closed code-shaped enum could not express.

Per `development-process.md` practice 8, this V-N is legitimate: genuine
uncertainty about a design choice's correctness (the closed enum's
domain-completeness), to settle empirically against a real non-code
domain — not deferral of a classifiable fix (no fix is in hand; opening
the enum now would be the premature move).

