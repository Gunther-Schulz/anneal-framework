# In-flight cross-cycle learning — the recurrence signal, run live: patch-sooner (speed) + basin-jump (quality)

**Status:** [DESIGN] — exploratory design, operator-raised 2026-06-08 (session 14). The **fast-loop twin** of
`framework-gap-receipt`: the *same* recurring-falsification-class signal, consumed **within a run, in-flight**
(next cycle) instead of cross-run, post-hoc (framework edit). Two consumers — a **speed** branch and a
**quality** branch. Built on the receipt's class-tally mechanism (shares it). When built: method-kernel
(cycle machinery, `core.md` §4.1) + hooks + corpus-evolution → anneal-dev + kernel-independent verify. Not
yet sequenced into NEXT-UP; naturally **downstream of `framework-gap-receipt`** (reuses its tally).

## The signal (and the soundness key — read first)
Within one run, **tally the fresh-context falsification findings by class across the run's cycles** (the
receipt's mechanism, run live). A class that recurs is a "**this run has a blind-spot**" signal.

**Load-bearing soundness:** the signal MUST be **orchestrator-computed from the falsification artifacts**
(external, objective) — **NOT** a self-review instruction to the forming context. A "review your own gaps and
adapt" instruction is the **self-certification trap**: the same context that *has* the blind-spot is asked to
notice its own blind-spot — the loaded-but-inert / can't-enumerate-own-blind-spots failure the whole framework
avoids (it's *why* falsification is fresh-context). Operator interjection works because the operator is
*external*; an instruction is not. Externalize the signal (the falsification artifacts are the external
check); don't ask the context to self-review. *(This is the empirical weak→strong gap: the system can
**articulate** a gap when the operator asks post-hoc; converting that to **standing in-flight
behavior-change** needs the external signal, not a prompt.)*

## Branch A — patch-sooner (SPEED; same output, fewer cycles)
Inject a **targeted directive** into the next cycle's investigation/forming brief ("this run has under-scoped
co-producers twice — investigate producers explicitly this cycle"). The loop converges in fewer cycles by
pre-empting the recurring class. **Value = cost (cycle count), not correctness** — the loop already converges
to the right answer (Unit-31 got there in 9 cycles); this gets there cheaper. Per "cost is the operator's
call," an efficiency lever.

**Also the "good priming" that could replace the static priming we removed** (`investigation-pass-lens-priming`):
not a speculative fixed checklist (crowds breadth → removed), but **one directive earned by this run's
demonstrated falsification pattern** (targeted, evidence-justified, far lighter). Don't pre-load assumptions
about what the AI will miss; feed back what it has *demonstrably* missed.

## Branch B — basin-jump (QUALITY; raises the ceiling — the major find)
The recurrence's *quality* reading: a class keeps recurring because the current design **structure** keeps
generating it — you're patching instances of a problem the structure makes inevitable. Treat recurrence as a
trigger to **question the design basin**: spawn a **structurally-different rival** that makes the whole class
*impossible*, rather than patching the Nth instance. (Unit-31: enumeration/co-producer fired cycles 3 *and*
5 → the quality move is "values route through shared sinks with ambiguous producers; what if the design
carried explicit provenance typing / a single-producer invariant so the class can't arise?")

**Why it's quality, not disguised speed:** the patch-loop, given infinite cycles, does **not** reach the
restructured design on its own — each cycle patches the *current* structure; the rivals mechanism (`core.md`
§4.1, "≥2 viable rival approaches") only fires when investigation *surfaces* a rival. If the forming anchored
on basin A and never generated B, the loop converges to best-of-A with zero deltas and **stops — it never
learns B exists.** The recurrence signal is what *prompts generating B*, making a better basin **reachable**
that was otherwise unreachable. Destination changes → ceiling rises → quality.

**Why major — it completes the framework's own metaphor.** The cycles currently do **within-basin** annealing
(perturb = patch D-items → refine the first structure to its best form). Lever-2 ("convergence = local-optimum
escape", `anneal-empirical-validation-experiment`) as built escapes the *first-plausible-design* optimum but
only to the best point of *that basin*; it does **not** do **between-basin** escape (a different structure).
Recurrence is the classical-annealing **"stuck" signal**; basin-jump is the **"raise temperature"** move. The
framework currently delivers half its namesake; this is the unbuilt half — and it sharpens Lever-2
(within-basin escape = built; between-basin = this). It also formalizes a *specific* operator interjection —
"you keep patching the same thing; should you restructure?" — distinct from "where are the gaps?"
(coverage/speed).

## The mechanism (operator's instinct: hooks)
A hook at the cycle boundary computes the class tally (mechanical, from the structured falsification
artifacts — orchestrator-side, not self-review) and, on recurrence, injects the Branch-A directive and/or
surfaces the Branch-B basin-question. The `convergence-cycle-mechanical-enforcement` family is the substrate.
Hooks do mechanical detection + injection; they need no judgment because the signal *is* mechanical (a
recurrence count) and the action stays conservative (below).

## Honest bounds (or it overclaims)
1. **Mechanical trigger, un-enumerable payoff.** The trigger guarantees the *question* gets asked / the
   directive injected (automatable); whether the restructure is good / the directive helps is the forming
   context's irreducible creative act. Branch B raises the ceiling's *possibility*, realized only if forming
   can generate a good restructure when prompted. Mechanical trigger, un-enumerable value — same shape as
   everything this session.
2. **Recurrence ≠ failure ≠ bad basin.** A class can recur because the problem is hard, not the structure
   wrong — or because the loop is *working as designed*. So: **surface the basin-question + spawn a structural
   rival; never auto-restructure / auto-redirect.** The normal falsification + rivals-comparison adjudicates;
   auto-acting would thrash. Kernel/high-stakes → the basin-jump candidate surfaces to the **operator**
   (in-flight has no operator otherwise).
3. **Bounded to caught classes** — same wall as the receipt; can't trigger on a novel escape (those never
   recur in the pattern). The missed side stays post-hoc/operator (`self-review-missed-side`).
4. **Dynamic crowding / instability.** A "focus on X" directive narrows breadth and can oscillate (chase the
   last gap). So: **one earned directive, not an accreting pile** (the additive-reflex, dynamic), and
   conservative/informational, to preserve the broad re-form that makes convergence stable
   (`lens-crowding-vs-broad-search`).

## Relates to
- `framework-gap-receipt` — the **slow-loop twin** (same recurring-class signal; cross-run post-hoc →
  framework edit). This is within-run in-flight → next-cycle. Reuses its class-tally; build on top.
- `investigation-pass-lens-priming` — Branch A is the **dynamic earned-priming** that could replace the static
  priming removed there (speculative checklist → evidence-earned directive).
- `convergence-cycle-mechanical-enforcement` — the hook substrate for in-flight detection + injection.
- `lens-crowding-vs-broad-search` — the dynamic-crowding risk (bound 4).
- `anneal-empirical-validation-experiment` — Lever-2 (convergence / local-optimum escape); Branch B sharpens
  it (within-basin built; between-basin = this).
- `core.md` §4.1 rivals mechanism ("≥2 viable rival approaches") — the structural-rival generator Branch B triggers.
- `self-improvement-signal-architecture` — the in-flight consumer of the **Q1 caught-side** signal (bounded to
  caught, per the umbrella's prune analysis).
- Origin: operator, 2026-06-08 (session 14).
