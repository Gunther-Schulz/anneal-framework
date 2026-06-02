# anneal-dev — Derivation rationale (pass 2)

Clean re-derivation of the anneal-dev instance from the
**de-polluted** anneal-framework spec + the corpus-evolution domain
facts. This is a fresh forward derivation, not an edit of pass-1:
the pass-1 draft (`dev-notes/derivation-pass1/`) was derived against
the un-de-polluted core and carries scar tissue — workarounds for
core strains that the de-pollution has since dissolved. This file
carries the §1 fit verdict, the lens-set path, the judgment calls,
the **scar-tissue-dissolved** map (the real point of the exercise —
the validation that the de-pollution abstractions worked), the
**residual strains** that survive de-pollution, and the naming
verdict.

---

## §1 — Domain-fit verdict

**The domain fits anneal's shape.** All three checks pass:

- **Open-ended.** A corpus-evolution task needs investigation and
  design, not execution of a known procedure: where a rule lives,
  what contract it encodes, what depends on it, and how to change it
  coherently are all investigated, not looked up. PASS.
- **Verifiable outcome.** "Done" is checkable against evidence:
  render-fidelity (clause-by-clause, separate context), coherence
  (cross-file/whole-corpus), skill-quality review, operator approval
  of the diff. These are dispatched-and-run, not asserted. PASS —
  and stronger than the §1 worst case (a domain with no executable
  verification): render-fidelity and coherence are genuinely
  executable (a separate context re-derives them), not merely static
  self-inspection.
- **Recurring blind-spots.** The domain has a body of recurring
  mistakes an expert watches for — the eight-phenomenon corpus the
  derivation was given. PASS, and it supports a **Path 1** lens set
  (incident-grounded), not the Path-2 bootstrap a fresh domain needs.

**Strains named** (each fits; the residual strains are detailed in
their own section below):

1. **Self-referential work product.** anneal-dev's verify battery
   (render-fidelity, coherence, skill-quality) is itself rule-corpus
   content a future anneal-dev run could edit. The framework's
   separate-context / isolation discipline keeps this safe (the
   checker is not the author), so the recursion does not break fit —
   it is why the verification battery leans on the framework's
   existing isolation rather than inventing instance-specific
   isolation.

2. **Design-decision body-shape (§5.2(b)) for prose rules.** A
   "what to build" body-shape (contract surface / acceptance
   criteria) binds for corpus-evolution but with a real strain —
   surfaced in Residual strains below. This is the known open
   framework question this derivation was asked to examine.

The multi-repo problem space and the prose-text basis are **no
longer strains** under the de-polluted core — see Scar tissue
dissolved.

---

## §2 — Inherited-and-fixed vs. supplied

**Inherited, NOT redesigned** (confirmed left untouched): the three
phases (investigate-design / implement / verify) and their specs;
the two-pass cycle and inspection; the basis rule and the
evidence-bearing-artifact rule; the tracker form and the
status-state machine; [READY] (incl. convergence cycle +
falsification pass); the two modes (interactive / auto-battle); the
orchestrator; the two values (the Purpose).

**Supplied** (and only this): bindings (§3, `bindings.md`); the
standardized lens set (§4, `lens-set.md`); the run-artifact
persistence mechanism (`persistence.md`); the **isolation slot**
binding (`bindings.md` — now a *declared* slot in the de-polluted
core, §4.2); plus the required-mechanism slots (extensions enable
mechanism, lens-supplement mechanism) and the optional presentation
slot.

The closed slot-set was respected: no new render-consumed slot was
invented. Multi-repo handling, the verification battery, and the
wrap-tolerant search were all placed as **binding refinements**
(extending existing rows / sections of the bindings), not as new
slots — per the §5 binding-refinement-vs-extension test. The
isolation slot is now an explicitly *declared* slot (`core.md` §4.2
"the **isolation slot** (`instantiation-guide.md` §2)"), filled
directly rather than worked around.

---

## §4 — Lens-set path and shape

