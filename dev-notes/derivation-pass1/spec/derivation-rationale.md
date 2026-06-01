# anneal-dev — Derivation rationale (pass 1)

Forward derivation of the anneal-dev instance from the
anneal-framework spec + the corpus-evolution domain facts.
Clean-room: derived forward from the framework, not reverse-
engineered from any existing solution. This file carries the §1
verdict, the lens-set path, the judgment calls, and the
**contract-1 findings** — where the framework's fixed method or
closed slot-set strained against the corpus-evolution domain.

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
  and notably stronger than the §1 worst case (a domain with no
  executable verification): the render-fidelity and coherence checks
  are genuinely executable (a separate context re-derives them), not
  merely static self-inspection.
- **Recurring blind-spots.** The domain has a body of recurring
  mistakes an expert watches for — the eight-phenomenon corpus the
  derivation was given. PASS, and it supports a **Path 1** lens set
  (incident-grounded), not the Path-2 bootstrap a fresh domain needs.

**Strains named** (each fits, but the framework is written assuming
a shape the domain bends):

1. **Multi-repo problem space.** The framework's scope, dispatch
   isolation (worktree), and run-state persistence are written
   assuming the run's work product and its state share **one git
   tree**. The corpus is multi-repo. The domain still fits — scope's
   mechanical search (grep) works across repos, and verification is
   well-defined — but the worktree-isolation and resume mechanics
   strain (detailed in the contract-1 findings below). This is the
   single largest strain.

2. **Scope's mechanical basis is text, not symbol.** §3 warns that a
   domain where "scope" has no mechanical search needs care. Scope
   here HAS a mechanical search (grep), so it fits — but the search
   is over **prose**, which wraps across lines, so a multi-word
   pattern can split mid-match. The binding handles this
   (wrap-tolerant: distinctive single tokens / newline-flattened
   input), and it is a genuine domain binding, not a framework gap.
   Recorded so the strain is visible.

3. **The work product is the methodology the tool implements.** This
   is a recursion strain, not a fit strain: anneal-dev's verify
   battery (render-fidelity, coherence, skill-quality) is itself
   rule-corpus content that a future anneal-dev run could edit. The
   framework's separate-context / isolation discipline is what keeps
   this safe (the checker is not the author), so the recursion does
   not break fit — but it is the reason the verification battery
   leans hard on the framework's existing isolation, rather than
   inventing instance-specific isolation.

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
persistence mechanism (`persistence.md`); plus the
required-mechanism slots (extensions enable mechanism, lens-
supplement mechanism) and the optional presentation slot.

The closed slot-set was respected: no new render-consumed slot was
invented. The multi-repo handling, the verification battery, and
the wrap-tolerant search were all placed as **binding refinements**
(extending existing rows / sections of the bindings), not as new
slots — per the §5 binding-refinement-vs-extension test.

---

## §4 — Lens-set path and shape

**Path 1 — incident-grounded.** The given recurring-mistakes corpus
IS the domain's incident history, so the set is derived from real
recurring failures, not blank-slate hypotheses. (Contrast Clippy's
own set, also Path-1-shaped, distilled from coding incidents.) Path 1
≠ complete-for-the-domain; completeness is still approached by use.

**Eight raw phenomena → six lenses + two dual-home phenomena.** The
judgment call (recorded in `lens-set.md`): **Lossy-rendering** and
**Over-claimed-verification** are *primarily* verification-battery
bindings (render-fidelity check; run-not-asserted discipline) and
impl-phase write-time self-check lenses — because the failure is
structural to the outcome and is caught by an executable check. But
each can also be introduced at *design time* (a decision that
commits to a softened render; a cycle recording an over-claimed
basis), so each ALSO appears as a cycle lens. The binding and the
lens compound — they do not duplicate: the lens catches the design
commitment, the battery catches the rendered/claimed artifact. The
other six (Bloat, Fragmentation, Leakage, Missed-dependents,
Unenforced-rule, Undefined-shorthand) are cycle lenses only.

The set is **closed** (eight named members; a lens is in it or not).

Lens-derivation note: each lens was anchored to an existing
framework concept rather than invented free — Bloat → Load-bearing
test; Leakage → framework-arbitrariness (contract 1); Unenforced-rule
→ evidence-bearing-artifact rule (§3.1) + prescription discipline;
Missed-dependents → Coupled-change forcing function (§3.2.2);
Over-claimed-verification → true-unit basis (§3.2). This keeps the
lens set from drifting into a second statement of framework rules
(itself a Fragmentation risk) — the lenses point at the framework
rule, they do not restate it.

