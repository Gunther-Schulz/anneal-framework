# Run: anneal-dev-rerender

- **Status:** PASSED
- **Phase:** investigate-design
- **Mode:** auto-battle (operator-requested) + render-commit gate (operator owns the render commit)
- **Task:** Re-render the anneal-dev plugin skill files (KEYSTONE, instance-reinstantiation Phase B step 2). FAITHFUL re-render (propagation), NOT de-bloat. Carry: (1) §4 spec-cleanup content, (2) the cite-glossary firewall (§-cites → glossary terms), (3) the harness-tool guide-note trace. CORPUS-EVOLUTION (work product = render OUTPUT `anneal-dev/plugin/*`, not kernel source) → render-fidelity verify is the critical check; no operator-soundness kernel gate; operator owns the render commit (present diff first).

> Run-state here (`anneal-framework/.anneal-dev/runs/`); WORK PRODUCT spans to the sibling `anneal-dev` repo (`plugin/skills/anneal-dev/{SKILL.md, phases/*, references/*}`, 2112 ln / 8 files). anneal-dev repo at HEAD `ee9e2e6` on main, clean. Re-rendering the REPO files does not affect the running cache (0.1.1); lands for future install.

---

## F-track (findings)

Divergence audit by subagent `a8dfe52f70ab7d08f` (reverse render-fidelity, all 8 files vs current source). KEY: the re-render is LIGHT — the big §4-cleanup items have ~zero render impact.

- **F1** [VERIFIED — addressed] Firewall §-cite leak-set in the render = **exactly 5** (mechanical check `rg -U '(core|modules)\.md[^\n]{0,4}§' anneal-dev/plugin/skills/anneal-dev`): SKILL.md:297 (`modules §2.1`), implement.md:132 (`core §4.2`), foundations.md:247 (`core §3.2.2`), post-run-review.md:8 (`modules §4`), post-run-review.md:10 (`modules §4.2`). The renders already apply the firewall to ~96% of the domain spec's §-cites; these 5 leak through. — basis: audit's mechanical grep (5 hits, no wrapped/bare misses). addressed by D2.
- **F2** [VERIFIED — addressed] Content-fidelity divergences = **3 hard V-N breadcrumb strips** (cleanup D6 stripped V-N from core; current `core.md` has ZERO — `rg 'V-[0-9]' spec/core.md` → none): investigate-design.md:151-152 (V-5), :256 (V-5), implement.md:35 (V-24). The heavy §4-cleanup items have ~zero render impact: falsification de-dup ALREADY mirrored (investigate-design carries requirement+cite, tracker.md owns the closed-set — matches post-D3 core); §4.2.x sub-numbers never surface (firewall→terms); foundations.md [READY] already the post-D4 thin-bridge shape. — basis: audit clause-by-clause + `rg 'V-[0-9]' spec/core.md`. addressed by D3.
- **F3** [VERIFIED — non-issue] The harness-tool run-state block (SKILL.md:31-37) traces FAITHFULLY to the merged instantiation-guide §2 note (all 4 load-bearing clauses present) — no change. — basis: audit clause-compare SKILL.md:31-37 ↔ instantiation-guide.md:93-101.
- **F4** [VERIFIED — deferred] Out-of-scope observations (filed, not fixed here): (a) `anneal-dev/spec/*` carries its OWN ~73 framework §-cites (e.g. bindings.md:94 `§1(a)`) — the firewall applies to instance SPECS too, but that's a METHOD-KERNEL edit (`anneal-dev/spec/*`), separate from this render run → file `apply-cite-glossary-to-anneal-dev-spec`; (b) tracker.md:213-226 [READY] reduced near-dup = de-bloat/consolidation opportunity, NOT a fidelity break (faithful-re-render excludes de-bloat); (c) tracker.md:279 (example ledger line) + verify.md:87 (`§1(a)`) pass the firewall's mechanical check (no file prefix) → leave. — basis: audit borderline/out-of-scope notes. deferred per D4 (trigger: the spec-firewall item / next anneal-dev re-render).

## D-track (design decisions)

