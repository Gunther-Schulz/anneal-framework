# Ad-hoc anneal use + graduation to an instance

**Status:** [READY] — exploration, operator-raised 2026-06-03 (operator reports doing it
already, "works reasonably well"). **No skill yet — earn it** (see recommendation). Two
mechanisms, kept separate: (1) ephemeral ad-hoc application; (2) graduation to a real
instance when a domain recurs.

## The two tiers
1. **Ephemeral ad-hoc use** — apply anneal's discipline to a one-off topic in a domain with
   no instance, binding the slots in-context for that single run; nothing persisted.
2. **Graduation** — when an ad-hoc domain recurs, promote it to a derived instance (the
   existing `instantiation-guide.md` process), **seeded by the accumulated ad-hoc evidence.**

## Grounding: ad-hoc = the derivation guide, minus persistence
`instantiation-guide.md`'s front half *is* what an ad-hoc run does:
- **§1 Domain-fit check** (open-ended / verifiable-outcome / recurring-blind-spots) — and it
  already draws the relevant line: *"A fixed procedure is a workflow skill, not an Anneal
  instance."*
- **§2 Inherit-vs-supply** — the fixed method kept, the domain slots bound.
An ad-hoc run is **§1 + §2 done inline + ephemerally**, running the three phases, *skipping*
"write the persistent spec / generate the plugin." So this is not a new mechanism to invent —
it's the guide in **ephemeral mode**.

## Instance? No — category error
An *instance* = **fixed** bindings for a **known** domain. Ad-hoc = **eliciting** bindings for
an **unknown** domain at runtime. An "ad-hoc instance" = an instance with no fixed bindings,
i.e. not an instance. The right artifact is a **thin entry-point + a slot-binding checklist**.

## Recommendation (additive-reflex discipline)
**Codify it first as a section in `instantiation-guide.md`** ("Applying anneal ad-hoc, without
building an instance") — the cheapest move, no new corpus artifact to maintain. **Promote to a
thin invokable skill only if repeated doc-driven use proves too clunky** — which is *literally
anneal's own graduation logic applied to its own tooling.* Don't build a skill/instance before
one's earned.

## The graduation path is the prize — and nearly free
An ad-hoc run is a **derivation probe**: it *empirically tests* the slot bindings a blind
derivation would otherwise *design and hope.* After a few ad-hoc runs in a domain, you have a
tested draft of the instance spec → run the existing guide, *seeded* by that evidence. This
turns instantiation from "design the bindings and hope" into "**promote the bindings you've
already validated**" — anneal's own ethos (ground claims in evidence, don't assert) applied to
instance-creation itself. Strongest argument that this belongs in the framework.

## The load-bearing risk to design against
`instantiation-guide.md` §1 flags it: a domain with no executable verification "still fits, but
verify is weaker." **Ad-hoc is exactly where independent/executable verification silently
degrades into vibes** — the slot most likely hand-waved when moving fast. The ephemeral
checklist **must force** "what counts as independent verification here?" up front, and **record
the strain** when there's none. Lose this and you're running the phase-shell without the rigor
that makes anneal worth anything.

## Timing
The contract-1 de-pollution (just shipped) was triggered by *exactly an ad-hoc anneal run* (the
writing-task "empirical tell" in `clippy-run-findings-dispatch-coupling.md` / `contract1-
depollution-cluster.md`). That work removed the coding-shaped concretions ad-hoc use had to
fight — so ad-hoc-with-light-binding should now work markedly cleaner than the run that
surfaced the problem. Good moment to codify.

## Note — "ad-hoc" may itself split (APF deep-read, 2026-06-03)
anneal is **design-first** (investigate-design before implement) — right for open-ended
*project* one-offs. But for *operational/recurring* ad-hoc domains (event → act → verify,
repeated), APF's **act-first late-binding** (spec concretized at runtime from injected context;
see `anneal-placement-and-improvement-research.md` APF deep-read) may be the better shape. So
ad-hoc use might not be monolithic: open-ended one-offs (design-first, as above) vs operational
loops (act-first). Watch for this fork when codifying the ephemeral mode.

## Relates to
- `instantiation-guide.md` (§1 fit-check + §2 inherit/supply — the ephemeral-mode source).
- `contract1-depollution-cluster.md` (the de-pollution that unblocks clean ad-hoc use).
- `instance-reinstantiation.md`, `planner-instance-exploration.md` (the graduation target = the
  same derivation process).
