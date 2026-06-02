# The standardized lens set

The pre-written inspection criteria the standardized inspection pass
applies — anneal-dev's recurring corpus-evolution blind-spots: the
looking an expert rule-corpus maintainer does that a novice would not
think to. The set is closed: a lens is in it or it is not. Each cycle's
standardized pass attests the lenses in scope that cycle; the whole set
is accounted for at [READY] (`tracker.md`).

Each lens fills the lens-entry shape — its **Name**, its **Question**
(the single question it asks of the work), and its **Scope** (what it
applies to, and the trigger that brings it into a cycle's standardized
pass).

**Project supplements.** Projects using anneal-dev may supply additional
lenses at `anneal-dev.config/lenses.md`. The runtime lens set is **core
(below) ∪ project supplement**, closed at the project's runtime; the
standardized pass iterates the union. Supplements are additive-only —
they cannot disable, narrow, or override the core set, and follow the
same Name/Question/Scope shape and skill-craft form discipline as core
lenses. Malformed supplement file = fail-loud halt at standardized-pass
dispatch (the supplement is evidence-bearing input; parse error surfaces
as a tracker finding for the operator). If a core lens consistently
mismatches a project's needs, the fix is at the instance-spec level
(sharpen the core lens), not at the project level (silence it).

## Lens vs. verification battery

Two of the domain's recurring phenomena — **Lossy-render** and
**Over-claimed-verification** — are watched *primarily* by the
verification battery (`phases/verify.md`: render-fidelity check, and the
"run-not-asserted" discipline) and by the impl-phase write-time
self-check (`phases/implement.md` Self-check at dispatch boundary). They
ALSO appear below as lenses, because the failure can be introduced at
*design/cycle* time — a design decision that commits to a softened
render, or a cycle that records an over-claimed "verified" basis — and
the standardized inspection pass must catch them there, before they
reach the work product. The binding and the lens compound: the lens
catches the design-time commitment, the battery catches the rendered
artifact.

The other six (Bloat, Fragmentation, Leakage, Missed-dependents,
Unenforced-rule, Undefined-shorthand) are cycle-applied lenses only.

---

## Bloat

- **Question:** does the cycle's rule-text add prose past what is
  load-bearing — sentences that restate, hedge, illustrate beyond one
  example, or narrate reasoning the rule does not act on? For each added
  or amended passage: name the load-bearing claim or premise it carries
  (per the Load-bearing test, `foundations.md`); a passage with no
  namable load-bearing function is bloat.
- **Scope:** any rule-text the cycle adds or amends — a new clause, an
  expanded section, a new example. Fires on the change-set's added
  prose; the operational test is the Load-bearing descriptor (would
  removing this passage change any rule the corpus encodes).

## Fragmentation

- **Question:** is the principle this cycle states or amends already
  stated elsewhere in the corpus — such that the corpus now holds two
  copies that can drift apart? The basis is a wrap-tolerant search for
  the principle's distinctive tokens across the whole corpus
  (`foundations.md` true-unit basis). If a copy exists, the cycle
  resolves to one canonical statement + cross-references, not a second
  copy.
- **Scope:** any cycle that states, restates, or amends a principle,
  rule, or defined behavior. Fires when the cycle commits a principle to
  text; the enumeration of existing statements is a completeness claim,
  search-established (`foundations.md`), not recalled.

## Leakage

- **Question:** does a rule placed in (or amended within) a file meant
  to be domain-general carry a domain-specific concretion — a named
  language, tool, file path, or problem-domain vocabulary that ties the
  rule to one domain? Apply the framework-arbitrariness test: would this
  rule still apply rendered into an instance for an unrelated domain? A
  rule that fails the test in a domain-general file is leakage; the fix
  is to move the concretion to the instance slot or generalize the rule.
- **Scope:** any rule-text the cycle adds or amends in a file whose
  level is "domain-general" (the framework spec, skill-craft canonical).
  Fires on edits to those levels; the level is read off the three-level
  test (`anneal-framework/spec/README.md` Architecture).

## Missed-dependents

