# Worktree isolation + integration — merge-tree-gated integration, reflink cache provisioning, escape-theater cut

**Status:** OPEN — **substantially reframed + de-risked 2026-06-07** (operator-driven
git/filesystem-capabilities research). Was: a 4-part finding (cross-session clippy run, 2026-06-02),
campaign ④a **fork-first** (gated on a cache architectural decision). Now: **the fork-first gate
dissolves** — (b) was misdiagnosed, (a) is already rendered, (c) folds into the gate, and **(d) is
SOLVED with proven cache machinery** (not moot — resolved; see below), not an open architectural
decision. **Two orthogonal axes were resolved this session:** integration robustness (the merge-tree
gate) and test-cache provisioning (the reflink-auto private-copy ladder). Residue is a clean
**gated-kernel** design — a *smaller, more robust* parallel path than today's. **Parallel fan-out is
real in practice (operator-confirmed)** — so the job is to harden the parallel path, not drop it.

## RESOLUTION (2026-06-07) — the robust, standards-conform design

The whole parallel-isolation apparatus was reaching for one thing — *land each unit's work onto
main completely, or fail loud, never silently* — by hand-rolling diff checks. Git already has the
primitive. The design below is **more robust and fewer moving parts** than the current render + the
originally-proposed (b) landing-check.

**1. Isolation — keep `git worktree`.** It's the right primitive (already rendered, see (a)).
Worktree from operator's `main`-HEAD-at-dispatch.

**2. Integration — serialized + gated, never conflict-suppressed.** As each unit returns, integrate
one at a time onto current main:
- **Gate:** `git merge-tree --write-tree <main> <unit-branch>` — an in-memory **real 3-way merge**
  against the true common ancestor, touching nothing. Exit contract (man page, git ≥2.38): **0 =
  clean, 1 = conflict, else = error.** Exit 1 → **HALT loud + surface** (the disjointness claim was
  violated → this unit should have been sequential). Exit ≥2 → error, halt.
- **Apply (only on exit 0):** `git merge --ff-only` (or `--no-ff`). **Never `-X ours/theirs`; never
  cherry-pick a commit range.** Disjoint changes land completely *by construction*.
- **Old-git (<2.38) fallback** — same robustness, any git: a real trial-merge into a throwaway
  worktree/index — `git merge --no-ff --no-commit`, inspect for conflict, `git merge --abort`. The
  gate is the *pattern*; merge-tree is just the zero-touch implementation.

**3. Upstream guard — scope-conformance.** `git show <sha> --stat` ⊆ the unit's declared file scope,
*before* the gate. Catches the other root (a subagent writing outside its declared scope) cheaply,
and reinforces the disjointness basis (`implement.md:49-53`).

### Empirical autopsy (this session — direct runs, git 2.54.0; scripts `/tmp/git-integration-probe.sh`, `/tmp/git-probe2.sh`)

9-cell battery (disjoint / far-apart / adjacent-insert / same-line / identical / delete-modify /
**stale-base** / **stale+overlap** / stale+context-shift):

- **Plain `cherry-pick` and `merge` NEVER silently drop.** Disjoint lands **COMPLETE** — *even across a
  stale base* (S5, S9). Every real overlap fails **LOUD conflict** (S3/S4/S6/S7/S8). The "silent hunk-drop"
  is **not** an inherent cherry-pick hazard.
- **The silent drop reproduces ONLY under a conflict-suppressing strategy:** `git merge -X ours u2` over a
  conflicting change → **exit 0, the change silently gone**. → **this is the actual mechanism of the
  2026-06-02 incident** (a `-X ours/theirs`-style auto-resolve, or genuinely-overlapping units that should
  have been sequential) — *not* a reason to bolt on a landing-check.
- **`git merge-tree --write-tree` predicted clean-vs-conflict correctly in all 9 cells**, zero-touch. It *is*
  the robustness primitive.

## Per-issue disposition

### (a) Escape to operator's main — **DONE (already rendered) + one Pareto cut**
Clippy already renders the path-relocation fix (`coding-clippy/.../phases/implement.md:102-122`):
worktree at `/tmp/clippy-wt-<run-id>-<unit-id>` (top-level, defensive `cd ../..` lands in `/tmp`),
branch `clippy/<run-id>/<unit-id>`, remote-strip, cwd-relative briefs, **pre/post HEAD verification**,
cherry-pick integration. Framework carries it as the escape-resistance guarantee (`spec/core.md:736-738`).
- **Cut (Pareto):** drop `git remote remove origin` + the **cwd-relative-brief soft rule**. The pre/post
  HEAD verification (`implement.md:115-118`) is the *actual* contamination guarantee — it catches an escape
  loudly regardless. Those two are belt-and-suspenders against a failure the hard check already catches; the
  soft path-rule is itself the brittlest piece (an agent can just violate it).

### (b) "Cherry-pick silent hunk-drop" — **MISDIAGNOSED → SOLVED by the gate**
Not inherent to cherry-pick (see autopsy). Roots are: (i) a conflict-suppressing `-X` strategy, or
(ii) a **false disjointness claim / scope violation** (units that overlapped but ran concurrent).
**Fix = the merge-tree gate (loud by construction) + scope-conformance + never `-X`** — replaces the
originally-proposed per-unit post-integration acceptance-re-pass, which was heavier *and* would have
dragged back suite-execution + the (d) cache question to defend a self-inflicted wound.

