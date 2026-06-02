# Contract-1 de-pollution cluster — design capture

Durable design artifact for the **next framework effort**: removing
the three coding-domain leaks from the anneal-framework core so the
spec is domain-independent at the *mechanism* level, not just the
architecture level. Written in-context (2026-06-01) so a fresh session
inherits the reasoning, not a thin summary. Found via a cross-session
analysis + confirmed by the first whole-corpus coherence-audit
(handoff `aba2b1b2b9b2c515b`, Lens 8). Not spec.

Resume: **Cycles a + b DONE** (2026-06-01, commits `3a2245b` + `8bf4d47`).
**Cycle c reframed by a bildhauer pass (2026-06-02)** — see Sequencing item 3:
it splits into a **safe de-code-ification sweep** (do now, a/b-style) and a
**parked completeness call** (closed-vs-open predicate enum — settle against a
built non-code instance, not now). A code-vocab inventory also surfaced two
**tail leaks the 3-leak framing missed** — T1 `file:line` citation form
(pervasive, safe) and T2 `code`/`fixtures` as work-product. Next action
(**locked order, 2026-06-02**): (1) **clippy-sync the a+b vocab — DONE**
(clippy v0.9.94, `56414d6`; archived [[clippy-isolation-render-release]]; spun
out [[daneel-cycle-b-sync]]); **head is now (2) Cycle c-safe** (item 3 below;
enum stays closed); (3) a **focused c-only clippy-sync**.

## The framing that matters (don't lose this)

The framework's **architecture is already domain-independent**: the two
invariants (grounded claims + coherent picture), the three phases, the
two-track tracker, the status-state machine, the basis rule,
inspection-via-lens, and the design↔impl split itself. And it already
**knows how to abstract** — three mechanisms are cleanly pushed into
**instance slots**:

- **work product** — glossary: "an instance binds it — code, for Clippy"
- **executable verification** — "the domain's executable verification" (not "pytest")
- **lens set** — instance-supplied (`modules.md` §2.2)

The bug is **non-uniform application of its own discipline**: three
*other* mechanism specs were written by reaching for the software
instance's concrete shapes instead of abstracting them + delegating to
an instance slot the way work-product / lens-set / executable-verification
already are. It's not that the framework *can't* abstract these — it
*didn't*, uniformly.

**The fix pattern (same for all three):** state the mechanism
domain-generally in core; push the code concretion into the instance
slot (clippy's `bindings.md` / `lens-set.md` — which for some of these
already carries the concretion). This is a **spec gap, not a render
gap** — clippy faithfully inherits the code shapes; the framework baked
them in (practice 1 → fix at source). The `foundation.md` contract-1
test — "would this rule still apply rendered into an unrelated domain
(legal / research / marketing)?" — **fails** on all three.

**Empirical tell (the strongest evidence):** another session ran anneal
on a *writing* task and had to **drop / reinterpret exactly these
three** — dropped §4.2's git isolation, reinterpreted §4.1.4's
falsification ("re-open each cited fact and try to falsify it"),
re-read §5.2(b) "signature/types" as "the section's claim-set +
acceptance criteria." A clean writing *instance* would **render** them
(the way clippy renders the coding one) if they were abstract. The
reinterpretation *was* the leak surfacing.

---

## Leak 1 — §5.2(b) design-decision "shape" (core.md:832-848)

**Current (code vocab as the *primary* definition, not illustration):**
- (a) target — "the named element being committed (**file, function,
  type**, behavior)"
- (b) shape — "for **new code**: the contract surface (**signature,
  types, error patterns**) in inline backticks; for amendment to
  existing **code**: the change as a delta"
- brevity — "Multi-statement **function bodies, validator internals,
  and migration SQL bodies** are implementation outputs…"

**Why it leaks:** a document or campaign work product has no signature /
function body / migration SQL. The definition reaches for code shapes.

**Abstract target form** (from the other session — preserve verbatim,
it's good):
> design carries the **contract surface — what's observable from
> outside the unit — not the realization output.**
> - code (clippy): signature / types / error patterns **vs** the function body
> - document: the claims a section asserts + their grounded bases + acceptance criteria **vs** the prose
> - campaign: message + audience + claim-set + evidence **vs** the copy

And the de-code-ified design↔impl sentence:
> impl realizes the design's committed contract into the work product,
> re-opening the cited sources to render them; it does not re-open the
> decision or discover new grounding.

**Instance delegation:** "contract surface" becomes a per-domain
binding (clippy: signature/types/error-patterns), parallel to the
existing work-product binding. (a) target = "an element of the work
product" (instance binds: file/function/type for code; section/claim
for a document). Brevity examples → "the realization output (the unit's
internal content) belongs at impl, not the design body"; concrete
examples instance-delegated or dropped.