## Persistence choice

One append-only markdown tracker per run under `.anneal-dev/runs/`,
with cycle-stamped standardized-pass + falsification-pass artifacts
and a per-run impl-plan file beside it; run resume by scanning for a
non-`PASSED` header Status. Mirrors Clippy's file mechanism (the
worked example) bound to the `anneal-dev` namespace. The one
deviation forced by the domain: the run-state lives in a single
**anchor repo** while edits may land across repos — recorded as a
strain (below).

## Extensions / presentation decisions

- **Extensions:** enable mechanism declared (required). One real
  extension declared — `on-verify-PASSED · render-and-open-diff`
  (re-render affected plugin files and present the diff on a passing
  spec change) — because the domain has a genuine post-PASSED
  bookend (the spec is verified, then rendered). A dirty-tree
  `on-instance-start` gate was considered and **rejected** as
  duplicating the framework's existing Main-tree integrity check
  (Additive-reflex anti-pattern).
- **Presentation:** filled minimally (framework-default menu, no
  persona, no flourish) and kept rather than deleted, to record the
  deliberate non-decision so a later reader does not re-open it.
- **Lens-supplement:** mechanism declared (required); a plausible
  project-house supplement (citation/cross-reference-syntax lens)
  noted.

---

## CONTRACT-1 FINDINGS — where the framework strained

These are the real point of the exercise: places where anneal's
FIXED method or CLOSED slot-set did not cleanly fit corpus-evolution.
Each names the specific spec element it strained against.

### Finding 1 — Single-tree assumption in impl-phase isolation (strongest)
**Strains against:** `core.md` §4.2 Isolation mechanism (worktree),
Main-tree integrity check, Provisioning; and `modules.md` §3.3
parallel-eligibility disjointness.
The worktree-isolation machinery is written for **one git tree**:
`git worktree add` off the operator's main HEAD, one HEAD snapshot,
one cherry-pick back. The corpus is **multi-repo**. A dispatch unit
whose edits span more than one repo has no single worktree to be
isolated in, and its disjointness cannot be established within one
tree. anneal-dev had to bind such units as **sequential by default,
one repo at a time** — which means a genuinely common
corpus-evolution unit (change a framework rule AND re-render it into
its instance plugin — two repos) is **forced sequential** even when
the two edits are causally independent. The framework offers no slot
for "multi-tree parallel-eligible unit." This is an instance binding
that works, but it leaves parallelism on the table the framework's
model would otherwise allow, and it is the clearest case of the
fixed method assuming a shape (single tree) the domain does not have.

