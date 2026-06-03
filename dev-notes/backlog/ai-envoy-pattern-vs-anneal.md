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

## Relates to
- `hooks/` (the existing anneal envoys), `spec/core.md` (basis rule + evidence-bearing-artifact rule),
  `instantiation-guide.md` §2-5 (the instance slot set — where an "envoy slot" would live if formalized).
- Sources: posthog.com/blog/envoy-wizard-llm-agent; dev.to/aws guardrails series.