**Edge cases / design questions:**
- This is the most *foundational* leak — every domain's design
  decisions use this shape. Get the "contract surface vs realization
  output" abstraction exactly right; it's the spine.
- "amendment: the change as a delta against current state" is already
  fairly general — keep.
- (c) acceptance criteria, (d) side-effects/failure-modes, (e) basis
  are already domain-general — leak is concentrated in (a) + (b) + the
  brevity examples.

**Interactions:** none hard; touches every design decision so it's the
cleanest standalone abstraction.

---

## Leak 2 — §4.2 implement isolation (core.md ~527-573)

**Current (VCS/filesystem mechanism):** "per-unit **git worktree**",
"unique **branch**", "strip remotes (`git remote -v`)", "pre/post
**`git rev-parse HEAD`** verification", "**cherry-pick** integration",
"`git worktree add`" (provisioning), "**venv**" (bootstrap). Plus the
Cycle-G additions: Main-tree integrity check (`git status --porcelain`,
`git reset --hard`) + spawn-fallback. = coherence-audit **F1** (Lens 8).

**Why it leaks:** git/VCS/filesystem-specific; meaningless for a
non-code work product. The *mechanism* (isolate concurrent units +
integrate after an integrity check) is general; the *tooling* is coding.

**Abstract target form:** core states the **principle + guarantees**,
not the tooling:
- parallel-eligible units are **isolated** — each works on a **separate
  copy** of the operator's work product so concurrent edits don't clash;
