# Intent-falsification soundness sweep — audit shipped enforcement for the self-certifying-form blind spot

**Status:** FIRST PASS DONE 2026-06-05 (4 targets: the 3 hooks + the step-4 discharge design).
Fix-queue below. Originally operator-requested 2026-06-04, surfaced FROM the
`foundation-invariants-register` anneal-dev run (B1/B2 intent-falsification findings).
Retrospective audit effort; **own scope, NOT the foundation-invariants run's.** A sweep,
not a single edit — it generates a fix-queue (each confirmed finding → its own method-kernel
edit through anneal-dev).

## First-pass results (2026-06-05) — 4 fresh-context, criteria-first intent-falsification passes
**Convergent finding (B1/B2 confirmed at scale):** every one of the 4 targets certifies **form**
(a string / token / state is present), not **binding** (the verification happened). Code-verified,
not adversarial inflation. **Crucial frame:** the framework's own stance is *hooks = surfacers,
operator = the irreducible gate* — so "doesn't independently bind" is **partly by design**. The
genuine defects are (a) **overclaim** — sold as binding where it's a surfacer (false comfort),
(b) **cheap surfacer-strengthening not taken** (the hook has the facts but checks form), and
(c) **self-minted signals** — the worst: a surfacer that surfaces a token the AI itself mints
surfaces *nothing* (pure theater). Humbling dogfood: the sweep found quick-win-1's own discharge
(commit `26ac662`) was ~1/9 binding — only render-fidelity (no-in-context) tied to real work; the
rest I self-attested. The fixes themselves are method-kernel edits that route through the very
gates being fixed (and the run-gate that governs kernel edits is itself self-dischargeable) — a
recursion to flag, not resolve here.

### THE FOUNDATIONAL FORK (operator-irreducible — anneal can't self-certify its own foundation)
For each gate: **bind it harder, or honestly re-label it a reminder?** The framework says the
operator is the irreducible soundness gate; under that, surfacers are correct — but then they must
NOT overclaim binding. Recommended floor: take the honest-relabel + cheap-strengthening wins (FQ-1/2/5/6/7)
regardless; the self-minted-signal items (FQ-3/4) need this fork decided first.

### Fix-queue (tiered; each → its own anneal-dev cycle when actioned)
**Tier 1 — high-leverage:**
- **FQ-1 [commit-msg] verdict-form parsing, not substring-presence.** ROOT gap: `c in msg` matches a
  check NAME anywhere — a message *disclaiming* the work ("I did not run the discharge" + the names
  listed) PASSES (Attack G, live-verified). Fix: each check name on its own line + a bracketed verdict
  matching an allowed grammar (`[subagent <id>, verdict]` | `[N/A: …]` | `[in-context …]` practice-6 only);
  reject names-without-verdicts. Highest leverage; makes the FOLD_INTO/JUDGMENT_NA blacklists moot.
- **FQ-2 [commit-msg] validate the mechanical N/A conditions the hook already computes.** The hook holds
  the diff; refute false N/As: reject `[N/A: not a method-kernel edit]` when KERNEL_SOURCE matched,
  `[N/A: no plugin/skills/*]` when INSTANCE_PLUGIN matched, `[N/A: single file]` when ≥2 files staged.
  Check the condition, not the prose.
- **FQ-3 [run-gate] the IN-PROGRESS signal is AI-self-mintable.** It reads `Status: IN-PROGRESS` from a
  `.anneal-dev/runs/*.md` file that lives UNDER the `.anneal-dev/` carve-out (so writing it is itself
  ungated) → the AI mints its own permission; the gate surfaces nothing. Needs the FORK: tie to a
  non-self-mintable signal (PostToolUse-on-skill-invocation state the AI's Edit/Write can't reach, or an
  orchestrator nonce) — or honestly re-label as a reminder.
