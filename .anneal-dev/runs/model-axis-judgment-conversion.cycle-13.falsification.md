# Mechanical falsification pass — cycle 13 (convergence)

Run: `model-axis-judgment-conversion`. Convergence cycle; this cycle's
intent-falsification pass ran clean (no `mechanical-falsification-candidate`
finding), so the mechanical pass runs. Fresh-context mechanical falsification
subagent. Self-hosting: live co-located spec governs (`spec/*`,
`anneal-dev/spec/bindings.md`, `foundation.md`).

Unit scope: the [VERIFIED] D-entry set at the convergence cycle's start —
D1, D2, D3, D4, D5, D6, D7, D8, D10 (9 entries). D9 is [CONDITIONAL] — out of
scope (its operator-resolvable assumption is discharged by verify, not
falsified textually).

Reduced-to-latest lines used: D1 :83-85 · D2 :166 · D3 :153 · D4 :178 ·
D5 :181-182 · D6 :185 · D7 :91 · D8 :175 · D10 :94.

Coupling-shape closed set (`spec/glossary.md` Coupling shape):
target-existence / target-dependents / target-behavior. Predicate closed set
(`spec/modules.md` §3.4): `any-match` / `any-outside-scope:<scope>` /
`expected-match:<pattern>`. Shape-coherence: target-dependents → any-match /
any-outside-scope; target-existence / target-behavior → expected-match.
The subagent declares candidate + predicate + result and fills per-candidate
holds-or-falsified by applying the predicate; the orchestrator independently
recomputes every verdict from the cited result.

Legend for `candidate`: each is an executable, wrap-tolerant query or a located
read, RUN this cycle; `result` cites the actual output verbatim/abridged.

---

## D1 — Home split (kernel principle ↔ instance model-tier concretion)

Basis (reduced-to-latest :83): F1 + located read `foundation.md:32-40` — one
fact: contract 3 enumerates "dispatch-orchestration mechanics" as an instance
slot. Shapes the basis depends on: target-existence (foundation contract-3
text licenses instance-side homing), target-dependents (F1's corpus-wide claim
that the framework spec carries no harness-model vocabulary that would conflict
with instance-side homing). Not a closed-set-rendering decision.

- **{target-existence}**
  - candidate: located read `foundation.md:32-40`, predicate
    `expected-match:dispatch-orchestration mechanics`
  - result: line 37 reads "domain-specific lens shapes,
    **dispatch-orchestration mechanics**. The architecture's instance slot, not
    framework gaps." Pattern present.
  - holds-or-falsified: **holds**
- **{target-dependents}**
  - candidate: `rg -n 'model tier|model-tier|dispatch model|harness model|checker.capability|above.*diverse.*equal-ceiling|top tier' spec/core.md spec/modules.md spec/glossary.md instantiation-guide.md`, predicate `any-match`
  - result: NO MATCHES. (F1 re-run `rg -n 'model' spec/core.md spec/modules.md spec/glossary.md instantiation-guide.md` returns only 4 non-harness hits: core.md:3 "the model" spine, core.md:385 "the AI's model of it", core.md:618 "intent-model", core.md:883 "append-only model".)
  - holds-or-falsified: **holds** (empty result → no falsifying match)
- **aggregate: holds**

---

## D2 — Kernel principle, re-formed 4 (two-axis checker-capability independence)

Basis (reduced-to-latest :166): F26 + F27 + cycle-8 basis (cycle-7
falsification result + F21 + F25 + located read `modules.md:288-329` — brief
clause (c) is where per-dispatch parameters live) + earlier `core.md:596-621`
(intent-pass names fresh-context/criteria-first as its independence levers) and
`core.md:554-587` (coverage-check (i)-(v), the mirror pattern). Amendment
decision (amends `core.md` §4.1.4, `modules.md` §3.4.1 + §3.3, glossary) →
target-dependents mandatory. Renders/branches on the closed enum
{above/diverse/equal-ceiling} + below-actor → target-behavior closed-set
candidate.

