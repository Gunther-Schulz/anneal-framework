# anneal-dev Specification — Bindings

anneal-dev is the Anneal framework instantiated for
**corpus-evolution** — the work of evolving a *rule-corpus*: the
body of spec-and-skill files that define an AI methodology and its
tools. The framework's method — the model, the mechanisms, the
grounding discipline, phase specs, and the status-state machine —
is specified in the `anneal-framework` repo (`spec/`). That spec is
domain-general; this document binds it to the corpus-evolution
domain.

anneal-dev adds nothing to the framework's method. It supplies the
things the framework leaves to the instance: the corpus-evolution
**bindings** below, the corpus-evolution **standardized lens set**
(`lens-set.md`), the **run-artifact persistence mechanism**
(`persistence.md`), and the **isolation slot** binding (below).

A note on terms: in this domain "corpus" is the multi-repo body of
rule-text — a domain-general methodology spec, skill-design
canonical guidance, per-domain instance specs, and the plugin skill
files those specs are RENDERED (paraphrased) into. A rule-corpus
edit changes prose and structure, not code.

---

## Bindings

Each domain-general term in the framework spec takes its
corpus-evolution value:

| Framework term | anneal-dev binding |
|---|---|
| the task | a corpus-evolution task — a change to the rules a corpus encodes (sharpen a rule, consolidate a fragmented principle, add a lens, re-render a softened clause) |
| a verified outcome | a rule-text edit whose render-fidelity, coherence, and skill-quality checks are dispatched-and-run clean (verify [PASSED]); the operator's diff-approval is the downstream §1(a) / commit gate, not part of verify |
| the problem space | the rule-corpus — a multi-repo body where rules encode contracts, cross-reference each other, and are RENDERED into shippable plugins |
| the work; producing the work | rule-text — the prose and structure of spec/skill files; editing that prose and structure |
| existing work | the rule-corpus as it currently stands — the prose, the structure, and the rendered plugins as currently shipped |
| an element of the work product | a rule (a load-bearing clause), a defined term, a section, a file, or a rendered plugin clause |
| the work product's **containers** (`core.md` §4.2, `glossary.md` Work product) | the corpus's **repositories** — each git repo (framework spec, skill-craft canonical, a per-domain instance repo) is one independently-isolable container; a unit's touched containers are the repos its edits land in |
| scope — the elements the work will modify | the set of spots encoding the contract being changed, across the whole corpus — every file/section/clause that states, cross-references, depends on, or RENDERS the contract |
| exhaustive search of an element's dependents | a **wrap-tolerant** text search across the whole corpus for every spot encoding or cross-referencing the contract — distinctive single tokens, or newline-flattened input, because prose wraps across lines and a multi-word pattern can split mid-match (the corpus-evolution binding of the framework's `search`, `core.md` §3.2) |
| a located read of the source (`core.md` §3.2) | a located read of the rule-text — the clause read to its visible close (the full sentence/paragraph/section the rule lives in, not a fragment), paired with one observable fact (a count, an enumerated member, the cited identifier) |
| a construct taken whole (`core.md` §3.2 true-unit basis) | a rule read to its visible close: the complete clause, the defining sentence of a term, the full enumeration of a closed set, or — for an amendment — the rule plus the cross-references that bind to it. The visible close of a prose construct is the syntactic close of the rule-bearing unit: the sentence's terminal punctuation, the paragraph's blank-line boundary, the section's next-heading boundary, or a closed set's final enumerated member |
| the domain's executable verification | the dispatched-and-run check battery (three checks): (a) **render-fidelity** — the rendered plugin checked clause-by-clause against its source spec in a SEPARATE context; (b) **coherence** — whole-document, cross-file, and whole-corpus set-level inspection; (c) a **skill-quality review** of changed skill files (see Verification battery below). Operator diff-approval is **not** a battery check — verify runs isolated from the operator; it is the §1(a) presentation / commit gate, downstream of [PASSED] |
| the standardized lens set | the corpus-evolution lens set (`lens-set.md`) |

Record only the values that bind framework terms to
corpus-evolution. Free-form rationale lives in
`derivation-rationale.md`, not in the table.

---

## Verification battery — what `verify` runs and shows

