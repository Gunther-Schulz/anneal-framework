# Run: f0-render-conventions

- **Status:** IN-PROGRESS
- **Phase:** investigate-design
- **Mode:** interactive
- **Task summary:** F0 render-convention gate (gates the clippy re-render) — make the
  instance-template / guide / glossary coherent on (1) slot scaffolding (the missing isolation
  slot file + the already-settled slot-as-file-vs-section model) and (2) the glossary as the
  binding-table interface (headwords for binding-table left-column terms carrying hidden
  framework semantics).

## Requirements record (R1..Rn — goal, separated from proposed solution)

- **R1.** The guide's claim that the instance-template scaffolds a placeholder file for every
  framework-recognised **spec slot** holds true (developer-time template-copy). Currently false
  for the isolation slot.
- **R2.** The slot-representation model (file-per-slot in template; instances may consolidate to
  sections) is coherent and consistently reflected across the guide §2, the template README
  enumeration, and the template `spec/` files — an instance author is not left guessing whether a
  slot exists or where it lives.
- **R3.** An instance author can resolve every framework term in the binding-table left column
  (`<instance>/spec/bindings.md`) through the **glossary**, without reading the framework spec —
  for terms carrying hidden framework semantics (the discriminator), avoiding both a leaky
  firewall and Additive-reflex bloat.
- **R4 (gate purpose).** R1–R3 hold *before* the clippy re-render consumes the template / guide /
  glossary — so the re-render lands against a coherent interface, not rendered twice.

**Operator's verbatim request (this run's invocation):** "F0 render-convention gate (batched
cycle; gates the clippy re-render). … (1) instance-template-slot-scaffolding — FORK-FIRST …
slot-as-file vs slot-as-section … Resolve the model, then scaffold the template to match. (2)
glossary-binding-table-interface-completeness — make the glossary cover the binding-table
left-column … Discriminator: a framework term needs a glossary headword iff an instance
referencing it would otherwise read the framework spec to learn its precise meaning." (Backlog:
`dev-notes/backlog/instance-template-slot-scaffolding.md`,
`dev-notes/backlog/glossary-binding-table-interface-completeness.md`.)

---

## F-track (findings)