**Path 1 — incident-grounded.** The given recurring-mistakes corpus
IS the domain's incident history, so the set is derived from real
recurring failures, not blank-slate hypotheses. Path 1 ≠
complete-for-the-domain; completeness is still approached by use.

**Eight raw phenomena → six lenses + two dual-home phenomena.**
**Lossy-render** and **Over-claimed-verification** are *primarily*
verification-battery bindings (render-fidelity check; run-not-asserted
discipline) and impl-phase write-time self-check lenses — because the
failure is structural to the outcome and is caught by an executable
check. Each can ALSO be introduced at *design time* (a decision
committing to a softened render; a cycle recording an over-claimed
basis), so each ALSO appears as a cycle lens. The binding and the
lens compound — they do not duplicate: the lens catches the design
commitment, the battery catches the rendered/claimed artifact. The
other six (Bloat, Fragmentation, Leakage, Missed-dependents,
Unenforced-rule, Undefined-shorthand) are cycle lenses only.

The set is **closed** (eight named members; a lens is in it or not).

Lens-derivation note: each lens is anchored to an existing framework
concept rather than invented free — Bloat → Load-bearing test;
Leakage → framework-arbitrariness (contract 1); Unenforced-rule →
evidence-bearing-artifact rule (§3.1) + prescription discipline;
Missed-dependents → **target-dependents** coupling shape
(`glossary.md`) + Coupled-change forcing function (§3.2.2);
Over-claimed-verification → true-unit basis (§3.2). This keeps the
lens set from drifting into a second statement of framework rules
(itself a Fragmentation risk) — the lenses point at the framework
rule, they do not restate it.

## Persistence choice

