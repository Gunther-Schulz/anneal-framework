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
(`lens-set.md`), and the **run-artifact persistence mechanism**
(`persistence.md`).

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
| a verified outcome | a rule-text edit whose render-fidelity, coherence, and skill-quality checks are dispatched-and-run clean and whose diff the operator approves |
| the problem space | the rule-corpus — a multi-repo body where rules encode contracts, cross-reference each other, and are RENDERED into shippable plugins |
| the work; producing the work | rule-text — the prose and structure of spec/skill files; editing that prose and structure |
| existing work | the rule-corpus as it currently stands — the prose, the structure, and the rendered plugins as currently shipped |
| an element of the work product | a rule (a load-bearing clause), a defined term, a section, a file, or a rendered plugin clause |
| scope — the elements the work will modify | the set of spots encoding the contract being changed, across the whole corpus — every file/section/clause that states, cross-references, depends on, or RENDERS the contract |
| exhaustive search of an element's dependents | a wrap-tolerant text search (grep) across the whole corpus for every spot encoding or cross-referencing the contract — distinctive single tokens, or newline-flattened input, because prose wraps across lines and a multi-word pattern can split |
| a located read of the source | a file:line read of the rule-text — the clause read to its visible close (the full sentence/paragraph/section the rule lives in, not a fragment) |
| a construct taken whole | a rule read to its visible close: the complete clause, the defining sentence of a term, the full enumeration of a closed set, or — for an amendment — the rule plus the cross-references that bind to it |
| the domain's executable verification | the dispatched-and-run check battery: (a) **render-fidelity** — the rendered plugin checked clause-by-clause against its source spec in a SEPARATE context; (b) **coherence** — whole-document, cross-file, and whole-corpus set-level inspection; (c) a **skill-quality review** of changed skill files; (d) **operator approval** of the resulting diff (see Verification battery below) |
| the standardized lens set | the corpus-evolution lens set (`lens-set.md`) |

Record only the values that bind framework terms to
corpus-evolution. Free-form rationale lives in
`derivation-rationale.md`, not in the table.

---

## Verification battery — what `verify` runs and shows

The framework's `verify` (`anneal-framework/spec/core.md` §4.3)
runs the domain's executable verification and shows its output;
"executable" means these checks are **dispatched/run, not
asserted**. anneal-dev's battery has four checks. Each is the
binding-row "executable verification" elaborated; this section is
a binding refinement, not a lifecycle extension
(`instantiation-guide.md` §5 binding-refinement-vs-extension test —
this refines the verification row of §3's table).

1. **Render-fidelity (separate-context).** For every changed rule
   that is rendered into a plugin, the rendered clause is checked
   **clause-by-clause against its source spec** in a context
   isolated from the one that wrote the render. This is mandatory
   isolation, not a per-task judgment: the renderer is blind to
   its own paraphrase-flattening (`foundation.md` contract 2 —
   "The renderer is blind to its own flattening"). The check
   confirms structural mechanisms survive as structural — closed
   enums stay enumerated, "must" stays "must" (not softened to
   "should"), no load-bearing clause silently dropped. This is
   the same isolation the framework already requires of verify
   (`core.md` §4.3); render-fidelity is the corpus-evolution
   content of that isolated pass.

2. **Coherence.** Whole-document, cross-file, and whole-corpus
   set-level inspection: every cross-reference resolves, no
   principle is restated-and-drifted across files, no closed set
   has a member stated in one place and missing in another, the
   changed rule reads coherently against the documents it lives
   among.

3. **Skill-quality review.** Each changed skill file (the rendered
   plugin skills) is reviewed against the skill-design canonical
   guidance — the full canonical sweep for the changed files.

4. **Operator approval of the diff.** The resulting rule-text diff
   is presented for the operator's approval. This is the
   consumer-observable terminal: the operator approving the diff
   is the domain's analogue of a passing test run.

A check is "run" only when it is dispatched and its output shown
(checks 1–3) or the approval recorded (check 4). A "verified" claim
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

## Dispatch subagent isolation — corpus-evolution binding

The framework (`core.md` §4.2) isolates a **parallel-eligible**
impl unit in a per-unit git worktree and runs a
**sequential/single** unit against the operator's main tree under an
integrity check. anneal-dev binds the worktree slots:

- **Multi-repo caveat (a strain — see `derivation-rationale.md`):**
  the corpus is multi-repo (framework spec, skill-craft canonical,
  per-domain instance repos). The framework's worktree isolation is
  written per single git tree. anneal-dev binds the worktree to the
  **repo a unit's edits land in**; a unit whose listed scope spans
  more than one repo is **sequential by default** (its disjointness
  cannot be established within one worktree) and runs against the
  operator's main tree under the integrity check, one repo at a
  time. Cross-repo parallel-eligibility is recorded as a strain, not
  resolved here.
- **Worktree path convention:** `/tmp/anneal-dev-wt-<run-id>-<unit-id>`
  (top-level `/tmp/`, outside the operator's repository tree).
- **Branch convention:** `anneal-dev/<run-id>/<unit-id>`.
- **Worktree creation:** `git worktree add /tmp/anneal-dev-wt-<run-id>-<unit-id> -b anneal-dev/<run-id>/<unit-id> <head-commit>`.
- **Remote stripping:** after creation, `git -C <wt> remote remove origin`
  (and other declared remotes).
- **Brief paths:** cwd-relative only; never the operator's main
  absolute path.
- **HEAD snapshot:** `git -C <operator-main> rev-parse HEAD` before
  dispatch, re-checked after; mismatch → halt + surface.
- **Integration:** `git -C <operator-main> cherry-pick <worktree-commit-sha>`
  after self-check passes and HEAD verification confirms clean.
- **Run-state provisioning:** `.anneal-dev/` is gitignored, so
  `git worktree add` does not carry run state in. Before dispatch
  the orchestrator copies `.anneal-dev/runs/` into the worktree; the
  copy is untracked there and never enters the cherry-pick.

For a **sequential/single** unit (main-tree path, no worktree) the
subagent runs in the operator's main repository — reading
`.anneal-dev/runs/` natively. Pre-dispatch: `git status --porcelain`
clean (else halt + surface) + `git rev-parse HEAD` snapshot. Post:
HEAD advanced by exactly the unit's commit with a clean tree.
Mismatch → `git reset --hard <snap>` + `git clean -fd`, then halt +
surface.

**Self-check lenses (write-time).** The framework
(`core.md` §4.2, `modules.md` §2.2) has the dispatched impl subagent
apply the standardized lenses most relevant to write-time issues to
its own diff before returning state. For anneal-dev these are:
**Lossy-render**, **Missed-dependents**, **Undefined-shorthand**,
and **Over-claimed-verification** (a write-time edit can introduce a
softened render, an unaccounted dependent, a new undefined term, or
an over-claim in the rule-text itself). Selected because each fires
on what an edit *introduces* into the diff; Bloat / Fragmentation /
Leakage / Unenforced-rule are cycle-level coherence lenses better
applied against the whole document at verify, not the unit diff.

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
