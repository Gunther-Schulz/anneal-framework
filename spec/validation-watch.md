# Diligence Framework — Validation Watch

Companion to the Diligence-framework spec; not part of it. The spec
states fixed decisions. Some were made best-effort, under genuine
uncertainty. This doc records those — the decision, why it was
uncertain, and the production signal that would prompt revisiting it.
The spec stays pure prescription; the uncertainty is tracked here.

Production signals come from any instance's real runs — Clippy's, or
a future sibling's.

---

## V-1. Standardized lens timing — per-cycle incremental

**Decision (`core.md`).** Standardized lenses are applied every
cycle, incrementally: each cycle's standardized inspection pass
applies the lenses whose scope that cycle's work touched.

**Why uncertain.** Chosen on the fail-safe principle — when
uncertain, check more and check earlier — not on evidence. The one
grounding incident applied the standardized lenses only as a late
correction pass, which was a low-adherence artifact, not a design
choice. There is no comparison between per-cycle and end-only
application; the quantitative value of per-cycle over end-only is
unverified.

**Production signal to watch.** Whether per-cycle standardized passes
mostly come back clean. If they routinely find nothing and findings
cluster only near [READY], end-only sweeping may suffice and
per-cycle is overhead. If per-cycle passes catch things early —
before the design locks them in — per-cycle is confirmed.

---

## V-2. The two-function model

**Decision (`glossary.md`, `core.md`).** The framework's mechanisms
are classified by one of two functions — inspection (with an ad-hoc
or standardized lens source) and gate. The spec is structured on this
model.

**Why uncertain.** The model is distilled from a single
investigation. It revised repeatedly before settling — a
generative/gate split, then a three-way open-looking / lensed / gate
model, then the current two-function model. It is the current working
model, not a measured or proven one.

**Production signal to watch.** Whether mechanisms encountered in real
runs classify cleanly as inspection or gate, and whether the
ad-hoc/standardized lens-source distinction holds. A mechanism that
fits neither function, or a lens that is clearly neither ad-hoc nor
standardized, is a signal the model needs revision.