- **FQ-4 [skill-craft-pre-edit] invocation ≠ application.** Satisfied by the skill-craft tool_use TOKEN,
  not by applying the discipline (call it, ignore the output, edit → passes). Needs the FORK: tie to a
  discipline PRODUCT (e.g. the commit-msg spec-origin/Pareto line, mirroring render-fidelity's binding leg)
  — or re-label as a reminder.

**Tier 2 — cheap honesty / correctness fixes:**
- **FQ-5 [step-4 design + commit-msg output] honest re-labeling (false-comfort).** dev-process:573 "the
  artifact IS the un-fakeable thing" + ":590 N/A reasons must be mechanically verifiable" OVERCLAIM — only
  1 of 9 discharge lines (render-fidelity no-in-context) genuinely binds; the green "✓ Discharge artifact
  validation passed" reads as "verified". Fix: (a) hook pass-line → "form present; author-attested unless a
  verifiable subagent ID is cited; presence ≠ verification"; (b) generalize the foundation-invariant "NOT a
  soundness certification" disclaimer (currently on 1 of 9 structurally-identical lines) to a block header;
  (c) reconcile :573 with reality (render-fidelity + operator-approval bind; the rest surface for audit).
- **FQ-6 [skill-craft-pre-edit] dead/loose code.** (a) `SKILL_CRAFT_CANONICAL` regex (`…/plugin/skills/
  skill-craft/`) matches no real install path (real path has no `/plugin/` segment) → decorative exemption;
  fix or delete+document. (b) `SKILL_CRAFT_INVOCATION` is an unanchored substring `skill-craft` → any skill
  name containing it discharges; anchor it. (c) `cosmetic-no-spec-origin` is self-claimable, unverified;
  tie to a hook-verified artifact.
- **FQ-7 [run-gate] over-loose IN-PROGRESS detection.** Regex `Status:?\*{0,2}\s*IN-PROGRESS` scanning the
  first 8 lines of ALL `*.md` → false-positives on prose ("Status held IN-PROGRESS" in real trackers) and
  stale PASSED trackers. Anchor to a real header line; scan only the canonical run tracker.
- **FQ-8 [commit-msg] `anneal-checkpoint:` prefix is a self-asserted full bypass.** A release commit can
  self-label a mid-implement checkpoint to skip the whole discharge. Require a co-located IN-PROGRESS
  tracker before honoring the prefix (composes with FQ-3 — inherits its weakness until FQ-3 lands).
- **FQ-9 [commit-msg] subagent IDs are free text, never cross-checked.** Best-effort cross-check against a
  transcript-ID manifest (local-hook ceiling — may resolve into FQ-5's honest relabel + FQ-1's allowlist).

**Known / accepted (NOT new — re-evaluate, don't re-file):**
- **Bash channel evades BOTH PreToolUse hooks** (run-gate + skill-craft-pre-edit match only
  Edit/Write/NotebookEdit; `sed`/`>`/`cp`/`mv`/`patch`/`git apply` bypass). Previously accepted
  (`skill-craft-pre-edit-hook-findings` F2, archived). The sweep re-surfaces it as a SHARED hole that
  **nullifies every other hook fix** (why parse verdict-form if Bash bypasses the gate?). Highest-leverage
  reconsideration: a `Bash` PreToolUse matcher screening kernel-path writes, OR move the real gate to
  tool-agnostic commit-time content checks. **Recommend promoting from "accepted" to "reconsider".**
- `git commit --no-verify` — deliberate, documented escape hatch. Not a finding.

### Unswept (per the cap — log; next passes)
- The structural-enforcement RULES that self-classify as enforcement (practices 8/10/11/12; the
  evidence-bearing-artifact rule) in `development-process.md` + `spec/core.md` — scope-item-1, not attacked.
- Shipped method-kernel edits in `.anneal-dev/runs/` (scope-item-2).
- The `anneal-dev` skill's own internal enforcement (convergence / mechanical+intent falsification passes).

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
