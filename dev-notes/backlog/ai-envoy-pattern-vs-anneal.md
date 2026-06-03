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

## Relationship to anneal — adjacent, not aligned (REVISED after the deeper pass)
**Initial framing ("anneal's hooks/basis-tools ARE envoys; same spine, different layers") was an
over-claim** — pattern-matching on a broad shared principle. The concrete PostHog picture corrects it.

- **They share only the WIDE umbrella:** reject model-recall-as-truth, lean on deterministic/external
  grounding. That tent also holds RAG, tool-use, guardrails, neurosymbolic — sharing it is weak
  evidence of a deep relation. ("neurosymbolic" for anneal is a loose analogy, not a classification —
  its "symbolic" half is deterministic *discipline*, not formal symbolic AI.)
- **They are different KINDS of thing — orthogonal anti-hallucination strategies:**
  - **Envoy = a DELEGATION tool.** Defined by *delegation + ground-truth-provision*: the agent hands a
    domain task to a purpose-built CLI that *does it right* (fetches the real key, writes current SDK
    code). It *substitutes* a correct tool-action for a hallucination-prone one.
  - **anneal = a METHODOLOGY.** A process the agent *follows* to evidence + structure its OWN work
    (basis rule, phases, tracker, separate-context verify). It *disciplines* reasoning; it doesn't do
    the task for the agent.
- **Why the earlier mapping fails on inspection:** anneal's **hooks are guardrails, not envoys** — they
  *block*, they don't *do/provide ground-truth*; a guardrail overlaps only the envoy's *secondary*
  (enforcement) aspect, not its *defining* (delegation + ground-truth) one. `rg`/`git` are *generic*
  tools the basis rule mandates, not purpose-built domain envoys.

**The one genuine, NARROW relation that survives — composition, not identity:** an envoy could be a
*tool an anneal run calls* (a basis-evidence source, or a deterministic action an implement-unit
delegates to). anneal *can use* envoys; anneal is not an envoy, and its hooks are not envoys.

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

**One finding here survives the relationship-revision (it's about anneal's tool-CHOICE, NOT about
anneal being an envoy — see REVISED relationship above):** anneal grounds + enforces via **CLI/hooks
(`rg`, `git`, the python hooks), not MCP**, and the emerging **CLI-beats-MCP** evidence (one report:
+28% task completion, +33% token-efficiency; "CLIs for execution/dev-tools, MCP for shared read-only
reasoning") supports that tool-choice for anneal's file-edit/git-native domain. (Independent point;
does NOT imply anneal's hooks "are envoys" — they're guardrails.)

**Refined design question:** anneal binds **"executable verification"** (the *check* half of the
envoy) as an instance slot, but the **data-provision half** (deterministic surfaces that *inject
ground-truth* — the envoy's "fetch real docs/keys") is **implicit**: the basis rule uses `rg`/`git`/
reads but never declares them as a named instance surface. Narrow open question — formalize a
"ground-truth / envoy surface" slot, OR is it already covered by executable-verification + the basis
rule (Additive-reflex check)? This is the sharper version of "formalize envoys?".

## PostHog's concrete envoy (the `@posthog/wizard`) — refines "what an envoy is"
`@posthog/wizard` (npm, MIT, Node, github.com/PostHog/wizard, v2.5.0) — an **"agentic CLI" that
wraps the Claude Agent SDK**. An OUTER coding agent (Claude Code etc.) runs it non-interactively:
`npx @posthog/wizard --ci --api-key $KEY --install-dir .`. It: detects the framework (16+), **fetches
the REAL API key** from the user's account → writes `.env` (kills key-hallucination), then uses the
wrapped agent to **read the user's code + inject the CURRENT PostHog SDK integration** (events,
config) — defeating training-lagged/stale-code. Refinements this forces on the model above:
- **An envoy is not "pure deterministic CLI" — it's a CLI that gives the outer agent a constrained,
  ground-truth-bearing *sub-tool* (here itself an LLM via Claude Agent SDK).** Determinism comes from
  *real data* (keys), *fixed flow* (`--ci`), and *current templates* — not from being LLM-free.
- **Envoy ⟂ MCP are complementary, confirmed:** the wizard *also* runs `npx @posthog/wizard mcp add`
  to install the PostHog MCP server. Envoy = one-shot correct *setup*; MCP = the *ongoing* interface
  the envoy installs.
- **Self-application parallel:** PostHog uses an agent (Claude Agent SDK) to build the tool that makes
  *other* agents reliable — directly analogous to anneal-dev (an agent methodology) evolving anneal.

## Relates to
- `hooks/` (the existing anneal enforcement-envoys), `spec/core.md` (basis rule + evidence-bearing
  -artifact rule = the data-envoy discipline), `instantiation-guide.md` §3 (the "executable
  verification" binding — the check-half) + §2-5 (where a "ground-truth surface" slot would live).
- Sources: posthog.com/blog/envoy-wizard-llm-agent; github.com/PostHog/wizard (the MIT impl);
  posthog.com/docs/ai-engineering/ai-wizard; jannikreinhard.com (CLI-beats-MCP); rudderstack.com
  (CLI + MCP two-interface pattern); dev.to/aws guardrails series.
