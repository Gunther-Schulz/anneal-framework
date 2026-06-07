# clippy-reinstantiation — cycle 7 intent-falsification-pass artifact (CONVERGED)

Fresh-context subagent (opus), criteria-first, convergence-seeking. Method grounded in live `core.md §4.1.4` + `modules.md §3.4.1`.

## Per-R# attack lines — ALL SERVED
- `{R1, attempted-refutation: rg deltas in spec/README.md (newly-in-scope) → empty; only framework-coupled content is the vw path (D17), outcome: SERVED}`
- `{R2, attempted-refutation: spec/README.md:26-28 "tracked in the framework's validation-watch.md" is a tracking-location cross-ref (no V-N token), referent folder exists → repoint (D17) faithful, not the F12 strip case, outcome: SERVED}`
- `{R3, attempted-refutation: rg '(core|modules)\.md[^\n]{0,4}§' spec/README.md → empty; its one cross-ref names the framework README by file, not §-number, outcome: SERVED}`
- `{R4, attempted-refutation: spec/README.md is git-tracked, non-archived, sibling to bindings.md/lens-set.md → D16's repo-rooted rg coherence check reaches it natively, outcome: SERVED}`
- `{R5, attempted-refutation: wc -w spec/README.md = 144, a spec file not always-loaded, far under threshold → no new flag obligation, outcome: SERVED}`

## New-obligation + whole-repo re-sweep
- spec/README.md carries NO §-cite/coupling-name/V-N beyond the single vw path (D17). 
- Whole-repo re-sweep (`--glob '!docs/archived/**'`): every vw-path/coupling-name/firewall/V-N site maps to a covering D-entry. No site outside a covering decision.

## VERDICT: CLEAN — no findings, 5/5 R# served, zero mechanical-falsification-candidate.
