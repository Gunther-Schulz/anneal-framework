# clippy-reinstantiation — cycle 5 intent-falsification-pass artifact (RE-CONVERGE)

Fresh-context subagent (opus), criteria-first. Method grounded in live `core.md §4.1.4` + `modules.md §3.4.1`. Verifies cycle-4 amendments + attacks residual.

## Per-R# attack lines
- `{R1, attempted-refutation: re-checked delta enumeration vs git log + D5–D14 cited sources (core.md:903 loopback triage, :981 requirements-coverage, post-run-review.md:163 Q7) present; current targets confirmed lacking them, outcome: SERVED}`
- `{R2, attempted-refutation: confirmed V-5/V-9 STRIP faithful — git show bf32f9c (deletes (V-5)/V-5/validation-watch.md), e453678 (glossary V-N strip), grep V-[0-9]+ spec/ → zero, outcome: SERVED}`
- `{R3, attempted-refutation: firewall mechanical check rg '(core|modules)\.md[^\n]{0,4}§' on BOTH instance specs — lens-set.md → 3 hits (:10,:75,:204) covered by neither D10 nor D12', outcome: FINDING (F-INT-5)}`
- `{R4, attempted-refutation: checked whether firewall coherence check (instantiation-guide.md:190) is enforced by the render-fidelity verify the design leans on — grep firewall/rg in phases/verify.md → empty; no D-entry renders/runs it at verify, outcome: FINDING (F-INT-6)}`
- `{R5, attempted-refutation: wc -w sweep (tracker 3015, investigate-design 2364, SKILL 2579, implement 1988, post-run-review 1622, lenses 1529, foundations 1459, verify 799) vs D15 flag+defer, outcome: SERVED — D15 sound, no file needs de-bloat to serve R1–R4}`

## Cycle-4 amendment soundness (verify leg) — all SOUND
- D6'/D14' (strip V-5/V-9): SOUND — strip matches deleted source (bf32f9c/e453678; spec/ grep zero).
- D12' (bindings.md §→glossary): SOUND, dischargeable (glossary terms exist for all spot-checked §). Count correction: bindings.md has 11 framework §-cites (6 core/modules + 5 instantiation-guide), not F14's "~15" — cosmetic; the `core.md §` exact grep missed them (citations spelled `` core.md` §`` with backtick before §); firewall regex `(core|modules)\.md[^\n]{0,4}§` catches them.
- D15 (budget flag/defer): SOUND — verify.md 799 has headroom; de-bloat is work-kind-2; SKILL.md (the activation file) IS de-bloated by D14.

## Per-finding lines (both route [VERIFIED — surfaced]; zero mechanical-falsification-candidate)
- `{finding: F-INT-5 — lens-set.md (sibling instance spec, edited by D10) carries 3 framework §-cites (modules.md §2.1 at :10,:204; core.md §3.2 at :75) violating the firewall (covers instance specs AND rendered files, instantiation-guide.md:187-188); D12' converted bindings.md only, D10 has no firewall clause, criterion-attacked: R3, refutation: rg '(core|modules)\.md[^\n]{0,4}§' coding-clippy/spec/lens-set.md → 3 hits, route: [VERIFIED — surfaced]}`
- `{finding: F-INT-6 — the firewall coherence check (rg §-numbers → empty), which is R4's acceptance gate per instantiation-guide.md:190 ("render-verify runs this as a coherence check; non-empty = finding"), is not part of the render-fidelity verify the design defers completeness to (D1'/D5–D14); no D-entry commits to running it at verify, criterion-attacked: R4/R3, refutation: grep firewall/rg phases/verify.md → empty; instantiation-guide.md:190 located read, route: [VERIFIED — surfaced]}`

## Cleared (not findings)
- post-run-review.md `development-process.md`/`practice 1` cross-refs: NOT a strip target — the render-source post-run-review.md carries them as load-bearing Q-set machinery (source :6,:59,:86,:224); stripping = Lossy (R2 violation). D13 correctly carries them.
- post-run-review.md:162 `validation-watch.md`: correctly repointed to folder by D13 (source references `dev-notes/validation-watch/`).
- D7/D8/D9/D13 delta sources: every claimed delta has a locatable sufficient source.

## Verdict
Cycle-4 amendments SOUND. 2 residual findings (F-INT-5, F-INT-6) — both pure judgment `[VERIFIED — surfaced]`, both R3/R4 coherence gaps of the firewall mechanism cycle-4 touched partially. Zero mechanical-falsification-candidate; every D5–D15 located read accurate; scope complete. **Working-context disposition: action both (requirement-anchored R3/R4, cheap) → D3'/D10'/D16 → intent-delta this cycle → mechanical skipped cycle 5.**
