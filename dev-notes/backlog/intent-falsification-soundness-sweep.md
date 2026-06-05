# Intent-falsification soundness sweep — audit shipped enforcement for the self-certifying-form blind spot

**Status:** SECOND PASS DONE 2026-06-05 (8 targets total: the 3 hooks + step-4 design, then the
structural-enforcement practices + the §3.1 keystone + the falsification machinery + the
intent-falsification pass itself). Fix-queue below reduces to 5 root moves. Only scope-item-2 (shipped
run artifacts) remains unswept. Originally operator-requested 2026-06-04, surfaced FROM the
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
  *(↑ scope-item-1-remainder + scope-item-3 were SWEPT in the second pass below; only scope-item-2 remains.)*
- **NEW target (2026-06-05, discovered by running the move-1 cycle): the [READY] / fresh-session-implementability
  machinery.** [READY]'s gates — fresh-session-implementability ("would a fresh session implement without a new
  design decision?"), standardized-coverage-accounted-whole, the convergence-clean judgment — are
  **orchestrator-self-attested** (the same context that wrote the design judges it ready), with per-step
  *citations* but no fresh-context re-derivation of the readiness verdict itself. The sweep's first two slices hit
  the hooks + §3.1 + the falsification dispatches but NOT this gate. **Observed instance (seed):** in
  `move1-s3.1-honest-relabel`, fresh-session-implementability self-attested **PASSED at cycle 2** — yet the
  downstream fresh-context convergence cycle then caught two real design refinements (F-C "external terminus"
  under-defined; F-A render-tracking), which a genuinely-implementable design would not have surfaced. The
  implementability self-judgment under-detected; only the convergence cycle (a real fresh-context pass) caught it.
  Same "self-recorded verdict < fresh-context check" class, at the [READY] machinery. (Adjacent to V-11
  per-step-evidence / V-16 design-validity-at-ready, but distinct: this is the *readiness verdict's* self-attestation,
  not the per-step evidence form.)

