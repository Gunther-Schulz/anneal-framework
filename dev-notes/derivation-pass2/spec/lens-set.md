# anneal-dev Specification — Lens set

anneal-dev's standardized lens set — the corpus-evolution recurring
blind-spots an expert rule-corpus maintainer watches for that a
novice would not think to. The framework leaves the *set* to the
domain instance (`anneal-framework/spec/modules.md` §2.2); modes and
artifact formats are framework-level and used as specified there.

Each lens fills the lens-entry shape — Name, Question, Scope — from
the framework's `modules.md` §2.1. Built on the anneal-dev bindings
(`bindings.md`).

## Path

**Path 1 — incident-grounded.** This domain has an incident
history: the recurring-mistakes corpus the derivation was given is
the accumulated body of rule-corpus-evolution failures an expert
has watched for, not blank-slate hypotheses. The set below is
derived directly from those incidents — each lens names a failure
class that has actually recurred. (Contrast: a fresh domain with no
incident history bootstraps Path 2 / validate-by-use,
`instantiation-guide.md` §4.) Path 1 does not mean the set is
complete-for-the-domain — completeness is approached as real runs
surface lenses the corpus didn't yet name; it means the set's
members are incident-grounded, not hypothesized.

## What became a lens vs. a binding

The recurring-mistakes corpus carried eight raw phenomena. Two of
them are not cycle-applied lenses but verification-battery bindings,
because the failure is structural to the domain's *outcome* and is
checked by an executable check, not by a per-cycle inspection
question:

- **Lossy-render** and **Over-claimed-verification** are watched
  primarily by the verification battery (`bindings.md` Verification
  battery: render-fidelity check 1, and the "run-not-asserted"
  discipline) and by the impl-phase write-time self-check
  (`bindings.md` Self-check lenses). They ALSO appear below as
  lenses, because the failure can be introduced at *design/cycle*
  time (a design decision that commits to a softened render, or a
  cycle that records an over-claimed "verified" basis) — and the
  standardized inspection pass must catch them there, before they
  reach the work product. The binding and the lens compound: the
  lens catches the design-time commitment, the battery catches the
  rendered artifact.

The other six phenomena (Bloat, Fragmentation, Leakage,
Missed-dependents, Unenforced-rule, Undefined-shorthand) are
cycle-applied lenses below.

---

## The set

### Bloat
- **Question:** does the cycle's rule-text add prose past what is
  load-bearing — sentences that restate, hedge, illustrate beyond
  one example, or narrate reasoning the rule does not act on? For
  each added or amended passage: name the load-bearing claim or
  premise it carries (per the framework's Load-bearing test,
  `anneal-framework/spec/glossary.md`); a passage with no namable
  load-bearing function is bloat.
- **Scope:** any rule-text the cycle adds or amends — a new clause,
  an expanded section, a new example. Fires on the change-set's
  added prose; the operational test is the Load-bearing descriptor
  (would removing this passage change any rule the corpus encodes).

### Fragmentation
- **Question:** is the principle this cycle states or amends already
  stated elsewhere in the corpus — such that the corpus now holds
  two copies that can drift apart? The basis is a wrap-tolerant
  search for the principle's distinctive tokens across the whole
  corpus (`bindings.md` exhaustive-search binding). If a copy
  exists, the cycle resolves to one canonical statement +
  cross-references, not a second copy.
- **Scope:** any cycle that states, restates, or amends a principle,
  rule, or defined behavior. Fires when the cycle commits a
  principle to text; the enumeration of existing statements is a
  completeness claim, search-established (`core.md` §3.2), not
  recalled.

### Leakage
- **Question:** does a rule placed in (or amended within) a file
  meant to be domain-general carry a domain-specific concretion — a
  named language, tool, file path, or problem-domain vocabulary that
  ties the rule to one domain? Apply the framework-arbitrariness
  test (`foundation.md` contract 1): would this rule still apply
  rendered into an instance for an unrelated domain? A rule that
  fails the test in a domain-general file is leakage; the fix is to
  move the concretion to the instance slot (`foundation.md`
  contract 3) or generalize the rule.
- **Scope:** any rule-text the cycle adds or amends in a file whose
  level is "domain-general" (the framework spec, skill-craft
  canonical). Fires on edits to those levels; the level is read off
  the three-level test (`anneal-framework/spec/README.md`
  Architecture).

