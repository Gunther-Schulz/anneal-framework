## V-27. Contract-2 render-ceremony cost on the dev-process-as-instance — does it justify itself?

**Status: WATCHING.**

**Decision (`framework-dev-as-anneal` locked decision; `foundation.md`
contract 2; `development-process.md` practice 2 / release loop).** Making
framework development a real anneal instance (anneal-dev) means the
development process itself becomes "anneal + corpus-specific bindings,"
rendered like any instance — so under contract 2 it incurs per-cycle
render-ceremony: the dev-process-as-instance gets re-rendered from the
shared kernel and fidelity-checked (separate context) like clippy/daneel.
The locked bet (`framework-dev-as-anneal` "honest cost"): that ceremony
replaces a worse, invisible cost already paid as drift.

**Why uncertain.** Whether the per-cycle re-render + fidelity check on the
dev-process-as-instance justifies itself cannot be settled until anneal-dev
is operational (step 5 dogfood + promotion). Two ways it could go: (a) the
shared kernel changes rarely enough that the ceremony is cheap and the
drift-prevention wins; (b) the kernel churns and the re-render/fidelity
overhead per cycle becomes a real burden disproportionate to the drift it
prevents. Not judgeable ahead of operation.

**Production signal to watch (n=1).** The first stretch of anneal-dev
operating as the actual dev-process: a kernel change forces a
dev-process-instance re-render + fidelity pass whose cost visibly exceeds
the drift it caught — or, conversely, a re-render catches a drift the old
advisory process would have missed. Either is n=1 evidence. **Specific
watch:** the re-render/fidelity cost per cycle vs. the drift-catch rate.

**n=1 (seed, 2026-06-02 — step-5 dogfood).** anneal-dev's first real run
(`daneel-cycle-b-sync`, run-state `.anneal-dev/runs/`) drove a **one-line,
behavior-preserving vocab swap** through the full ceremony: investigate-design +
standardized pass + convergence cycle + fresh-context falsification pass +
isolated 3-check verify battery. **Cost side:** ceremony-to-change ratio was high
(full convergence/falsification/isolated-battery for a 2-word swap). **Catch
side:** no drift caught that the old advisory process would have missed *on this
change* (it was trivially correct) — BUT the isolated verify *independently
reproduced* the grep evidence (F1=1, F2=∅) rather than trusting the working
context's claim, so the contract-2 separate-context discipline did real work even
here. **Verdict: inconclusive at n=1** — the change was too small to stress
ceiling case (b) (kernel churn forcing costly re-renders). Watch continues; the
discriminating signal is a *larger* change, or a kernel change forcing a
dev-process-instance re-render. NB this was an instance-corpus dogfood, not
anneal-dev operating *as* the dev-process (the promotion case is still untested).

Per `development-process.md` practice 8, this V-N is legitimate: genuine
uncertainty about a design choice's correctness (whether the
instance-ceremony cost is justified), to settle empirically once anneal-dev
operates — not deferral of a classifiable fix (no fix is in hand; the
ceremony is the locked design, watched for whether it pays off).

