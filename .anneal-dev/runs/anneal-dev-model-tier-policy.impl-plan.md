# Impl plan — anneal-dev-model-tier-policy

1 dispatch unit, sequential, dispatched to an in-place subagent under the
Integrity check (`core.md` §4.2.4). Single container: the anneal-framework repo.

## U1 (first; sequential; in-place) — realizes D1–D9
Implements: D1, D2, D3, D4, D5, D6, D7, D8, D9.
Element/contract scope:
- `anneal-dev/spec/bindings.md` — add a new section "## Dispatch model tier —
  corpus-evolution binding" after the Isolation slot section (the policy: blanket
  top-tier pin across all anneal-dev dispatch kinds; downgrade forbidden; tier
  named in `anneal-dev.config/model-tier.md`, absent = inherit session, never
  downgrade; FLOOR-not-guarantee framing; term defined inline). AND add
  `model-tier.md` to the "Operator-editable artifacts" set + the "First-run
  bootstrap" enumeration (now 4 placeholders).  [rule-corpus edit → skill-craft
  invocation REQUIRED before the edit; run-gate hook requires the IN-PROGRESS run]
- `anneal-dev.config/model-tier.md` — CREATE, content `opus` + header comment
  (slot name + pointer to bindings.md "Dispatch model tier" + how-to-pin).
- `anneal-dev.config/README.md` — add one line documenting the model-tier override.
- `dev-notes/backlog/instance-reinstantiation.md` — append this run's source-delta
  to the render-debt "Queue".
- `dev-notes/backlog/clippy-run-findings-dispatch-coupling.md` — relate-note
  (sibling dispatch-model precedent, opposite polarity).
- `dev-notes/backlog/multivoter-verify-no-predicate-claims.md` — relate-note (F8:
  the blanket pin forecloses verify-cross-tier-diversity; resolve there if
  model-diversity-for-verify is pursued).

Disjointness basis: N/A — single unit, no concurrent units.

## Not in impl (release-loop steps, post-verify)
- `git mv dev-notes/backlog/anneal-dev-model-tier-policy.md archive/` (archive on ship — release step 5).
- Post-run: re-render anneal-dev plugin + reinstall (operator's "get the newest version active" — resolves F9; the instance-reinstantiation batch, anneal-dev portion).
