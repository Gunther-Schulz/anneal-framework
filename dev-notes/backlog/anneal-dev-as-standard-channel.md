# anneal-dev as THE channel for all corpus work (render + re-render + instantiate)

**Status:** OPEN — strategic, operator-raised 2026-06-03. **Strategy/design deliberately
deferred to a fresh session** (esp. the repo-merge question). This file captures the
idea durably so it survives the session boundary; it is NOT yet a decision.

## The idea

Make **anneal-dev the de-facto standard channel for as much corpus work as possible** —
so future renders/instantiations can't silently bypass the discipline (Bloat/Fragmentation
lenses, render-fidelity verify, skill-craft review) that keeps the corpus clean. "No
mistakes in the future" = the channel is the *only* sanctioned path, ideally enforced,
not merely recommended.

## Current state (verified 2026-06-03)

- **Re-rendering existing instances: mandated, but only in prose.** `development-process.md`
  ("development runs through anneal-dev… the rigor is not optional") + `spec/README.md:50`
  ("re-rendering runs as corpus-evolution through the anneal-dev instance"). Real rule —
  but **no structural enforcement** (no gate forces it; a hand-render breaks only prose).
- **Instantiation (deriving a NEW instance): NOT routed through anneal-dev.** The
  `instantiation-guide.md` is a standalone derivation procedure; it routes the instance's
  *ongoing evolution* to anneal-dev (lines 405/436/438) but not the *derivation act*. Gap.

## The sub-questions to settle (a fresh session)

1. **Enforcement:** is the stated mandate enough, or does "render/instantiate runs through
   anneal-dev" need a structural forcing function (the way edits are gated by the skill-craft
   hook)? What would that even look like for a render path?
2. **Instantiation through anneal-dev:** route new-instance derivation (the instantiation-guide
   procedure) through an anneal-dev run, so a *new* instance is born clean + verified, same as
   a re-render. Does the instantiation-guide become an anneal-dev mode/extension?
3. **Repo merge (the big one):** should `anneal-dev` and `anneal-framework` **merge into one
   repo**? anneal-dev is the framework instantiated for corpus-evolution; the framework spec is
   its render source. They're tightly coupled (this session kept tripping over the cross-repo
   boundary). Merging could make "the spec + the tool that evolves and renders it" one unit —
   but it has real costs (anneal-dev is a packaged/installable plugin; the framework is a spec;
   render-source vs render-target boundaries; the kernel-independent-verify rule rests partly on
   their separation). **Strategy + tradeoffs = its own session.**

## Relates to
- `instance-reinstantiation.md` — the near-term work this principle governs (re-render via anneal-dev).
- `dev-process-adoption.md` — established the "everything through anneal-dev" two-regime routing (this extends it to render + instantiate + enforcement).
- `framework-dev-as-anneal.md` — made anneal-dev a real instance; this asks it to also own rendering/instantiation.
- `anneal-dev-extension-render-gate.md` — the render path's gating question (a piece of sub-question 1).
