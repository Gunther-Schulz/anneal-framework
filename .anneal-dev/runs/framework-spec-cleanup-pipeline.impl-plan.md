# Impl plan — framework-spec-cleanup-pipeline

2 dispatch units, **fully sequential** (Unit 2 depends on Unit 1's rendered
§4.2.x headings for its cite-retargets). No parallel-eligibility claimed — the
units are dependency-ordered, not disjoint, so no disjointness search applies.
Both touch rule-corpus spec files → each dispatched subagent invokes skill-craft
(Skill tool) before editing, per the method-kernel gate.

## Unit 1 — `core.md` §4 re-derivation (first)
Implements: **D2** (core part), **D3** (core §4.1.4 part), **D4** (core part), **D5**, **D6**.
- Element/contract scope: `spec/core.md` only — §Purpose, §4.1 (passes wording + §4.1.1 [READY] home), §4.1.4 (de-dup to requirement+cite), §4.2 (re-org → §4.2.1–8), §5.3 (→ thin bridge), §4.1.2/§4.1.4/§4.2 (strip 3 breadcrumbs); + intra-core cite-retargets (442/649/700/949/953/958 §4.2; 287/300/304 §5.3→§5.2).
- The coherent §4 rewrite is one unit (practice-6 integrate-don't-insert): re-org, de-dup, consolidate, link, strip interweave within core.md's prose.
- Dependencies: first (none).

## Unit 2 — cross-file dependents (after Unit 1)
Implements: **D2** (cross-file cite-retargets), **D3** (modules §3.4 = retained home, confirm no edit needed), **D4** (glossary Pass-entry passes-fix).
- Element/contract scope: `spec/modules.md` (§4.2 cite-retargets 60/95/253/265/279/280/288 → §4.2.x), `spec/glossary.md` (Pass entry 232–233 "exactly two" → two-by-default+convergence-third; §4.2 cite-retargets 122/207/215/227/250/328/338/343), `instantiation-guide.md` (§4.2 cite 94 → §4.2.3 Isolation).
- Dependencies: after Unit 1 (cite-retargets resolve against Unit 1's actual §4.2.x headings, not just the locked scheme — coherence over the marginal parallelism gain on 3 small files).

## Release tail (post-verify, not impl units)
Rendered §4 dependents (anneal-dev/clippy/daneel/campaign-craft phase files) are
D1 target-behavior [CONDITIONAL] — re-rendered at the release loop (development-process
step 3/6), surfaced by anneal-dev's `render-and-open-diff` extension on verify [PASSED].
Method-kernel verify adds the kernel-independent review (skill-craft self-review + operator).
