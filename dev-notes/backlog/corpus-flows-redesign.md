# Re-design the corpus-work paths into one clear, contained system

**Status:** OPEN — strategic, operator-raised + widened 2026-06-03. **Strategy/design
deliberately deferred to a fresh session.** This file captures the problem + the goal
durably; it is NOT yet a design. (Was filed narrowly as "anneal-dev as the standard
channel"; widened to the full path re-design — anneal-dev-as-the-channel is the likely
*answer*, not the whole question.)

## The problem — the three paths are convoluted

There are three distinct kinds of corpus work, and right now they're tangled — different,
unclear, partly-unenforced routing; cross-repo boundaries we kept tripping over this session:

1. **New instantiation** — derive a brand-new instance for a domain.
2. **Dev work on anneal itself** — edit the framework spec / anneal-dev (method-kernel + corpus-evolution).
3. **Re-rendering existing instances** — propagate spec changes into the rendered plugins.

## The goal

**One clear, contained system** where each of the three paths is well-defined, its boundaries
explicit, and (strong hypothesis) **all three run through anneal-dev** as the single enforced
de-facto channel — so the discipline (Bloat/Fragmentation lenses, render-fidelity verify,
skill-craft review) can't be bypassed, and there's no future drift back into convolution.

## Current state (verified 2026-06-03) — why it's convoluted

- **Re-render existing instances:** prose-mandated through anneal-dev (`development-process.md`,
  `spec/README.md:50`), but **no structural enforcement** — a hand-render breaks only prose.
- **Dev on anneal itself:** runs through anneal-dev (the method-kernel rule), **but** the spec
  lives in `anneal-framework` and anneal-dev is a *separate repo* — the cross-repo render-source
  vs render-target boundary is where most of this session's friction came from.
- **New instantiation:** the `instantiation-guide.md` is a **standalone manual procedure** — it
  routes an instance's *ongoing evolution* to anneal-dev but **not the derivation act itself.**
- Net: three paths, three different routing stories, one of them unenforced and one not routed
  at all. Convoluted.

## The re-design questions (a fresh session)

1. **Define the three paths cleanly** — name each, its inputs/outputs, and the boundaries between
   them (when does "dev on anneal" end and "re-render" begin?).
2. **Route all three through anneal-dev?** Make it the one channel — likely yes; confirm and design
   the instantiation path as an anneal-dev mode/extension, not a separate manual guide.
3. **Enforcement** — does the channel need a structural forcing function (like the skill-craft edit
   gate), or is the stated rule + the verify battery enough? What does that look like for a render path?
4. **Repo merge (the big lever):** should `anneal-dev` and `anneal-framework` **merge into one repo**?
   Much of the convolution is the cross-repo boundary. Merging could make "the spec + the tool that
   evolves/renders it" one unit — but it has real costs (anneal-dev is a packaged installable plugin;
   spec is render-source; the kernel-independent-verify rule rests partly on their separation). The
   merge is *one candidate answer* to the convolution, weighed in the re-design — not assumed.

## Relates to
- `instance-reinstantiation.md` — the near-term render work this would govern.
- `dev-process-adoption.md` (archived) — established the two-regime "everything through anneal-dev" routing; this extends it to instantiation + render + enforcement.
- `framework-dev-as-anneal.md` (archived) — made anneal-dev a real instance; this asks it to own all three paths.
- `anneal-dev-extension-render-gate.md` — the render path's gating question (a piece of #3).
- `anneal-dev-impl-checkpoint-vs-discharge-hook.md` — a concrete #3-enforcement coordination case: anneal-dev's impl-Checkpoint mandates a per-unit commit, but the dev-process rule-corpus discharge hook gates such commits on verify+operator. The two pieces of dev-machinery must be reconciled here (e.g. checkpoint-*save* ≠ release-*commit* for rule-corpus; or scope the hook to merges). Surfaced by the cite-glossary run (F9/D7), confirmed by the harness-tool run (avoided only via carried foreknowledge — i.e. unfixed at source).
- `instantiation-guide.md` — the doc that would change most if instantiation routes through anneal-dev (#2).
