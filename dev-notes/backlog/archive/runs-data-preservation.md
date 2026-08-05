# Run-state preservation — track the run-state slot instead of gitignoring it

**Status:** [PARTIAL] DECIDED 2026-06-06 (simple path) — framework formalization pending. Resolved
through a multi-step operator discussion during the `v-entry-is-post-ship-only` run: **track
the run-state slot in place; do NOT gitignore it** (default-on). No archive folder, no
lifecycle extension, no relocation — see "SIMPLEST approach" below (the decided answer). It is
a **framework policy on the run-state-directory slot, for ALL instances** (`.anneal-dev/` is
anneal-dev's binding; each instance binds its own).
- **This-repo behavior APPLIED 2026-06-06:** `.gitignore` changed from `.anneal-dev/` to just
  `.anneal-dev/allow-adhoc-kernel-edit`; `.anneal-dev/runs/` now tracked; the provisional
  `dev-notes/run-history/` copy removed.
- **Remaining = the framework formalization:** change the First-run bootstrap so the run-state
  slot defaults to tracked (`foundation.md` / `anneal-dev/SKILL.md`), rendered to all instances
  → its own anneal-dev cycle (kernel-adjacent; kernel-independent verify).
- The lifecycle-extension + archive-folder framing below is **superseded** (kept as the
  heavier-alternative reasoning trail — the path NOT taken, and why).

## SIMPLEST approach — track the run-state slot in place (DECIDED 2026-06-06)
**Scope (operator-corrected): this is a framework policy on the run-state-directory SLOT, for
ALL instances** — `.anneal-dev/` is just anneal-dev's binding of that slot (`foundation.md`
"instance-bound location"); clippy/daneel/etc. each bind their own. The decision is rendered per
instance, not a this-repo path choice.