One append-only markdown tracker per run under `.anneal-dev/runs/`,
with cycle-stamped standardized-pass + falsification-pass artifacts
and a per-run impl-plan file beside it; run resume by scanning for a
non-`PASSED` header Status. The run-state directory lives in the repo
the run was invoked from, while edits land across the repos in scope
— which the de-polluted core (`core.md` §6 "not assumed to share a
container with the work product") supports natively; it is no longer
recorded as a strain (see Scar tissue dissolved #2).

## Extensions / presentation decisions

- **Extensions:** enable mechanism declared (required). One real
  extension declared — `on-verify-PASSED · render-and-open-diff`
  (re-render affected plugin files and present the diff on a passing
  spec change). A dirty-tree `on-instance-start` gate was considered
  and **rejected** as duplicating the framework's integrity check,
  which already refuses-and-surfaces on a non-clean container before
  an in-place dispatch (`core.md` §4.2) — the Additive-reflex
  anti-pattern.
- **Presentation:** filled minimally (framework-default menu, no
  persona, no flourish) and kept rather than deleted, to record the
  deliberate non-decision so a later reader does not re-open it.
- **Lens-supplement:** mechanism declared (required); a plausible
  project-house supplement (citation/cross-reference-syntax lens)
  noted.

---

## Scar tissue dissolved

The validation that the de-pollution worked: per pass-1 workaround,
(a) what pass-1 did, (b) the cleaned-core change that dissolved it
(cited against current core text), (c) what pass-2 does instead.

### 1. Single-tree → multi-container (pass-1 Findings 1+2, the largest simplification)

- **(a) Pass-1 did:** the framework's impl-isolation (`core.md` §4.2)
  and run-state (`core.md` §6) assumed ONE git tree, so pass-1 bound
  cross-repo dispatch units as **sequential by default, one repo at a
  time** (`pass1/bindings.md` Multi-repo caveat) — forcing even
  causally-independent two-repo units (change a framework rule AND
  re-render it into its instance plugin) into sequential execution —
  and bound the worktree machinery directly (`git worktree add`, one
  HEAD snapshot, `cherry-pick` back). Run-state was pinned to an
  **anchor repo** as a separate workaround (`pass1/persistence.md`
  Multi-repo resume caveat). Both were recorded as the deepest strain
  and "the place most worth a framework-spec conversation."

- **(b) Cleaned-core change:** §4.2 now declares the work product
  **multi-container** — "A work product may span **multiple
  containers** (a repository, a document set, a dataset) that are
  independently isolable; each container the unit touches is checked
  independently against the **state marker** the instance binds"
  (core.md §4.2 Integrity check). The git-specific machinery is gone
  from the core — replaced by a declared **isolation slot**
  ("the instance binds the concrete mechanism — the **isolation
  slot** (`instantiation-guide.md` §2) — which carries copy creation,
  the identifier, escape-resistance, the **state marker** … the
  restore mechanism, and which non-tracked run-inputs are
  provisioned", core.md §4.2). §6 Run lifecycle now states run-state
  is "**not assumed to share a container with the work product**".
  Parallel-eligibility is per the unchanged disjointness rule
  (`modules.md` §3.3) over the unit's touched containers.

- **(c) Pass-2 does:** binds each repo as one container and fills the
  isolation slot cleanly (`pass2/bindings.md` Isolation slot). A
  multi-repo unit is **not** sequential because it spans repos — it
  is parallel-eligible iff its touched containers are search-
  established disjoint from every in-flight unit's, exactly as the
  framework specifies for any unit. The "sequential by default for
  cross-repo units" workaround is **dropped**. The integrity check
  runs per touched container; the state marker is each repo's HEAD.
  Run-state lives in the invocation repo with the work product
  spanning the scope repos — recorded as the framework's intended
  shape, **not** a strain; the anchor-repo workaround is **dropped**
  (`pass2/persistence.md`). Pass-1's Finding 4 (render-fidelity
  isolation aligning "by luck of structure") also dissolves: the
  isolation slot makes the per-container isolation a declared
  mechanism, not a structural coincidence the binding leans on.

### 2. Coupling shapes abstracted → paraphrase drift is first-class (pass-1 Finding 5)

- **(a) Pass-1 did:** the falsification coupling-shape closed set was
  code-shaped (`target-shape` / `target-uses` / `target-behavior`),
  so a corpus dependent like a **paraphrased restatement** or a
  **rendered plugin clause** had no native member; pass-1 forced it
  into `target-uses` + a `[CONDITIONAL]`-by-runtime-behavior escape,
  and named this "the most likely place a future corpus-evolution
  run finds the falsification pass's shape coverage awkward."

- **(b) Cleaned-core change:** the closed set is now general —
  **target-existence / target-dependents / target-behavior**
  (`glossary.md` Coupling shape; `core.md` §4.1.4; `modules.md`
  §3.4). `target-dependents` is defined as "**what depends on or
  uses the target**" and explicitly "Amendment decisions
  (`core.md` §3.2.2) always include this shape; the
  target-dependents candidate re-runs §3.2.2's reference enumeration
  as its search" (`glossary.md`). The instance binds the concrete
  evidence form.

- **(c) Pass-2 does:** binds **paraphrase drift as a first-class
  `target-dependents` case** — cross-references, paraphrased
  restatements, rendered clauses, closed-set members, and
  defined-term uses are all the corpus-evolution forms of
  target-dependents (`pass2/lens-set.md` Missed-dependents). The
  forced `target-uses`-plus-escape framing is **dropped**. A
  paraphrase a search can reach (shared distinctive tokens) is a
  plain target-dependents search; a paraphrase that resolves only at
  render-time (a search cannot exhibit it) goes `[CONDITIONAL]`, its
  basis the dependent exercised by render-fidelity / coherence. The
  glossary scopes §3.2.2's runtime-`[CONDITIONAL]` path to
  **target-behavior**; routing a render-resolved **target-dependents**
  case through it is a **binding extension**, not a verbatim-native
  fit — surfaced as residual strain **R4** below.

### 3. Abstracted mechanism vocabulary → instance binds the concrete forms

- **(a) Pass-1 did:** wrote against a core that still named `file:line`,
  `grep`, and `code`/`fixtures`, so the bindings restated those as
  if binding core literals (e.g. "a file:line read", "a wrap-tolerant
  grep"). Pass-1 Finding 6 also recorded "construct taken whole"'s
  "visible close" as a code-only syntactic token that becomes a
  judgment call for prose.

- **(b) Cleaned-core change:** the core now names framework concepts
  the instance binds — "**a located read of the source**" (not
  `file:line`; `file:line` survives only as a marked "for code"
  example, `core.md` §3.1 line 114), "**search**" / "re-runnable
  search" / "executable query" (not `grep`), "**the work product**"
  (not `code`/`fixtures`). The `for code:` markers in `modules.md`
  §3.4 (evidence-locator, pattern form) signal these as instance
  bindings.

- **(c) Pass-2 does:** binds the concrete corpus-evolution forms AS
  bindings of the abstracted core concepts — `search` → a
  **wrap-tolerant** prose text search (distinctive single tokens /
  newline-flattened input, because prose wraps); `a located read of
  the source` → a located read of the rule-text to its visible
  close, paired with one observable fact; `the work product's
  containers` → the corpus's repositories (`pass2/bindings.md`
  table). For pass-1 Finding 6, pass-2 gives the prose "visible
  close" a **mechanical** binding — the syntactic close of the
  rule-bearing unit (sentence terminal punctuation / paragraph
  blank-line / section next-heading / closed-set final member) —
  rather than leaving it a naked judgment (`pass2/bindings.md`
  construct-taken-whole row). The reference to wrap-tolerant search
  is a binding refinement, not a new slot.

### Net effect vs pass-1, per file

- `bindings.md` — **removed:** the "sequential by default for
  cross-repo units" workaround and the worktree-machinery binding
  framed as core literals; the `target-uses`+escape dependent
  framing; restatement of `file:line`/`grep` as core terms.
  **Added (declared-slot fill, not new content):** the isolation
  slot binding (copy / identifier / escape-resistance / state marker
  / restore / provisioning), the container↔repository row, the
  mechanical prose visible-close. Net: a cleaner binding of a
  declared slot replacing a workaround of an undeclared one.
- `persistence.md` — **removed:** the "Multi-repo resume caveat (a
  strain)" subsection (anchor-repo workaround). **Replaced with:** a
  "run state spans containers" subsection framing the same layout as
  the core's intended shape (§6), not a strain. Leaner.
- `lens-set.md` — **removed:** the `target-uses`+`[CONDITIONAL]`-escape
  framing in Missed-dependents; "verbatim grep" phrasings.
  **Replaced with:** target-dependents-anchored framing + native
  runtime-resolution path. Same lens count (8), tighter anchoring.
- `extensions.md` — **changed:** the rejected-gate rationale now
  cites the per-container integrity check (`core.md` §4.2) rather
  than "Main-tree integrity check"; rejection stands on its merits.
- `lens-supplement.md`, `presentation.md`, `README.md` — carried
  forward; `README.md` updated to name the isolation-slot binding and
  the scar-tissue-dissolved map. No scar tissue in these.

---

## Residual strains

Strains that STILL bend the fixed method after de-pollution. Surfaced
for the orchestrator; **not** fixed here (the instance never governs
its own foundation).

### R1 — §5.2(b) design-decision body-shape for prose rules (the known open question)

> **RESOLVED 2026-06-02** at the framework core (the "observable from outside"
> discriminator was abstracted to a coupling-based test); live status +
> resolution in `dev-notes/backlog/anneal-dev-framework-flowback.md` R1. Kept
> below as the derivation's original finding.

**Strains against:** `core.md` §5.2 Body shape (b)+(c) + the
`Contract surface` / `realization output` split (`glossary.md`).

The body-shape is a "what to build" shape: (b) for a new element, its
**contract surface** (what's observable from outside it); for an
amendment, the change as a delta; (c) **acceptance criteria** —
observable conditions for the decision to count as implemented. The
realization output (the element's internal content) is "**produced at
impl, not recorded in the design decision body**" (`core.md` §5.2).

For corpus-evolution this binds, but with a real strain: for a prose
**rule**, the contract surface / realization-output split is genuinely
blurry. A rule's "contract surface" — the AI behavior it forces, the
evidence-bearing artifact it requires, the closed set it names — is
largely *carried by its exact prose*. The realization output (the
rule's internal content) is "the exact wording," which the project's
own development process already treats as produced at impl, not design
(`development-process.md`: "Rule-corpus drafting is file-bound … Exact
rule wording … does NOT appear in conversation before the Edit"). So
the split *maps* — design fixes the rule's contract (what behavior it
forces, what artifact, against which source clause); impl produces the
exact sentences. The strain is the width of the grey band: for a code
element a function signature crisply separates contract from body; for
a rule, *how much* of the wording is contract (a softened "must"→
"should" changes the contract; a synonym substitution does not) is a
judgment the framework does not give a mechanical line for.

This means **(c) acceptance criteria** are the load-bearing part of
the body-shape for this domain (the observable conditions: "renders
with every 'must' preserved", "the closed set enumerates N members",
"the cross-reference resolves") — they carry what (b)'s
contract-surface delta would carry crisply in code. The binding leans
on (c) to compensate for (b)'s blur. **Surfaced as evidence, not
fixed:** whether the framework should give the contract-surface /
realization-output split a sharper instance-binding hook for domains
where the work product IS prose is the open framework question. Pass-1
did not examine this (it predates the question's framing); pass-2
records it as the one body-shape strain that de-pollution did not
touch.

### R2 — "the domain's executable verification" remains singular-framed (pass-1 Finding 3, partially residual)

**Strains against:** `core.md` §4.3 "**the** domain's executable
verification is run and its output shown"; `foundation.md` contract 3
("pytest …, debugger trace …" — single-artifact examples).

Corpus-evolution's verification is an irreducible **battery of four
heterogeneous checks**, one of which (render-fidelity) is itself a
fresh-context dispatch and one of which (operator approval) is a human
act, not a program. The binding fits — "executable" generalizes to
"dispatched/run, not asserted," and the multi-container abstraction
removed the *isolation* half of pass-1's concern (the battery's
render-fidelity check now inherits a *declared*-slot isolation, not a
structural coincidence). But the spec's singular noun and
single-artifact examples still lean on a narrower mental model than a
plural, partly-human, partly-dispatch-recursive battery supplies. Not
blocking; the binding refinement (`bindings.md` Verification battery)
carries it. Lower-severity than pass-1 ranked it, because the
isolation-alignment worry (pass-1 Finding 4) is gone.

### R3 — operator approval as a verify "check" is a human act inside an isolated context

> **RESOLVED 2026-06-02 — the binding was the issue, not the framework.** Operator
> approval is not a verify check: verify runs isolated from the operator (`core.md`
> §4.3), so diff-approval is the §1(a) presentation / commit gate downstream of
> [PASSED]. pass-2's battery is corrected to three dispatched checks (`bindings.md`);
> operator approval re-placed at the §1(a) gate. Live status in
> `dev-notes/backlog/archive/anneal-dev-framework-flowback.md` R3. Kept below as the
> original residual-strain framing.

**Strains against:** `core.md` §4.3 (verify runs **isolated** from
the working context; the operator-expected-action bound, §1).

The verification battery's check (d) is **operator approval of the
diff** — but verify runs in an isolated context, and the operator's
protocol-expected actions are bounded to menu selection + free-form
interjection (`core.md` §1 Operator-expected action bound). Operator
approval of a diff at verify is closer to the implement→verify and
[READY] menu moments than to a check the isolated verify context
*runs*. The binding treats it as "the consumer-observable terminal …
the domain's analogue of a passing test run" (`bindings.md`), which
fits the *spirit* (a passing external signal), but the framework does
not cleanly model a verify-internal check that is a human menu act.
Minor; surfaced because it is the one battery check that is neither
dispatched nor program-run, and the framework's verify-isolation
language does not name it. (Distinct from R2: R2 is about plurality;
R3 is about one check being human.)

### R4 — a render-resolved target-dependents dependent has no native runtime-resolution path (surfaced by the verify pass)

> **RESOLVED 2026-06-02 — the title's premise was wrong.** Grounding `core.md`
> §3.2.2 showed it already covers this: "a preserved-behavior claim … the
> behavior resolves at runtime through a dependent the reference-search does not
> surface … → [CONDITIONAL], basis exercised by executable verification." A
> render-resolved paraphrase is exactly that, so it routes the **native**
> target-behavior path — there was no missing mechanism and no "binding
> extension" (this section's framing, and the C2 framing above, were both misled
> by the glossary presenting dependents=search / behavior=runtime as a clean
> split). Fix: a glossary bridge sentence (`glossary.md` Coupling shape).
> Live status in `dev-notes/backlog/anneal-dev-framework-flowback.md` R4. Kept
> below as the derivation's original (over-stated) finding.

**Strains against:** `glossary.md` Coupling shape — the runtime-
`[CONDITIONAL]` escape is scoped to **target-behavior**;
**target-dependents** is defined as search-dischargeable ("re-runs
§3.2.2's reference enumeration as its search") — + `core.md` §3.2.2 /
§4.1.4 falsification.

A corpus dependent that resolves only at render-time — a paraphrase a
rendered plugin carries that a corpus search cannot exhibit — is a
**target-dependents** dependent, yet search cannot discharge it. The
framework gives the runtime-`[CONDITIONAL]` escape to
**target-behavior** only, so anneal-dev routes the search-unreachable
paraphrase dependent through §3.2.2's runtime path as a **binding
extension**: sound in substance (the dependent is exercised by the
render-fidelity / coherence battery, exactly as a runtime claim's
basis is exercised by executable verification), but it extends a
behavior-scoped mechanism to a dependents case the framework does not
natively cover. The de-pollution abstracted the coupling-shape *set*
(Finding 5, dissolved) but did not give **target-dependents** a
runtime-resolution path; for a domain whose dependents include
render-resolved paraphrase, that is the missing piece. The pass-2
draft first asserted this as a native fit; the separate-context verify
caught the over-claim, and it is corrected here and recorded as the
fourth residual strain.

---

## Naming verdict

**Ratify `anneal-dev` / `corpus-evolution`.** The cleaned core does
not change the framing:

- **`corpus-evolution`** names the domain accurately — evolving a
  rule-corpus (the multi-repo body of spec-and-skill files defining a
  methodology and its tools). The de-pollution did not narrow or
  widen this domain; it removed code-shaped *assumptions* the domain
  had to bend around, which makes the binding cleaner but leaves the
  domain identity unchanged.
- **`anneal-dev`** names the instance as the tool that evolves the
  anneal triad itself (framework spec, skill-craft canonical,
  instance renders). Plain working name, no persona (`presentation.md`).
  The self-referential character (the methodology evolving its own
  methodology) is a property of the *work product*, not a reason to
  rename — the framework's isolation discipline is what makes the
  self-reference safe, and the name need not encode it.

No cleaned-core change touches the domain boundary or the instance's
identity. Naming stands.

---

## Framework-layer questions surfaced (for the orchestrator — not acted on)

1. **R1 — §5.2(b) for prose work products.** Should the
   contract-surface / realization-output split (`core.md` §5.2,
   `glossary.md`) carry an instance-binding hook for domains where
   the work product IS prose, where exact wording straddles contract
   and realization? This is the known open framework question the
   derivation was asked to examine; pass-2's evidence is R1 above.
2. **R2 — singular "executable verification".** Whether `core.md`
   §4.3's singular noun + single-artifact examples (`foundation.md`
   contract 3) should acknowledge a multi-check battery shape, or
   whether the existing "dispatched/run, not asserted" generalization
   is deemed sufficient framing.
3. **R3 — human check inside isolated verify.** Whether the framework
   should model a verify-internal check that is an operator act
   (approval) rather than a dispatched/program-run check, given
   verify's isolation and the §1 operator-expected-action bound.
4. **R4 — runtime-resolution path for target-dependents.** Whether
   `core.md` §3.2.2 + the `glossary.md` coupling-shape entry should
   give **target-dependents** a runtime-`[CONDITIONAL]` resolution
   path (basis: the dependent exercised by executable verification)
   for a dependent a search cannot exhibit — the render-resolved
   paraphrase case — paralleling the existing **target-behavior**
   path. anneal-dev currently binds this as an extension (R4 above).