### (c) Stale-base worktree — **FOLDS INTO THE GATE**
Stale base + disjoint edits integrates cleanly (S5, S9); stale base + overlap is caught by the gate
(S7). Clippy already pins the worktree base to `<head-commit> = operator main HEAD at dispatch`
(`implement.md:107-108`). Residual harness fail-loud `worktree base == main HEAD` check is belt-and-
suspenders on top of the gate — low priority.

### (d) Test-execution deps in the isolated copy — **RESOLVED (proven cache machinery), not moot**

**Moot-by-routing in the current topology, solvable cheaply if per-unit testing is adopted.** Today
no suite runs in the cacheless worktree: implement-phase self-check is the **three write-time lenses**
(no suite, `implement.md:179-197`); the suite runs at **verify**, which is **context-isolated (subagent),
not worktree-isolated** → it runs against operator's **main tree natively, cache present** (`verify.md:7-20,50`).
So verify-on-main is the test gate and needs no provisioning. **But** the operator confirmed test-running
subagents are real and that per-unit in-worktree testing (early + parallel regression detection) is a
legitimate option — so the cache question is *resolved*, not punted. The standard CI parallel-cache problem;
proven machinery:

**The deciding constraint — the isolation invariant extends to caches.** A worktree exists to give each
agent *private mutable state*; a build/checker cache **is** mutable state. **Rule: every mutable cache is a
private per-worktree copy; only immutable / content-addressed caches may be shared.** This is what keeps
cache-sharing from re-opening the old cross-pollination breach (agents seeing/clobbering each other's state).

- **Universal mechanism (machine- *and* toolchain-agnostic):** `cp --reflink=auto -r <declared-cache-dirs>
  <worktree>/` — one standard command. COW filesystem (btrfs/XFS-reflink/ZFS/APFS) → instant clone; else →
  full copy. **Either way a *private* copy** → isolation preserved, no cross-pollination. The instance/operator
  declares the **cache-dir list** per project (`target/`, `node_modules`, **and linters/checkers** `.mypy_cache`,
  `.ruff_cache`, `.pytest_cache`, `__pycache__`, `.gradle`…); the mechanism is uniform. Checker caches are small
  → full-copy fallback is cheap even off-COW.
- **Share (read-only, safe by construction — no provisioning):** content-addressed / immutable caches —
  **Go `GOCACHE`** (content-addressed, concurrency-safe, already user-global), dependency-download caches
  (`~/.cargo/registry`, `~/.npm`, pnpm store, uv). Same content → same key → no clobber; reads don't mutate.
- **REJECT (the cross-pollination vectors):** a **shared writable mutable cache dir** (concurrent agents
  clobber each other) and **hardlinking a mutable cache** (writes leak through the shared inode). *Not*
  "read-only shared cache" (wrong model — serializes or can't accept the worktree's new artifacts) and *not*
  blanket hardlinking.
- **Enabler — worktree placement:** put worktrees on the **repo's own volume but outside the repo tree**
  (reflink works + escape-resistance holds). The current `/tmp` placement (a) is **tmpfs → no reflink**, which
  is what makes a test-running worktree slow; same-volume-but-outside-repo fixes it without weakening (a).

**Empirical grounding** (`/tmp/cache-isolation-probe.sh`, this machine = btrfs): reflink copy on btrfs is
instant and **stays private** — mutating a copy left source + sibling unchanged (no cross-pollination);
**hardlinking a mutable file leaked** the write through to the source (why mutable caches must not be hardlinked);
`cp --reflink=auto` on tmpfs fell back to a full copy (universal floor holds). Refs:
[howardjohn — Sharing Rust Build Cache](https://blog.howardjohn.info/posts/shared-rust-build/),
[kache](https://kunobi.ninja/blog/what-kache-actually-caches).

**Composes with the gate, doesn't replace it:** the merge-tree gate checks *textual* landing-completeness;
a per-unit suite run (now cheap) checks *semantic* regression — orthogonal, compose if per-unit testing is
adopted. **The fork (still a choice, now informed):** adopt per-unit in-worktree testing (cheap cache, earlier
+ parallel regression catch) **or** keep verify-on-main as the single test gate (cache-free floor). Lean:
ship the cache-provisioning seam regardless (pure upside, proven); decide per-unit-testing adoption on its own
merits.

## Level + relates

**Level.** Was Framework §4.2 + clippy render + harness, fork-first. **Now gated-kernel, mostly
clippy-render:** the merge-tree gate + scope-conformance + escape-theater cut + the **cache-provisioning**
(reflink-auto private-copy of a declared cache-dir list) + **worktree-placement on the repo's volume**
(off tmpfs `/tmp`) are clippy **isolation-slot bindings** (`implement.md` Isolation mechanism). The
framework §4.2.3 **Provisioning** rule already fits the cache (a non-tracked run-input provisioned into the
copy + excluded from integration) — the only sharpening it wants is "provision as a **private copy**, never
a shared mutable mount" (the isolation invariant). Plus the integration one-liner: **fail loud, never
conflict-suppress** (forbid `-X ours/theirs`). Both small, evaluate at the re-render. **Campaign ④a's
fork-first gate (the cache decision) dissolves → ④a is now plain gated-kernel.**

Feeds **[[instance-reinstantiation]]** (this design lands in the clippy re-render). Relates to
**[[clippy-run-findings-dispatch-coupling]]** (Cycle 2 isolation + Cycle G main-tree integrity),
**[[dispatch-brief-one-source-of-truth]]** (④a sibling). Also informs **[[impl-dispatch-workflow-substrate]]**
— the gate is a tiny scripted step a Workflow substrate would re-script in-agent rather than fix as rules.