- after a unit completes, the orchestrator **integrates** its changes
  into the operator's main work product after an **integrity check**
  (the unit changed only its scope; the main wasn't contaminated);
- sequential/single units may work **in place** (on the main work
  product) under an in-place integrity check (clean precondition +
  changed-by-exactly-this-unit detect + restore-on-mismatch);
- spawn-failure → working-context fallback, surfaced.
- the instance binds the **concrete** isolation + integration mechanism.

**Instance delegation:** clippy's `bindings.md` §Dispatch isolation
**already carries** the git slot values (worktree path, branch,
creation/strip/cherry-pick/HEAD commands). So most of the work is
**removing** the git vocab from core.md (abstract it) + verifying
clippy's binding carries everything core drops. The folded audit **F2**
(glossary entries for "Main-tree integrity check" + "spawn-fallback")
lands here — **define them with the abstract vocab**, not git-flavored
(that's why F2 was folded: defining them git-flavored now then
re-abstracting = churn, and it'd pollute the currently-clean glossary).

**Edge cases / design questions:**
- "integration" (cherry-pick) → "merge the unit's changes into the
  main work product"; "integrity check" (HEAD + clean tree) →
  "verify the unit changed only its scope + main uncontaminated."
- **Open:** does the framework even specify isolation at the *mechanism*
  level, or just the *principle* (no cross-unit clash, no main
  contamination, clean integration) + delegate the whole mechanism?
  Leaner = state guarantees, delegate mechanism entirely. Decide at the
  design surface.
- Is "separate copy + merge" meaningful for non-code domains? Yes — any
  work product can be copied + merged (separate drafts, separate
  campaign-artifact copies). The VCS is just the coding *binding* of
  copy+merge. So the abstraction holds.
- **Multi-tree work product (from anneal-dev pass-1):** the corpus is
  multi-repo, so the abstraction must not assume the run's work product
  lives in ONE tree — isolation, integration-integrity, and §6 run-state
  all currently inherit a single-tree assumption. See the Pass-1
  corroboration section below.

**Interactions:** freshest leak (Cycle G just rebuilt this whole
section — dispatch decomposition, Main-tree integrity, spawn-fallback).
Context is warm. Render impact: clippy `implement.md` Isolation +
`bindings.md` §Dispatch isolation **keep** the git specifics (correct
instance binding); core de-git-ifies; re-render implement.md from
abstracted core.

---

## Leak 3 — §4.1.4 + modules.md §3.4 + glossary falsification (HARDEST)

**Current (assumes a code target + grep semantics; CLOSED ENUM):**
- **Coupling shapes** (glossary, closed set of 3): target-shape /
  target-uses / target-behavior — assume the target is a **code symbol**
  with a **signature, callers, and runtime behavior**.
- **Falsification predicates** (closed set of 3): `any-match` /
  `any-outside-scope:<scope>` / `expected-match:<pattern>` — defined in
  **grep-result-line semantics**.
- Both are **closed enums** — can't be reinterpreted per-domain without
  amending the spec (unlike work-product, which an instance just binds).

**Why it leaks:** a document's "decision" has no callers / runtime
behavior; the predicates are search-result semantics. And the
closed-enum-ness means a non-code instance *can't* bind around it — it
has to amend the framework. That's the contract-1 failure with teeth.

**Abstract target form:**
- Coupling shapes → domain-general categories of how a claim couples to
  the rest of the work: **target-existence** (the target exists with
  its claimed surface), **target-dependents** (what depends on / uses
  it), **target-behavior** (its behavior/effect under inputs). The
  3-category *structure* may largely survive; the **code glosses**
  ("signature / callers / runtime-behavior") get abstracted +
  instance-bound.
- Falsification predicates → the predicate computes holds-or-falsified
  from the candidate's **evidence** (a search / read / exercise result).
  The predicate *types* are general — "any positive result falsifies",
  "any result outside the named scope falsifies", "missing expected
  property falsifies." The instance binds the concrete **evidence form**
  (clippy: grep result lines). Keep the enum closed but **domain-general
  at the type level**, concrete-search instance-bound.

**Edge cases / design questions:**
- This is the **most intricate** mechanism (coupling shapes feed the
  convergence-cycle falsification pass + the candidate-set coverage
  check + the predicate-shape-coherence rules). Abstract without
  breaking the machinery — go slow, lean on a design surface + heavy
  step-4.
- **Open:** can the closed enum stay closed once abstracted, or does
  domain-generality require an open/extensible predicate set? Lean:
  closed-but-abstract (predicate *types* general; evidence
  instance-bound) — but verify against a non-grep instance mentally.
- The Cycle-3 work already started here: glossary `target-behavior`
  carries the runtime-resolved [CONDITIONAL] cross-ref to §3.2.2. The
  folded audit **F3** (the [CONDITIONAL]→[AUTO-ACCEPTED]→verify handoff
  is implicit; falsification covers [VERIFIED] only) lands here — state
  the handoff explicitly when this section is rewritten.

**Interactions:** Cycle 3 (behavioral-coupling) touched `target-behavior`
+ the executable-basis routing. Render impact: clippy `lens-set.md` /
`lenses.md` + the falsification render in `investigate-design.md`.

---

## Pass-1 (anneal-dev) corroboration — 2026-06-01

The first forward-derivation of the **anneal-dev** instance (anneal bound
to corpus-evolution; `dev-notes/derivation-pass1/`) independently hit these
leaks from a fresh angle — strong corroboration, plus one expansion, one
test-case, and one downgrade. anneal-dev is now a **second non-code
validation instance** alongside the (parked) planner, partly filling the
validation gap below: its bindings are the test of whether each abstract
form renders cleanly into a non-code domain.

- **Leak 2 (§4.2) — EXPANDED: drop the single-*tree* assumption, not just
  the git tooling.** The corpus is **multi-repo**; a run's work product can
  span trees (change a framework rule AND re-render it into its instance
  plugin = two repos). The current abstract form ("each unit works on a
  separate copy of *the* work product") still implicitly assumes ONE
  work-product tree, and run-state (**§6** run lifecycle) + isolation +
  integration-integrity all inherit it. Cycle a's abstraction must make "the
  work product" potentially multi-tree: isolation, integrity, and run-state
  must not assume work product and run-state share one tree. anneal-dev had
  to bind cross-repo units sequential-by-default + anchor-repo run-state as a
  workaround — scar tissue Cycle a should dissolve. **Pulls §6 into Leak 2.**
- **Leak 3 (§4.1.4) — CORROBORATED + concrete test case.** A corpus
  dependent the closed code-shaped coupling enum can't express: a
  **paraphrased restatement elsewhere** / a **rendered (paraphrased) plugin
  clause** — invisible to a verbatim grep, forced into `target-uses` +
  [CONDITIONAL]. Exactly the closed-enum-with-teeth failure Leak 3 names;
  validate that the proposed **target-dependents** abstraction covers
  "paraphrase drift" as a first-class dependent shape.
- **§4.3 executable-verification — DOWNGRADED to an examples nit (not a new
  leak).** Pass-1 first flagged §4.3's singular noun + program-shaped
  examples (pytest/build/debugger) as straining against corpus-evolution's
  4-check, partly-human, partly-recursive verification *battery*. But this
  file already counts executable-verification among the **already-abstracted**
  mechanisms ("the domain's executable verification", not "pytest"). The
  abstraction holds; only the *illustrative examples* lean program-shaped —
  light touch when a nearby cycle is open, not its own leak.
- **§3.2 "visible close" (minor) + render-fidelity isolation-boundary
  (near-miss)** — observations only; anneal-dev bound both. Logged so they're
  not re-discovered, not scoped as cycles.

## Sequencing

Recommended order **a → b → c** (clearest → hardest):

1. **Cycle a — Leak 2 (§4.2 isolation). DONE 2026-06-01 (commit `3a2245b`).**
   De-code-ified §4.2 to guarantees + delegated git to a declared instance
   **isolation slot**; consolidated the **Integrity check** (two forms, in-place
   restores / isolated halts-without-restore); made the work product
   **multi-container** (pulled the single-tree assumption from §4.2/§6);
   absorbed F1 + F2 (glossary entries Integrity check + Spawn-fallback).
   **Folded in a 4th leak:** dropped instance-name illustrations (Clippy/Daneel)
   from the spec proper. Clippy spec conformed; plugin re-render + release
   deferred → [[clippy-isolation-render-release]]. Surfaced →
   [[instance-template-slot-scaffolding]].
2. **Cycle b — Leak 1 (§5.2b design-shape). DONE 2026-06-01 (commit `8bf4d47`).**
   §5.2(b) now records the **contract surface** (observable from outside the
   element) vs the **realization output** (internal content); kept "behavior" as a
   target; canonical glossary **Contract surface** entry. **Define+derive — NO new
   binding term** (avoided a cross-instance ripple). Clippy plugin re-render (§5.2
   body-shape, verbatim-stale `tracker.md`) folds into
   [[clippy-isolation-render-release]]. Review surfaced the term recurs
   code-flavored beyond §5.2b → Cycle c.
3. **Cycle c — Leak 3 (§4.1.4 falsification). REFRAMED by a bildhauer pass
   (2026-06-02)** into two parts:
   - **(c-safe) de-code-ification sweep — do now, a/b-style, low-risk.** Abstract
     the coupling-shape *glosses* (signature/type/decorator → contract surface;
     call-sites/imports → dependents; runtime behavior) and the predicate
     *grep-semantics* (`result line`/`glob`/`directory`/`regex:` → "the
     candidate's evidence"); state **F3** (the [CONDITIONAL]/[AUTO-ACCEPTED]→verify
     handoff — falsification covers [VERIFIED] only); reconcile §4.3
     `consumer-observable surface` with `contract surface`; §5.1 `file/symbol`.
     **Keep the predicate/coupling enums CLOSED** (current behavior preserved).
   - **(c-parked) the completeness call — DEFER to a built non-code instance.**
     Whether the 3 predicate types are domain-*complete* can't be settled without
     a non-code instance exercising falsification (planner / anneal-dev). Do NOT
     lock completeness; do NOT build a speculative open enum. When c-safe ships
     with the enum closed, register a `validation-watch` entry to watch the first
     non-code falsification. **Retracted overclaim:** "3 types are logically
     complete" — unverifiable; honest frame is "current-best, amend if a real
     domain proves a 4th needed; that amendment is the accepted trade vs a
     premature open enum." If 3 is wrong, we recreate the contract-1 failure one
     level up — known and accepted.
   - **Watch during c-safe: paraphrase-drift dependents** — a paraphrased
     restatement invisible to verbatim grep (e.g. a rendered plugin clause) may
     have NO existing evidence-binding — the one place "no new binding" could
     break. Verify when abstracting `target-dependents`.

**Tail leaks (code-vocab inventory, 2026-06-02 — the 3-leak framing undercounted):**
- **T1 — `file:line` citation form (~10+ sites: §3.2 / §4.1 / §5.1 / modules).**
  Core hardcodes `file:line` for "a located citation" (a document cites
  `section:¶`). SAFE: "a located read of the source" is already a bound term;
  mechanical sweep → "a located citation." Not speculative.
- **T2 — `code`/`fixtures` as work-product (core:475, 817).** §4.2/§5.1 say
  "editing code" / "code or fixtures" for "the work product." Two sites, mechanical.
- Benign (verified, leave): `runtime` (general), `result line` in the §4.1.2
  record sense, generic `file` persistence locations, "presented as code" (markdown).

Each is a full framework cycle: practice-9 design surface (the
domain-general vocabulary IS the design work) → skill-craft gate →
abstract core + delegate to instance slot → re-render clippy → step-4
(framework-spec self-review + render fidelity + practice-4 contract
audit — **wrap-tolerant** per the new practice-4 rule). A non-code
instance derivation (the planner, when built) is the real validation
that the abstraction worked.

## Risks

- **Over-abstraction:** stripping so much that the mechanism stops being
  load-bearing (practice 7 foundation-work full-discipline). The
  guardrail: each abstract form must still let clippy *render* the exact
  current behavior. If clippy can't render it back, the abstraction lost
  content.
- **Closed-enum (leak 3):** the genuinely-hard one. **Bildhauer resolution
  (2026-06-02):** keep closed-but-abstract as the default — opening the enum is
  the *premature* move (extensibility for domains that don't exist). Don't claim
  completeness; accept that if a real non-code domain needs a 4th predicate type,
  that's a framework amendment (the contract-1 failure recreated one level up) —
  the correct trade. Settle empirically against the first non-code instance, not
  by assertion now.
- **Validation gap:** without a second (non-code) instance, "is it
  *really* domain-general now?" stays partly unproven — the planner
  build (parked, pre-build) is the test. Note this in each cycle's
  validation-watch.
