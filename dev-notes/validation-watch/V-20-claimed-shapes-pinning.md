## V-20. Basis-body claimed-shapes pinning — does the bounded judgment hold?

**Status: WATCHING.**

**Decision (`core.md` §4.1.4 + `modules.md` §3.4 + `glossary.md`
Coupling shape; commit pending).** The candidate-set form
requires per-D-entry candidates covering "every shape the basis
claims." The closed enum (target-shape / target-uses /
target-behavior) bounds the set to three. **target-uses** has a
mechanical pin: §3.2.2 amendment decisions always include it.
**target-shape** and **target-behavior** have no mechanical
pin — the subagent infers per-basis which shapes apply from
the basis text. Bounded judgment within a structurally-enforced
closed enum.

**Why uncertain.** The basis-body shape (`core.md` §5.2 (a)-(e))
does not carry an explicit "claimed shapes: [list]" field.
Whether the subagent's per-basis shape inference reliably
matches the basis's actual dependencies is the open question.
Adding the explicit field to §5.2 (b) would mechanically pin
all three shapes, removing the residual judgment — but at the
cost of an additional design-decision body field for every
[VERIFIED] D-entry. Pareto cost vs. benefit isn't established
empirically.

**Production signal to watch.** A run where the falsification
candidate set produced `holds` aggregate, followed by a
downstream catch (implement-loopback or verify [ISSUES FOUND])
on a coupling the candidate set didn't cover — and the missed
coupling matches a shape the basis depended on but the
candidate set didn't tag. If observed at n=1, sharpen `core.md`
§5.2 (b) body shape to carry an explicit claimed-shapes
enumeration; the falsification subagent then matches the
candidate set's shape tags against the basis's claimed-shapes
field mechanically.

Closing criterion (WATCHING → FIX-SHIPPED): observed n=1
instance of the production signal; ship the claimed-shapes
field. FIX-SHIPPED → RESOLVED on first observed run where the
mechanically-pinned shapes catch what the bounded-judgment
shape-inference would have missed.

Per `development-process.md` practice 8, this V-N is legitimate
(form depends on whether the bounded-judgment shape-inference
fails empirically — the fix is classifiable
structural-enforcement once observed, but the signal-existence
is the genuinely uncertain question).

---