- **D1** [VERIFIED] SCOPE — the re-render edits **5 files** in `anneal-dev/plugin/skills/anneal-dev/`: `SKILL.md`, `phases/implement.md`, `phases/investigate-design.md`, `references/foundations.md`, `references/post-run-review.md`. Change-set = 5 §-cite re-points (F1) + 3 V-N breadcrumb strips (F2). FAITHFUL re-render only. (verify.md, references/{lenses,tracker}.md = clean of in-scope changes.) EXCLUDED with basis: the soft [READY] near-dup (de-bloat, F4b), the 2 borderline bare-§ (pass the firewall check, F4c), anneal-dev/spec's own §-cites (method-kernel, separate, F4a). — basis: F1, F2, F3 (the audit's complete enumeration; mechanical firewall check = 5).
- **D2** [VERIFIED] THE 5 RE-POINTS → glossary terms: SKILL.md:297 `modules §2.1` → drop the §; reference the Name/Question/Scope lens-entry shape (placeholder text); implement.md:132 `core §4.2` → "Integrity check" / the Isolation slot (`bindings.md` Isolation slot already cited adjacent at :131); foundations.md:247 `core §3.2.2` → glossary **Coupling shape** (target-behavior); post-run-review.md:8 `modules §4` → glossary **Post-run review**; post-run-review.md:10 `modules §4.2` → glossary **Post-run review** (the no-persistence rule is part of that term's home). — basis: F1 + glossary-headword lookup (audit). Realization (exact phrasing) at impl, faithful to the term + the adjacent source.
- **D3** [VERIFIED] THE 3 STRIPS — remove the V-N breadcrumbs (no current source post-cleanup): investigate-design.md:151-152 (V-5), :256 (V-5), implement.md:35 (V-24). Strip the breadcrumb, preserve the surrounding rule prose. — basis: F2 (`rg 'V-[0-9]' spec/core.md` → none).
- **D4** [VERIFIED] EXCLUSIONS (committed, file-don't-defer): file `apply-cite-glossary-to-anneal-dev-spec.md` (the anneal-dev/spec §-cite debt + the soft [READY] near-dup as a consolidation note), a method-kernel follow-on; leave the 2 borderline bare-§ (firewall-check-clean). — basis: F4.

---

## Cycle 2 (convergence — D1 FALSIFIED) + Cycle 3 (re-formation)

Cycle-2 convergence falsification (`a35fcd294e34c42d0`, fresh, re-derived independently): D1
falsified (a missed content divergence); D2, D3 hold. Cycle 3 re-forms D1.

### F-track
- **F5** [VERIFIED — addressed] (cycle 2→3): a 4th content divergence the audit/D1 missed — the
  spec-cleanup §5.3 collapse ([READY] "Relationship" full-restatement → thin status→[READY] bridge,
  commit bf32f9c) was NOT propagated to the renders. Both `foundations.md:391-404` (CONFIRMED by
  orchestrator direct read: full restatement vs thin core.md §5.3:915-922) AND `tracker.md:213-226`
  (same restatement) still carry the OLD full [READY] supporting-facts list. The full list
  legitimately lives once in `investigate-design.md` (← §4.1.1); these two should be thin bridges.
  — basis: cycle-2 falsification D1 + direct reads (foundations.md:393-404, core.md:915-922,
  tracker.md:213-226). addressed by re-formed D1.

### D-track
- **D1** [INVALIDATED] (cycle 2): change-set "5 re-points + 3 strips" contradicted by F5 (a missed
  §5.3-collapse propagation). — basis: cycle-2 falsification (aggregate falsified).
- **D1** [PENDING] (cycle 2): reopened. — basis: tracker.md (falsified → [INVALIDATED]→[PENDING]).
- **D1** [VERIFIED] (cycle 3, re-formed): change-set = **5 §-cite re-points** (F1) + **3 V-N
  breadcrumb strips** (F2) + **2 [READY] thin-bridge propagations** (F5): render `foundations.md:391-404`
  and `tracker.md:213-226` [READY] sections → re-render faithful to the current thin `core.md §5.3`
  (gate via status tags + point to the [READY]-judgment home; drop the full supporting-facts
  restatement, which stays once in `investigate-design.md` ← §4.1.1). foundations.md CONFIRMED
  divergent; tracker.md rendered-faithful-to-its-source with render-fidelity verify as backstop.
  Files now touched: SKILL.md, phases/{implement,investigate-design}.md, references/{foundations,
  tracker,post-run-review}.md (6 files). — basis: F1, F2, F5; the cycle-2 falsification (firewall=5
  + de-dup-mirror independently re-confirmed; only the §5.3 propagation was missing).
  - de-dup mirror + firewall (5) carried over from cycle 1, independently re-confirmed cycle 2 — not re-opened.

---

## Cycle 4 (convergence — D1 FALSIFIED again) + Cycle 5 (re-form to section-level) — PAUSED for operator

Cycle-4 fresh convergence falsification (`a8568c6e7efe41151`): a 3rd §4-content divergence (the
two-vs-three-passes reconciliation, bf32f9c §4.1). Orchestrator-confirmed (render investigate-design.md:9-10
vs core.md:257/271-272). The audit underestimated the §4 render impact (it's section-level, not "light-touch").

### F-track
- **F6** [VERIFIED — addressed] 3rd divergence: bf32f9c §4.1 reconciled the cycle pass-count ("two passes" → "two by default" + "convergence adds a third pass"); render investigate-design.md:9-10/:35 carries the OLD absolute framing. — basis: render :9-10 vs core.md:257/271-272 (direct read). addressed by re-formed D1 (section-level).
- **F7** [VERIFIED — addressed] META: the investigation-pass audit's completeness CONCLUSION ("no clause rewrites / light-touch") was unreliable — 2 convergence falsifications each found a §4 divergence it missed. The audit eyeballed the render vs current spec instead of diffing the §4-re-derivation source-delta (bf32f9c). The orchestrator over-trusted a secondary-source CONCLUSION (recorded the audit's completeness call as F2 [VERIFIED] cycle 1) — basis-rule "Secondary sources": a sub-agent's cited facts are basis, its interpretation/completeness-conclusion is not. — basis: cycles 2+4 falsifications. addressed by the re-scope + a filed method finding + the operator retrospective.

### D-track
- **D1** [INVALIDATED]→[PENDING] (cycle 4): line-level "5 re-points + 3 strips + 2 [READY]" contradicted by F6 (a 3rd divergence the line-level enumeration missed). — basis: cycle-4 falsification.
- **D1** [PENDING→re-form] (cycle 5, SECTION-LEVEL): change-set = (A) 5 firewall §-cite re-points + (B1) 3 V-N breadcrumb strips + (B2) **a FAITHFUL re-render of the §4/§5.3-derived render content against the CURRENT core.md §4/§5.3** — investigate-design.md (cycle/passes/[READY]/convergence/falsification), foundations.md + tracker.md ([READY] relationship), and a clause-check of implement.md/verify.md (§4.2/§4.3). Enumerate by DIFFING the source-delta (bf32f9c §4 re-derive), preserving anneal-dev's corpus-evolution binding (faithful, not de-bloat). The render-fidelity verify (clause-by-clause vs current §4) is the completeness guarantee. NOT YET [VERIFIED] — held pending operator (re-scope + the queued audit-vs-falsification retrospective). — basis: F1, F2(strips), F5, F6 + the section-level re-scope.

---

## Cycle 5 resolved → Cycle 6 (fresh convergence on section-level D1) — operator: file + continue

Method finding filed: `dev-notes/backlog/anneal-dev-rerender-changeset-by-source-delta.md` (F7's home).

- **D1** [VERIFIED] (section-level, locked): change-set = re-render the **§4/§5.3-derived content of the 7 affected files** faithful to the CURRENT source (preserving anneal-dev's corpus-evolution binding — faithful, not de-bloat), via source-delta diff (the method finding applied): `phases/investigate-design.md` (§4.1 cycle/passes/[READY]/convergence/falsification), `phases/implement.md` (§4.2 + the V-24 strip + the §4.2 firewall re-point), `phases/verify.md` (§4.3), `references/foundations.md` (§5.3 [READY] thin-bridge + the §3.2.2 firewall re-point), `references/tracker.md` (§5.3 [READY]), `SKILL.md` (the §2.1 firewall re-point in placeholder text — harness block already faithful), `references/post-run-review.md` (the §4/§4.2 firewall re-points). `references/lenses.md` EXCLUDED (renders modules §2 lens-set, not §4/§5.3; firewall-clean, breadcrumb-clean). The render-fidelity verify (clause-by-clause vs current source) is the completeness guarantee. — basis: F1, F2(strips), F5, F6 + the source-delta method.

---

## [READY] (cycle 6 convergence clean) — auto-battle → implement

- **Convergence cycle 6 CLEAN** (falsification `a67a60e194afa77ee`): section-level D1 holds — lenses.md clean (excluded correctly), no missed category/file (every render-impacting change from bf32f9c/e453678/b56f7d8/8b8a4ac targets one of the 7), firewall(5)+breadcrumbs(3) all within the 7. Zero D-delta.
- **Fresh-session implementability: PASSED** — the change-set (per-file edit list below) is specified + source-grounded; the render-fidelity verify is the completeness guarantee.
- **Commit handling:** rule-corpus (plugin render) → discharge hook fires → impl STAGES only (no commit); orchestrator commits post-verify + presents the render diff for operator review (operator owns the render commit).

### Impl plan — 1 unit, single container (anneal-dev repo), sequential/in-place, STAGED-only
Re-render the §4/§5.3-derived content of the 7 files faithful to current source (source-delta method); preserve anneal-dev's corpus-evolution binding (faithful, not de-bloat). Per-file:
- `phases/investigate-design.md`: §4.1 cycle pass-count reconciliation (:9-10 "two passes"→"two by default" + the convergence-adds-a-third, per core.md:257/271-272) + 2 V-N strips (:151,:256) + faithful-check the [READY]/convergence/falsification content vs current §4.1/§4.1.4 (the FULL [READY] list stays here ← §4.1.1).
- `phases/implement.md`: V-24 strip (:35) + §4.2 firewall re-point (:132 → Integrity check/Isolation slot) + faithful-check §4.2 content.
- `phases/verify.md`: faithful-check §4.3 content (audit: otherwise clean).
- `references/foundations.md`: §5.3 [READY] section (391-404 → thin bridge per core.md:915-922) + §3.2.2 firewall re-point (:247 → Coupling shape).
- `references/tracker.md`: [READY] section (213-226 → thin, faithful to current §5.3/§4.1.1).
- `SKILL.md`: §2.1 firewall re-point (:297 → Name/Question/Scope lens-entry shape; placeholder text).
- `references/post-run-review.md`: §4/§4.2 firewall re-points (:8,:10 → Post-run review).

---

## implement — done (staged, not committed); → verify

Impl subagent `ad9f906be38da573e` (branch `rerender-spec-cleanup` in anneal-dev repo). Orchestrator integrity check: HEAD unmoved at `ee9e2e6`, exactly 6 files staged (verify.md needed no edit — §4.3 clean, as planned), goal-checks both EMPTY (`rg '(core|modules)\.md…§'` + `rg 'V-[0-9]'` over the render → clean). `git diff --stat`: 6 files, +45/-54 (net -9; faithful — strips/re-points/consolidation reduce, only the convergence-third-pass clause added). Orchestrator reviewed the diff: re-points target glossary terms (Integrity check/Coupling shape/Post-run review/lens-entry shape), [READY] thin-bridges (foundations.md:391-404, tracker.md:213-226) faithfully mirror core.md §5.3:915-922, pass-count matches core.md:257/271-272. No loopback finding. Staged-only (commit post-verify per F9/D7).

---

## verify [PASSED] (isolated) — run complete; render commit pending operator (operator owns render commits)

Isolated verify subagent `a541985a81287760f`. All three checks accounted for; render-fidelity swept exhaustively clause-by-clause; finding ledger EMPTY.
- Check 1 planned-vs-actual: D1/D2/D3 present + correct; every diff hunk maps to a decision (design-completeness clean).
- Check 2 lenses: all cited-clean — Lossy-render critically clean (the 3-item [READY] condition set preserved verbatim in both thin-bridges; full list lives once in investigate-design.md ← §4.1.1; no condition lost).
- Check 3 battery: (a) render-fidelity EXHAUSTIVE — pass-count faithful (core.md:257/271-272), [READY] thin-bridges faithful (core.md §5.3:915-922), 5 re-points → existing glossary terms (glossary:40/87/217/435), 3 V-N strips clean, BOTH greps empty, exhaustive sweep = NO residual divergence; (b) coherence — all cross-refs resolve; (c) skill-craft form — clean (faithful render, no de-bloat, net -9 lines).
- Recursion check (CLAUDE.md): the verify is a rule-corpus subagent PASS → orchestrator independently reviewed the staged `git diff --cached` before+after verify (re-read before push). 

### Step-4 discharge (plugin render; corpus-evolution — no operator-soundness kernel gate)
- Render fidelity: [verify a541985a81287760f, PASSED — exhaustive clause-by-clause vs current source; both firewall+V-N greps empty]
- Spec-origin trace: [verify a541985a81287760f, PASSED — every edit traces to a current-source clause]
- Skill-craft full review on changed skill files: [verify a541985a81287760f invoked skill-craft, clean — the changed files ARE plugin skill files]
- Practice-4 dependent audit: [verify, clean — the render is the dependent of the spec changes; all propagated, no residual]
- Practice-6 whole-document coherence: [verify, clean]
- Cross-spec multi-file coherence: [verify, clean — cross-refs resolve]
- Skill-craft self-review on framework-spec section: [N/A: no framework-spec section changed — work product is render OUTPUT]
- Skill-craft self-review on commits to skill-craft canonical files: [N/A: none in change-set]

### Run outcome
- anneal-dev run: **PASSED** (auto-battle; cycles 1→6 incl. 2 convergence-falsification loopbacks that caught real §4 divergences the audit missed; re-scoped section-level; impl re-rendered from source; render-fidelity verify exhaustive-clean).
- Render: 6 files, +45/-54, STAGED on branch `rerender-spec-cleanup` in the anneal-dev repo — NOT committed (operator owns the render commit; present diff first).
