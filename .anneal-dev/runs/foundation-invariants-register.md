# foundation-invariants-register

- **Status:** PASSED
- **Phase:** verify
- **Mode:** interactive
- **Task:** Build the foundation-invariants register (anchor-gated, externally
  anchored kernel invariants) + wire a per-touched-invariant holds/violates
  artifact into the method-kernel-edit verify (development-process.md §2 +
  release-loop step 4) + a protection marker on register-invariant changes.
  Method-kernel edit; operator decide-ahead locked 3 forks (scope=register-only,
  membership=anchor-gated, protection=enforced-marker). Operator input is a
  strong input, confirmed/sharpened on evidence per anneal-dev.

## F-track (findings)

- F1 [VERIFIED — non-issue] Scope of the contract (method-kernel-edit verify
  discipline) is contained to the framework repo; absent from skill-craft and
  all instances — basis: search `grep -rniE 'self-certif|kernel-independent|method-kernel'`
  over {anneal-framework, skill-craft, coding-clippy, daneel, campaign-craft,
  bauleitplan-anneal, anneal-dev}; non-empty only in anneal-framework/{development-process.md,
  CLAUDE.md, hooks/anneal-dev-run-gate.py}.
- F2 [VERIFIED — non-issue] The proven dev-notes spec-wired-companion shape is a
  folder: file-per-entry + README + archive/ — basis: `ls dev-notes/validation-watch/`
  → 28 V-N entry files + README.md + archive/ (one observed member: V-28-never-captured-requirement.md).
- F3 [PENDING] Of the 6 operator-proposed seed invariants, 4 are live kernel
  invariants but 2 ("exclusion-obligation", "falsifiability-gate") are candidate
  sharpenings, not held invariants — basis: seed locator grep — basis-rule
  (`spec/core.md` §3.2.2 via glossary.md:53), complete-state (`spec/core.md:18`),
  loopback (`spec/modules.md:116`/core.md §4.1.4), verify-isolation
  (`foundation.md:28-29`, `spec/core.md:142`) all LOCATED; "falsifiab" matches only
  the falsification-*predicate* mechanism (`spec/modules.md:343`), not a general
  acceptance-gate invariant — the sharp gate is research finding [5]'s "importable
  acceptance GATE sharper than re-checkability" (adoptable, not held).
- F4 [PENDING] New kernel terms "foundation invariant" / "foundation-invariants
  register" are absent from the glossary → practice-10 entries needed — basis:
  `grep -nE '^\*\*' spec/glossary.md` enumerated ~40 terms; none is "foundation
  invariant" or "invariants register".
- F5 [VERIFIED — non-issue] hooks/commit-msg is extensible and dev-notes/ is NOT
  currently gated by it → a narrow Invariant-change-ratified marker check on
  foundation-invariants/ touches is an additive, local-only change — basis: read
  hooks/commit-msg RULE_CORPUS_PATTERN (lines 39-44) — pattern enumerates
  spec/development-process/post-run-review/instantiation-guide/foundation/plugin-skills/
  instance-template/.claude-plugin; dev-notes/ absent.

## D-track (design decisions)

- D1 [VERIFIED] SCOPE — the contract being changed (method-kernel-edit verify
  discipline) is encoded at: `development-process.md` §2 (lines 25-36),
  release-loop intro (lines 543-544), release-loop step-4 discharge artifact
  (lines 567-579); `CLAUDE.md` lines 14-20 (repo-local restatement = dependent);
  `hooks/anneal-dev-run-gate.py` (references discipline; routing-gate, not
  verify-content — no edit). New artifact: `dev-notes/foundation-invariants/`.
  Protection home: `hooks/commit-msg`. basis: F1 search (completeness) + located
  reads of each cited line range.
