# Framework-spec cleanup — rederive / de-chaos via anneal-dev

**Status:** OPEN — **operator-flagged as the NEXT major effort (2026-06-02)**, once the current [[anneal-dev-impl-skillcraft-gate]] run confirms anneal-dev works end-to-end + lands. Proposed 2026-06-02 (operator: "main anneal was quite chaotic; refactor strongly OR rederive from itself"). **Method-kernel effort** (edits `anneal-framework/spec/*`) → per the refined bootstrap rule ([[dev-process-adoption]]) it DRIVES through anneal-dev + a kernel-independent verify (skill-craft review + operator). FOUNDATIONAL; large.

**Already done (do NOT redo):** the contract-1 de-pollution ([[contract1-depollution-cluster]], DONE 2026-06-02) made the agnostic core domain-independent at the *mechanism* level (removed code-domain leaks: pytest / file:line / code-as-work-product), + a whole-corpus coherence-audit (handoff `a3a2adda5508d9cdf`, 2 fixes `8bfa20b`). The domain-pollution chaos + cross-corpus drift are fixed.

**NOT done — structural / bloat de-chaos.** No dedicated effort has cleaned the spec for *structure / size / clarity*. `spec/core.md` is **978 lines** (large); the de-pollution targeted domain leaks, not general bloat/structure/readability.

**Approach — rederive from itself (anneal-dev).** anneal-dev IS anneal applied to corpus-evolution; its standardized lens set is exactly the de-chaos toolkit — **Bloat, Fragmentation, Leakage, Missed-dependents, Unenforced-rule, Undefined-shorthand**. The refined bootstrap rule now sanctions running it on the kernel (drive + kernel-independent verify), so soundness is guaranteed by the verify, not the driver. Highest-value self-hosting use: anneal cleaning its own foundation.

**Suggested shape:** (1) open with a fresh whole-corpus **coherence-audit** (the 10-lens pass names the structural debt — the map); (2) drive the fixes through **anneal-dev** cycles (its lenses + tracker + the falsification pass, just proven on [[anneal-dev-impl-skillcraft-gate]]); (3) kernel-independent verify each (skill-craft + operator).

**Sequence:** AFTER [[anneal-dev-impl-skillcraft-gate]] lands — that fix makes the cleanup's dispatched impl edits gate cleanly (smoother; not strictly blocking, since spawn-fallback works either way). Don't start before the current run completes.

Relates to [[contract1-depollution-cluster]], [[framework-dev-as-anneal]], [[dev-process-adoption]], [[anneal-dev-impl-skillcraft-gate]].

## Coherence-audit map (2026-06-02, subagent `ac1856832b8712fda`)

Full-systematic 10-lens pass over the kernel (core/modules/glossary/foundation). Honest-termination: Lens 1 (load-bearing) carried the debt (3 HIGH); Lens 9 → 1 MEDIUM; Lens 8 → 0 (explained — contract-1 de-pollution closed leakage; re-run explicitly, not a suspicious zero). The cleanup runs, ranked:

- **S1 (HIGH)** — split `core.md §4.2 implement` (217 ln = 22% of the file, ~9 jobs, un-sub-numbered unlike §4.1/§4.3) into §4.2.x. Behavior-preserving; biggest navigability win; self-contained. Touches ~10 bare-"§4.2" cite-targets.
- **S2 (HIGH)** — de-duplicate falsification-pass mechanics (triplicated: `core.md §4.1.4` + `modules.md §3.4` + `glossary.md`); home the algorithm in modules §3.4, reduce core to requirement+cite (−~40 ln from the spine). 3-file cascade.
- **S3 (HIGH)** — practice-1/practice-8 three-form mis-attribution (the operator-flagged target). The three-form *taxonomy* is practice 8's; practice 1's adherence rule *requires* it. Origin `development-process.md:257`; rendered into `glossary.md:430`, `modules.md:467` + clippy/daneel. Fix upstream, re-render. Cross-triad.
- **S4 (MED)** — consolidate fragmented `[READY]` (§4.1.1–4 + §5.3 duplicate the supporting-facts list) + fix Lens-7 contradiction ("a cycle has two passes" vs the convergence cycle's three). Pairs with S1.
- **S5 (MED)** — link the two foundation roots (`foundation.md` 3 contracts vs `core.md §Purpose` 2-item rubric, unlinked — Lens 9 grounding-chain gap). One sentence; cheapest load-bearing finding.
- **S6 (MED)** — strip validation-watch provenance breadcrumbs from canonical core prose (`core.md:454-456`, `:488-490`); borderline STRIP/KEEP, decide per-instance; sequence last.

**Run sequence:** S5 → S1 → S2 → S4 → S3 → S6. Each a method-kernel anneal-dev run (drive + kernel-independent verify). First cleanup commit carries `Coherence-audit-handoff: ac1856832b8712fda` (practice 12).
