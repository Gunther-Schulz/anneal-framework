# Impl plan — spec-cleanup-s3-attribution

**1 dispatch unit** (the whole fix is a small coherent wording change across 3
files in one repo; no cross-unit dependency to split on). Sequential/single →
dispatched to ONE subagent, in-place under the Integrity check. **Now that the
subagent-dispatch hook is fixed, this dispatches to a subagent normally** (no
spawn-fallback) — a real exercise of the hook fix in the impl phase. The subagent
invokes skill-craft before editing (all 3 files are gated rule-corpus).

## Unit 1 — S3 attribution fix + glossary breadcrumb strip (first/only)
Implements: **D2** (attribution) + **D3** (strip).
- Element/contract scope, all in the `anneal-framework` repo:
  - `development-process.md:257` — rephrase "practice 1's three-form enumeration discharge" → attribute forms to practice 8, enumeration to practice 1.
  - `spec/glossary.md:433` — same rephrase; **+** strip V-N from 3 entries (Recall pool, False-[READY], Convergence exception), keeping each entry's spec cross-ref.
  - `spec/modules.md:467` — same rephrase.
- Dependencies: first (none). No render tail (F3 — clippy/daneel don't carry the attribution).
- Behavior-preserving (the adherence-gap rule is unchanged; attribution clarity + breadcrumb removal only).
