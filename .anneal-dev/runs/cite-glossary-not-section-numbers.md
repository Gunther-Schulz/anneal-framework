# Run: cite-glossary-not-section-numbers

- **Status:** PASSED
- **Phase:** verify
- **Mode:** auto-battle (switched from interactive at cycle 2 per operator)
- **Task:** Settle the render convention — an instance spec references the framework's method ONLY through framework glossary terms, never framework section-numbers (FB-3). Method-kernel edit (`spec/glossary.md` interface + `instantiation-guide.md` rule; possibly `spec/README.md`) → anneal-dev + kernel-independent verify (skill-craft self-review + operator soundness). Keystone-first: unblocks the anneal-dev re-render (its render cites framework §-numbers in 9 places).

> Work product: the `anneal-framework` repo (the convention's home). Per-instance citation re-pointing is downstream render work (instance-reinstantiation, Phase B) governed by this convention, NOT edited in this run.

---

## F-track (findings)

- **F1** [PENDING] No instance→framework citation-style rule exists in the framework today; the convention is net-new. — basis: `rg -ni "glossary|section number|citation|cite" instantiation-guide.md` → only binding/extension prose; §3 (instantiation-guide.md:139-158) binds domain terms but states no rule on citation form.
- **F2** [PENDING] Instance repos cite framework §-numbers across two populations — (a) instance-SPEC source (`<instance>/spec/{bindings,lens-set,debugging-disciplines}.md`) and (b) RENDERED plugin files (`<instance>/plugin/.../{references,phases}/*.md`). — basis: `rg -n "§[0-9]" <repo> -g '*.md'` per repo → clippy spec (bindings.md:45-173, lens-set.md:6-204), daneel (spec + plugin verify.md:146 / post-run-review.md:7), bauleitplan (plugin references only: foundations.md:72-82, tracker.md:5-6, lenses.md:6), anneal-dev (spec + plugin: 9 cites).
- **F3** [PENDING] The glossary already absorbs the layout-coupling — it cites `core.md §`-numbers 71× internally (e.g. "The basis rule is specified in `core.md` §3.2"); so "the glossary owns the term→section mapping" is largely already true. The gap is completeness, not creation. — basis: `rg -c "§[0-9]" spec/glossary.md` → 71; located read glossary.md:53-54.
- **F4** [PENDING] The binding-table left column (`<instance>/spec/bindings.md`) is already a term interface (framework term → domain value) but binds concepts that are NOT glossary headwords — e.g. "the domain's executable verification" is a binding row (clippy/bindings.md:33, daneel:36, anneal-dev:44) and appears in core.md/glossary prose, but has no glossary entry. — basis: located read clippy/spec/bindings.md:21-34; `rg "executable verification"` → glossary.md:52,100 use it in prose, not as a defined headword.
- **F5** [PENDING] Framework-INTERNAL docs (instantiation-guide.md, development-process.md, glossary.md) also cite `core.md §`-numbers, but these are intra-framework (one repo, one maintainer) — NOT the brittle cross-repo coupling the finding targets. — basis: located read instantiation-guide.md:84-90 (cites `spec/core.md §6`, `modules.md §3.1/§3.2/§3.3` — same-repo).

## D-track (design decisions)

- **D1** [OUTLINED] SCOPE — this run settles the CONVENTION and edits the framework only: (a) `instantiation-guide.md` (state the rule), (b) `spec/glossary.md` (complete it as the instance-facing interface for every concept instances cite), (c) `spec/README.md` (name the glossary's interface role; reconcile with "definitions-only"). The per-instance citation re-pointing is NOT in this run — it is downstream render work (instance-reinstantiation Phase B) this convention governs. — basis: instance-reinstantiation.md:47-62 lists `cite-glossary-not-section-numbers` as a render-CONVENTION prerequisite to settle BEFORE the per-instance re-renders.
  - considered: also re-point every instance citation now (rejected: that is the reinstantiation effort's per-instance render work, F2; settling-the-convention ≠ applying-it).
  - considered: include framework-internal §-cites in scope (rejected: intra-repo coupling is not the finding's cross-repo brittleness, F5).
- **D2** [OUTLINED] THE RULE (firewall) — add to `instantiation-guide.md` a citation discipline: an instance spec references the framework's method ONLY through framework glossary terms; it never cites a framework section-number (`core.md §X`, `modules.md §X`). The glossary is the instance-facing interface — it owns the term→section mapping (defines the term, points internally to the specifying section); the instance names the term, the glossary resolves it. §-coupling stays legal intra-framework (incl. inside the glossary), forbidden across the instance boundary. — basis: F1 (no rule today), F3 (glossary already maps term→section).
- **D3** [PENDING] INTERFACE COMPLETENESS — for D2 to be viable, every framework concept an instance cites must be a glossary term. Approach: enumerate the distinct framework concepts instances cite (by §-number AND binding-table row), check each against the glossary headword set, close gaps (add entries for concepts lacking them — e.g. "executable verification" + whatever the enumeration surfaces). The required-term-set is the interface-completeness target. — basis (to search-establish next cycle): F4 (binding-table binds non-glossary concepts); the cited-concept set is a completeness claim needing a corpus-wide search.
- **D4** [PENDING] ENFORCEMENT — D2 is a load-bearing rule, so per the prescription discipline (spec/README.md:97-119: load-bearing rule → structural enforcement) it needs an evidence-bearing check, not prose-only. Candidate: a render-time / CI check that an instance repo contains zero framework `§`-citations (grep-shaped, evidence-bearing). Decide form next cycle. — basis: spec/README.md:97-119 (Prescription discipline); Unenforced-rule lens (this cycle's standardized pass).

---

## Cycle 2 appends (mode switched to auto-battle)

Subagent `aa8a9e95d7b3601e9` returned the complete §-cite enumeration + glossary-gap
diff; orchestrator spot-verified the load-bearing GAP claims by located read (below).

### F-track

- **F1** [VERIFIED — addressed] no instance→framework citation rule exists → D2 adds it. — basis: D2.
- **F2** [VERIFIED — addressed] §-cite set now search-established complete (clippy spec 24 / rend 7; daneel 11 / 2; anneal-dev 73 / 7; bauleitplan 0 / 7) → scoped by D1, re-point is Phase B. — basis: D1; subagent enumeration `aa8a9e95d7b3601e9` (relayed file:line lists).
- **F3** [VERIFIED — addressed] glossary already maps term→section (71×) → D2 firewall rests on it. — basis: D2.
- **F4** [VERIFIED — addressed] binding-table binds non-glossary concepts → filed as D6. — basis: D6.
- **F5** [VERIFIED — addressed] framework-internal §-cites are intra-repo → scoped out by D1. — basis: D1.
- **F6** [VERIFIED — addressed] interface-completeness gap, spot-verified: the §-cited method gaps reduce to **2 real new headwords** — (a) "evidence-bearing-artifact rule" (§3.1; only in prose at glossary:432), (b) "post-run review" (modules §4; only in prose at glossary:361,426). "Model" §1 is NOT a new gap — it re-points to the existing **Operator** headword (role-separation principle, glossary:268). Technical binding terms (located read / construct taken whole / executable verification / problem space) confirmed NOT headwords → D2b/D6. — basis: located reads glossary:258,268 (Operator absorbs role-separation), glossary:432 (evidence-bearing only prose), glossary:361/426 (post-run only prose); `rg "**…"` → 4 binding terms NOT headwords. addressed by D3 (§-cited gaps) + D6 (binding gaps).
- **F7** [VERIFIED — addressed] bauleitplan-anneal has NO `spec/` dir (rendered-only instance) — its framework §-cites live entirely in `plugin/` → its Phase-B re-render has no spec layer to re-point. — basis: subagent enumeration (bauleitplan only `plugin/`). addressed by D1.

### D-track

- **D1** [VERIFIED] SCOPE — this run edits the framework only: `spec/glossary.md` (+2 headwords, F6), `instantiation-guide.md` (the rule + its check), `spec/README.md` (name the glossary's interface role). Per-instance §-cite re-pointing = Phase B; binding-table completion = D6. — basis: the complete §-cite enumeration (search-established, F2); instance-reinstantiation.md:47-62 (convention-prerequisite, re-point downstream).
- **D2** [VERIFIED] THE RULE (firewall) — instance specs reference the framework's method ONLY through glossary terms, never a framework §-number; glossary is the instance-facing interface (owns term→section mapping); §-coupling legal intra-framework, forbidden across the instance boundary. — basis: F1, F3.
- **D3** [VERIFIED] INTERFACE COMPLETION (D2a) — add exactly 2 glossary headwords ("evidence-bearing-artifact rule"; "post-run review"); every other §-cited concept re-points to an existing glossary term per the subagent's §→concept→term mapping (Model§1→Operator; §4.1→investigate-design; §3.2→Basis; §4.1.4→Convergence cycle; etc.). Realization (exact entry prose) at impl. — basis: F6 (spot-verified gap = 2); subagent §→concept table (`aa8a9e95d7b3601e9`).
- **D4** [VERIFIED] ENFORCEMENT — the rule carries a mechanical check: an instance repo's files contain zero framework `§`-citations (`rg '(core|modules)\.md[^\n]{0,4}§' <instance>` → empty); stated in the guide as the rule's check and run as a coherence check at render-verify. The grep output is the evidence-bearing artifact. — basis: spec/README.md:97-119; D2.
- **D5** [VERIFIED] README/GUIDE RECONCILIATION — name the glossary the instance-facing interface (additive to "definitions-only": the glossary defines the term AND points to its specifying section — already done 71×, so no conflict). — basis: spec/README.md:77-81; F3.
- **D6** [CONDITIONAL] FILE BINDING-TABLE COMPLETENESS — file the binding-table interface-completeness (the ~5-6 technical binding-table terms → glossary headwords: located read of the source, construct taken whole, exhaustive search of dependents, executable verification, an element of the work product, containers) as its OWN backlog item, informed by this run's enumeration. Committed: file-not-fold (separable per the finding's own caveat). Assumption: operator accepts the separation → [AUTO-ACCEPTED] at [READY] (auto-battle). — basis: cite-glossary-not-section-numbers.md:13-16 (the caveat); F4, F6.
  - considered: fold D2b into this run (rejected: the caveat frames it as separable "real work"; folding bloats the keystone-unblock run and is not required to re-render any instance — binding-table terms are prose, not §-cites).

---

## Cycle 3 (convergence — falsified) + Cycle 4 (re-formation) appends

Cycle-3 convergence falsification (fresh subagent `abdae88a728929cd7`) flipped D3:
D1/D2/D4/D5 hold; D3 falsified (a third §-cited gap). Cycle 4 re-forms D3 to count=3.

### F-track
- **F6** [INVALIDATED]→[PENDING] corrected: the §-cited method gaps = **3**, not 2 — the cycle-2 "spot-verified gap=2" sampled a subset (Model/post-run/evidence-bearing + binding terms) and did not iterate the full §-cited-concept set, missing §3.2. — basis: cycle-3 falsification (D3 target-dependents positive).
- **F6** [VERIFIED — addressed] (cycle 4): gap=3; addressed by re-formed D3. — basis: D3 (re-formed).
- **F8** [PENDING] (cycle 3): `modules.md §3.2` "standardized-pass findings artifact" is cited live by instance specs (clippy/spec/bindings.md:48, anneal-dev/spec/persistence.md:6, daneel/spec/bindings.md) but has NO glossary headword; siblings §3.3→"Impl plan"(glossary:343), §3.4→"Falsification pass"(:152) each have one; "Pass"(:232) defers the artifact to `modules.md §3.2` (:240-241). — basis: cycle-3 falsification artifact + orchestrator greps (headword absent; :152/:343 present).
- **F8** [VERIFIED — addressed] (cycle 4): addressed by re-formed D3 (3rd headword). — basis: D3 (re-formed).

### D-track
- **D3** [INVALIDATED] (cycle 3): "exactly 2 headwords" contradicted by F8 (a third gap). — basis: cycle-3 falsification (aggregate falsified).
- **D3** [PENDING] (cycle 3): reopened for re-formation. — basis: tracker.md Design-decision states (falsified → [INVALIDATED]→[PENDING]).
- **D3** [VERIFIED] (cycle 4, re-formed): add exactly **3** glossary headwords — (1) "evidence-bearing-artifact rule" (§3.1; → "Basis and evidence" section, glossary:47), (2) "standardized-pass findings artifact" (modules §3.2; → near "Pass" glossary:232, parallel to its §3.3/§3.4 siblings), (3) "post-run review" (modules §4; → "Triage and review classifications" section, glossary:423). Every OTHER §-cited concept re-points to an existing glossary term (Model§1→Operator; §3.3 "implementation decomposition"→Impl plan; §3.2-basis→Basis; §4.1.4→Convergence cycle; etc.). Realization (entry prose) at impl. — basis: cycle-3 falsification (the complete §-cited-concept iteration → 3 gaps); the §→concept→term mapping (subagent `aa8a9e95d7b3601e9`).

---

## [READY] (cycle 5 convergence clean) — auto-battle, proceeding to implement

- **Convergence:** cycle-5 fresh convergence CLEAN — zero D-track deltas; falsification
  `a24f45d2678d4c54c` returned D1-D5 all hold; re-formed D3 "exactly 3 gaps" survives
  completeness falsification (21 distinct cited sections, 18 covered, 3 gaps, no 4th).
- **D6** [AUTO-ACCEPTED]: the [CONDITIONAL] (file binding-table completeness separately) was
  not operator-overridden at [READY] (auto-battle) -> recorded [AUTO-ACCEPTED]; surfaced for
  the operator's post-run review. The binding-table completeness files as its own item.

### Fresh-session implementability — PASSED (per-step external evidence)

A session with only this tracker implements the locked design without a new design decision:
- **Step 1** glossary headword "evidence-bearing-artifact rule" -> target `spec/glossary.md`
  "Basis and evidence" section (glossary:47-113, no such headword today); source `core.md` §3.1.
  ext-evidence: located read glossary:47-113.
- **Step 2** glossary headword "standardized-pass findings artifact" -> near "Pass"
  (glossary:232-244, which defers the artifact to `modules.md` §3.2 at :240-241); parallel to
  siblings "Falsification pass" (:152) / "Impl plan" (:343). ext-evidence: located read glossary:232-244,152,343.
- **Step 3** glossary headword "post-run review" -> "Triage and review classifications"
  (glossary:423-446, concept used undefined at :426); source `modules.md` §4. ext-evidence: located read glossary:423-446.
- **Step 4** firewall citation rule + grep-check -> `instantiation-guide.md` §3-area
  (instantiation-guide.md:139-158, no citation rule today). Rule per D2; check per D4. ext-evidence: located read instantiation-guide.md:139-158.
- **Step 5** name glossary the instance-facing interface (reconcile definitions-only) ->
  `spec/README.md:77-81`. ext-evidence: located read README:77-81.
- **Step 6** file the binding-table-completeness backlog item (D6) -> `dev-notes/backlog/`.
- Result line: **PASSED** — each step carries an external citation; no step introduces a new
  design decision (targets, sections, 3-headword count all specified). Recorded for post-run review.

### Status confirmations (cycle-5 re-attested)
- **D1** holds · **D2** holds · **D3** holds (3 gaps) · **D4** holds · **D5** holds · **D6** [AUTO-ACCEPTED].
- F1-F8 all [VERIFIED — addressed]. No [INVALIDATED] open; no load-bearing finding below [VERIFIED].

---

## Cycle 6 — implement loopback (commit-mechanics finding) + re-[READY]

Impl unit U1 (subagent `a0249e9266d032a6f`) produced the rule-text faithfully (3 files,
+42/-0, staged; orchestrator integrity check: HEAD unmoved at 2f96c43, exactly the 3
in-scope files, additive) but HALTED on commit — surfacing two findings. The convention
design D1-D6 is unchanged; the staged rule-text is redo-inherited and audited FAITHFUL
(orchestrator review of `git diff --cached`: 3 glossary headwords definitions-only +
source-pointed; firewall rule at §3-end no-renumber; README bullet additive).

### F-track
- **F9** [VERIFIED — addressed] commit-mechanics: the repo's `commit-msg` hook IS active
  (`core.hooksPath=hooks/`) and requires a full Step-4 discharge artifact (7 checks) on
  EVERY rule-corpus commit — so a pre-verify impl-checkpoint commit (as the impl-plan/brief
  assumed) cannot be produced honestly (the discharge needs verify-phase results + operator
  approval). Subagent correctly refused `--no-verify` + refused to fabricate. — basis:
  hooks/commit-msg:38-46 (REQUIRED_CHECKS=7) + :116-124 (presence gate); git config
  core.hooksPath=hooks/. addressed by D7.
- **F10** [VERIFIED — addressed] realization-fidelity: the brief's prescribed "Post-run
  review … after verify [PASSED]" would NARROW the source — `modules.md` §4 runs the review
  "at any point during/after a run, at operator discretion". Subagent wrote source-faithful
  prose (realization is impl's authority per D3; implement.md "locked design/cited source is
  authority"). Not a design change; flagged for verify to re-check vs modules §4. — basis:
  subagent located read modules.md §4; the staged glossary "Post-run review" entry.

### D-track
- **D7** [VERIFIED] COMMIT HANDLING (this run): the rule-text is committed ONCE, post-verify,
  carrying the Step-4 discharge artifact (assembled from verify results + the kernel-independent
  review) + operator soundness sign-off; there is NO separate pre-verify impl-checkpoint commit
  for this rule-corpus run. Impl's "save" until then = the staged working tree + this tracker
  record (resume-recoverable). This is the development-process release-loop flow, not a change
  to the convention (D1-D6). D7 adds no rule-text → no new falsifiable coupling shape → the
  cycle-5 convergence over the rule-text design (D1-D6) still stands. — basis: development-process.md
  release loop (step-4 discharge) + hooks/commit-msg (the active gate); F9.

### Re-[READY] (cycle 6)
- Rule-text PRODUCED + staged + integrity-clean + audit-faithful (no re-implement needed —
  redo-inherited). Convention design D1-D6 unchanged + cycle-5-convergence-clean. D7 handles
  commit-sequencing. Fresh-session implementability still PASSED (the [READY] result line above
  holds; D7 only re-sequences the commit). Impl plan amended: U1 = produce rule-text (DONE,
  staged) → carry to verify → commit-with-discharge at release (D7), no pre-verify commit.
- Proceeding to **verify** (fresh isolated context) on the staged rule-text.

### Filed (per "file, don't defer")
- anneal-dev METHOD finding (separate from this convention): impl-phase Checkpoint
  (`phases/implement.md`) mandates a per-unit commit as the persistence reference, but the
  anneal-framework `commit-msg` hook requires a Step-4 discharge (verify-phase + operator) on
  every rule-corpus commit — so per-unit pre-verify commits are impossible for rule-corpus runs.
  → backlog item `anneal-dev-impl-checkpoint-vs-discharge-hook.md`.


---

## verify [PASSED] (isolated) — run complete; release pending operator soundness sign-off

Isolated verify subagent `a50dd0e6410b7cfab`. All three checks accounted for; battery
dispatched-and-shown. Post-verify extension: none (render-and-open-diff disabled).

```
Verify result: [PASSED] (isolated)
Finding ledger: (empty — no new findings)
```

- **Check 1 planned-vs-actual:** D1-D5 HOLD (D6/D7 not in change-set); design-completeness audit clean (no uncovered material element).
- **Check 2 lenses:** all 8 cited-clean (Bloat/Fragmentation/Leakage/Missed-dependents/Unenforced-rule/Undefined-shorthand/Lossy-render/Over-claimed-verification).
- **Check 3 battery:** (a) fidelity — 3 glossary entries faithful to sources; **F10 re-check PASSED** ("Post-run review" wording mirrors modules.md:408 "at any point during or after a run, at the operator's discretion" — NOT narrowed); (b) coherence — all cross-refs resolve, README interface bullet does not contradict definitions-only, intra-framework §-pointers legal; (c) skill-craft form self-review — invoked, clean (no Additive-reflex, definitions-only honored, firewall mechanically enforced).

### Step-4 discharge artifact (assembled for the rule-corpus commit)
- **Render fidelity** — [N/A: `git diff --cached --name-only` = 3 files, zero `plugin/skills/` render files]
- **Practice-4 dependent audit** — [a50dd0e6410b7cfab, clean: additive-only, no rule changed/removed; instance §-cites are Phase-B re-point targets enumerated in D1/F2]
- **Skill-craft full review on changed skill files** — [N/A: zero skill files in change-set (no `plugin/skills/`)]
- **Skill-craft self-review on framework-spec section** — [a50dd0e6410b7cfab, clean: form/discipline review via skill-craft on glossary+README+guide additions]
- **Skill-craft self-review on commits to skill-craft canonical files** — [N/A: zero skill-craft canonical files in change-set]
- **Practice-6 whole-document coherence** — [a50dd0e6410b7cfab, clean]
- **Cross-spec multi-file coherence** — [a50dd0e6410b7cfab, clean: glossary↔guide↔README↔core/modules sources resolve]
- **Spec-origin trace** — [N/A: zero instance plugin-render files in change-set]
- **Operator soundness sign-off (kernel-independent, development-process.md)** — PENDING (the human half; FORM half discharged above via skill-craft).

### Run outcome
- anneal-dev run: **PASSED** (interactive cycles 1-2 → auto-battle cycles 3-6 → verify PASSED).
- Rule-text: staged (3 files, +42/-0), NOT yet committed — awaits operator soundness sign-off + the discharge commit (D7).
- [AUTO-ACCEPTED]: D6 (file binding-table completeness separately — filed: `dev-notes/backlog/glossary-binding-table-interface-completeness` pending; see note). Surfaced for post-run review.
- Filed: `dev-notes/backlog/anneal-dev-impl-checkpoint-vs-discharge-hook.md` (F9/D7 method finding).
