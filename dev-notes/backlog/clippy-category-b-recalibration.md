# Clippy Category-B recalibration — verify-by-substrate, falsification gating, convergence cost, lens promotion

**Status:** [READY] — filed 2026-07-10. Evidence-backed by a corpus-complete audit of
all 34 clippy runs in beat-the-books (`.clippy/runs/`, ~171 falsification D-entry
evaluations, 26 falsification passes, 38 stdpass artifacts) plus session forensics
(Jul 2026 long session + Nov 2025 pre-clippy Cursor transcripts). Findings files:
the auditing session's scratchpad `findings/` (tracker-auditor, episode-analyst,
cursor-forensics-1/2); key numbers reproduced below so this item is self-contained.

## The evidence (headline numbers)

- **Falsification pass: 4 flips / ~171 [VERIFIED] evaluations (~2.3%).** 2 genuine
  would-have-shipped bugs (mw23 D8 bankroll re-key: cited 3 consumer sites, real set
  8 — money-path KeyError class; unit-9-s2 D4: falsification subagent *ran* the
  validator and proved every form submission would reject — caught at design time).
  2 process/hygiene. Both genuine catches came from passes that **ran code**; the
  dominant `target-uses` re-grep mode scored 1 real hit in ~50 greps.
- **Convergence cycle: zero independent catches.** The only dedicated convergence
  artifact (unit-34) was 12/12 holds. The one arguable catch (mwh F14 per-wallet
  cursors) was an investigation finding hosted in a convergence cycle.
- **Isolated verify: the productive stage — but only its real-substrate execution.**
  Genuine catches all execution-class (asyncpg `AmbiguousParameterError` on the
  default path, `MIN(uuid)` → zero bets placed, real-Jinja 500, PydanticUndefined
  prefill) — every one invisible to the green mock suite. The re-read-only findings
  were cosmetic.
- **Verify's misses line up exactly with where it didn't touch the real substrate:**
  unit-34's boot-crashing migration + silent 701-row discard passed falsification,
  convergence, stdpass AND isolated verify (verify checks files, not live prod
  schema); caught by an operator prod check. mw23 F33 (feature with no code path)
  missed by verify's completeness audit; caught by the operator's "anything
  missing?". The scariest bug (F28 fail-toward-live) was caught by the
  implement-phase self-check loopback, not by any Category-B stage.
- **Cycle-1 standardized lens pass: cheapest productive stage** (Silent-substitution
  tz catch, Coupled-change closing-line catch — both cycle-1); repeat passes
  re-confirm.
- **Fail-open incident (2026-07-05 → 09), the motivating case for the lens below:**
  a name-hardcoded `one_per_game` filter (plain implementation) was armed by a later
  plain strategy addition; the fail-open dispatch site silently exempted the new
  strategy for days, while its fail-closed sibling site errored loudly and was fixed
  same-day. Same defect class as the D8 falsification catch — incomplete enumeration
  of dispatch/consumer sites.

## Changes proposed (in value order)

1. **Verify must execute against the real substrate.** Make real-substrate execution
   (ephemeral/real DB for SQL + migrations, real template renders, live-schema check
   before migration sign-off) a required leg of verify, not an incidental one. This
   is the single highest-leverage change: every genuine verify catch was
   execution-class, and every documented verify miss is where execution was absent.
   Fallback semantics when no substrate is reachable: surface "without substrate"
   loudly (parallel to the existing isolation fallback), never silently pass.

2. **Gate the falsification pass on blast radius; prefer runtime-probe candidates.**
   Falsification earns its cost on large multi-file refactors and money/data-path
   changes; on small additive/mirror slices it was dead weight (0 catches in ~67
   evaluations across the June-15/16 + July-06 batches). Candidate quality rule:
   a runtime probe (run the function/query) outranks a re-grep; a line whose only
   candidates are re-greps of already-cited queries is low-value — require at least
   one candidate per basis that *executes* where the basis claims runtime behavior.

3. **Cheapen the convergence cycle to a stop-signal.** One convergence cycle, not
   iterated; drop any implication that it is a bug net. Its value is "we've stopped
   finding things," which one clean cycle establishes.