### Missed-dependents
- **Question:** for a rule the cycle changes, removes, or replaces,
  does the basis enumerate every dependent across the whole corpus —
  every spot that states, cross-references, depends on, or RENDERS
  the changed contract? Dependents are the framework's
  **target-dependents** coupling shape (`glossary.md` Coupling
  shape: "what depends on or uses the target"); in corpus-evolution
  they take these forms — **cross-references** (a `§N`/file-name
  pointer to the changed rule), **paraphrased restatements** (the
  same rule worded differently elsewhere — invisible to a verbatim
  search), **rendered clauses** (the plugin paraphrase of the rule),
  **closed-set members** (the rule names a member enumerated in more
  than one file), and **glossary/defined-term uses** (the rule uses
  a term whose definition the change affects). A search on one form
  only, declared as the dependent set, is missing its true-unit
  basis — the silent-substitution shape (`core.md` §3.2).
- **Scope:** any change, removal, or replacement of an existing rule
  (the framework's Coupled-change / completeness-claim forcing
  function, `core.md` §3.2.2). The enumeration spans every corpus
  repo (framework spec, skill-craft, instance specs, rendered
  plugins); the search is wrap-tolerant per `bindings.md`. A
  paraphrased restatement or a rendered clause is a
  target-dependents dependent the wrap-tolerant search reaches
  directly when it shares distinctive tokens; one that a search
  cannot exhibit because it resolves only through paraphrase at
  render-time is recorded [CONDITIONAL], its basis the dependent
  exercised by the render-fidelity / coherence checks (`core.md`
  §3.2.2, §4.3; `bindings.md` Verification battery) — the
  **target-behavior** runtime case (the rule's behavior resolving
  *through* that render-resolved dependent), §3.2.2's native path
  (documented at `glossary.md` Coupling shape target-dependents).

### Unenforced-rule
- **Question:** for a rule the cycle states or amends, is there an
  artifact in which the rule's violation would be visible — a closed
  enum, a gated check, an evidence-bearing artifact the rule forces,
  a "must" the renderer carries structurally — or is it stated as
  prose-suggestion only? Apply the framework's enforcement-strength
  discipline (`anneal-framework/spec/README.md` Prescription
  discipline): a load-bearing rule left as unenforced prose is
  under-prescribed. Name the artifact in which following-the-rule
  produces something and not-following produces nothing
  (`core.md` §3.1); if none, the rule is unenforced.
- **Scope:** any load-bearing rule the cycle states or amends. Fires
  when the cycle commits a rule that prescribes AI behavior; the
  question is the §3.1 evidence-bearing-artifact test applied to the
  rule itself, not to the cycle's mechanism output.

### Undefined-shorthand
- **Question:** does the cycle introduce or rely on a shorthand term
  — a coined phrase used as if it had a fixed meaning — that has no
  single definition the corpus points to? The basis is a
  wrap-tolerant search establishing whether the term is defined
  (glossary entry, or a single canonical defining sentence) and
  whether existing uses agree with that definition. An undefined or
  multiply-defined shorthand is interpreted inconsistently across
  the corpus.
- **Scope:** any cycle that introduces a new term, or uses an
  existing coined term in a load-bearing way. Fires at the moment
  the term is committed to text; the definedness check is a
  completeness claim over the term's uses, search-established
  (`core.md` §3.2).

### Lossy-render
- **Question:** does a design decision this cycle commits — one that
  will be rendered into a plugin — preserve the source rule's
  enforcement strength and completeness, or does it commit to a
  paraphrase that softens a "must" to a "should", drops a clause, or
  flattens a closed enum into open prose? The check is against the
  source spec clause the decision renders, named in the decision's
  basis. (The rendered artifact itself is checked by the
  render-fidelity battery, `bindings.md`; this lens catches the
  softening at design time, before it is rendered.)
- **Scope:** any design decision the cycle commits whose target is a
  rendered plugin clause, or any cycle work that paraphrases a
  source rule. Fires when a render/paraphrase is committed; the
  source clause is read whole (`bindings.md` construct-taken-whole)
  so the comparison is against the full source, not a fragment. Also
  a write-time self-check lens (`bindings.md`).

### Over-claimed-verification
- **Question:** does any "verified" / "checked" / "confirmed" claim
  the cycle records assert more than the cited basis actually
  establishes — a basis covering part of the set claimed whole, a
  read of one clause standing in for "all references checked", a
  "render is faithful" claim with no clause-by-clause artifact? The
  check re-opens the claim's cited basis against its stated unit
  (`core.md` §3.2 true-unit basis): the basis must cover the claim's
  true unit, not a coarser proxy.
- **Scope:** any completeness or verification claim the cycle records
  in the tracker — a finding's verification evidence, a design
  decision's basis, a [READY] supporting fact. Fires on every
  recorded "verified"-class claim; the lens is the true-unit-basis
  rule applied to the corpus-evolution claims. Also a write-time
  self-check lens (`bindings.md`).

---

## Supplement mechanism

anneal-dev's lens-set slot extends with a project-supplement
mechanism per `instantiation-guide.md` §4 "Optional:
project-supplemental lenses". Declared in `lens-supplement.md`.