- **Question:** for a rule the cycle changes, removes, or replaces, does
  the basis enumerate every dependent across the whole corpus — every
  spot that states, cross-references, depends on, or RENDERS the changed
  contract? Dependents are the framework's **target-dependents** coupling
  shape (`anneal-framework/spec/glossary.md` Coupling shape: "what
  depends on or uses the target"); in corpus-evolution they take these
  forms — **cross-references** (a `§N`/file-name pointer to the changed
  rule), **paraphrased restatements** (the same rule worded differently
  elsewhere — invisible to a verbatim search), **rendered clauses** (the
  plugin paraphrase of the rule), **closed-set members** (the rule names
  a member enumerated in more than one file), and
  **glossary/defined-term uses** (the rule uses a term whose definition
  the change affects). A search on one form only, declared as the
  dependent set, is missing its true-unit basis — the silent-
  substitution shape (`foundations.md`).
- **Scope:** any change, removal, or replacement of an existing rule
  (the framework's Coupled-change / completeness-claim forcing function,
  `foundations.md` Replacement, removal, or amendment). The enumeration
  spans every corpus repo (framework spec, skill-craft, instance specs,
  rendered plugins); the search is wrap-tolerant. A paraphrased
  restatement or a rendered clause is a target-dependents dependent the
  wrap-tolerant search reaches directly when it shares distinctive
  tokens; one that a search cannot exhibit because it resolves only
  through paraphrase at render-time is recorded [CONDITIONAL], its basis
  the dependent exercised by the render-fidelity / coherence checks
  (`foundations.md` Replacement, removal, or amendment; `phases/verify.md`
  Verification battery) — the **target-behavior** runtime case (the
  rule's behavior resolving *through* that render-resolved dependent).

## Unenforced-rule

- **Question:** for a rule the cycle states or amends, is there an
  artifact in which the rule's violation would be visible — a closed
  enum, a gated check, an evidence-bearing artifact the rule forces, a
  "must" the renderer carries structurally — or is it stated as
  prose-suggestion only? Apply the enforcement-strength discipline
  (`anneal-framework/spec/README.md` Prescription discipline): a
  load-bearing rule left as unenforced prose is under-prescribed. Name
  the artifact in which following-the-rule produces something and
  not-following produces nothing (`foundations.md`
  evidence-bearing-artifact rule); if none, the rule is unenforced.
- **Scope:** any load-bearing rule the cycle states or amends. Fires
  when the cycle commits a rule that prescribes AI behavior; the
  question is the evidence-bearing-artifact test applied to the rule
  itself, not to the cycle's mechanism output.

## Undefined-shorthand

- **Question:** does the cycle introduce or rely on a shorthand term — a
  coined phrase used as if it had a fixed meaning — that has no single
  definition the corpus points to? The basis is a wrap-tolerant search
  establishing whether the term is defined (glossary entry, or a single
  canonical defining sentence) and whether existing uses agree with that
  definition. An undefined or multiply-defined shorthand is interpreted
  inconsistently across the corpus.
- **Scope:** any cycle that introduces a new term, or uses an existing
  coined term in a load-bearing way. Fires at the moment the term is
  committed to text; the definedness check is a completeness claim over
  the term's uses, search-established (`foundations.md`).

## Lossy-render

- **Question:** does a design decision this cycle commits — one that will
  be rendered into a plugin — preserve the source rule's enforcement
  strength and completeness, or does it commit to a paraphrase that
  softens a "must" to a "should", drops a clause, or flattens a closed
  enum into open prose? The check is against the source spec clause the
  decision renders, named in the decision's basis. (The rendered
  artifact itself is checked by the render-fidelity battery,
  `phases/verify.md`; this lens catches the softening at design time,
  before it is rendered.)
- **Scope:** any design decision the cycle commits whose target is a
  rendered plugin clause, or any cycle work that paraphrases a source
  rule. Fires when a render/paraphrase is committed; the source clause
  is read whole (`foundations.md` true-unit basis, construct taken
  whole) so the comparison is against the full source, not a fragment.
  Also a write-time self-check lens (`phases/implement.md`).

## Over-claimed-verification

- **Question:** does any "verified" / "checked" / "confirmed" claim the
  cycle records assert more than the cited basis actually establishes —
  a basis covering part of the set claimed whole, a read of one clause
  standing in for "all references checked", a "render is faithful" claim
  with no clause-by-clause artifact? The check re-opens the claim's
  cited basis against its stated unit (`foundations.md` true-unit
  basis): the basis must cover the claim's true unit, not a coarser
  proxy.
- **Scope:** any completeness or verification claim the cycle records in
  the tracker — a finding's verification evidence, a design decision's
  basis, a [READY] supporting fact. Fires on every recorded
  "verified"-class claim; the lens is the true-unit-basis rule applied
  to the corpus-evolution claims. Also a write-time self-check lens
  (`phases/implement.md`).