## Second-pass results (2026-06-05) — 4 more passes: structural-enforcement practices · §3.1 keystone · the falsification machinery · the intent-falsification pass itself
**Form-not-binding confirmed at the ROOT and recursively — but the FOUNDATION is SOUND; the defect is
localized OVERCLAIM.** §3.1 (the keystone every dispatched check cites) does not bind: its "separate
checker" **relocates** fakeability one level up — the orchestrator (the AI, §4.2.6) is the SOLE
tracker-writer, so a recorded "separate-checker PASS" is indistinguishable from a self-authored one (no
dispatch provenance). The genuine non-fakeable termini that DO exist: (a) the **operator's irreducible
soundness pass**, and (b) checkers terminating at an **external re-checkable fact** — verify executing the
work, the §4.2.4 Integrity state-marker, git-log cycle-counts. Everything else is a **strong surfacer**,
not a binding gate. The spec is HONEST about this in places (§4.1.4:529-532 "not a soundness certificate;
operator irreducible") — so the framework's FOUNDATION (operator-irreducible + strong-surfacers) is sound;
the defect is **localized overclaims** selling surfacers as binding ("the guarantee comes from the checker"
§3.1; "the artifact IS the un-fakeable thing" dev-process:573; "structural enforcement" on practices 10/11;
"holds"/"clean" on the falsification passes).

**The recursion, explicit + unavoidable:** the intent-falsification pass — the instrument this sweep IS —
partially binds (genuinely fresh-context dispatch + operator-independent teeth on the mechanical-candidate
route) but its "evidenced clean" judgment verdict is **vacuously fakeable by the spec's own admission**
(`modules.md`:436-439 "can be vacuously satisfied… not rubber-stamp prevention") and its intent-model is
anchored to a designer-authored requirements record. **So these sweep findings are SURFACED, not certified**
— nothing internal to intent-falsification distinguishes a genuine clean from a vacuous one; only the
**operator (+ the skill-craft form review, per CLAUDE.md's kernel-independent leg)** closes the loop. This
audit included.

**⚠ Self-catch:** pass 7 caught that **V-26's archival earlier this session was a circular error**
(spec-closure can't certify spec-correctness) → **reversed** (V-26 restored WATCHING).

### Root moves (the ~25 granular FQs across both slices reduce to these 5; each → its own anneal-dev cycle)
> **Cross-cutting lens (2026-06-05 — operator-raised during campaign ②): token-efficiency vs
> convergence-coverage.** Before adding ANY soundness-machinery in this cluster (dispatch-witness manifest,
> `ready-machinery-self-attestation`, `method-kernel-soundness-verdict-locus`,
> `foundation-register-intent-falsification-anchors`), apply the test: *does the convergence cycle's existing
> fresh-context pass already cover this?* If yes, self-attestation backstopped by convergence is acceptable —
> adding a check costs tokens without proportional value (Bloat lens + practice-7 proportionality at the meta
> level: "most token-efficient without sacrificing value/performance"). First to (likely) FAIL the test:
> `ready-machinery-self-attestation` (readiness verdict is convergence-backstopped → close-as-covered, not new
> machinery — see that item's Disposition leaning). The manifest (Move-2) PASSES the test: dispatch-provenance
> is the one thing convergence does NOT witness.
> **Move-1 cycle SETUP (2026-06-05 — anneal-dev invoked, paused at investigate-design before run state).**
> Confirmed scope (a contract change, practice-4 dependent audit owed at the fresh resume): the overclaim
> vocabulary lives at **`spec/core.md` §3.1** (source) + **`development-process.md` practices 8/10/11/12 +
> :573** + is **rendered verbatim into every instance's `foundations.md`** (e.g. anneal-dev plugin
> `references/foundations.md` L106-145 carries "the guarantee comes from the checker"). So the cycle edits
> §3.1 → propagates to the practices/dev-process → re-renders each instance (the render-tail).
> **Design seed:** §3.1 ALREADY carries the strong/weak gradient ("strong = points at external re-checkable
> truth; weak = a claim about the run's own state") — the fix *sharpens its own gradient*: a self-recorded
> textual-re-derivation verdict is a WEAK artifact; name the binding terminus (external fact / operator).
> Not a new concept → a clean amendment. **Verify must add the kernel-independent legs** (skill-craft form +
> operator soundness); the sweep finding is SURFACED not certified, so the operator's soundness ON THE
> DESIGN is where it gets certified. Paused fresh because the keystone deserves full-discipline design +
> un-rushed operator soundness (practice 7).

1. **[KEYSTONE] Honest relabel at §3.1 — distinguish external-terminus checkers (bind) from
   textual-re-derivation checkers (surface).** Stop attributing "the guarantee" / "un-fakeable" /
   "structural enforcement" generically; name the real binding root (operator soundness pass +
   external-fact checkers). ONE conceptual fix, MANY sites: §3.1, dev-process:573, practices 10/11, the
   discharge green-✓, the falsification "holds" labels. Cheap (re-labeling, no new machinery); removes the
   false comfort the whole sweep objected to. **Highest leverage.** (subsumes FQ-5, FX-A/B/C/F, FQ-K1/K2, FQ-B·pass7)
   - **Move-1 PARTIALLY SHIPPED `819e84e` (2026-06-05, method-kernel anneal-dev run, operator step-4-approved):**
     §3.1 keystone (producer-independence bind test + F-B fence) + `development-process.md` practices 10/11/12 +
     step-4 + `glossary.md` term + `foundation.md` + `instantiation-guide.md`. Render-follow queued to the
     render-debt batch (D7). **Still in root-move-1 scope, NOT yet done:** the commit-msg hook's green-✓ output
     relabel (FQ-5) + the falsification "holds" labels (FQ-B·pass7) — those are separate sites/cycles.
     **Residual absolute-"un-fakeable"
     site, OUT of move-1's D6 scope → swept here:** `development-process.md:438` (practice-11 keep-as-is rule)
     "the named loss is **the un-fakeable evidence** the keep is defensible" — same self-recorded-artifact shape
     (the named-loss is first-judge-authored; its correctness is operator-re-derivable → a weak/strong-surfacer
     artifact, not absolutely un-fakeable). Verify and the form-review split on it; left out of move-1 to avoid
     widening the release. Reconcile it (→ "the named loss is the evidence the operator second-judges") when this
     move-1 keystone lands. (Move-1 also caught + fixed an in-scope sibling at `development-process.md:538`.)
2. **[ARCHITECTURAL] Dispatch-witness manifest as §3.1 first-class instrument.** (Fork decided 2026-06-05,
   broadened in scope: not a tactical FQ patch, a §3.1 instrument.) The single lever that converts surfacers
   → strong-surfacer-with-active-fabrication-cost for **dispatch-class claims**: a PostToolUse-on-Agent hook
   records each dispatched subagent (agentId, timestamp, prompt-hash) to a manifest; non-producing checkers
   (commit-msg gate, end-of-run audit) re-derive cited dispatch claims against the manifest. Faking it
   requires explicit Edit/Write to the manifest path, visible in the transcript — §3.1's gradient promotes
   the artifact from "weak (self-recorded)" to "strong surfacer (checker-re-derivable against an external
   fact)." Operator-irreducible gate retained for **non-dispatch claims** (the bind/surface split: manifest
   for dispatch evidence; operator for soundness).
   **The primitive renders into six sites:** (a) intent-falsification pass artifact (`core.md §4.1.4` +
   `modules.md §3.4.1`) — manifest entry proves a fresh-context subagent ran; (b) mechanical falsification
   pass artifact (same locus) — same; (c) verify isolation (`core.md §4.3`, `phases/verify.md`) — manifest
   entry proves the verifier was separate-context; (d) run-gate IN-PROGRESS signal (FQ-3) — alternative
   non-self-mintable signal via PostToolUse-on-Skill(anneal-dev); (e) step-4 discharge subagent-ID cites
   (FQ-9/A) — commit-msg cross-checks against manifest; (f) anneal-dev-evaluation-discipline Tier-2 signature
   (filed 2026-06-05) — the signature becomes manifest-observable. (subsumes FQ-3, FQ-9·pass1, FQ-K3,
   FQ-A·pass7.)
   **Harness-capability check (2026-06-05):** PostToolUse fires on the `Agent` matcher (confirmed via
   `claude-code-guide` agent against Claude Code docs). The `tool_response` shape is not documented for
   subagent calls — empirical verification of the agentId field path is an investigate-design pass within the
   cycle, NOT a fork blocker. No harness-side audit log is documented (manifest is operator-owned).
   **Composes with:** `anneal-dev-evaluation-discipline` (gives the Tier-2 signature its un-fakeable artifact);
   `instance-domain-invariant-register` (sibling instrument at the work-product layer); V-30 (manifest enables
   automated catcher for dispatch-class violations — V-30's closing rule gains real teeth).
3. **[FALSE-COMFORT] Carry every caveat to its point-of-use.** Vacuity caveat → the [READY] artifact; enum-
   scope caveat → the mechanical "holds" site; presence≠correctness → practices 10/11; soundness-vs-form
   disclaimer → a discharge-block header, not 1-of-9 lines. The caveats EXIST; they're just not where the
   comfort is generated. (subsumes FQ-5, FQ-C·pass7/8, FX-D/E)
4. **[CHEAP EXTERNAL CHECKS] Verify against external facts where the hook/orchestrator already can.** Verdict-
   form parsing not substring-presence (FQ-1); validate the mechanical N/A conditions the commit-msg hook
   already holds the diff for (FQ-2); re-run a sampled subset of falsification `result` fields (FQ-C·pass7).
5. **[ENUM COMPLETENESS] The closed 3-shape/3-predicate falsification enum needs an exhaustiveness basis or an
   explicit residual** (FQ-D·pass7); "holds" relabeled enum-scoped; bind shape-coverage to the design's
   ACTUAL couplings, not the basis's self-declared ones (FQ-E·pass7). **This is the root of the V-26 reversal.**

**Known/accepted reconsideration (carried):** the **Bash channel** evades both PreToolUse hooks — still the
shared hole that nullifies hook fixes; promote to "reconsider" (a Bash matcher, or tool-agnostic commit-time
checks). Reframe under the surfacer lens: if the hooks are surfacers for a cooperating AI, the Bash bypass is
acceptable (a cooperating AI won't `sed`-edit to dodge its own reminder) — which is itself a reason to take
move 1 (stop calling them gates).

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
