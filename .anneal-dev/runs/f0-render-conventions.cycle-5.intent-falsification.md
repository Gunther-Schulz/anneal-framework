# f0-render-conventions — cycle 5 (re-convergence) intent-falsification-pass

Fresh-context dispatch (subagent `a364ea59c3eaba468`, opus, criteria-first) on the RE-FORMED design
D1–D5. **Result: NO D-track delta — design holds.** Mechanical falsification pass RUNS this cycle
(intent clean → sequencing rule).

## Per-R# attack lines
- **{R1, refutation:** enumerated the closed slot set (guide:135-146) vs `ls instance-template/spec/`
  (isolation.md absent), **outcome: served}** — D2 adds the last missing member; guide:18 "every slot"
  becomes true, no other slot lacks a file.
- **{R2, refutation:** traced the linear guide reader :18→:92→:108→:135; `rg consolidat
  instantiation-guide.md` → only post-:135, **outcome: finding}** (F-INTENT-1).
- **{R3, refutation:** template bindings left-column discriminator subset vs glossary + firewall
  (`rg -c '(core|modules)\.md.*§' instance-template/spec/bindings.md` = 0), **outcome: served}** — D4
  covers exactly the hidden-semantics terms; template (the author's copy surface) is firewall-clean.
- **{R4, refutation:** R1∧R2∧R3 composition, **outcome: finding}** (inherits F-INTENT-1).

## Per-finding lines (both [VERIFIED — surfaced] — judgment-class, no coupling-shape falsification)
- **F-INTENT-1 [VERIFIED — surfaced]** {criterion: R2/R4; refutation: `rg -n 'consolidat|may.{0,15}
  section' instantiation-guide.md` → matches only at/after :135, zero before the worked examples at
  :92/:108; route: `[VERIFIED — surfaced]` (no closed predicate decides reader-confusion)}. D5's clause
  is authored right but placed AFTER the examples that trigger the contradiction. **Impl guidance:**
  place the reconciliation (or a forward-pointer) at/before the FIRST worked example (guide:92), not
  only at :135. Folds into D5's realization (placement is impl detail; D5's resolution unchanged).
- **F-INTENT-2 [VERIFIED — surfaced]** {criterion: R3/F-E precision; refutation: `awk -F'|' '/^\|/{if
  ($2 ~ /(core|modules)\.md.*§/) print NR}'` over the three bindings.md → left-column cites are
  anneal-dev rows 39/42/43 ONLY; clippy line-6 is intro prose without a § (not a table cite, not a
  firewall match); clippy + daneel binding tables clean; route: `[VERIFIED — surfaced]`}. Corrects F-E:
  binding-table render-debt = **anneal-dev rows 39/42/43 only** (drop "clippy 6"). Confirms F-E's
  [VERIFIED — deferred] trigger is well-formed (maps to foundations.md canonical "executable-
  verification output class" — the §3 firewall check `rg` at guide:182-187).

## Summary
No D-delta. R1/R3/R4-core hold; the one R2 concern (F-INTENT-1) is a placement refinement of D5
(surfaced, terminal, folded as impl guidance), and F-INTENT-2 tightens F-E's enumeration. Design holds;
proceed to the mechanical falsification pass.