- D2 [PENDING] REGISTER — home `dev-notes/foundation-invariants/` (folder:
  file-per-invariant + README + archive/, the validation-watch shape per F2);
  membership = (live kernel invariant) ∧ (genuine external anchor); the anchor is
  the entry's whole justification; an invariant anchorable only to anneal itself is
  EXCLUDED (stays an ordinary kernel rule). Per-kernel-edit artifact: a
  per-touched-invariant holds/violates-against-its-anchor ledger. README carries
  the anti-false-comfort residual in plain words ("register-clean ≠ sound; novel
  unsoundness still needs the operator; dogfood + outside check, never dogfood
  alone"). Seed set pending F3 resolution. basis: operator decide-ahead lock
  (strong input) + F2 model; seed-set detail blocked on F3.
- D3 [OUTLINED] VERIFY-WIRING — `development-process.md` §2 + release-loop step-4
  discharge gains a Foundation-invariant check for method-kernel edits: the
  per-touched-invariant holds/violates-against-anchor artifact (D2), referencing
  the register. Exact discharge-template line shape + §2 wording = next-cycle
  design. basis: located read of step-4 discharge template (lines 567-579) — the
  insertion point for a new check line.
- D4 [CONDITIONAL] PROTECTION — extend `hooks/commit-msg`: a commit whose diff
  touches a registered-invariant file under `dev-notes/foundation-invariants/`
  requires an `Invariant-change-ratified: <operator-approval-ref>` line (mechanical,
  git-observable; same shape as the Coherence-audit-handoff marker). LOCAL-ONLY to
  this repo (operator-directed this session) — never packaged/rendered to instances;
  narrow path-match avoids the open commit-msg-hook-packaging-overmatch concern.
  Assumption (operator-resolvable): detection granularity = any touch to an
  invariant file (vs. content-diff of the invariant claim only). basis: operator
  free-form directive ("sufficient to have it local only to this repo") + F5 hook
  read.
- D5 [VERIFIED] SCOPE-EXCLUSIONS — the canonical-scenario regression suite and the
  different-model soundness checker are EXCLUDED from this run and filed as their
  own backlog items (they sit atop the register; the checker overlaps
  multivoter-verify-no-predicate-claims + inherits its validate-before-adopt gate
  on anneal-reliability-measurement). basis: operator decide-ahead lock + backlog
  item "Candidate machinery" section (3 candidates; (3) "needs (1)/(2) as stable
  ground").
- D6 [PENDING] TERMINOLOGY — practice-10 glossary entries for the new load-bearing
  kernel terms (per F4), in the same commit as the wiring. Exact term set + entry
  bodies = next-cycle design. basis: F4.

## Cycle 2 — append-only ledger lines (auto-cycle; operator authorized cycle-to-READY)

- F3 [VERIFIED — non-issue] Seed set resolves to 5 LIVE externally-anchored
  invariants; the 2 candidate-seeds are dropped (stay backlog tier 4) — basis:
  seed locator (cycle 1) + research finding [5] framing falsifiability-gate as an
  "importable acceptance GATE sharper than re-checkability" (i.e. adoptable, not
  held). The 5: basis-rule, complete-state, verify-isolation, loopback/not-settled,
  exclusion-via-named-falsifier (the last absorbs the live form of both dropped seeds).
- F4 [VERIFIED — non-issue] New kernel terms' home is the register README, NOT
  spec/glossary.md — basis: `grep correctness-watch|quality-watch spec/glossary.md`
  → ABSENT; same terms defined in dev-notes/validation-watch/README.md:30-37. A
  dev-notes companion defines its own terms in its README; putting them in the
  rendered glossary would be Leakage (dev-process concept into domain-general spec).
- F6 [VERIFIED — non-issue] D3b/D4 hook additions do not collide with the open
  commit-msg-hook-packaging-overmatch item — basis: read of that item + hooks/commit-msg
  — the overmatch is in RULE_CORPUS_PATTERN matching `.claude-plugin/*` packaging; D3b
  (kernel-source pattern: spec/foundation/development-process/post-run-review/
  instantiation-guide/anneal-dev-spec) and D4 (dev-notes/foundation-invariants/INV-*.md)
  are additive on new narrow patterns, neither broadens RULE_CORPUS_PATTERN nor matches packaging.
- D2 [VERIFIED] REGISTER — home dev-notes/foundation-invariants/ (folder:
  INV-<n>-<slug>.md per invariant + README.md + archive/, validation-watch shape F2).
  Membership = (live kernel invariant) ∧ (genuine external anchor); anchor is the
  entry's whole justification; anneal-only-anchorable invariant EXCLUDED. Seed = 5
  entries, each {invariant : kernel-home : external-anchor}: (1) basis-rule :
  core.md §3.2.2/glossary.md:53 : Zave & Jackson "Four Dark Corners of RE" —
  *designation*; (2) complete-state : core.md:18 : Zave & Jackson — S,K⊢R; (3)
  verify-isolation : foundation.md:28-29 + core.md §4.3 : SGV verifier-actor
  independence + self-preference (verify-techniques [0],[3],[4]); (4)
  loopback/not-yet-settled : core.md §4.1.4 + loopbacks : Platt Strong-Inference
  recycle + Quine-Duhem; (5) exclusion-via-named-falsifier : core.md §4.1.4
  falsification pass : Platt exclusion + Gunter et al. WRSPM (ICRE2000, completeness
  provably insufficient for soundness) — the soundness keystone. Per-kernel-edit
  artifact: per-touched-invariant holds/violates-against-anchor ledger. README
  carries the anti-false-comfort residual in plain words + the new-term definitions
  (D6). basis: F2 model + F3 seed resolution + cycle-1 seed locator reads.
- D3 [VERIFIED] VERIFY-WIRING — (a) development-process.md §2 (lines 25-36): the
  kernel-independent review gains a third leg, the foundation-invariant check (the
  per-touched-invariant holds/violates-against-anchor artifact per the register),
  beside skill-craft (form) + operator (soundness); the check FOCUSES the operator's
  soundness pass (names touched invariants + anchors to satisfy), never replaces it.
  (b) release-loop step-4 discharge template (lines 567-579): + line `- Foundation-invariant
  check (per dev-notes/foundation-invariants/; method-kernel edits) → [holds/violates
  artifact OR subagent ID+verdict] OR [N/A: not a method-kernel edit — cite paths]`.
  basis: located read of §2 + step-4 template (the insertion points).
- D3b [VERIFIED] WIRING-ENFORCEMENT — hooks/commit-msg requires the Foundation-invariant
  check line when the staged diff touches kernel-source (new KERNEL_SOURCE pattern:
  spec/*.md, foundation.md, development-process.md, post-run-review.md,
  instantiation-guide.md, anneal-dev/spec/*); same structural-enforcement shape as the
  existing 7 REQUIRED_CHECKS; local-only. basis: F5 hook read (REQUIRED_CHECKS lines
  52-60 — the extension point) + F6 (no overmatch collision).
- D4 [CONDITIONAL] PROTECTION — hooks/commit-msg: a staged diff that MODIFIES (M) or
  DELETES (D) an existing invariant file (dev-notes/foundation-invariants/INV-*.md;
  README.md + archive/ exempt) requires `Invariant-change-ratified: <operator-approval-ref>`
  (git-observable via --diff-filter=MD; marker shape parallels Coherence-audit-handoff).
  Additions (A) of new invariant files exempt — adding a check does not weaken the
  foundation; this run's register-creation commit is an Addition, so it needs no marker
  (operator's verify-step ratification IS the creation ratification — no bootstrap
  paradox). Local-only. Assumption (operator-resolvable): M/D-only granularity vs
  all-touches. basis: operator directive (local-only) + F5 hook read.
- D6 [VERIFIED] TERMINOLOGY — folded into D2: new terms ("foundation invariant",
  "foundation-invariants register", "anchor-gated", "Invariant-change-ratified marker")
  defined in the register README, NOT spec/glossary.md (leakage-avoidance). basis: F4.

## Cycle 3 — convergence cycle (new-surface investigation + falsification pass)

New surfaces investigated this cycle (each new by file/query/located-read not in prior cycles):
- F7 [VERIFIED — non-issue] Run-gate hook defines the method-kernel-edit source set
  as KERNEL_PATTERNS (hooks/anneal-dev-run-gate.py:57-62): /spec/.+\.md$,
  /foundation\.md$, /development-process\.md$, /post-run-review\.md$,
  /instantiation-guide\.md$ (/spec/ covers anneal-dev/spec/*) — basis: located read
  of lines 57-62. → D3b mirrors this set (consistency).
- F8 [VERIFIED — non-issue] "invariant" is a genuinely new corpus term — basis:
  `grep -rniE '\binvariant' spec/ foundation.md development-process.md CLAUDE.md
  post-run-review.md instantiation-guide.md anneal-dev/spec/` → EMPTY. No existing
  definition to collide with (strengthens F4/D6); no Fragmentation.

Basis-only refinements (sub-annotations; resolution unchanged; NOT D-deltas):
  - D2 (cycle-2 line): entry (1) basis-rule home tightens `core.md §3.2.2` →
    `core.md §3.2` (the basis rule section; §3.2.2 is its amendment sub-aspect) —
    basis: `grep '### 3.2 The basis rule' spec/core.md` → line 153.
  - D3b (cycle-2 line): kernel-source set = the run-gate's KERNEL_PATTERNS
    (F7), not a divergent pattern — basis: F7.

## Cycle 3 falsification result + Cycle 4 correction (convergence loopback)

Falsification artifact persisted: .anneal-dev/runs/foundation-invariants-register.cycle-3.falsification.md
Cycle-3 falsification: D2,D3,D3b,D5,D6 = holds; D1 = FALSIFIED (target-dependents).

- F1 [VERIFIED — non-issue] (CORRECTION of the cycle-1 line; prior wording inaccurate)
  The cycle-1 search was malformed — narrowed by `grep -v 'dev-notes/(backlog|research)'`,
  i.e. excluded dev-notes by assumption (foundations.md: a search narrowed by where
  members are assumed to live is "a declared scope wearing a search's clothing").
  Full re-run `grep -rniE 'self-certif|kernel-independent|method-kernel'` (no exclusion)
  over all 7 repos: tokens appear in 26 anneal-framework files — 3 NORMATIVE encodings
  {development-process.md, CLAUDE.md, hooks/anneal-dev-run-gate.py} + 23 NON-NORMATIVE
  references (all dev-notes/backlog/*.md — discussion/working-notes); normative kernel
  (spec/, foundation.md, post-run-review.md, instantiation-guide.md, anneal-dev) and
  skill-craft/clippy/daneel/bauleitplan = EMPTY — basis: cycle-3 falsification subagent
  a7910d90c28a205be full-search result.
- D1 [PENDING] (reopened — cycle-3 falsification flipped [VERIFIED]→[INVALIDATED]→[PENDING]).
- D1 [VERIFIED] SCOPE (re-stated precisely) — the contract (method-kernel-edit verify
  discipline) is NORMATIVELY ENCODED at, and the edit sites are: development-process.md
  §2 (lines 25-36) + release-loop step-4 discharge (lines 567-579); CLAUDE.md lines 14-20
  (repo-local restatement = dependent); hooks/anneal-dev-run-gate.py (references; routing
  gate, no edit). New artifact dev-notes/foundation-invariants/; protection in hooks/commit-msg.
  dev-notes/backlog/*.md REFERENCES the discipline non-normatively (working-notes; NOT
  practice-4 dependents — they neither render nor enforce the contract; updated by normal
  backlog grooming, and foundation-self-certification-machinery.md archives with this work),
  so they are NOT edit sites. basis: corrected F1 (full search, normative/non-normative
  classification by the fresh-context subagent).

## Cycle 5 — convergence loopback (Missed-dependents: CLAUDE.md restatement)

New surface: located read CLAUDE.md:14-21 (the "Development process grounding" restatement of the kernel-independent review).
- F9 [VERIFIED — addressed by D3 amendment] CLAUDE.md:14-21 enumerates the
  kernel-independent review's grounds as "skill-craft self-review (form) + the
  operator (soundness)" and points to development-process.md for the discipline. If
  §2 gains the foundation-invariant-check leg (D3), this summary becomes a stale
  enumeration → Missed-dependents (D1 named CLAUDE.md a dependent; D3 omitted it as
  an edit site). basis: located read CLAUDE.md:14-21 (operator-instructions content)
  vs D3 §2 amendment.
- D3 [VERIFIED] VERIFY-WIRING (amended — edit set += CLAUDE.md) — unchanged (a)+(b)
  [§2 lines 25-36 gains the foundation-invariant-check leg of the kernel-independent
  review = the per-touched-invariant holds/violates-against-anchor artifact that
  FOCUSES the operator's soundness pass (does not replace it); step-4 discharge
  template gains the check line]; PLUS (c) a terse CLAUDE.md:14-21 update naming the
  foundation-invariant register check alongside "(form) + (soundness)", keeping the
  "read development-process.md" pointer. basis: F9 + located reads of §2/step-4/CLAUDE.md.

## Intent-falsification pass (SEPARATE soundness/judgment pass; subagent a8375ec939824751a; operator-requested experiment)
Distinct from the mechanical convergence falsification. Found 2 blocking + 2 notable + 1 anchor caveat; conceptual core (anti-circularity, recursion, anchor-reality) SURVIVES. → LOOPBACK (design not [READY]).

- F10 [PENDING] (B1) D3b wires the foundation-invariant check as a self-dischargeable
  REQUIRED_CHECK (string-presence, like the existing 7) → the AI runs its own subagent +
  writes "holds [id]"; the operator is in the loop only via generic step-4 approval, not a
  soundness gate. Risk: false mechanical-comfort — "the hook enforces it" reads as
  "soundness enforced" when the hook checks a string. basis: hooks/commit-msg:125-163
  (validate_discharge = presence + fold-into patterns only) + D3b.
- F11 [PENDING] (B2) D4's marker does not BIND the named threat — the AI writes the
  `<operator-approval-ref>` string; --no-verify bypasses; a local hook CANNOT verify an
  operator approved (that is operator-detection, which foundations.md declares a malformed
  enforcement form). D4-as-binding-gate is malformed; it is honestly an audit-trail +
  friction mechanism. basis: hooks/commit-msg:25 (--no-verify) + foundations.md
  Operator-expected-action-bound ("enforcement requiring operator-detection is malformed").
- F12 [PENDING] (N1) Anti-false-comfort residual lives only in the register README — read
  at register-time, NOT at discharge-time where the false comfort is generated. basis:
  D2 (README residual) vs the discharge line carrying only "holds/violates".
- F13 [PENDING] (N2) "FOCUS-not-add" is an unproven hypothesis — the 3 shipped edits'
  operator "ship its" do not establish the operator's cost was re-deriving KNOWN invariants
  (which the register shrinks) vs judging NOVELTY (which it cannot touch). Genuine
  design-uncertainty → validation-watch material (practice 8). basis: backlog lines 70-72.
- F14 [PENDING] (S2-caveat) Entry-3 (verify-isolation) anchor "SGV" is the loosest fit —
  SGV is criteria-first/independence broadly; the precise anchor for verifier-actor
  isolation is the self-preference/self-recognition findings (verify-techniques [3],[4]).
  basis: subagent anchor inspection.
- S1/S3 SURVIVES: anti-circularity (anchor-gated membership genuinely external + stronger
  than anneal; F3 dropped 2/6 seeds = the gate biting), recursion (never-self-certify holds
  by the exclusion rule). No action.

Reopened by loopback:
- D3 [PENDING] (reopened — F10/F12) re-design the wiring: foundation-invariant check FEEDS
  the operator's irreducible soundness pass (NOT a self-dischargeable substitute); residual
  on the discharge LINE (F12).
- D3b [PENDING] (reopened — F10) the hook forces artifact PRESENCE, not soundness; do not
  oversell as soundness-enforcement.
- D4 [PENDING] (reopened — F11) re-state honestly as audit-trail + friction (visible,
  deliberate, ratification-claiming act); binding = AI-discipline + operator review; drop
  the "binding gate / stops circularity" overclaim (per foundations.md operator-detection rule).
- D2 [PENDING] (reopened — F14) tighten entry-3 anchor to verify-techniques [3],[4]
  (self-preference/self-recognition = verifier-actor independence).

## Cycle (loopback fixes) — corrected enforcement design

- D2 [VERIFIED] REGISTER (re-confirmed; entry-3 anchor tightened per F14) — unchanged
  except: entry (3) verify-isolation anchor = verify-techniques findings [3],[4]
  (self-preference / self-recognition → verifier-actor independence; a verifier sharing
  the actor's model inherits over-scoring), replacing the broad "SGV" framing. The
  README still carries the anti-false-comfort residual AND the term defs. basis: F14 +
  verify-techniques [3],[4].
- D3 [VERIFIED] VERIFY-WIRING (re-wired per F10/F12) — (a) §2: the foundation-invariant
  artifact (per-touched-invariant holds/violates-against-anchor) is an explicit INPUT
  that FOCUSES the operator's irreducible soundness pass — NOT a co-equal mechanically
  discharged leg; the kernel-independent review stays skill-craft (form) + operator
  (soundness), with the register artifact as the soundness pass's grounding input. (b)
  step-4 discharge line records BOTH the produced artifact AND the operator's soundness
  verdict on it, AND carries the residual inline: `- Foundation-invariant check
  (method-kernel edits) → [per-touched-invariant holds/violates: subagent id] +
  [operator soundness verdict] — known-invariant only; novel soundness = operator` OR
  [N/A: not a method-kernel edit — cite paths]. (c) terse CLAUDE.md:14-21 update naming
  the register artifact as the soundness-pass input. basis: F10/F12 + located reads.
- D3b [VERIFIED] WIRING-ENFORCEMENT (re-framed per F10) — hooks/commit-msg requires the
  Foundation-invariant check LINE present on kernel-source commits (mirror run-gate
  KERNEL_PATTERNS): this forces the focusing artifact to be PRODUCED + PRESENTED, it does
  NOT and cannot enforce the soundness judgment (that is the operator's, gated by step-4
  approval as for all checks). The hook's honest job: catch a SKIPPED foundation-invariant
  artifact, not certify soundness. basis: F10 + hooks/commit-msg:125-163 (presence-check).
- D4 [VERIFIED] PROTECTION (re-stated honestly per F11) — the Invariant-change-ratified
  marker is an AUDIT-TRAIL + DELIBERATE-FRICTION mechanism: a commit that MODIFIES/DELETES
  a registered invariant (INV-*.md; --diff-filter=MD) must carry a visible,
  ratification-CLAIMING line, making invariant-weakening a deliberate, logged, operator-
  claiming act rather than a silent edit. It is NOT an unbypassable gate (--no-verify
  exists; a local hook CANNOT verify an operator actually approved — that is
  operator-detection, malformed enforcement per foundations.md). Binding = AI-discipline +
  the operator's review catching a bogus ratification claim. Local-only. The "stops
  circularity / binding gate" claim is dropped; the value is visibility + friction +
  audit-trail. basis: F11 + foundations.md operator-detection rule + hooks/commit-msg:25.
- F13 disposition: → validation-watch entry (NOT closed here) — "Does the register SHRINK
  the operator's soundness pass, or add net artifacts? Focus-payoff unproven by the 3
  shipped edits." Build proceeds (anchor-grounding value holds regardless); watch against
  future kernel edits. (To be authored in dev-notes/validation-watch/ at implement.)

D-track after fixes: D1,D2,D3,D3b,D4,D5,D6 all [VERIFIED]; F10/F11/F12/F14 addressed by the
above; F13 → validation-watch. Re-convergence + a re-run intent-falsification on the
corrected design follow before [READY].

## Intent-falsification round 2 (on corrected design; subagent aa950c4252d921e20) — consistency defect

Verdict: YES-IF-fixed. B1/B2 genuinely fixed (not relabeled); anti-circularity + operator-irreducibility hold; D4 honesty earns its place. ONE defect (3 faces):

- F15 [PENDING] D4's operator-detection honesty was NOT applied to D3. D3's discharge
  line `[operator soundness verdict]` slot is AI-fillable + hook-greenlit on string-presence
  → (a) adds no new gating event (the single global step-4 approval, development-process.md
  :567-575, was always the gate); (b) reintroduces operator-detection-dependence (the hook
  cannot distinguish an operator-originated verdict from an AI-pre-filled one); (c)
  engagement-erosion — trains the operator to RATIFY a pre-filled verdict rather than
  ORIGINATE one (subtler than B1: keeps operator in-loop while hollowing the verdict). Plus:
  the hook's `✓ Discharge ... passed` (commit-msg:251) is an un-annotated comfort surface
  the residual does not reach. basis: foundations.md:50-58 (operator-detection malformed) +
  development-process.md:567-575 (single global approval) + commit-msg:251.
- D3 [VERIFIED] VERIFY-WIRING (re-corrected per F15; operator-detection honesty applied
  UNIFORMLY) — the AI-produced foundation-invariant artifact is a FOCUSING INPUT
  (per-touched-invariant holds/violates against anchors), explicitly NOT a soundness verdict.
  Discharge line carries the artifact + residual, with NO AI-authored operator-verdict slot:
  `- Foundation-invariant check (method-kernel edits) → [per-touched-invariant holds/violates
  artifact: subagent id] — FOCUSING INPUT for the operator's soundness pass; NOT a soundness
  verdict (known-invariant only; novel soundness = operator)` OR [N/A: not a method-kernel
  edit — cite paths]. §2: the operator ORIGINATES the soundness verdict (the global step-4
  approval is the gate); the artifact focuses, never pre-empts it — same honesty as D4 (the
  AI does not author the operator's judgment). basis: F15.
- D3b [VERIFIED] WIRING-ENFORCEMENT (re-corrected per F15) — hook forces the focusing-artifact
  line PRESENT on kernel-source commits; for such commits its pass signal states it confirms
  artifact-PRESENCE, NOT soundness ("✓ foundation-invariant focusing artifact present — NOT a
  soundness certification; operator soundness verdict required"). basis: F15 + commit-msg:251.

S1/S3 (anti-circularity via anchor-gated membership+exclusion; operator structurally
irreducible — register can never speak to novel/anneal-only soundness) SURVIVE — strongest part.

## Final convergence (post-F15) + [READY] artifacts

Standardized pass (F15-fix cycle): Over-claimed-verification CLEAN — the F15 fix REMOVED an
overclaim (the AI-pre-filled operator-verdict slot); Unenforced-rule CLEAN — D3b reframed to
the honest form (hook forces artifact PRESENCE, pass-signal disclaims soundness); Bloat CLEAN
(no added prose); Missed-dependents/Leakage/Fragmentation/Undefined-shorthand — no new surface
(F15 tightened framing within existing sites). Lossy-render N/A (spec-only cadence).

Mechanical falsification: D3/D3b sites unchanged by F15 (framing-only) → cycle-6 target-existence
holds carries forward; D1 (cycle-4), D2/D3b/D5/D6 unchanged. Zero new D-track delta → CONVERGED.

Soundness (intent-falsification, ad-hoc): 2 rounds run; round 1 → B1/B2 (blocking, fixed),
round 2 → F15 (notable, fixed); structural core (anti-circularity, operator-irreducibility)
held through both. Round 3 available on request; the operator's soundness sign-off at `next
phase` is the irreducible gate per the method-kernel-edit discipline (NOT the ad-hoc check).

Fresh-session implementability: PASSED — per implementer step, external evidence:
- U1 REGISTER: folder model `ls dev-notes/validation-watch/` (F2); 5 invariant homes located
  (core.md §3.2; core.md:18; foundation.md:28-29 + core.md §4.3; core.md §4.1.4 ×2 — cycle-6
  falsification holds); 5 anchors in dev-notes/research/ (Zave-Jackson [1]/[0]; verify-techniques
  [3],[4]; Platt [4] + Quine-Duhem [7]; Gunter WRSPM [3]) — all extracted + verified this run.
- U2 WIRING: located reads development-process.md §2 (25-36), step-4 template (567-579),
  CLAUDE.md (14-21) — insertion points confirmed (cycle-6 holds).
- U3 HOOK: hooks/commit-msg REQUIRED_CHECKS (52-60) + pass-signal (251); run-gate KERNEL_PATTERNS
  (57-62, F7); --diff-filter=MD (git) — all read.
- U4 BACKLOG: multivoter item reframed (DONE this run) + sweep item created (DONE); remaining =
  file candidate-2 (scenario suite) + ready parent for archive (at persist).

Convergence cycle outputs (investigation new-surface + falsification + zero-delta) complete.
→ [READY]. Awaiting operator `next phase` (= the method-kernel-edit operator soundness sign-off).

## IMPLEMENT — unit completions

- U1 [COMPLETE] REGISTER (D2, D6) — created dev-notes/foundation-invariants/{README.md,
  INV-1-basis-rule.md, INV-2-complete-state.md, INV-3-verify-isolation.md,
  INV-4-loopback-not-settled.md, INV-5-exclusion-via-named-falsifier.md, archive/.gitkeep}.
  Subagent a093223eb1bcd68c0; skill-craft invoked; anchors+homes verified against
  files/research (no blind transcription); self-check 4-lens + scope CLEAN; no loopback.
  Persistence: working-tree change-set (uncommitted — deferred to the operator-approved
  release commit per commit-discipline; per-unit checkpoint commits skipped, in-session run).

- U2 [COMPLETE] VERIFY-WIRING (D3) — development-process.md §2 (foundation-invariant
  focusing artifact added as a FOLLOWING sentence; review-grounds sentence + "never
  self-certify" framing UNCHANGED, verified) + step-4 discharge template (+1 check line,
  mechanically-checkable N/A) + CLAUDE.md grounding bullet (terse register mention, pointer
  kept). Subagent ab3d1b1a9ce7ae946; skill-craft invoked; self-check 4-lens + scope CLEAN;
  no loopback. Persistence: working-tree (uncommitted; deferred to release).

- U3 [COMPLETE] WIRING-ENFORCEMENT + PROTECTION (D3b, D4) — hooks/commit-msg +154/-0:
  KERNEL_SOURCE_PATTERN (mirrors run-gate KERNEL_PATTERNS, F7) → requires "Foundation-invariant
  check" line on kernel-source commits (block-if-absent; pass-note disclaims soundness, D3b
  honest framing); INVARIANT_FILE_PATTERN + --diff-filter=MD → requires Invariant-change-ratified
  marker on MODIFY/DELETE of INV-*.md (Additions/README/archive exempt; D4 audit-trail+friction
  framing). Subagent ab19d7a8cd7de7d4a; py_compile OK; 9 cases traced (incl. run's-own-release
  PASSES). self-check 4-lens + scope CLEAN; no loopback. Persistence: working-tree (uncommitted).

- IMPLEMENT [COMPLETE] — U1+U2+U3 done; U4 (backlog grooming: file candidate-2 scenario suite,
  ready parent for archive) deferred to persist (step 7). → verify (isolated).

## verify round 1 → [ISSUES FOUND] → loopback → fix → delta re-verify

Verify (isolated, subagent ab88771bd4e7f265c): D1-D6+D3b planned-vs-actual CLEAN (5
kernel-homes spot-checked vs source; §2 unsoftened; hook traced 8 cases; glossary clean),
all 8 lenses CLEAN, battery (a)/(c) N/A confirmed by path-evidence, (b) coherence RUN clean.
ONE finding:
- F-DC1 [VERIFIED — addressed] design-completeness: F13's committed disposition (→ author a
  validation-watch entry "at implement") was NOT produced — F13 left short of a valid terminal.
  Addressed: authored dev-notes/validation-watch/V-29-register-focus-payoff.md (the committed
  artifact). basis: V-29 file exists. Fix is behavior-preserving (additive dev-notes companion;
  no rule/render changed) → delta re-verify.
- F13 [VERIFIED — deferred] focus-payoff uncertainty → validation-watch V-29 (WATCHING). Trigger
  (observable event class): a future method-kernel edit exercising the register (a kernel-source
  commit carrying the foundation-invariant discharge artifact) re-fires V-29's production-signal
  evaluation at post-run review. basis: V-29 authored; disposition cites V-29's trigger.

## verify round 2 (delta) → [PASSED] — RUN COMPLETE

Delta re-verify (isolated, subagent a518e32c300a6531c):
- F-DC1 [VERIFIED — addressed] V-29 authored + valid (WATCHING, not premature); matches F13.
- F13 [VERIFIED — deferred] valid terminal (trigger = future method-kernel edit exercising the register).
- Behavior-preserving regression CLEAN (only the V-29 file added beyond the verified U1/U2/U3 change-set).

Verify result: [PASSED] (isolated, delta). Run Status → PASSED. render-and-open-diff extension
disabled (spec-only cadence) → no post-verify render. Release (steps 5-7) pending operator approval.
Persist done: parent backlog item archived; V-29 watch filed; backlog rehomed (multivoter reframed,
sweep + canonical-scenario-suite + deferred-finding-owed-artifact filed).
