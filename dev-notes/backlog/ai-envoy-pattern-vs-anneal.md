# AI Envoy pattern ↔ anneal — relationship + "formalize envoys?" exploration

**Status:** OPEN — exploratory / research (Phase D), operator-raised 2026-06-03. Captures a
grounded analysis + a sharpened deep-research question for a fresh `/clear`'d run. Not a
committed framework change.

## The term (grounded, light web-check)
**"AI Envoy"** is a real but *emerging* term; **PostHog** appears to be its origin/popularizer
("We built an AI envoy, you can too", `posthog.com/blog/envoy-wizard-llm-agent`). Definition:
a **deterministic, CLI-based surface injected into an AI agent session** that (a) enforces
progression conditions, (b) injects up-to-date docs / agent-rules, (c) corrects hallucinations
(PostHog's case: hallucinated API keys, out-of-date code), (d) "sheepdog" — keeps the agent in
productive territory. Sits in the established **neurosymbolic / deterministic-validation /
"rules LLMs cannot bypass"** family (DEV.to/AWS guardrails series, neurosymbolic literature).

## Relationship to anneal — same spine, different layer
Both attack **model-recall-as-truth (hallucination)** with the same move: ground in **external,
deterministic, re-checkable evidence/enforcement**, not model confidence. anneal's tagline
("Convert AI confidence into AI evidence") IS the envoy philosophy, lifted from tool-layer to
methodology-layer.

- **Envoy = tool layer.** A reliable surface the agent calls for a real answer / a hard rule.
- **anneal = methodology layer.** The **basis rule** (every load-bearing claim cites a re-runnable
  search or located read, never recall) + phases + tracker + the coherent-complete-picture invariant.

**anneal already CONTAINS envoy-shaped pieces:**
1. **Basis-evidence sources ARE envoys** — `rg`/`git`/located reads are the deterministic surfaces
   anneal's basis-artifacts draw on. An AI Envoy is, in anneal's vocabulary, a basis-evidence source.
2. **The hooks ARE envoys (enforcement half)** — `skill-craft-pre-edit.py` + the `commit-msg`
   discharge hook are deterministic CLI surfaces injected to enforce progression + block drift —
   exactly the envoy's "enforce best-practices/versioning, rules LLMs cannot bypass" role.
3. **anneal is itself neurosymbolic** — neural reasoning (investigate-design) + symbolic
   deterministic anchors that can't be overridden (the **evidence-bearing-artifact** rule, closed-set
   enums, the gates). The envoy is the tool-primitive of the same principle.

**Complementary, not competing:** an AI Envoy is an excellent *citizen* of an anneal run (a
basis-source / guardrail); anneal is the *process that decides to consult it + records the evidence*.

## The open design question (the actual exploration)
anneal HAS envoys (hooks + basis-tools) but does NOT *name* "deterministic surface / envoy" as a
first-class concept. Is there value in formalizing it — e.g., an instance **declaring its envoy set**
(the deterministic surfaces its basis-evidence + enforcement draw on), parallel to how it declares
its lens set / verification battery / isolation slot? Weigh against the Additive-reflex anti-pattern
(it may already be adequately covered by basis-evidence + hooks + the verification battery — naming
it might be a concept that doesn't earn its place). Genuine design question; not yet decided.

## Sharpened deep-research question (for a fresh `/clear`'d deep-research run)
> Is "AI Envoy" an established pattern — canonical source (PostHog?), who else uses it, related named
> patterns (MCP servers, guardrail tooling, context-providers, neurosymbolic validation)? And
> architecturally, how does the envoy/deterministic-surface pattern relate to an evidence-mandating
> methodology like anneal — overlap, layering, and what (if anything) each could adopt from the other
> (esp.: should anneal formalize an "envoy/deterministic-surface" slot)?

## Deeper pass (2026-06-03) — concrete mechanics + the CLI-vs-MCP landscape

**Envoy = a CLI the agent runs in its terminal** (PostHog source, grounded): it (a) prints to
stdout → injects real data/docs/rules into the agent's context, (b) mutates project files directly
(`.env`, code, config) — e.g. fetches real API keys via API and writes them in (no hallucination),
(c) "enforces progression conditions — doesn't move to the next step until requirements satisfied"
(succeed-with-correct-output, or fail/block → agent sees failure + retries). Recipe: take existing
CLI → add non-interactive mode → fetch-real-data + inject deterministically → instrument
success/failure → ship updates immediately (no model retraining). **Explicitly NOT MCP** — an envoy
*can configure* MCP, but the envoy itself is a CLI-in-terminal. (Disambiguation: the **"AI envoy"
pattern** (PostHog) ≠ **"Envoy AI Gateway"** (the Envoy-proxy MCP gateway, Tetrate/Bloomberg) — two
unrelated "Envoy"s.)

**This sharpens the anneal mapping — and externally validates a design choice:**
- anneal's deterministic surfaces are **CLI/hook-based, not MCP** — exactly the envoy shape:
  basis-tools (`rg`/`git`/located reads = the "print real data into context" half) + the hooks
  (pre-edit, commit-msg discharge = the "enforce progression, succeed-or-block" half — the discharge
  hook literally won't let a release commit proceed without the verification artifact).
- **External validation:** emerging evidence that **CLI tools beat MCP for agents** (one report:
  +28% task completion, +33% token-efficiency; "CLIs for execution/dev-tools, MCP for shared
  read-only reasoning") supports anneal's CLI/hook-native grounding+enforcement for its
  file-edit/git-native corpus-evolution domain.
- **Neurosymbolic alignment:** "separate reasoning from execution" + "deterministic validation LLMs
  can't override" = anneal's investigate-design (reasoning) vs hooks + basis-rule + verify-battery
  (symbolic, deterministic, un-overridable). anneal is itself a neurosymbolic methodology.

**Refined design question:** anneal binds **"executable verification"** (the *check* half of the
envoy) as an instance slot, but the **data-provision half** (deterministic surfaces that *inject
ground-truth* — the envoy's "fetch real docs/keys") is **implicit**: the basis rule uses `rg`/`git`/
reads but never declares them as a named instance surface. Narrow open question — formalize a
"ground-truth / envoy surface" slot, OR is it already covered by executable-verification + the basis
rule (Additive-reflex check)? This is the sharper version of "formalize envoys?".

## Relates to
- `hooks/` (the existing anneal enforcement-envoys), `spec/core.md` (basis rule + evidence-bearing
  -artifact rule = the data-envoy discipline), `instantiation-guide.md` §3 (the "executable
  verification" binding — the check-half) + §2-5 (where a "ground-truth surface" slot would live).
- Sources: posthog.com/blog/envoy-wizard-llm-agent; jannikreinhard.com (CLI-beats-MCP);
  rudderstack.com (AI agents need two interfaces: CLI + MCP); dev.to/aws guardrails series.
