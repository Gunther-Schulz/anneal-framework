# Dispatch brief — "reference by letter" is unenforceable for a context-less spawned agent

**Status:** [READY] — finding (cross-session clippy run, 2026-06-02). Framework/
instance dispatch-mechanism gap. Distinct from the cluster in
[[clippy-run-findings-dispatch-coupling]] (model/isolation/behavioral) and from
[[anneal-dev-impl-skillcraft-gate]] (invoking skill-craft from dispatch).

**Gap.** The dispatch-brief template says the brief MUST NOT restate the load/
return boilerplate ((a)/(d)) — "reference them by section letter only." But a
freshly-spawned **general-purpose subagent has zero shared context**: it cannot
resolve "(a)/(d)" — the only way it obtains that content is the orchestrator
handing it over. So "reference by letter" presumes a shared context that does
not exist; the orchestrator is forced to **reconstruct the mandated boilerplate
by hand every dispatch** → (1) protocol reliability rides on the AI faithfully
re-deriving it, (2) it is exactly where a brief silently *diverges* from the
canonical protocol, (3) restating (a)/(d) violates the template's own MUST-NOT.
Owned, observed deviation in the dump's run.

**Root shape.** Today brief = orchestrator reconstructs everything. Should be =
fixed protocol boilerplate (one source) + per-unit slots (orchestrator-authored).
Any reconstruction is a drift surface.

**Fix candidates (ranked):**
1. **Ship dedicated anneal/clippy subagent types** (`clippy-impl`,
   `clippy-verify`, `clippy-falsify`) whose system prompt is a thin bootstrap:
   "read `phases/<phase>.md` (a)/(d) from the skill dir, follow verbatim; apply
   the self-check; halt-and-loopback on any actioned finding." Dispatch then
   carries only (b) tracker path + (c) unit scope. Mandated parts become
   *structural* — the orchestrator can't restate (a)/(d) because it no longer
   authors them; also lets a verify-agent ship with no write tools. **Rule:** the
   agent prompt must *point at* the phase file, not inline it (one source of
   truth; no drift on a skill update).
2. **Fill-in-the-blank brief template** in the skill (`{skill_dir}`,
   `{tracker_path}`, `{unit_D#}`, `{unit_scope}` slots) — orchestrator
   instantiates mechanically. Weaker (orchestrator still emits the boilerplate).
3. **Minimal spec change**: replace "reference by letter" with the exact verbatim
   bootstrap-pointer line the orchestrator must emit (path + pointer), closing the
   "presumes shared context" hole even without #1/#2.

**Level.** Framework (§4.2 dispatch-brief) + clippy render (+ possibly
plugin-shipped agents). Relates to [[clippy-run-findings-dispatch-coupling]],
[[anneal-dev-impl-skillcraft-gate]].