4. **Promote a Dispatch-exhaustiveness lens to the core lens set.** Currently piloted
   as a project supplement in beat-the-books `clippy.config/lenses.md`. Nothing about
   it is domain-specific; it closes the fail-open dispatch class that both the D8
   falsification catch and the one_per_game incident instantiate. Proposed core text:

   > **Dispatch-exhaustiveness**
   >
   > - *Question:* does the cycle's work add or rename an enum-like value (strategy
   >   name, variant id, type tag) — and if so, is every site that branches on that
   >   value search-enumerated and updated (or covered by an exhaustiveness test
   >   wired to the registry), and does each dispatch fail closed on unknown values
   >   (loud error, never silent exemption)?
   > - *Scope:* any cycle whose work adds/renames an enum-like value, or touches a
   >   site that branches on one.

   On promotion, the beat-the-books supplement entry should be retired (supplements
   are the staging area; core is the destination for proven lenses).

5. **Mandatory absence-check in the closed artifact.** The operator's "anything
   missing?" question outperformed verify's design-completeness audit (mw23 F33).
   Add a named closed-artifact line at [READY] and at verify-terminal: "Absence
   check: what does the locked design require that no code path yet provides?" —
   answered with a cited basis, not a bare "none."

6. **Models config: widen the dispatch-model enum.** `bindings.md` currently fixes
   `opus, sonnet, haiku`. Accept any model string (forward-compatible with
   fable-class models); drop haiku from the placeholder text (operator-confirmed
   useless for these tasks). Keep the recommended `impl: sonnet / verify: opus`
   split — operator-validated: impl units execute a locked design, so the
   open-design intelligence demand does not apply to them.

7. **Two-directional lens accretion via post-run review.** Post-run review currently
   evaporates by design. Have it end by proposing (a) candidate lens entries
   (Name/Question/Scope) for `clippy.config/lenses.md` — operator accepts/rejects —
   and (b) retirement candidates: core/supplement lenses that have not fired a real
   finding across N runs. Complements the precipitation discipline: a lens whose
   check is mechanical should be proposed as a CI test, not kept as a lens.

## Keep/cut taxonomy (the framing behind the changes above)

Derived from the skills-minimalism lens (skills = temporary patches for model
weakness; delete as models improve; accrete from failures) applied to clippy's
full content, then confirmed by the audit numbers:

- **Rails — never cut** (not model-weakness patches; durable regardless of
  model tier): basis rule, append-only tracker (anti-amnesia ledger), verify
  isolation / separate-checker, loopback semantics, per-unit commits,
  scope-as-search-established, closed-artifact discipline (committed
  recommendation, no posed choices), fresh-session implementability test
  (audits the artifact, not the model).
- **Category A — lens set: keep with retirement policy.** Lenses are accreted
  scar tissue from real incidents; keep each while models still fail that
  way; retire on evidence (change 7 above). Two-directional accretion.
- **Category B — self-attestation-distrust machinery: first to cut.**
  Convergence mechanics, candidate-shape taxonomy, mechanical predicates —
  built because "yes I checked" couldn't be trusted. Audit: falsification
  ~2.3% flip rate (pays only on large refactors, only when it runs code),
  convergence zero independent catches. Verify-by-execution is the keeper.
- **Pruning order:** Category B enforcement prose first, Category A
  lens-by-lens on evidence, rails never. When cutting Category B, keep the
  artifact shapes (auditability) and drop the redundant re-checking.
- Clippy's deepest value, one line: **the two primitives it *enforces* rather
  than leaves remembered — the on-disk ledger and fresh-context verification**
  (the global CLAUDE.md frame now carries self-dispatched versions; clippy is
  where they're guaranteed).

## Relation to existing backlog

Overlaps in spirit with `convergence-mechanical-pass-value.md` and
`verify-model-diversity.md` (not read in-depth here — reconcile at pickup). The
evidence corpus above is the strongest empirical input the framework has had on
which Category-B stages earn their cost; whatever the final rendering, the
per-stage numbers should anchor it.