- **{target-existence}** (amend-target intent-pass paragraph)
  - candidate: located read `spec/core.md:596-621`, predicate
    `expected-match:criteria-first`
  - result: core.md:597 "fresh-context, **criteria-first** adversarial attack
    on whether the locked design serves its intent"; the paragraph (596-621)
    names fresh-context/criteria-first as the independence levers and carries no
    checker-capability axis (the delta D2 adds). Pattern present.
  - holds-or-falsified: **holds**
- **{target-existence}** (reduced-latest cited read — brief clause (c))
  - candidate: located read `spec/modules.md:288-329`, predicate
    `expected-match:unit scope`
  - result: modules.md:288 "**Dispatch-brief schema.**"; clause (c) at 300-314
    is "**unit scope**" carrying the per-dispatch parameters (implement /
    convergence-falsification / intent-falsification). Pattern present.
  - holds-or-falsified: **holds**
- **{target-dependents}** (reference enumeration of the intent-independence rule-statement)
  - candidate: `rg -n 'criteria-first' --glob '!.anneal-dev' --glob '!dev-notes'`, predicate `any-outside-scope:{spec/core.md, spec/glossary.md, anneal-dev/plugin/**}`
  - result: 3 hits — `spec/core.md:597` (§4.1.4, D2 target), `spec/glossary.md:227` (Intent-falsification entry, D2/D7 target), `anneal-dev/plugin/skills/anneal-dev/phases/investigate-design.md:289` (render = D8 render-debt). All within scope; no rule-statement dependent outside the D2 target set ∪ D8 render plan.
  - holds-or-falsified: **holds**