### Finding 2 — Run-state lives in one tree; work product spans trees
**Strains against:** `core.md` §6 Run lifecycle ("A run's state …
persists across interruptions; a run … resumes from that state");
`instantiation-guide.md` §5 filesystem-layout (one repo's
`.gitignore`).
Framework persistence assumes the run's state and its work product
share a tree. Here `.anneal-dev/runs/` can only live in one repo
(the anchor), while edits land across repos. Resume re-derives
cross-repo edit state from the tracker's commit references rather
than from scanning each repo — a workable binding, but the framework
gives no concept of a **run that spans repos**, so the anchor-repo
choice is an instance invention filling a gap the slot-set does not
name.

### Finding 3 — "executable verification" is a multi-check battery, not one runnable thing
**Strains against:** `core.md` §4.3 "Executing the verification —
the domain's executable verification is run and its output shown";
the singular framing of "the domain's executable verification"
(also `foundation.md` contract 3: "what 'executable verification'
means in the domain (pytest …, debugger trace …)").
The framework's examples (pytest, build, linter, debugger trace) are
**single runnable artifacts**. Corpus-evolution's verification is an
irreducible **battery of four heterogeneous checks**, one of which
(render-fidelity) is *itself* a fresh-context dispatch and another
of which (operator approval) is a human act, not a program. The
binding fits — "executable" generalizes cleanly to "dispatched/run,
not asserted" — but the spec's singular noun ("the domain's
executable verification") and its program-shaped examples strain
against a domain where verification is a plural, partly-human,
partly-dispatch-recursive battery. Not a blocking gap; a place where
the spec's framing leans on a narrower mental model than the domain
supplies.

### Finding 4 — Render-fidelity wants a verify SUB-check with its own isolated dispatch, and the framework only models verify-level isolation
**Strains against:** `core.md` §4.3 verify isolation (verify as a
whole is isolated) vs. the domain's need for render-fidelity to be
checked in a context that did not produce *the render* specifically.
Verify already runs isolated, so render-fidelity inherits isolation
for free — this is why fit holds. But the precise thing that must be
isolated in this domain is "the context that wrote the paraphrase,"
which is the **impl/render** context, not the verify context; the
framework models isolation at the verify boundary, and the domain's
fidelity check happens to align with it. It aligned by luck of
structure, not because the framework has a "render-vs-renderer
isolation" concept. If a future domain needed the fidelity check at
a different boundary, the closed model would not have a slot for it.
Recorded as a near-miss: the fit is real but rests on an alignment
the framework does not name.

### Finding 5 — Coupling shapes (closed set) are code-shaped; corpus dependents include "paraphrased restatement," which no shape cleanly covers
**Strains against:** `glossary.md` Coupling shape (closed set:
target-shape / target-uses / target-behavior) + `core.md` §4.1.4 /
`modules.md` §3.4 falsification candidate-set shape coverage.
The convergence-cycle falsification pass requires a candidate per
**coupling shape** the basis depends on, from a **closed set of
three** defined in code terms (signature/contract; call-sites/
imports; runtime behavior). In corpus-evolution, a rule's dependents
include a **paraphrased restatement elsewhere** and a **rendered
(paraphrased) plugin clause** — a dependent that a verbatim grep
cannot exhibit and that does not map cleanly onto target-shape /
target-uses / target-behavior. The closest fit is `target-uses`
(treat the restatement/render as a "use" of the rule) plus the
[CONDITIONAL]-by-runtime-behavior escape (`core.md` §3.2.2) for the
paraphrase the read cannot exhibit — which is the binding I took
(see `lens-set.md` Missed-dependents and `bindings.md` §3.2.2
handling). But the closed coupling-shape set is genuinely
code-flavored: "paraphrase drift" is a first-class corpus dependency
shape with no native member, forced into `target-uses` + a
[CONDITIONAL] escape. This is the most likely place a future
corpus-evolution run finds the falsification pass's shape coverage
awkward.

### Finding 6 (minor) — "construct taken whole" assumes a syntactic close; a prose rule's "whole" is judgment
**Strains against:** `core.md` §3.2 true-unit basis ("a claim about
a *construct* … has the whole construct as its unit; its basis is a
read to the construct's visible close").
"Visible close" is crisp for code (a function's closing brace, a
statement's end). For a prose rule, the "whole construct" is the
clause/paragraph/section that carries the rule — and where a rule's
*whole* ends (one sentence? the paragraph? the section + its
cross-references?) is a judgment call, not a syntactic token. The
binding handles it ("read to its visible close: the complete clause
… or — for an amendment — the rule plus the cross-references that
bind to it"), but the framework's "visible close" language assumes a
syntactic boundary the domain does not always have. Minor: it adds
judgment where code had a token, but does not break the rule.

---

## Summary of strains, ranked by how much they bent the framework
1. **Single-tree assumption** (Findings 1 + 2) — the framework's
   impl-isolation and run-state model assume one git tree; the
   multi-repo corpus is the deepest strain and the place most worth
   a framework-spec conversation (is there a "multi-tree run"
   concept the closed slot-set should recognize?).
2. **Coupling-shape closed set is code-shaped** (Finding 5) —
   "paraphrase drift" has no native shape; forced into target-uses +
   [CONDITIONAL].
3. **Singular "executable verification"** (Finding 3) — generalizes
   fine to "dispatched/run, not asserted," but the spec's framing and
   examples lean program-shaped.
4. **Isolation-boundary alignment** (Finding 4) and **prose
   visible-close** (Finding 6) — near-misses; fit holds, but rests
   on alignment/judgment the framework does not name.

None of these blocked the derivation — every slot filled and the
method was inherited unchanged. They are the forward-derivation's
evidence about whether the framework can instantiate for its own
domain: **it can, but the single-tree assumption and the code-shaped
coupling-shape set are the two places the fixed method visibly
assumes a narrower world than corpus-evolution presents.**
