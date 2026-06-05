# Intent-falsification soundness sweep — audit shipped enforcement for the self-certifying-form blind spot

**Status:** OPEN — operator-requested 2026-06-04, surfaced FROM the
`foundation-invariants-register` anneal-dev run (B1/B2 intent-falsification findings).
Retrospective audit effort; **own scope, NOT the foundation-invariants run's.** A sweep,
not a single edit — it generates a fix-queue (each confirmed finding → its own method-kernel
edit through anneal-dev).

## Why (the discovery)
The foundation-invariants run ran a **single criteria-first intent-falsification** (judgment
pass: state the design's intent independently, attack whether the design serves it) and
caught **2 blocking flaws the mechanical convergence-falsification confirmed-clean past**:
the register's own enforcement was *self-dischargeable* (AI writes the string the hook
checks) and its protection marker was *overclaimed as binding* (a local hook cannot verify
operator approval — operator-detection, malformed per `anneal-dev` foundations). Strong n=1:
**mechanical and judgment checks have non-overlapping blind spots.** Mechanical machinery
certifies its own *form* (string present ✓) and is structurally blind to whether the form
*binds*. Every prior anneal-dev run was certified WITHOUT a structured intent-falsification
— so shipped enforcement likely carries siblings of B1/B2.

## The failure-class to hunt (from B1/B2)
- (i) **Self-dischargeable enforcement** — the gate checks an artifact the AI itself
  produces/writes (string-presence, self-authored verdict); no independent tie to the thing
  it claims to enforce.
- (ii) **Overclaimed gate** — sold as a binding gate, actually bypassable friction
  (`--no-verify`, prose-only) — the gap between claimed and actual enforcement strength.
- (iii) **Operator-detection-dependent enforcement** — enforcement that silently requires
  the operator to detect/verify (malformed per foundations.md Operator-expected-action-bound).
- (iv) **False-comfort artifact** — a residual/caveat ("X ≠ sound", "known-limits") placed
  where it is NOT read at the moment the comfort is generated.

## Scope (start high-risk; risk-ordered, don't boil the ocean)
1. **The enforcement machinery first** (where B1/B2 lived): `hooks/` (commit-msg discharge,
   anneal-dev-run-gate, skill-craft-pre-edit) + the **step-4 discharge artifact** machinery
   + the **structural-enforcement rules** in `development-process.md` + `spec/core.md` that
   self-classify as "structural enforcement" (practices 8 / 10 / 11 / 12; the
   evidence-bearing-artifact rule) — for each: does it actually bind, or self-certify /
   overclaim / require operator-detection?
2. **Shipped method-kernel edits** (the prior PASSED runs in `.anneal-dev/runs/`).

## Method
Per-target **fresh-context intent-falsification**, criteria-first: state the mechanism's
intent independently, then a default-skeptical attack on whether it binds (not whether its
claims are grounded — that is the mechanical pass). **Single check, not multi-vote** — the
foundation-invariants run validated single-check sufficiency; the research deflated quorum.

## Cost / caution (practice 7)
Expensive (a fresh context per target) and it WILL surface a fix-queue (if a fresh design
hid one, mature machinery hides more). Risk-order, cap per pass, log what was not swept;
each confirmed finding becomes its own classifiable fix (practice 8) through anneal-dev.

## Observed seed (2026-06-05, from quick-win `anneal-dev-plugin-dangling-anti-patterns-ref`)
The **commit-msg step-4 discharge** gate was exercised live on a one-line cosmetic
plugin-render fix (commit `26ac662`) — an unplanned probe of scope-item-1. Two data
points for the sweep to chase:
- **Binds (conformant-success):** the **render-fidelity leg (practice 2)** accepts only
  `[subagent ID, verdict]` or mechanical N/A — *no in-context option*. That forced a
  fresh verifier which **caught a source-absent accretion the actor (renderer) had
  under-weighted**. The "renderer is blind to its own flattening" rationale held
  empirically → that leg resists self-discharge. Evidence the no-in-context rule is
  load-bearing, not ceremony.
- **Candidate class-(i) finding — N/A validated by *form*, not by *binding*:** the hook
  accepts a self-authored `[N/A: <reason>]` if the reason dodges a **banned-phrase
  blacklist** (FOLD_INTO / JUDGMENT_NA patterns). It cannot verify the N/A *condition*
  actually holds — a plausible-but-false "mechanically-verifiable" reason passes. The
  actor produces most of the 7-check discharge himself; only render-fidelity (+ the
  spec-origin trace) is independently tied. Attack target: does the discharge bind, or
  does it self-certify its own *form* (the exact B1/B2 shape)?
- **Proportionality probe (practice 7):** the full 7-check discharge fired on a one-line
  cosmetic cite — friction that could pressure toward `--no-verify` (class-ii bypass).
  Whether that is correct (a render edit IS a rule-corpus change) or over-scoped (no
  cosmetic-render carve-out) is a sweep question, not yet adjudicated.

## Relates to
- **Prospective sibling** — `verify-model-diversity` (reframed this session:
  mechanism → single intent-falsification; add an intent-falsification leg to anneal-dev's
  convergence/verify). This sweep is the **retrospective** application; that item is the
  **prospective** wiring. Do the wiring and the sweep need not repeat per-run.
- `coherence-audit` — a different audit lens-set (set-level drift). Intent-falsification is
  per-mechanism soundness-vs-intent; candidate to become a coherence-audit lens OR a sibling
  sweep mode. Decide which when this runs.
- Origin: `foundation-self-certification-machinery` / the `foundation-invariants-register`
  run (B1/B2 = the seed findings; tracker in `.anneal-dev/runs/`).
- **External corroboration** — Hylak, *How to Evaluate AI Agents* (howtoeval.com, 2026):
  "offline evals must be code-aware, not prompt-level." Reusable statement of this sweep's
  lesson — **verify the entangled/enforced form, not the isolated unit** (B2 = a hook that
  can't verify operator approval is an enforced-form flaw invisible to spec-text review).
  Aims the per-target attack: attack the rendered + hooked + operator-interactive form, not
  the spec clause in isolation.