- **F1 [VERIFIED — non-issue]** The slot-as-file-vs-section "fork" is already settled in the live
  corpus — not an open decision. basis: located read `instance-template/README.md:53-59` ("The
  template's one-file-per-slot structure is for discoverability … you may consolidate … the
  framework requires the slot content, not the file structure. Closed-slot discipline applies
  regardless of file layout").
- **F2 [VERIFIED — addressed→D2]** `instance-template/spec/` has no `isolation.md` — the isolation
  slot (a required supplied mechanism per guide §2) is unscaffolded. basis: `ls
  instance-template/spec/` → {bindings, extensions, lens-set, lens-supplement, persistence,
  presentation, README}.md, no isolation; located read `instantiation-guide.md:102-108` (isolation
  is a "You supply" mechanism slot).
- **F3 [VERIFIED — addressed→D3]** The template README's slot enumeration omits isolation —
  "Required-mechanism slots" lists only `extensions.md` + `lens-supplement.md`. basis: located read
  `instance-template/README.md:33-49`.
- **F4 [VERIFIED — addressed→D2]** The guide's "scaffolds a placeholder file for every slot" claim
  is therefore false for isolation (developer-time template-copy). basis: located read
  `instantiation-guide.md:16-18` ("The template scaffolds a placeholder file for every slot the
  framework recognises") + F2.
- **F5 [VERIFIED — non-issue]** Instances vary validly under F1: anneal-dev declares isolation as a
  `bindings.md` section ("## Isolation slot — corpus-evolution binding"), clippy consolidates all
  slots into `bindings.md` sections. Neither is a defect; only the template scaffold + its README
  enumeration are. basis: located reads `anneal-dev/spec/bindings.md:124`, `coding-clippy/spec/
  bindings.md` (sections: Bindings/Lens set/Run-artifact persistence/Operator-editable artifacts/
  Extensions/Dispatch models/Dispatch isolation).
- **F6 [PENDING]** Binding-table left-column terms lack glossary headwords (item 2). search:
  `grep -ciE '\*\*[^*]*<term>' spec/glossary.md` → 0 for {located read, taken whole, true-unit,
  visible-close, executable verification}; >0 for {element, container}. The per-term discriminator
  pass (R3) is not yet run — held [PENDING] for cycle 2.

## D-track (design decisions)

- **D1 [VERIFIED]** Slot-representation model = the existing settled one (file-per-slot in the
  template for discoverability; instances may consolidate slots into sections; closed-slot
  discipline regardless of layout). No new model is designed; the work is to make the template +
  guide + README *consistent* with it. basis: `instance-template/README.md:53-59` (F1).
  - considered: redesign to slot-as-section-only or slot-as-file-mandatory (rejected: the live
    corpus already settles the hybrid; both reduce expressiveness with no defect to fix — F1/F5).
- **D2 [PENDING]** Add `instance-template/spec/isolation.md` — a placeholder scaffold matching
  `persistence.md`'s style (header comment → `core.md` §4.2.3; placeholder sections matching the
  isolation slot's declaration shape per guide §2:102-108 — copy creation, unit identifier,
  escape-resistance, state marker the integrity check reads, restore mechanism, provisioned
  non-tracked run-inputs; OPTIONAL/required marker per the README's slot category). Closes F2/F4.
  Needs body-detail (the exact placeholder content) to reach [VERIFIED] — cycle 2.
- **D3 [PENDING]** Amend `instance-template/README.md` to enumerate `isolation.md` in its slot list
  (category: required-mechanism, alongside persistence as a required supplied mechanism). Closes
  F3. Amendment decision — basis owes a references-enumeration of the README's slot-list +
  consistency with guide §2's slot set. Cycle 2.
- **D4 [PENDING]** (item 2) Add glossary headwords for the binding-table left-column terms passing
  the R3 discriminator. Needs the per-term discriminator pass against the live glossary + the
  instances' binding-table left columns (anneal-dev/clippy/daneel). Cycle 2.

---

## Cycle 2 (appends — append-only ledger)

### F-track
- **F7 [VERIFIED — non-issue/→D4]** R3 discriminator pass result. NEEDS-definition (resolvable only
  via core.md today): `located read of the source`, `executable verification` (both *listed* in
  glossary **Basis** but not defined — basis: located read `glossary.md:49-54`, lists forms +
  points to `core.md §3.2`); `construct taken whole`/true-unit (absent — search `grep -i 'taken
  whole\|true-unit' glossary.md` → 0 outside binding-table cite); `wrap-tolerant search` (**Completeness
  claim** `glossary.md:77-79` says "a mechanical search (core.md §3.2)", undefined). ALREADY-COVERED:
  `containers` (**Work product** `glossary.md:140` defines it), `scope` (**Scope** headword). EXCLUDED
  self-evident (R3): `the task`, `the problem space`, `existing work`, `the work`, `an element of the
  work product` (constituent-clear + instance defines its own elements).
- **F8 [VERIFIED — surfaced]** The binding-table left-column citations point at `core.md` for the
  NEEDS-definition terms (e.g. `a located read of the source (core.md §3.2)`), so even once the
  glossary defines them, the firewall isn't *complete* until those citations re-point to the glossary.
  basis: located read `anneal-dev/spec/bindings.md:41-44`. Routed: re-pointing the binding-table
  citations is instance-render work (per instance), out of this template/guide/glossary batch — recorded
  for the operator; not blocking R3 (the glossary-resolvability R3 requires is met by D4).

### D-track
- **D2 [VERIFIED]** Add `instance-template/spec/isolation.md` — placeholder scaffold, `persistence.md`
  style. Body: header comment naming the slot + `core.md §4.2.3`/`§4.2` pointer; "OPTIONAL/required"
  marker = **required-mechanism** (per D3 category); "## <Instance>'s isolation mechanism" with empty
  placeholder sub-sections matching the slot's declaration shape (copy creation; unit identifier;
  escape-resistance; the state marker the integrity check reads; the restore mechanism; which
  non-tracked run-inputs are provisioned); a commented-out small example optional. Domain-general (no
  language/tool concretion). Closes F2/F4. basis: located reads `instance-template/spec/persistence.md`
  (style), `instantiation-guide.md:102-108` (declaration shape — 6 elements), `:400-408` (placeholder
  content style), `anneal-dev/spec/bindings.md:124-168` (worked-example shape).
- **D3 [VERIFIED]** Amend `instance-template/README.md` slot enumeration: add `spec/isolation.md` as a
  **required-mechanism slot** (the framework *requires* the isolation guarantees and the instance
  *supplies* the mechanism — `instantiation-guide.md:102-108`), placed with persistence as a required
  supplied mechanism, carrying the `core.md §4.2.3` pointer. Closes F3. Amendment basis: the README
  slot-list (`:22-49`) is the sole enumeration of template slot files (search: `grep -n 'spec/.*\.md'
  instance-template/README.md`); behavior added (one slot line), none removed/changed.
  - considered: place under a new "Required-mechanism" framing distinct from persistence (rejected:
    persistence is the existing sibling required supplied mechanism, already under "Required slots";
    consistency over re-categorization — no defect in the current split).
- **D4 [VERIFIED]** Sharpen the glossary so the binding-table interface is resolvable without a spec
  read (R3), for the F7 NEEDS set only: make **Basis** (`glossary.md:49-54`) *define* its three listed
  forms — `located read` (the clause read to its visible close + exactly one observable fact),
  `construct taken whole`/true-unit, `executable verification` (the dispatched-and-run check) — and make
  **Completeness claim** (`:77-79`) *define* `wrap-tolerant search` (distinctive single tokens /
  newline-flattened, because prose wraps). Concise gloss + retained `core.md §3.2` pointer (the full
  rule stays in core.md — no Fragmentation; the glossary gives the interface-sufficient definition). NO
  new headwords (Additive-reflex caveat, R3). Closes F6/F7. Amendment basis: the two entries are the
  sole glossary homes of these terms (search `grep -in 'located read\|taken whole\|executable
  verification\|mechanical search' glossary.md`); behavior = list→define (additive sharpening), nothing
  dropped.
  - considered: 4 new standalone headwords (rejected: Bloat/Fragmentation — the terms are basis-rule
    sub-forms already grouped under Basis/Completeness-claim; define-in-place is the Pareto move).
  - basis strengthened (cycle 2, run): definitional homes = **Basis** `glossary.md:50,52`,
    **Completeness claim** `:79`; `taken whole`/`true-unit`/`wrap-tolerant` → `grep` 0 hits in
    glossary (genuinely absent, must add); Missed-dependents `grep -rn 'glossary.md (Basis|Completeness)'`
    across anneal-dev/clippy/framework specs + guide → **0** (no external dependent re-points; additive).
- **D3 basis strengthened (cycle 2, run):** `grep -rn 'spec/.*\.md' instance-template/README.md` →
  the slot-list at `:25-48` is the sole template-slot-file enumeration (guide:274 = presentation-vs-
  extensions context, not a slot-file list); adding `spec/isolation.md` there is complete.

---

## Cycle 3 — CONVERGENCE CYCLE (intent-falsification ran; mechanical skipped: intent-delta this cycle)

Fresh-context intent-falsification (subagent `aebac44b2b059c540`, opus, criteria-first) produced a
**D-track delta** — design NOT [READY]. Artifact:
`.anneal-dev/runs/f0-render-conventions.cycle-3.intent-falsification.md`.

### F-track
- **F-A [VERIFIED — surfaced]** README slot buckets (`README:24-42`: Required={bindings,persistence,
  lens-set} + Required-mechanism={extensions,lens-supplement}) vs guide's "four required" grouping
  (`guide:137`) place isolation differently — D3 put it in bucket-2 (w/ extensions), guide groups it
  in bucket-1 (w/ persistence). Judgment; informs the D3 revision. basis: `sed 135,142p guide` vs
  `sed 24,42p README`.
- **F-B [PENDING]** Guide §2 designates isolation's worked example as a `bindings.md` **section**
  (`guide:108`); clippy (`coding-clippy/spec/bindings.md:169`) + anneal-dev (`anneal-dev/spec/
  bindings.md:124`) realize it as sections; **no isolation.md anywhere**. Scaffolding it as a file (D2)
  contradicts the guide + both instances → the "where does the slot live?" inconsistency R2 forbids.
  NB: the template **already** uses files for `persistence.md`/`presentation.md` while the guide's
  worked examples for those are also bindings.md sections — so the real gap is the **guide §2 doesn't
  carry the template-file-vs-instance-consolidation story** the template README:53-59 does. basis:
  `grep 'Dispatch isolation' guide`→:108; instance reads.
- **F-C [PENDING]** Guide `:18` ("scaffolds a placeholder file for every slot") is a slot-enumeration
  surface **outside** the README — D3's "sole enumeration" basis is false; and `:18` ("file for every
  slot") contradicts `:108` (isolation = section): the guide is internally inconsistent about isolation.
  basis: `grep 'placeholder file for every slot' guide`→:18.
- **F-D [PENDING]** The bindings-table left-column **cells** cite `core.md §3.2` in-cell (anneal-dev
  rows 42/43) → an author resolves via core.md, not the glossary D4 sharpens; `rg '(core|modules)\.md
  …§' anneal-dev/spec/bindings.md` → 30 matches (also a guide §3 firewall-rule violation). Defining the
  terms (D4) doesn't close R3 — the left-column citations must re-point to the glossary. basis: rg result.

### D-track — reopened + revised directions (cycle 4 designs them)
- **D2 [INVALIDATED]→[PENDING]** (F-B falsified the file-form premise). Revised direction: KEEP
  isolation.md (consistent with the existing `persistence.md`/`presentation.md` template files) but
  re-form PAIRED with D5 (the guide reconciliation) so the file-scaffold + section-worked-example are
  no longer contradictory.
- **D3 [INVALIDATED]→[PENDING]** (F-C falsified sole-enumeration). Revised: account for guide `:18` as a
  second surface (handled by D5), and re-decide isolation's README bucket (F-A — likely bucket-1 with
  persistence, the guide's grouping).
- **D4 [INVALIDATED]→[PENDING]** (F-D falsified glossary-resolvability). Revised: KEEP the glossary
  define + ADD re-pointing the binding-table left-column citations from `core.md §3.2` to the glossary
  (template bindings.md in-scope; existing instances anneal-dev/clippy = render-debt). This is what
  actually closes R3's firewall.
- **D5 [OUTLINED] (NEW)** Reconcile guide §2's representation story: the template scaffolds a FILE per
  slot (discoverability) and instances may CONSOLIDATE to `bindings.md` sections (the worked examples
  clippy/anneal-dev ARE consolidated) — fix `guide:18` + the worked-example framing (`:92` persistence,
  `:108` isolation, `:120` presentation) so they carry the template-README:53-59 reconciliation rather
  than contradict the file scaffold. Addresses F-B + F-C. basis: `README:53-59` (the reconciliation that
  belongs in the guide too); guide `:18,:92,:108,:120`.

---

## Cycle 4 — design re-form (addresses the cycle-3 convergence deltas)

### F-track
- **F-E [VERIFIED — deferred]** The bindings-table LEFT-COLUMN `core.md` citations that F-D flagged are
  in the **realized instances only** — `anneal-dev/spec/bindings.md` rows 39/42/43, `coding-clippy/spec/
  bindings.md` (6 cites). The **template** `bindings.md` is already firewall-clean (`grep -cE '(core|
  modules)\.md.{0,4}§' instance-template/spec/bindings.md` → **0**) and points authors at the glossary.
  So once D4 defines the terms, R3 holds for the template + every new instance via the template; the
  existing instances' re-point is **render-debt** (clippy's rides the F0-gated clippy re-render;
  anneal-dev's is its own instance hygiene). Deferred → trigger: the clippy/anneal-dev re-render.
  basis: `grep` counts (template 0 / clippy 6 / anneal-dev 30) + guide §3 firewall rule `:169-186`.

### D-track — re-formed to [VERIFIED]
- **D2 [VERIFIED]** (re-form) Add `instance-template/spec/isolation.md`, `persistence.md`-style scaffold
  (header → `core.md §4.2.3`; "## <Instance>'s isolation mechanism" with empty placeholder sub-sections
  for the 6-element declaration shape: copy creation / unit identifier / escape-resistance / state
  marker the integrity check reads / restore mechanism / provisioned non-tracked run-inputs; required —
  no OPTIONAL marker, like persistence.md; domain-general). Coherence with the section-form worked
  examples is provided by **D5**. basis: located reads `instance-template/spec/persistence.md` (style +
  the template ALREADY files-per-slot for persistence/presentation), `instantiation-guide.md:102-108`
  (6-element decl shape), `:400-408` (placeholder content style), `anneal-dev/spec/bindings.md:124-168`
  (worked-example content).
- **D3 [VERIFIED]** (re-form) Amend `instance-template/README.md`: add `spec/isolation.md` under
  **"Required slots"** (with persistence — the guide's "four required" grouping; resolves F-A away from
  the bucket-2 placement), `core.md §4.2.3` pointer. basis: README "Required slots" bucket `:22-32`,
  guide §2:102-108 (isolation = required supplied mechanism, peer to persistence), README:25-48 sole
  template-slot-file enumeration; the guide `:18` "every slot" surface is handled by D5 (not D3).
  - considered: bucket-2 "Required-mechanism slots" w/ extensions (rejected, F-A: those "declare the
    mechanism even when no items declared"; isolation is a must-fill substantive mechanism like
    persistence — bucket-1).
- **D4 [VERIFIED]** (re-form — leaner than cycle-3 implied) Sharpen glossary **Basis** (`:49-54`) to
  DEFINE its three listed forms (`located read` = clause read to visible close + exactly one observable
  fact; `construct taken whole`/true-unit; `executable verification` = the dispatched-and-run check) and
  **Completeness claim** (`:77-79`) to DEFINE `wrap-tolerant search` (distinctive single tokens /
  newline-flattened); concise gloss + retained `core.md §3.2` pointer; NO new headwords. Closes R3 for
  the template (already firewall-clean) + new instances; existing-instance re-points = F-E render-debt
  (NOT expanded into D4 — F-D's instance-re-point scope was over-reach; template is clean). basis: F7 +
  F-E (template 0 cites) + the glossary entries are the sole homes (cycle-2 sub-annotation).
- **D5 [VERIFIED]** (new) Add a reconciliation clause to guide §2 (at the slot-set definition
  `:135-146`) — the template scaffolds one FILE per slot for discoverability; a stabilized instance MAY
  consolidate slots into `bindings.md` sections (cross-reference `instance-template/README.md` "After
  instantiation", the canonical statement — Fragmentation: cross-ref, NOT a duplicate), so the worked
  examples (`:92` persistence, `:108` isolation, `:120` presentation) read as consolidated instances,
  not contradictions of `:18`. Closes F-B/F-C. basis: `instance-template/README.md:53-59` (canonical
  consolidation statement to cross-ref), guide `:16-22,:92,:108,:120,:135-146`; amendment is additive
  (a clause + cross-ref), removes nothing.

---

## Cycle 5 — RE-CONVERGENCE (intent-falsification CLEAN, no D-delta; mechanical pass running)

Fresh-context intent-falsification (subagent `a364ea59c3eaba468`, opus, criteria-first) on D1–D5 →
**no D-track delta**. Artifact: `.anneal-dev/runs/f0-render-conventions.cycle-5.intent-falsification.md`.

### F-track
- **F-INTENT-1 [VERIFIED — surfaced]** D5's reconciliation clause, placed at guide:135-146, sits AFTER
  the §2 worked examples (`:92`,`:108`) that exhibit the file-vs-section contradiction → a linear reader
  hits the contradiction before the reconciliation. Judgment-class (no closed predicate for reader-
  confusion). **Impl guidance folded into D5:** place the reconciliation / a forward-pointer at/before
  the FIRST worked example (`guide:92`), not only at `:135`. basis: `rg -n 'consolidat' guide` → only
  ≥:135.
- **F-INTENT-2 [VERIFIED — surfaced]** Corrects F-E enumeration: the binding-table left-column `core.md`
  cites are **anneal-dev rows 39/42/43 ONLY**; clippy + daneel binding tables are firewall-clean (clippy
  line-6 is intro prose, no §). basis: `awk -F'|' '/^\|/{if($2~/(core|modules)\.md.*§/)print NR}'` over
  the three bindings.md → anneal-dev only.
- **F-E [VERIFIED — deferred] (corrected line)** Binding-table left-column render-debt = **anneal-dev
  `bindings.md` rows 39/42/43 only** (drop "clippy 6" / "anneal-dev 30"; the 30 were mostly prose-body,
  not left-column). Trigger (well-formed): the §3 firewall coherence check `rg '(core|modules)\.md…§'
  <instance>` (guide:182-187) re-firing at the anneal-dev re-render — foundations.md canonical
  "executable-verification output class." basis: F-INTENT-2.

### D-track
- **D5 [VERIFIED] (basis refinement, resolution unchanged)** — placement detail added: the reconciliation
  is realized at/before the first worked example (`guide:92`) per F-INTENT-1, not only at `:135`. (Impl
  realization detail; D5's resolution "add a guide §2 reconciliation cross-referencing README:53-59" is
  unchanged — not an amendment.)
- **D1–D4 unchanged** ([VERIFIED]); intent pass falsified none. Mechanical falsification pass over D1–D5
  dispatched next.

### Convergence outcome — CLEAN ([READY] reached)
Mechanical falsification (subagent `ac95111a7deddda9f`, opus; `.../cycle-5.falsification.md`):
**D1–D5 ALL HOLD** (orchestrator-computed). Intent CLEAN + mechanical ALL-HOLD → **zero D-track deltas
→ convergence cycle clean.**

**Fresh-session implementability test: PASSED** (per-implementer-step external evidence):
- U1/D2 → located reads `instance-template/spec/persistence.md` (style) + `instantiation-guide.md:102-108`
  (the 6 declaration elements) + `anneal-dev/spec/bindings.md:124-168` (worked example).
- U2/D3 → located read `instance-template/README.md:22-32` ("Required slots" bucket shape).
- U3/D4 → located reads `spec/glossary.md:49-54` (Basis) + `:77-79` (Completeness) + `core.md §3.2`
  (the source definitions to gloss).
- U4/D5 → located reads `instance-template/README.md:53-59` (canonical statement) + `instantiation-guide.md:92`
  (placement anchor).
Every step carries an external citation → PASSED (no step answered from recall).

Impl plan: `.anneal-dev/runs/f0-render-conventions.impl-plan.md` (4 units, all parallel-eligible).
**[READY]** presented to operator for `next phase`.
