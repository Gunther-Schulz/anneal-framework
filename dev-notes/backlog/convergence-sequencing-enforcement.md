# Convergence-pass sequencing — enforce intent→mechanical ordering structurally (not prose)

**Status:** [PARTIAL] L3 (skill-craft) **SHIPPED 2026-06-05** (v1.0.58); L1 (anneal-dev kernel) **SHIPPED 2026-06-05**
(spec-only release `f74b145`; render-follow queued to `instance-reinstantiation`). **Both levels shipped — this
item archives once the render-debt batch carries L1's source-delta into the instances.** Discovered 2026-06-05
when the orchestrator (the AI) ran the convergence cycle's
two falsification passes **in PARALLEL** instead of sequenced — the **operator caught it**. A form-not-binding /
unenforced-rule instance living in the convergence machinery (intent-falsification-soundness-sweep **scope-item-3**,
which pass-8 marked "swept" but missed this — itself a sweep blind spot).

## The finding
The convergence cycle's two passes are SEQUENCED: intent-falsification runs **first**; only when it comes up clean
does the mechanical pass run (intent-delta → mechanical skipped, the stale-run guard). But that sequencing is stated
**prose-only** (`spec/core.md §4.1.4` :410-419; `modules.md §3.4`) with **no enforcement artifact** — on the clean
path a correctly-sequenced run and a parallel run leave **identical artifacts**, so nothing catches a violation. The
orchestrator (sole executor, §4.2.6) self-sequences; the rule fell to **operator-detection** (malformed per
`foundations` Operator-expected-action-bound). The two passes are presented as structurally-symmetric siblings with
the gating dependency in prose → parallelizing is the *natural* error. It happened **twice**: at anneal-dev authoring
(prose-only sequencing shipped) and at live execution (the AI parallel-dispatched having just read the rule).

## The fix — three levels (fix-at-source: L3 → L1)
- **L3 [skill-craft] — SHIPPED v1.0.58** (commit `9771523`, `github.com/Gunther-Schulz/skill-craft`). The
  authoring-time root: skill-craft had no discipline for **conditionally-dependent + independently-dispatchable**
  operations. Added to Forcing-functions: temporal keywords express order but don't enforce it; for dispatchable
  steps, encode the dependency in the dependent step's **input** + have its artifact **cite** the prerequisite's
  result; + review-checklist mirror. Plus the **salience half**: the enforcement-register proportionality
  (workflow→structural / judgment→evidence-backed principles) was absorbed ~71 lines before its carve-out, leaking
  the gate register into judgment-skill authoring → elevated to the Layer-2 intro + new **"Scope precedes default"**
  principle + 12th review-checklist item **"Salience / reading order"**. (Salience half sourced from the operator's
  other-session dev-notes — `pbs-bureau/learnings:311`, "carve-out comes too late in reading order".)
- **L1 [anneal-dev kernel] — SHIPPED `f74b145`** (anneal-dev run `l1-convergence-pass-sequencing`, operator
  step-4-approved). Applied to `spec/core.md §4.1.4` + `modules.md §3.3/§3.4`: the mechanical pass's input carries
  this-cycle's intent-clean verdict (D2), its artifact **cites** it in a per-artifact header (D3), the
  coverage-check clause (v) re-derives + rejects a mismatch (D4), the prose names the structural bind (D5).
  **Plus (run-surfaced):** the convergence cycle's own intent-falsification pass caught a **carry-forward
  legitimacy hole** (a behavior-preserving carry-forward let a stale intent-clean carry across a design change,
  its legitimacy resting on orchestrator say-so) → **D7 removed the carry-forward optimization** (the intent pass
  now runs every convergence cycle; simpler + tighter). Render-follow queued to the render-debt batch (ALL
  instances; not behavior-preserving → needs render-fidelity verify).
- **L2 [anneal-framework]** — likely **subsumed** by L3 (the spec itself is authored under skill-craft form
  discipline). Not opened separately unless L1 shows the spec's own ordering dependencies need a framework-level lens.

## Relates to
- `intent-falsification-soundness-sweep` — confirmed **scope-item-3** finding (the falsification-pass machinery's
  own enforcement) that pass-8 marked swept but missed. The L1 fix is effectively a new sweep root-move.
- `auto-battle-cadence-mode` — the **auto-cycle** mis-sequenced the convergence passes: datapoint that auto-cycle
  cannot be trusted to sequence the convergence passes unattended (the operator gate caught it). Bears on whether
  auto-cycle should halt at the convergence cycle.