On reflection (operator: "why move them instead of just not gitignoring it? and why gitignore
anything at all?"), the **extension + separate archive folder below is over-built, and so is
'gitignore the transient bits.'** The minimal, sound answer:
- **Track the run-state slot in place. Gitignore nothing of it.** Commit completed runs via
  normal git flow. No lifecycle extension, no copy-on-close, no archive folder, no naming.
- **Why faithful, not just simple:** `foundation.md` already calls the run-state dir *"the
  project's accumulated anneal-dev history; nothing is overwritten."* The framework already
  homes history there — tracking just stops *hiding* it. The current bootstrap's wholesale
  gitignore of the slot is the thing to change.
- **Default on/off** = whether the bootstrap gitignores the slot (on = tracked). Lean ON (the
  recoverable-vs-unrecoverable asymmetry above).
- **"Don't commit into a dotdir" dissolves:** `.github/` is the precedent.
- **Local override-flags are the ONE real gitignore — and they're not framework run-state.**
  This repo's `.anneal-dev/allow-adhoc-kernel-edit` is the run-gate hook's bypass: a *local
  override* (one dev's momentary "allow ad-hoc kernel edits"), gitignored like `.env` —
  committing it imposes one person's bypass on every checkout. But that marker belongs to this
  repo's self-hosting run-gate hook; a downstream instance has no such hook. So override-flags
  are a **separate, local, per-instance concern**, NOT part of the framework run-state policy.
- **Residuals (minor):** an in-progress tracker shows modified during a run (commit on close);
  prior-trackers-aren't-basis is unchanged (physical presence is gitignore-independent;
  `verify.md` rule handles it); the slot grows unbounded as tracked history (intended).

**This SUPERSEDES the lifecycle-extension + archive-folder framing below** (kept as the heavier
alternative + reasoning trail). If ratified: the framework bootstrap stops gitignoring the
run-state slot (default-on); for THIS repo now, remove the `dev-notes/run-history/` provisional
copy, un-gitignore `.anneal-dev/runs/`, and `git add` it; keep a local gitignore only for the
`allow-adhoc-kernel-edit` override-flag.

## Framework formalization — IN-FLIGHT 2026-06-06 (run `run-state-tracked-by-default`)
The framework bootstrap change is being done now (not a later cycle) — anneal-dev run
`run-state-tracked-by-default` edits `instantiation-guide.md` §5 + `persistence.md` +
`bindings.md` + `core.md` §4.2.4 (run-state tracked by default; per-instance binding per D3; the
in-place integrity check + restore + separate-copy integration exclude the run-state dir on the
work-product-vs-bookkeeping boundary). Verify + commit pending.

**Follow-up surfaced (NOT actioned this run — `F-prov-framing`):** four framework provisioning
sites still read "non-tracked run-inputs" / "not part of the tracked work product" —
`spec/core.md:734`/`:736`, `instantiation-guide.md:107`, `anneal-dev/spec/bindings.md:129`. Under
tracked run-state "non-tracked" is now **mildly misleading** (run-state IS git-tracked), but the
rule **stays true** (run-state isn't *work-product*) → surfaced-not-actioned per the
requirements-anchor brake (R4 doesn't fail). A small terminology cleanup ("run-inputs outside the
tracked work product") — do as a quick follow-up spec edit (or fold into the next kernel touch);
NOT worth a loopback. Consistency note: the prior convergence corrections in that run fixed the
same staleness class on sibling sites, so Pareto-consistency favors the cleanup eventually.

## Framework framing (the heavier alternative — lifecycle extension; superseded by the above unless the extra separation is wanted)
This is **not** a path this repo picks; it's a framework affordance defined in anneal and
rendered to every instance. Clean fit with the **existing lifecycle-extension mechanism**
(`SKILL.md` Post-verify extensions; `anneal-dev.config/extensions.enabled`):
- **Mechanism:** an `archive-run` **lifecycle extension** firing `on-verify-PASSED` — sibling
  to `render-and-open-diff`, same capability boundary (writes a non-spec output path, no
  run-completion blocking, no tracker modification). It copies the completed run's tracker +
  per-cycle artifacts to the standard location.
- **Per-instance toggle** (`extensions.enabled`) makes it general (any instance can
  enable/disable), so it is NOT self-hosting-only. **Default on-vs-off is an OPEN sub-decision**
  (operator-raised 2026-06-06) — and the lean is **ON**, on an **asymmetry** argument:
  default-on-but-unwanted is *recoverable* (gitignore/delete the archive path, once);
  default-off-but-wanted is *unrecoverable* (the run is gone — the exact loss that prompted
  this item). Fail the default toward the recoverable side. Plus **discoverability** — an
  off-by-default toggle is effectively never found, so off ≈ feature-dead. On is **benign if
  write-not-commit** (like `render-and-open-diff`: artifacts land in a visible tracked path,
  normal git flow preserves them, no auto-commit). **Counter (the real cost):** per-run
  **working-tree intrusion** — a downstream dev sees archive files in `git status` after every
  run; minor + self-correctable, but real. Net lean: **default ON, write-not-commit**; settle
  in the cycle.
- **Standard location** is **framework-defined** (so every enabling instance archives
  consistently). The sub-decision — a committed `.anneal-dev/` subdir (gitignore
  `.anneal-dev/runs/` specifically, commit `.anneal-dev/archive/`) **vs** a standard
  committed top-level the bootstrap creates — is a **design fork for this cycle, with the
  operator**. NOT pinned ad-hoc.
- **This run's archive** at `dev-notes/run-history/v-entry-is-post-ship-only/` (commit 1) is a
  **PROVISIONAL placeholder** — it preserved the history (the immediate concern) but is not
  the standard; relocate to the framework-standard path when this cycle lands.

→ a framework anneal-dev cycle: extension declaration (anneal spec) + bootstrap/gitignore
change + the standard-location fork + render to instances; kernel-independent verify.

## The tension
anneal-dev gitignores `.anneal-dev/` as **runtime state** (the bootstrap adds it to
`.gitignore`; `foundations.md` "Operator-editable artifacts" + verify.md "Prior-run
trackers are not basis material"). The run tracker + per-cycle falsification/standardized
artifacts live there. Rationale (sound for the downstream case): a project *using*
anneal-dev doesn't want anneal's run trackers cluttering its repo or polluting future runs.

**But for self-hosting** (anneal-framework developing itself), the runs ARE valuable
**methodology-development history** — the empirical record of how the method behaves. They
are lost the moment they're gitignored: local-only, machine-bound, gone on a fresh clone.

## Evidence (this run)
`v-entry-is-post-ship-only` is a rich case study in convergence churn (D2 reworked 4×,
D4 dropped at implement, the gold-plating across cycles 4–8). The **best evidence of how
that happened** — the tracker + `.cycle-4/6/8.intent-falsification.md` — is gitignored →
will not survive in the repo. Only the **distillation** (the cycle-4→8 table in
`convergence-surfaced-finding-action-brake.md`, the `proportional-cycle-weight` datapoint)
is committed. The essentials survive; the exhaustive ledger does not. The operator judged
this loss not acceptable for the self-hosting repo.

## The asymmetry (why a blanket policy is wrong)
- **Downstream project** — runs = disposable runtime state; gitignore is correct (clean
  repo, no pollution).
- **Self-hosting (this repo)** — runs = methodology history; gitignore loses it.

A single blanket gitignore can't serve both. This is a **self-hosting-only** policy
question, like the live-spec-governs rule in `CLAUDE.md`.

## Options (operator fork — decide before any cycle)
- **(a) Self-hosting exception** — un-gitignore `.anneal-dev/runs/` in *this* repo only;
  commit completed trackers as history. Simplest; but commits live runtime state
  (incl. in-progress trackers, the `allow-adhoc` marker) → noise + the pollution hazard
  below.
- **(b) Run-archival on close (recommended seed)** — on verify [PASSED], distill/move the
  completed run's tracker + pass artifacts to a **committed** `dev-notes/run-history/<run>/`
  (curated, read-only history), leaving `.anneal-dev/runs/` gitignored for live state. A
  clean separation: live runtime gitignored; closed-run history committed. Mirrors how
  backlog `archive/` preserves shipped items.
- **(c) Status quo** — distill only the lessons to the backlog (current). Rejected by the
  operator's note (loses the blow-by-blow).

## The pollution hazard (constrains the fix)
verify.md: "**Prior-run trackers are not basis material**; the current tracker must carry
re-grounded basis." So whatever is preserved must be **inert to future runs** — history a
human reads, NOT a source a future run's verify/investigation treats as basis. Option (b)
(a distinct `run-history/` path, not `.anneal-dev/runs/`) keeps it inert by location;
option (a) risks a future run scanning a committed prior tracker as if live. This argues
**(b) over (a)**.

## Relates to
- `CLAUDE.md` "Session continuity — repo, not auto-memory" — the same principle (durable
  state in the repo, not opaque runtime) — currently the runs data violates it by living in
  gitignored `.anneal-dev/`. This item extends that principle to run history.
- `convergence-surfaced-finding-action-brake` — the run whose lost tracker prompted this; its
  committed cycle-table is the current (lossy) distillation.
- `proportional-cycle-weight` + `post-run-review-nonsensical-cycle-probe` — preserved run
  history is the **input** those analyses (and any cross-run method study) read.
- `anneal-reliability-measurement` — cross-run history is the measurement substrate.
- Origin: `v-entry-is-post-ship-only` run, operator note 2026-06-06.