The framework's `verify` (`anneal-framework/spec/core.md` §4.3)
runs the domain's executable verification and shows its output;
"executable" means these checks are **dispatched/run, not
asserted**. anneal-dev's battery has three dispatched checks. Each is
the binding-row "executable verification" elaborated; this section is
a binding refinement, not a lifecycle extension
(`instantiation-guide.md` §5 binding-refinement-vs-extension test —
this refines the verification row of §3's table).

1. **Render-fidelity (separate-context).** For every changed rule
   that is rendered into a plugin, the rendered clause is checked
   **clause-by-clause against its source spec** in a context
   isolated from the one that wrote the render. This inherits
   verify's framework-mandated isolation (`core.md` §4.3): verify
   as a whole runs in a context separate from the one that
   produced the work, so the render-fidelity check is conducted
   by a context that did not write the render. The check confirms
   structural mechanisms survive as structural — closed enums
   stay enumerated, "must" stays "must" (not softened to
   "should"), no load-bearing clause silently dropped. This is
   the corpus-evolution content of verify's isolated pass; the
   isolation is framework-supplied, not instance-invented
   (`foundation.md` contract 2 — "The renderer is blind to its own
   flattening").

2. **Coherence.** Whole-document, cross-file, and whole-corpus
   set-level inspection: every cross-reference resolves, no
   principle is restated-and-drifted across files, no closed set
   has a member stated in one place and missing in another, the
   changed rule reads coherently against the documents it lives
   among.

3. **Skill-quality review.** Each changed skill file (the rendered
   plugin skills) is reviewed against the skill-design canonical
   guidance — the full canonical sweep for the changed files.

**Operator approval is not a battery check.** verify runs **isolated
from the operator** (`core.md` §4.3), so it cannot run an operator
action. The resulting rule-text diff is approved by the operator at
verify's presentation — the §1(a) menu-selection (`core.md` §1) /
release-loop commit gate — **downstream** of verify's [PASSED]. It is
the domain's analogue of shipping a green build, not a check the
isolated verify context runs.

A check is "run" only when it is dispatched and its output shown
(checks 1–3). A "verified" claim
that asserts more than was actually dispatched-and-shown is the
over-claimed-verification failure shape the lens set watches
(`lens-set.md`); the battery closes it by making each check an
artifact the isolated verify context produces, not a claim the
working context makes.

**De-prioritization** of a non-failure check output requires an
artifact (`core.md` §4.3): a config entry or a tracker entry naming
the output class + reason. De-prioritization without an artifact is
the silent-substitution shape.

**Behavior-preserving classification** (`core.md` §4.3 delta-vs-fresh
re-verify): a rule-text fix is **behavior-preserving** when it does
not change which rules the corpus encodes nor what any rendered
plugin clause prescribes — e.g., a pure copy-edit, a basis-only
strengthening, a wording tightening that preserves every "must" and
every closed-set member. A fix that adds/removes/re-strengthens a
rule, or that re-renders a clause whose prescription changes, is
**not** behavior-preserving and triggers a fresh verify pass.
Un-classified defaults to fresh.

---

## Isolation slot — corpus-evolution binding

The framework's impl-phase isolation (`core.md` §4.2) requires the
instance to bind the **isolation slot**: copy creation, the unit
identifier, escape-resistance, the state marker the integrity check
reads, the restore mechanism, and which non-tracked run-inputs are
provisioned. The work product is **multi-container** — each
container is checked independently against the state marker
(`core.md` §4.2 Integrity check). anneal-dev's containers are the
corpus's **repositories** (the bindings table); a dispatch unit
touches one or more repos, and each touched repo is one container.

- **Container ↔ repository.** Each git repository the corpus spans
  (framework spec, skill-craft canonical, per-domain instance
  repos) is one independently-isolable container. A unit whose
  listed scope spans more than one repo touches more than one
  container; the integrity check runs per touched container
  (`core.md` §4.2). Parallel-eligibility is established by the
  framework's disjointness rule unchanged: a unit is
  parallel-eligible when its listed element and contract scopes —
  and so its touched containers — are disjoint from every
  in-flight unit's, search-established (`modules.md` §3.3). A
  multi-repo unit is not sequential *because* it spans repos; it is
  sequential only if its scope is not search-established disjoint
  from an in-flight unit's, exactly as the framework specifies for
  any unit.

- **Separate copy (parallel-eligible units).** For each touched
  container, a separate copy of that repo at the unit's base
  commit, created outside the operator's repository tree.
  - **Copy path convention:** `/tmp/anneal-dev-copy-<run-id>-<unit-id>-<container>`
    (top-level `/tmp/`, outside any operator repo tree).
  - **Branch convention:** `anneal-dev/<run-id>/<unit-id>`.
  - **Escape-resistance:** after copy creation, declared remotes
    are stripped from the copy, and the subagent's brief carries
    cwd-relative paths only — never an operator repo's absolute
    path — so a defensive traversal cannot reach the operator's
    work product (`core.md` §4.2 escape-resistant).

- **Unit identifier.** `anneal-dev/<run-id>/<unit-id>` — the branch
  name, which the operator can audit and which scopes the unit's
  recorded changes.

- **State marker.** Per touched container, the repository's HEAD
  commit: snapshotted before dispatch, re-read after. The
  integrity check (`core.md` §4.2) reads this marker per container.
  - **Isolated (parallel-eligible) units:** each touched
    container's HEAD is confirmed **unchanged** across the unit's
    work (the unit worked on its separate copy). A changed HEAD
    means the unit escaped isolation — halt and surface, no
    auto-restore (cause uncertain, `core.md` §4.2).
  - **In-place (sequential/single) units:** each touched container
    confirmed **clean before dispatch** (else refuse and surface),
    HEAD snapshotted, and after return confirmed advanced by
    **exactly the unit's intended change** and no other
    modification. On mismatch, **restore** the pre-dispatch state
    (discard the subagent's writes) and halt and surface.

- **Restore mechanism.** Reset the touched container to its
  snapshotted HEAD and discard uncommitted changes, returning the
  repo to its pre-dispatch state (`core.md` §4.2 in-place
  mismatch path).

- **Provisioning.** Run-inputs a dispatched unit reads that are not
  part of the tracked work product — the run-state directory
  `.anneal-dev/runs/` (`persistence.md`), which is gitignored and so
  not carried by a copy — are provisioned into the separate copy
  before dispatch and excluded from integration (`core.md` §4.2
  Provisioning). Project bootstrap (what a repo needs merely to be
  runnable) stays out of scope. For an in-place unit, the subagent
  reads run state and the runnable environment natively from the
  operator's repo (no provisioning, `core.md` §4.2).

- **Integration.** After the unit's changes are verified clean
  (self-check passed and the integrity check confirms no
  contamination), the orchestrator integrates **only the unit's
  changes** into the operator's work product, per touched
  container — no copy-side metadata crosses over (`core.md` §4.2
  Integration).

**Spawn-fallback** (`core.md` §4.2, `glossary.md` Spawn-fallback):
if a separate copy or isolated subagent cannot be established, the
unit is implemented in the working context and surfaces "without
isolation"; the isolation guarantee is waived, never silently
taken as independent.

**Self-check lenses (write-time).** The framework
(`core.md` §4.2, `modules.md` §2.2) has the dispatched impl subagent
apply the standardized lenses most relevant to write-time issues to
its own change-set before returning state. For anneal-dev these are:
**Lossy-render**, **Missed-dependents**, **Undefined-shorthand**,
and **Over-claimed-verification** (a write-time edit can introduce a
softened render, an unaccounted dependent, a new undefined term, or
an over-claim in the rule-text itself). Selected because each fires
on what an edit *introduces* into the change-set; Bloat /
Fragmentation / Leakage / Unenforced-rule are cycle-level coherence
lenses better applied against the whole document at verify, not the
unit change-set. The **change-set-vs-listed-scope check**
(`core.md` §4.2) also applies: change-set-referenced identifiers ∖
listed scope = ∅; an out-of-scope reference is an actioned finding.

## Operator-editable artifacts

Per `instantiation-guide.md` §5 filesystem-layout rule,
operator-editable artifacts live at `anneal-dev.config/` (committed),
distinct from `.anneal-dev/runs/` (gitignored runtime state — see
`persistence.md`). The operator-editable set:

- `lenses.md` — lens-supplement mechanism (per `lens-supplement.md`)
- `extensions.enabled` — extension enable file (per `extensions.md`)
- `README.md` — operator-facing explainer

**First-run bootstrap.** On first run in a project, anneal-dev adds
`.anneal-dev/` to the repo's `.gitignore` (creating it if absent)
and bootstraps `anneal-dev.config/` with the placeholder files
above, each per `instantiation-guide.md` §5 Placeholder content
style.
