# Fable-era recalibration — the framework's tier assumptions, re-examined

## Origin

2026-07-26 session (beat-the-books): two production Clippy auto-battle
runs on a Fable-5 orchestrator with opus falsifiers/verify and sonnet
impl. The Clippy-INSTANCE findings live in
`coding-clippy/todo/fable-era-findings-2026-07-26.md` (HIGH; four lens/
phase amendment candidates with measured fire rates, delta-scoped
falsification rounds, config enum gap). THIS item is the
framework-level half: the operator's observation cuts both ways —
Clippy AND anneal-dev were built by and around Opus; a top tier above
Opus re-opens calibration assumptions in the framework itself, not
just in one instance.

## Framework-level questions the session's evidence bears on

1. **Separate-checker principle: re-validated, tier-independent.** The
   strongest result: a BELOW-orchestrator-tier falsifier productively
   falsified top-tier-authored designs in 6 of 7 rounds, including
   pure orchestrator errors. The framework's core bet (self-blindness,
   not capability, is what fresh context buys) holds upward. Candidate:
   record this as validation evidence (validation-watch entry), not a
   spec change.

2. **Dispatch model-tier semantics under an above-Opus tier.**
   anneal-dev pins `model-tier.md: opus` as the FLOOR ("never
   downgraded"). With fable available: (a) the floor-only semantic
   can't express "verify at fable, produce at opus" cost shaping;
   (b) "top-tier model identifier" instructions drift when the lineup
   moves. Candidate: re-examine the model-tier slot's semantics
   (floor vs per-class routing à la clippy.config/models) at the
   BINDINGS level so every instance inherits the answer. Related
   instance fact: clippy's models enum omits fable entirely.

3. **Orchestrator-inline re-grounding vs dispatch-everything.** When
   the orchestrator tier ≥ checker tier, aggressive inline
   re-grounding of relayed claims (secondary-source rule applied at
   the orchestrator before booking) caught same-day errors at near-zero
   cost, while fresh-context dispatch stayed load-bearing for
   self-blindness only. Framework question: does core.md's isolation
   rationale (§4.2 area) need a sentence distinguishing
   capability-motivated dispatch (obsolete when orchestrator ≥
   checker) from blindness-motivated dispatch (tier-independent,
   keep)? Guard against the failure mode of reading this as "smart
   orchestrator needs no checker" — the evidence says the opposite.

4. **Falsification round economics** (framework side of clippy
   Finding 5): if delta-scoped rounds are adopted, the convergence
   requirement's wording ("[READY] requires a convergence cycle...
   falsification pass over [VERIFIED] decisions") is where the
   full-width-vs-delta semantics actually bind — the fix lands in the
   framework spec section clippy's phase file instantiates, or it
   lands nowhere.

5. **Leanness with usage data, both corpora.** Framework spec: 2,586
   lines; clippy corpus: 2,204; every falsifier/verify dispatch
   re-reads ~950 of the latter. The existing
   `clippy-reference-file-debloat` item now has real usage data (see
   the clippy todo item §Finding 6). Same measurement should run for
   anneal-dev's own dispatch briefs before cutting anything (measure
   then cut — per `core-md-bloat-measure-then-cut`'s existing
   discipline).

## Process

Triage FIRST against existing backlog items (fold-in candidates:
`clippy-category-b-recalibration`, `clippy-reference-file-debloat`,
`verify-model-diversity`, `core-md-bloat-measure-then-cut`) — this
item may mostly DISTRIBUTE into them rather than stand alone; what
remains standalone is #2 (model-tier slot semantics) and the #1
validation-watch entry. Evidence base: the two beat-the-books trackers
(`.clippy/runs/2026-07-26-*.md`) + seven falsification artifacts.
Fresh session, anneal-dev vehicle, together with the clippy todo item.

## Update 2026-07-27 — discovery-dispatch evidence for items 2 + 3 (line-matching run)

Item 3 now has live evidence in BOTH directions, so its question
sharpens from "does core.md need a distinguishing sentence" to "the
distinction is three-way": (a) blindness-motivated dispatch —
tier-independent, keep (2026-07-26 evidence above); (b)
capability-motivated dispatch — obsolete when orchestrator ≥ checker,
replaced by inline re-grounding; (c) NEW: quota-motivated dispatch —
discovery sub-questions statable complete before the answer is known,
routed to a cheaper tier at citation parity (line-matching run cycle 1:
sonnet surface map, 4/4 load-bearing citations re-grounded clean),
while open-judgment reads stay inline (the run's load-bearing find —
quarter-line signature distortion — was unbriefable, surfaced only by
reading). Bearing on item 2: the operator's top tier draws a CAPPED
pool (sub limit), so routing currency is orchestrator-tokens-spent,
not token totals — this decides floor-vs-per-class in favor of
per-class routing and adds a third class candidate (`discovery`)
beside impl/verify at the bindings level. Instance capture:
coding-clippy/todo fable-era findings, Finding 4 (revised 2026-07-27
to the two-directional form). The operator-corpus rendering of the
same rule (CLAUDE.md model-routing cost gloss + dispatch-discipline
discovery-brief exception) landed 2026-07-27 (dotfiles 66fcea0) —
item 2's bindings semantics should stay coherent with that form when
it executes.

## Update 2026-07-27 — live delta-semantics evidence for item 4

The game-matching run's fix cycle (clippy todo, "Evidence addendum"
+ "Amendments from the game-matching fix-cycle", same file as the
instance findings) executed the missing middle tier live:
decision-scoped re-verify — untouched decisions carried forward with
an explicit basis line, the amended decision's citation closure fully
re-attested, finding-closure proven by re-running the ORIGINAL
detection probes (mutants must now die), executable battery never
scoped down. Verify rd2 [PASSED] on that scoping. Bearing on item 4:
when the convergence requirement's wording is re-opened, the delta
semantics should be defined by CITATION CLOSURE of the amended
decisions (mechanical, computable from tracker basis lines), not by
the binary behavior-preserving/fresh classification — the framework
spec section clippy's phase file instantiates is still where this
binds. Also note: the run's compressed cycle was operator-authorized
ad-hoc; the framework change is what makes it protocol-legal.
