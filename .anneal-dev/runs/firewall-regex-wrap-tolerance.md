# Run: firewall-regex-wrap-tolerance

- **Status:** PASSED — **SHIPPED `103e2e7` (main, pushed 2026-06-16).** Backlog item archived; README NEXT-UP advanced (open 62 → 61). (delta-verify [PASSED] isolated ad8f8feb — F5 closed, WRAP=1/PROSE=0; step-4 self-review a4fcc021 PASS + 1 fix-now applied; operator: "ship".)
- **Phase:** verify (cycle-2 [READY] → impl → verify [ISSUES FOUND] F-batch-1 → loopback → cycle-3 D3 fix → cycle-4 convergence CLEAN → delta-verify [PASSED])
- **Mode:** auto-battle
- **[READY] (cycle 2):** convergence CLEAN — intent CLEAN (`.cycle-2.intent-falsification.md`, all R# served, 4 irreducible [VERIFIED — surfaced] residuals) + mechanical ALL-HOLDS (`.cycle-2.falsification.md`, D1/D2 hold) + zero D-deltas. **Fresh-session implementability: PASSED** — per-step evidence: D1 → `instantiation-guide.md:189` (the current regex, the swap site) + `spec/glossary.md:84-87` (the wrap-tolerant idiom to cite) + the empirical test (NEW `rg -U '(core|modules)\.md[^A-Za-z0-9]{0,12}§'` catches wrap, no prose FP); D2 → `dev-notes/backlog/instance-reinstantiation.md` (the render-debt queue). Converged in 2 cycles (design empirically grounded upfront → convergence found only irreducible residuals).
- **Task:** Make the citation-firewall coherence-check regex (instantiation-guide.md:187-191)
  wrap-tolerant — the current `rg '(core|modules)\.md[^\n]{0,4}§'` is single-line and MISSES a
  §-citation split across a line wrap (the clippy-reinstantiation finding-B residual), giving
  false-clean on an acceptance gate. Non-kernel (instantiation-guide.md = corpus-evolution).

## Requirements record (R1..Rn — the goal, separated from any proposed solution)

**Operator verbatim request:** "yes lets do it" (remote-control) → resolved to running the
second candidate pair sequentially; this is the first (non-kernel) item:
`firewall-regex-wrap-tolerance`.

- **R1** — The firewall coherence-check catches a framework §-citation that is **split across a
  line wrap** (e.g. `` `modules.md` `` at end of line, `§2.2` at the start of the next) — the
  residual that escaped clippy-reinstantiation's firewall passes.
- **R2** — The check does NOT over-match (no false positive on prose where `core.md`/`modules.md`
  and `§` are separated by actual words, not a citation gap).
- **R3** — The check matches the framework's own **wrap-tolerant** mechanical-search idiom
  (`glossary.md` Completeness claim / `core.md` §3.2: distinctive single tokens, or
  newline-flattened input, because prose wraps and a multi-word pattern can split mid-match).

---

## F-track (findings)

- **F1** [VERIFIED — non-issue] The current firewall regex is wrap-blind: `(core|modules)\.md[^\n]{0,4}§`
  uses `[^\n]{0,4}`, which cannot span a newline. **Empirically tested:** against a wrap fixture
  (`` `modules.md` `` + newline + `  §2.2`) the current regex returns **0** (misses); against normal
  cites it returns 2 (catches). basis: located read `instantiation-guide.md:187-191` + Bash test
  (`rg -c '(core|modules)\.md[^\n]{0,4}§'` → wrap:0, normal:2, prose:0, neither:0). → grounds D1, R1.
- **F2** [VERIFIED — non-issue] Missed-dependents: the firewall regex's ONLY home in this repo is
  `instantiation-guide.md:188-189` (the canonical convention). No copy in spec/, anneal-dev/,
  instance-template/, development-process.md, post-run-review.md, README.md. The instances that RENDER
  the firewall check (clippy/daneel) are SEPARATE repos → render-debt (propagate on next re-render).
  basis: search `grep -rnE '\(core\|modules\)|firewall|section-number citation|\[\^\\n\]\{0,4\}'`
  across the repo → 1 home (instantiation-guide.md:188-189). → grounds D1 (scope), D2 (render-debt).
- **F3** [VERIFIED — non-issue] The framework's canonical wrap-tolerant idiom: "Its basis is a
  **wrap-tolerant** mechanical search — matched on distinctive single tokens, or against newline-flattened
  input, because prose wraps across lines and a multi-word pattern can split mid-match (`core.md` §3.2)."
  basis: located read `spec/glossary.md:84-87`. → grounds D1 (the fix must match this), R3.
- **F4** [VERIFIED — non-issue] The wrap-tolerant candidate is empirically validated:
  `rg -U '(core|modules)\.md[^A-Za-z0-9]{0,12}§'` — against the same fixtures: **wrap:1 (CATCHES)**,
  normal:2, **prose:0 (no false positive** — "core.md is the kernel. The next §" doesn't match because
  alphanumerics break the gap)**, neither:0. The matched wrap span is `modules.md` + backtick + newline
  + indent + `§`. `-U` (multiline) lets the non-alnum gap span the newline. basis: Bash test
  (`rg -Uc '(core|modules)\.md[^A-Za-z0-9]{0,12}§'` → wrap:1, normal:2, prose:0, neither:0;
  `rg -Uo` shows the matched span). → grounds D1, R1, R2.

- **F5** [VERIFIED — addressed] (cycle-2 verify [ISSUES FOUND], F-batch-1; loopback) The D2 render-debt entry
  cited the discharge target as a brittle line-ref `:294`, but the same edit prepended the entry above it,
  moving the target to :306 — a self-stale line-number reference (ironically the exact brittle-line-ref class
  this item discourages). basis: verify subagent ad1592f5b9f098b32 + `git show HEAD:…|sed -n '294p'` (pre-edit
  target) vs `sed -n '306p'` (post-edit). disposition addressed-by → D3 (cycle 3). (D1/D2's substance NOT
  invalidated — the finding is a reference nit in the D2 entry's prose.)
- **F6** [VERIFIED — addressed] (release step-4 skill-craft self-review, subagent a4fcc021cfeedc163; notable,
  fix-now) The `{0,12}` firewall-regex gap bound was a naked numeric parameter — its empirical choice-criterion
  (corpus deepest indent ~6 spaces, so worst wrapped-cite gap ~8, so 12 gives headroom) was established in the
  intent pass but unstated in the rule-text. Fixed at instantiation-guide.md:191 — added a tight criterion clause
  ("12 covering a wrapped cite's backtick + newline + the corpus's shallow indent, with headroom"). Behavior-preserving
  (the regex is unchanged; only the explanatory parenthetical gained the criterion) so no regex re-verify. (1
  observation kept: the FP-justification prose is the load-bearing correctness argument.) basis: anti-patterns.md
  Naked-judgment + the cycle-2 intent pass's corpus measurement.

---

## D-track (design decisions)

- **D1** [VERIFIED] **Replace the firewall regex with the wrap-tolerant form.** At
  `instantiation-guide.md:189`, replace `rg '(core|modules)\.md[^\n]{0,4}§' <instance>` with
  `rg -U '(core|modules)\.md[^A-Za-z0-9]{0,12}§' <instance>` and add a brief inline note that it is
  **wrap-tolerant** (multiline `-U`; the gap is non-alphanumeric — whitespace / newline / backtick /
  punctuation, up to 12 chars — so a §-cite split across a wrap is caught, while prose between `.md`
  and `§` is NOT a false positive because words break the gap), matching the basis-rule wrap-tolerant
  idiom (`glossary.md` Completeness claim / `core.md` §3.2). (a) target: the firewall-check regex at
  instantiation-guide.md:189 + its surrounding sentence; (b) shape: a delta — swap the regex + a clause
  noting wrap-tolerance; (c) accept: the documented check catches the wrap fixture and does not match the
  prose fixture (the F1/F4 test cases); (d) failure modes: too-small a bound misses deep indents (12
  covers backtick+newline+~10-space indent — corpus wraps shallowly), too-large risks false positives
  (mitigated by the non-alphanumeric class — alphanumerics break any prose gap); (e) basis: F1, F3, F4.
  considered: `rg -U --multiline-dotall '...\.md.{0,8}§'` (rejected: `.` dotall matches alphanumerics →
  over-matches prose, F4-equivalent risk); a `tr '\n' ' '` newline-flatten pre-pass (rejected: a 2-stage
  pipeline is heavier than the single `-U` command; same effect).
- **D2** [VERIFIED] **Render-debt note for instances.** The firewall check is rendered into each
  instance's render-verify (clippy/daneel — separate repos, not in this repo, F2). Those renders carry
  the old single-line regex until their next re-render. Queue a render-debt row in
  `dev-notes/backlog/instance-reinstantiation.md` so the wrap-tolerant regex propagates to each instance
  on its next re-render. (a) target: the instance-reinstantiation render-debt queue; (b) shape: a row
  noting the firewall-regex wrap-tolerance update; (c) accept: the render-debt is queued; (d) failure
  modes: none (the within-repo source is fixed by D1; instances inherit on re-render); (e) basis: F2.

### Cycle 3 (post-loopback) — D3 + Cycle 4 (convergence)

- **D3** [VERIFIED] (cycle 3, per F5) **Fix the self-stale line-ref in the D2 render-debt entry.** Replace
  "(referenced at `:294` under clippy's reinstantiation residuals)" with a **content anchor** — "(filed under
  clippy's reinstantiation residual-tails list)" — dropping the brittle line number (the same content-anchor-over-
  line-number lesson this item embodies). (a) target: instance-reinstantiation.md render-debt entry's discharge
  clause; (b) shape: replace the line-ref with a content anchor; (c) accept: no `:NNN` line-ref in the entry; the
  content anchor resolves to the residual-tails list; (d) failure modes: none; (e) basis: F5. (dev-notes file =
  not rule-corpus; behavior-preserving.)
- **F5** [VERIFIED — addressed] (cycle 3) addressed by D3 (content anchor replaces the line-ref). basis: D3 [VERIFIED] cycle 3.
- **Cycle 4 (convergence):** the D3 fix is **behavior-preserving** (a dev-notes content-anchor fix; D1/D2 substance
  unchanged → the design's intent-serving unchanged) → the cycle-2 intent-clean result CARRIES FORWARD (re-trigger
  reuse rule). Mechanical re-check (D3 only; D1/D2 carry forward cycle-2 holds): {D3 target-existence
  `expected-match:"residual-tails"` + `any-match` for a residual `:[0-9]+` line-ref in the entry → content anchor
  present, NO line-ref remains → **holds**}. Zero new D-deltas → convergence CLEAN → [READY]. Delta-verify next
  (behavior-preserving fix → delta scope: confirm F5 closed + firewall-regex regression).
