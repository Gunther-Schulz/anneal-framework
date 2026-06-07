# f0-render-conventions — cycle 3 (convergence) intent-falsification-pass

Fresh-context dispatch (subagent `aebac44b2b059c540`, opus, criteria-first). Attacked the locked
[VERIFIED] design D1–D4 against R1–R4. **Result: D-track delta** — mechanical falsification pass
**SKIPPED this cycle** (`mechanical skipped: intent-delta this cycle`). Design NOT [READY].

## Per-R# attack lines
- **{R1, refutation:** enumerated guide §2 slot set (`:82-108,:137`) vs `ls instance-template/spec/`
  (no isolation.md), **outcome: finding}** (F-C — second enumeration surface at guide `:18`).
- **{R2, refutation:** cross-read guide §2 (`:108,:120,:135-140`), README (`:24-50`), instances
  (clippy `bindings.md:169`, anneal-dev `:124`), **outcome: finding}** (F-A, F-B).
- **{R3, refutation:** extracted anneal-dev + clippy bindings left columns; ran `rg '(core|modules)\.md
  …§' anneal-dev/spec/bindings.md` → 30 matches, **outcome: finding}** (F-D).
- **{R4, refutation:** checked D2 file-form vs clippy's section-form realization for the re-render gate,
  **outcome: finding}** (R4 = conjunction over R1–R3; F-B/F-D break it).

## Per-finding lines + orchestrator-computed verdicts
- **F-B** {criterion: R2; refutation: `grep 'Dispatch isolation' instantiation-guide.md`→`:108`;
  clippy `bindings.md:169`, anneal-dev `:124` = sections, no isolation.md; route:
  **mechanical-falsification-candidate** — target-dependents of D2 basis; predicate
  `expected-match:isolation.md` over guide+instances}. **VERDICT: falsified** (no isolation.md
  anywhere but the proposed scaffold; guide+both instances use a `bindings.md` section). → **D2
  [INVALIDATED]→[PENDING]**.
- **F-C** {criterion: R2; refutation: `grep 'placeholder file for every slot' instantiation-guide.md`
  →`:18` (outside README); route: **mechanical-falsification-candidate** — target-dependents of D3
  basis; predicate `any-outside-scope:instance-template/README.md`}. **VERDICT: falsified** (guide `:18`
  is a slot-enumeration surface outside the README; D3's "sole enumeration" premise false). → **D3
  [INVALIDATED]→[PENDING]**.
- **F-D** {criterion: R3; refutation: `rg 'core\.md §3\.2' anneal-dev/spec/bindings.md` → rows 42/43
  cite core.md in-cell; route: **mechanical-falsification-candidate** — target-behavior of D4 basis;
  predicate `expected-match:` glossary-term-only left column}. **VERDICT: falsified** (the left-column
  cells point the author at core.md, not the glossary D4 sharpens; glossary-define alone does not close
  R3's firewall). → **D4 [INVALIDATED]→[PENDING]**.
- **F-A** {criterion: R2; refutation: `sed '135,142p' guide` ("four required") vs `sed '24,42p' README`
  (3+2 buckets, isolation in neither); route: **[VERIFIED — surfaced]**} — judgment: D3's
  "required-mechanism" bucket-placement vs the guide's "four required" grouping; terminal, informs the
  D3 revision.

## Most serious (subagent summary, orchestrator-concurred)
F-B: the design scaffolds isolation as a file while the guide's worked example + both instances treat
it as a `bindings.md` section — introducing the exact "where does the slot live?" inconsistency R2
forbids, feeding R4. Coupled with F-D: D4 cannot satisfy R3 because the left-column cells still cite
`core.md §3.2` and no D-entry removes them.