- **{target-behavior}** (closed enum completeness — the set D2 renders/branches on)
  - candidate: located read reduced-latest D2 line (`.anneal-dev/runs/model-axis-judgment-conversion.md:166`, clauses (viii)+(ix) — the enum's defining source pre-render; `rg -n 'Checker-capability' spec/ anneal-dev/spec/` confirms zero live-spec rendering yet), predicate `expected-match:regex:above.*diverse.*equal-ceiling`
  - result: :166 (ix) worked examples "…parameter at T1 → **above**/declared · …that model → **diverse**/declared · …the actor model itself → **equal-ceiling**/assumed · …dispatch parameter at T2 under a T1 actor → **no relation, malformed dispatch**"; clause (viii) "the enum stays three-membered, the below-actor input class **loudly not-covered** (named disposition)". All three members + the below-actor input class dispositioned. Pattern present (above…diverse…equal-ceiling in sequence).
  - holds-or-falsified: **holds**
- **aggregate: holds**

---

## D3 — Instance binding amendment, re-formed 4 (three-step relation rule, boundary cell)

Basis (reduced-to-latest :153): F23 + F25 (opus finding-C) + cycle-6 basis
(F17 + `bindings.md:312-325` bootstrap-placeholder format) + located read
`anneal-dev.config/model-tier.md` — one fact: no `order:` line exists today.
Amendment decision (amends `anneal-dev/spec/bindings.md` §Dispatch model tier +
both config artifacts) → target-dependents mandatory. Branches on the enum
{above/diverse/equal-ceiling} in operator-facing words → target-behavior
closed-set candidate.

- **{target-existence}** (current blanket rule + no-order-line, the state the delta amends)
  - candidate: located read `anneal-dev/spec/bindings.md:265-289` + `grep -c 'order:' anneal-dev.config/model-tier.md`, predicate `expected-match:runs at the configured model tier`
  - result: bindings.md:265-269 "**The rule (blanket).** Every anneal-dev subagent dispatch — across **all** dispatch kinds … **runs at the configured model tier**" with no actor-relative clause; `grep -c 'order:' anneal-dev.config/model-tier.md` → 0 (no ordering declared, D3's inert-by-default premise). Pattern present.
  - holds-or-falsified: **holds**
- **{target-dependents}** (reference enumeration of the model-tier binding rule)
  - candidate: `rg -ln 'Dispatch model tier|model-tier' --glob '!.anneal-dev' --glob '!dev-notes/backlog'`, predicate `any-outside-scope:{anneal-dev/spec/bindings.md, anneal-dev.config/model-tier.md, anneal-dev.config/README.md, anneal-dev/plugin/**, dev-notes/**}`
  - result: 8 hits — `anneal-dev/spec/bindings.md`, `anneal-dev.config/model-tier.md`, `anneal-dev.config/README.md` (all D3 targets); `anneal-dev/plugin/skills/anneal-dev/SKILL.md`, `.../references/foundations.md` (render = D8 render-debt); `dev-notes/briefs/2026-07-17-…`, `dev-notes/briefs/2026-07-16-…`, `dev-notes/validation-watch/V-29-…` (dev-notes informational, non-rule-corpus). All within scope; no binding-rule dependent outside the D3 target set ∪ D8 render plan ∪ dev-notes.
  - holds-or-falsified: **holds**
- **{target-behavior}** (closed enum the three-step rule branches on)
  - candidate: located read reduced-latest D3 line (`…-conversion.md:153`) + carried cycle-6 three-step rule (:135), predicate `expected-match:equal-ceiling`
  - result: :153 "runs per the three-step relation rule, and **absent a declared ordering** it runs the **actor model itself** … header = **equal-ceiling** + ordering-basis: assumed"; cycle-6 :135 "a strictly higher tier where one exists (**above**); else a different model within the actor's tier (**diverse**); else same-model, recorded **equal-ceiling**". All three members dispositioned; the boundary-cell member (equal-ceiling/assumed) present. Pattern present.
  - holds-or-falsified: **holds**
- **aggregate: holds**

---

## D4 — Closed-set completeness claim, re-formed 2 (category-keyed always-include + worked example)

Basis (reduced-to-latest :178): F29 + cycle-6 basis (F14 + F16 + located read
`modules.md:405-411` — the amendment/target-dependents always-include sentence
is the verbatim pattern mirrored). Amendment decision (amends `core.md` §3.2.2
+ `modules.md` §3.4) → target-dependents mandatory. The decision itself is
about closed-set completeness and its §5.2(c) worked example uses the run's own
enum {above/diverse/equal-ceiling} + below-actor as the closed set →
target-behavior closed-set candidate.

- **{target-existence}** (mirror source — the always-include precedent)
  - candidate: located read `spec/modules.md:405-411`, predicate
    `expected-match:always include`
  - result: modules.md:408-411 "Amendment decisions (`core.md` §3.2.2)
    **always include** target-dependents in the basis's claimed shapes; the
    candidate set's target-dependents candidate re-runs §3.2.2's reference
    enumeration as its search." Pattern present — the verbatim always-include
    pattern D4 mirrors for the closed-set case.
  - holds-or-falsified: **holds**
- **{target-dependents}** (reference enumeration of §3.2.2, the amended artifact)
  - candidate: `rg -n '3\.2\.2|closed value set|closed-set|closed set' spec/core.md spec/modules.md spec/glossary.md`, predicate `any-outside-scope:{spec/core.md, spec/modules.md, spec/glossary.md}`
  - result: hits confined to the three kernel spec files — `spec/glossary.md` (4,58,105,106,109,127,133,536), `spec/modules.md` (359,389,408,410,486,497), `spec/core.md` (247 = the §3.2.2 home, 526,547,558,560,1180). No §3.2.2 cross-reference outside the kernel spec (renders are D8's). All within scope.
  - holds-or-falsified: **holds**
- **{target-behavior}** (closed-set member completeness — the enum D4's worked example ranges over)
  - candidate: located read reduced-latest D4 line (`…-conversion.md:178`), predicate `expected-match:loudly not-covered`
  - result: :178 "member dispositions: above = datapoint-warranted full elevation, diverse = residual-visible, equal-ceiling = residual-visible, below-actor input class = **loudly not-covered** → all named → the closed-set candidate (`expected-match` on each member in the basis) holds". Every member + below-actor dispositioned; the completeness-critical below-actor disposition (F27's former gap) present.
  - holds-or-falsified: **holds**
- **aggregate: holds**

---

## D5 — Worked-boundary-example obligation, re-formed 2 (tasked checkers + worked example)

Basis (reduced-to-latest :181 + :182 sub-annotation): F29 + cycle-8 basis
(F22 + cycle-4 basis + located read `core.md:406-426` — one fact, corrected
cycle-13: the §4.1.1 supporting-facts enumeration contains no §5.2(c)/
worked-example item) + the F26→D2(ix) ledger sequence. Amendment decision
(amends `core.md` §5.2 Body-shape (c) + §4.1.1 + one §4.1.4 sentence) →
target-dependents mandatory. Not a closed-set-rendering decision.

- **{target-existence}** (amend-targets: §5.2(c) current text + §4.1.1 enumeration gap)
  - candidate: located read `spec/core.md:1172-1187` + `spec/core.md:406-426`, predicate `expected-match:observable conditions`
  - result: core.md:1177 "**acceptance criteria** — **observable conditions** for the decision to count as implemented" — Body-shape (c) as claimed, no boundary-example obligation. §4.1.1 (406-426) supporting-facts enumeration (standardized lens set · last cycle's pass · every decision [VERIFIED]/[AUTO-ACCEPTED] · embedded target-naming/count premises carry re-runnable basis · no finding open · convergence intent-findings dispositioned) contains no §5.2(c)/worked-example item — confirming the sub-annotation's corrected observable fact. Pattern present.
  - holds-or-falsified: **holds**
- **{target-dependents}** (reference enumeration of Body-shape §5.2)
  - candidate: `rg -n 'Body shape|Body-shape|acceptance criteria|§5\.2|5\.2 \(c\)' spec/core.md spec/modules.md spec/glossary.md`, predicate `any-outside-scope:{spec/core.md, spec/modules.md, spec/glossary.md}`
  - result: all hits within the kernel spec — "Body shape" only at `core.md:1172` (the home, D5 target); "acceptance criteria" at `core.md:1177` (D5 target); the remaining §5.2 references are kernel-internal state-machine citations (core.md 69,365,389,416,425,549,630,650,670,899,1124,1244,1302; modules.md 23,75,113,403; glossary.md 335,404,411). No Body-shape (c) dependent outside the kernel spec (renders are D8's). All within scope.
  - holds-or-falsified: **holds**
- **aggregate: holds**

---

## D6 — Domain-claim re-derivation, re-formed 2 (claimed/re-derived pair + worked example)

Basis (reduced-to-latest :185): F29 + cycle-6 basis (F20 + `core.md` §3.1
evidence-bearing gradient + cycle-1 located read `modules.md:483-485` — the
refutation field currently requires "the located read or query that surfaced
the concern" without a primary-source requirement) + the F28 ledger event; the
MATCH-cell worked example cites primary source `bindings.md:265-276`. Amendment
decision (amends `core.md` §4.1.4 intent-pass + `modules.md` §3.4.1 refutation
field) → target-dependents mandatory. Not a closed-set-rendering decision
(references the route closed set but leaves it unchanged).

- **{target-existence}** (amend-target refutation field + the worked example's primary source)
  - candidate: located read `spec/modules.md:483-485` + `anneal-dev/spec/bindings.md:265-276`, predicate `expected-match:the located read or query that surfaced the concern`
  - result: modules.md:483-485 "**refutation** — **the located read or query that surfaced the concern** (per `core.md` §3.2 — search-established, not a recalled hypothesis)" — as claimed, no claimed/re-derived-pair requirement (the delta D6 adds). D6's MATCH-cell primary source bindings.md:265-269 reads "Every anneal-dev subagent dispatch — across **all** dispatch kinds … runs at the configured model tier" (zero actor-relative clauses), grounding the worked example's re-derived-fact. Pattern present.
  - holds-or-falsified: **holds**
- **{target-dependents}** (reference enumeration of the refutation field)
  - candidate: `rg -n 'refutation' spec/core.md spec/modules.md spec/glossary.md`, predicate `any-outside-scope:{spec/modules.md §3.4.1}`
  - result: 4 hits, all in `spec/modules.md` §3.4.1 — 453 (`attempted-refutation` schema line), 459 (per-R# attempted-refutation), 477 (per-finding schema line), 483 (the refutation field, D6 target). No refutation-field dependent outside §3.4.1 (renders are D8's). All within scope.
  - holds-or-falsified: **holds**
- **aggregate: holds**

---

## D7 — Glossary (new "Checker-capability relation" entry + extend "Intent-falsification pass")

Basis (reduced-to-latest :91): F4 + located read `glossary.md:226-236` — one
fact: the intent-falsification entry names fresh-context/criteria-first only.
Amendment decision (extends an existing glossary entry) + new-entry addition →
target-dependents mandatory (new-term collision / no second definition).
Defines the enum {above/diverse/equal-ceiling} → target-behavior closed-set
candidate.

- **{target-existence}** (the entry D7 extends)
  - candidate: located read `spec/glossary.md:226-236`, predicate
    `expected-match:criteria-first`
  - result: glossary.md:226-228 "**Intent-falsification pass** — the
    convergence cycle's judgment-class soundness pass: a fresh-context,
    **criteria-first** … adversarial attack …"; the entry (226-236) names
    fresh-context/criteria-first only, no checker-capability axis. Pattern
    present.
  - holds-or-falsified: **holds**
- **{target-dependents}** (new-term collision — no pre-existing conflicting definition)
  - candidate: `rg -n 'Checker-capability|checker capability|checker-capability' spec/glossary.md`, predicate `any-match`
  - result: NO MATCHES. (F10 distinct-term check `rg -n 'capability' spec/glossary.md` → 207,223 "falsifying capability" (the Falsification-predicate entry, unrelated phrase), 527,532 "capability-boundary" (extensions, a distinct concept). No pre-existing "checker-capability relation" definition to collide with — the acceptance "no second definition anywhere" is satisfiable.)
  - holds-or-falsified: **holds** (empty result → no colliding definition)
- **{target-behavior}** (closed enum the entry defines)
  - candidate: located read reduced-latest D7 line (`…-conversion.md:91`), predicate `expected-match:above/diverse/equal-ceiling`
  - result: :91 "new entry 'Checker-capability relation' (definition + closed enum **{above/diverse/equal-ceiling}** + §4.1.4/§3.4.1 citations)". All three members enumerated as the entry's closed set. Pattern present.
  - holds-or-falsified: **holds**
- **aggregate: holds**

---

## D8 — Dependents plan, re-formed 4 (three dependent kinds; daneel locator corrected)

Basis (reduced-to-latest :175): cycle-11 finding-2 pair (executed ls/find/rg
queries, orchestrator-computed falsification) + cycle-6 basis (three dependent
kinds; clippy confirmed local-source; copywriting-quill not a render instance;
`instance-reinstantiation.md:61-66` per-instance keyed rows). The entry's whole
content is a target-dependents enumeration → target-dependents candidate
(re-run the enumeration); the daneel row keys to a rendered-plugin locator
whose existence is a target-existence claim → target-existence candidate.

- **{target-dependents}** (re-run the cross-instance render + spec-binding enumeration)
  - candidate: `rg -l 'intent-falsification|convergence cycle' /home/g/dev/Gunther-Schulz/coding-clippy` + `rg -ln 'Dispatch models|dispatch model' /home/g/dev/Gunther-Schulz/coding-clippy/spec/` + `rg -l 'intent-falsification|convergence cycle' /home/g/.claude/plugins/cache/daneel`, predicate `any-outside-scope:{/home/g/dev/Gunther-Schulz/anneal-framework/anneal-dev/plugin, /home/g/dev/Gunther-Schulz/coding-clippy, /home/g/.claude/plugins/cache/daneel}`
  - result: clippy render tree = 5 files (`docs/what-clippy-is.md`, `plugin/skills/clippy/SKILL.md`, `.../references/tracker.md`, `.../references/foundations.md`, `.../phases/investigate-design.md`) + spec dispatch-binding `coding-clippy/spec/bindings.md`; daneel cache render = 3 files (`daneel/daneel/0.2.50/skills/daneel/references/closed-artifact.md`, `.../references/foundations.md`, `.../phases/investigate-design.md`). All hits within the three enumerated dependent scopes (anneal-dev plugin = self, clippy, daneel cache). No render/binding dependent outside D8's enumerated set.
  - holds-or-falsified: **holds**
- **{target-existence}** (daneel render exists at the cache locator; no local source → locate-source-first)
  - candidate: `find /home/g/dev/Gunther-Schulz -maxdepth 2 -iname '*daneel*'` + `ls /home/g/.claude/plugins/cache/daneel/daneel/0.2.50/skills/daneel`, predicate `expected-match:daneel/daneel/0.2.50`
  - result: `find` → only `/home/g/dev/Gunther-Schulz/beat-the-books/.daneel` (run-state, no skills tree — confirming "no local source repo," the locate-source-first class); the render exists at cache locator `/home/g/.claude/plugins/cache/daneel/daneel/0.2.50/skills/daneel/{references,phases}` (3 files enumerated above). D8's row keys to the rendered-plugin locator + locate-source-first, not to the dead `beat-the-books/.daneel` locator (the cycle-11 correction). Pattern present in the render locator.
  - holds-or-falsified: **holds**
- **aggregate: holds**

---

## D10 — Verify dispatch stays under the blanket floor (not elevated)

Basis (reduced-to-latest :94): requirements record (operator verbatim: fork (a)
NARROW, scoped to intent-falsification) — one fact: the disposition names the
judgment-class leg (intent-falsification) as the carve-out scope. Not an
amendment (D10 emits no kernel text — F30), not a closed-set-rendering
decision. Sole shape: target-existence of the requirements-record scope
statement.

- **{target-existence}** (requirements record scopes the carve-out to intent-falsification, keeping other legs — incl. verify — in the floor)
  - candidate: located read requirements record R1/R2 (`.anneal-dev/runs/model-axis-judgment-conversion.md:29-35`), predicate `expected-match:mechanical/lens legs stay inside the same-tier floor`
  - result: R1 :29-31 "carves the **judgment-class check (intent-falsification)** out of the same-tier floor"; R2 :34-35 "The carve-out is **scoped, not blanket**: **mechanical/lens legs stay inside the same-tier floor**". The requirements record scopes elevation to the intent-falsification leg only; verify (a non-intent-falsification leg) stays in the floor — D10's committed position. Pattern present.
  - holds-or-falsified: **holds**
- **aggregate: holds**

---

## Summary (one line per decision-ID)

- **D1** → aggregate **holds** (target-existence, target-dependents)
- **D2** → aggregate **holds** (target-existence ×2, target-dependents, target-behavior)
- **D3** → aggregate **holds** (target-existence, target-dependents, target-behavior)
- **D4** → aggregate **holds** (target-existence, target-dependents, target-behavior)
- **D5** → aggregate **holds** (target-existence, target-dependents)
- **D6** → aggregate **holds** (target-existence, target-dependents)
- **D7** → aggregate **holds** (target-existence, target-dependents, target-behavior)
- **D8** → aggregate **holds** (target-dependents, target-existence)
- **D10** → aggregate **holds** (target-existence)

**No entry falsified.** All 9 [VERIFIED] D-entries hold across every covered
coupling shape. No [INVALIDATED]→[PENDING] flip triggered by this pass.

Gap surfaced for the orchestrator (not silently filled): the closed-set
(target-behavior) candidates for D2/D3/D4/D7 use the **design's own tracker
D-entry** as the enum's defining source, because the canonical render (the D7
glossary "Checker-capability relation" entry) is not yet in the live spec —
`rg -n 'Checker-capability' spec/ anneal-dev/spec/` returns zero (design phase,
pre-impl). Once rendered, the same closed-set candidates should re-run against
the rendered glossary entry as the defining source; for this pre-render
convergence cycle the tracker entry is the only extant defining source.
