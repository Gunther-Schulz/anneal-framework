# Framework-spec cleanup — rederive / de-chaos via anneal-dev

**Status:** OPEN — **operator-flagged as the NEXT major effort (2026-06-02)**, once the current [[anneal-dev-impl-skillcraft-gate]] run confirms anneal-dev works end-to-end + lands. Proposed 2026-06-02 (operator: "main anneal was quite chaotic; refactor strongly OR rederive from itself"). **Method-kernel effort** (edits `anneal-framework/spec/*`) → per the refined bootstrap rule ([[dev-process-adoption]]) it DRIVES through anneal-dev + a kernel-independent verify (skill-craft review + operator). FOUNDATIONAL; large.

**Already done (do NOT redo):** the contract-1 de-pollution ([[contract1-depollution-cluster]], DONE 2026-06-02) made the agnostic core domain-independent at the *mechanism* level (removed code-domain leaks: pytest / file:line / code-as-work-product), + a whole-corpus coherence-audit (handoff `a3a2adda5508d9cdf`, 2 fixes `8bfa20b`). The domain-pollution chaos + cross-corpus drift are fixed.

**NOT done — structural / bloat de-chaos.** No dedicated effort has cleaned the spec for *structure / size / clarity*. `spec/core.md` is **978 lines** (large); the de-pollution targeted domain leaks, not general bloat/structure/readability.

**Approach — rederive from itself (anneal-dev).** anneal-dev IS anneal applied to corpus-evolution; its standardized lens set is exactly the de-chaos toolkit — **Bloat, Fragmentation, Leakage, Missed-dependents, Unenforced-rule, Undefined-shorthand**. The refined bootstrap rule now sanctions running it on the kernel (drive + kernel-independent verify), so soundness is guaranteed by the verify, not the driver. Highest-value self-hosting use: anneal cleaning its own foundation.

**Suggested shape:** (1) open with a fresh whole-corpus **coherence-audit** (the 10-lens pass names the structural debt — the map); (2) drive the fixes through **anneal-dev** cycles (its lenses + tracker + the falsification pass, just proven on [[anneal-dev-impl-skillcraft-gate]]); (3) kernel-independent verify each (skill-craft + operator).

**Sequence:** AFTER [[anneal-dev-impl-skillcraft-gate]] lands — that fix makes the cleanup's dispatched impl edits gate cleanly (smoother; not strictly blocking, since spawn-fallback works either way). Don't start before the current run completes.

Relates to [[contract1-depollution-cluster]], [[framework-dev-as-anneal]], [[dev-process-adoption]], [[anneal-dev-impl-skillcraft-gate]].
