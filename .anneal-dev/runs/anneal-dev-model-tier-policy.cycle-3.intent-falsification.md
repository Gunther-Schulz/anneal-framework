# Intent-falsification pass — cycle 3 (convergence attempt, clean-convergence cycle)

Run: anneal-dev-model-tier-policy. Dispatched to a fresh-context subagent
(criteria-first). Orchestrator routing/verdicts recorded below (the subagent
declares; the orchestrator is first-judge per practice 11, re-deriving against
the framework). Result: 3 findings → 1 D-delta (D5) → **mechanical falsification
pass SKIPPED this cycle** (`mechanical skipped: intent-delta this cycle`, per
`spec/core.md` §4.1.4 sequencing + `modules.md` §3.4 skip carve-out).

## Per-R# attack lines

- `{R1, attempted-refutation: read core.md dispatch sites (§4.1.4/§4.2.2/§4.3) + D3, outcome: served — every dispatch kind is a subagent call carrying an observable model param; blanket holds, no per-dispatch judgment}` (but see Finding 1 + Finding 2 for residual costs)
- `{R2, attempted-refutation: git ls-files anneal-dev.config/ + D4, outcome: served — value in a tracked operator-editable config, no spec edit to change tier}`
- `{R3, attempted-refutation: rg -ni "model" spec/*.md foundation.md → only "the Model"/"intent-model"; glossary clean, outcome: served}`
- `{R4, attempted-refutation: D7 + intent source "Floor, not guarantee", outcome: served — but Finding 1: floor framing does not disclose the verify-side same-tier coupling}`
- `{R5, attempted-refutation: D2 + foundation contract 3 + clippy "zero framework presence", outcome: served — no spec/* change, other instances untouched}`

## Per-finding lines + orchestrator routing

- `{finding: blanket pin forces verify onto the SAME tier as the actor — the same-base-model coupling INV-3's anchor warns against; the rule makes it mandatory, foreclosing the cross-tier-diversity lever the framework's own Arm C research leans toward; floor framing does not disclose this, criterion-attacked: R4 + the D7 "does not undermine INV-3" claim, refutation: core.md:795-812 (verify isolation = context-only) + INV-3 anchor + anneal-empirical-validation-experiment.md:69 (Arm C open question), route: [VERIFIED — surfaced]}`
  → **Orchestrator verdict: [VERIFIED — surfaced]** (F8). Pure judgment; terminal; feeds operator soundness pass. NOT acted on by exempting verify (that would contradict R1's blanket intent — operator's call to override). Strengthens the relate-to `multivoter-verify-no-predicate-claims` (D7).
- `{finding: D5 no-bootstrap → the top-tier floor is absent-by-default in an installed-elsewhere project (no model-tier.md), weakening R1's "top tier always" to "only where the operator hand-created the file", criterion-attacked: R1, refutation: instantiation-guide.md:135-146 (closed-slot) + :380-401 (bootstrap covers recognized slot kinds) + bindings.md:241-251 (enumeration omits model-tier), route: mechanical-falsification-candidate}`
  → **Orchestrator verdict: re-derived. The mechanical candidate (is model-tier.md in the bootstrap list?) comes up `holds` against D5's §5 basis (§5 DOES permit non-bootstrapped operator-editable artifacts — `instantiation-guide.md`:352-356).** BUT the JUDGMENT concern (the no-downgrade floor is always on via D3, but the TOP-TIER PIN defaults to session-inherit, so R1's "top tier" is not met in low-session installed-elsewhere usage) is persuasive → **drives a D5 amendment (flip to bootstrap a commented placeholder).** D-track delta.
- `{finding: D8 defers the anneal-dev plugin render → the running/cached plugin does not carry the tier rule until re-render+reinstall, so anneal-dev's own immediately-following runs do not enforce the floor it just authored (self-governing render-debt), criterion-attacked: R1 (unenforced in the running tool), refutation: instance-reinstantiation.md render policy + cache-not-updated-until-reinstall + D8, route: [VERIFIED — surfaced]}`
  → **Orchestrator verdict: [VERIFIED — surfaced]** (F9). Terminal. Resolved by the operator's post-run activation request (re-render + reinstall anneal-dev). The subagent's cache-version cite (0.1.1) is stale — actual cache is 0.1.2; substance (render-debt staleness) unaffected. D8's spec-only cadence stands (operator-ratified); activation is post-run.

## Convergence status this cycle
NOT clean — Finding 2 drove a D5 amendment (D-track delta). Mechanical falsification
pass skipped (intent-delta). Loop continues → cycle 4.
