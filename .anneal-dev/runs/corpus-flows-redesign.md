# Run: corpus-flows-redesign

- **Status:** PASSED
- **Phase:** verify
- **Mode:** interactive
- **Task:** Re-design the three corpus-work paths (new-instantiation / dev-on-anneal / re-render-existing-instances) into one clear, contained, single-channel (anneal-dev) system with explicit boundaries + structural enforcement. Spine: the anneal-dev↔anneal-framework repo-merge fork (question #4). Strategy/design deliberation — turn `dev-notes/backlog/corpus-flows-redesign.md` into a decided design. Method-kernel-adjacent (touches `spec/README.md`) → verify adds kernel-independent review (skill-craft self-review + operator) per `development-process.md` lines 19-32.

---

## F-track (findings)

- **F1 [PENDING]** Path-1 (new instantiation) is split: `instantiation-guide.md` §1-5 (domain-fit, write spec, bind, derive lens-set) is a STANDALONE MANUAL procedure; only §6 ("With the spec settled… built and evolved as corpus-evolution work — run through anneal-dev") routes the BUILD/render through anneal-dev. — basis: located read `instantiation-guide.md` §6 lines 428-438 (the "run through the anneal-dev instance" hand-off sentence) + §1 lines 40-60 (manual domain-fit check).
- **F2 [PENDING]** Path-2 (dev-on-anneal) routes corpus-evolution AND method-kernel edits through anneal-dev; method-kernel adds a kernel-independent verify (skill-craft self-review + operator). — basis: located read `development-process.md` lines 9-32 (the two-regime routing block; "runs through anneal-dev" + "never certifies a kernel edit alone").
- **F3 [PENDING]** Path-3 (re-render existing instances) is PROSE-mandated through anneal-dev with NO structural routing-enforcement: the `skill-craft-pre-edit.py` hook gates Edits to `plugin/skills/*/` on a skill-craft invocation, NOT on anneal-dev routing — a hand-render through skill-craft (bypassing anneal-dev) passes the hook. — basis: located read `spec/README.md` lines 50-52 ("Re-rendering runs as corpus-evolution work through the anneal-dev instance") + `development-process.md` lines 173-187 (hook scans for `Skill skill-craft`, not anneal-dev).
- **F4 [PENDING]** Stale parenthetical: `development-process.md` lines 17-18 "(Run followed-in-context until anneal-dev is packaged for install.)" is false — anneal-dev IS packaged (plugin.json + marketplace.json + installed pin 0.1.2). — basis: located read `development-process.md` lines 17-18 + file existence `anneal-dev/plugin/.claude-plugin/plugin.json`.
- **F5 [PENDING]** The kernel-independent-verify rule does NOT rest on repo SEPARATION (backlog's stated merge cost): it rests on render-lineage (anneal-dev rendered FROM the kernel → shares its blind spots) + outside-kernel checkers (skill-craft, a different corpus; the operator, human). Merging git repos changes neither. foundation.md's 3 contracts reference render-lineage + domain-binding, never repo count. — basis: located read `development-process.md` lines 19-32 (rationale = "a checker built from the kernel shares its blind spots") + `foundation.md` lines 10-40 (3 contracts; observable fact: zero repo-boundary reference).
- **F6 [PENDING]** The anneal-dev coupling ALREADY straddles the repo boundary asymmetrically: anneal-dev's operator-config (`anneal-framework/anneal-dev.config/`) + runtime state (`anneal-framework/.anneal-dev/runs/`) + render-SOURCE (`anneal-framework/spec/`) live in anneal-framework, while the render-OUTPUT + marketplace + version-pin live in the separate anneal-dev repo with its own remote. — basis: located read dir listing `anneal-framework/anneal-dev.config/` exists + `anneal-dev/.claude-plugin/marketplace.json` exists (one anneal-dev, two repos hosting its parts).
- **F7 [PENDING]** LIVE symptom of the boundary: clean `0.1.2` render is UNPUSHED (anneal-dev `main...origin/main [ahead 2]`; origin still `ee9e2e6`), and THIS session loaded the skill from the `0.1.1` cache despite `installed_plugins.json` pointing at `0.1.2` — cross-repo packaging boundary producing live version/cache confusion. — basis: search `git -C anneal-dev status -sb` → "ahead 2"; skill activation base-dir `…/anneal-dev/0.1.1/…` vs `installed_plugins.json:144` installPath `…/0.1.2`.
- **F8 [PENDING]** Path-3 routing is NOT adopted into instances: `beat-the-books/clippy` + `bauleitplan-anneal` have NO CLAUDE.md; `daneel` + `coding-clippy` CLAUDE.md carry rendered-language but ZERO anneal-dev mention. The "route re-renders through anneal-dev" rule lives in the framework SEED (`instance-template/CLAUDE.md`) but hasn't propagated. — basis: search `rg -l anneal-dev` over the 4 instance repos → empty; `ls CLAUDE.md` absent for clippy + bauleitplan. (Relates: `adoption-instance-settlement` backlog item.)
- **F9 [PENDING]** The routing principle is FRAGMENTED across ≥3 framework homes — `development-process.md` (corpus-evolution/method-kernel), `instantiation-guide.md` §6 (build), `spec/README.md` :50 (re-render) each independently state "run through anneal-dev." Drift risk; the redesign must canonicalize to one statement + cross-refs, not add a 4th. — basis: search (`re.render` + `corpus.evolution` tokens) each returns development-process.md + instantiation-guide.md + spec/README.md.

---

## D-track (design decisions)

- **D1 [VERIFIED]** SCOPE (foundational): the routing-contract — how the three corpus-work paths route + are enforced — is encoded in 6 anneal-framework root docs (`development-process.md`, `instantiation-guide.md`, `spec/README.md`, `README.md`, `CLAUDE.md`, `instance-template/CLAUDE.md`) PLUS the per-instance CLAUDE.md adoption surface (F8); `spec/glossary.md` + `spec/modules.md` carry the re-render METHOD DEFINITION (dependents to audit at change-time, not routing-prose to rewrite). — basis: wrap-tolerant searches, executable queries: `rg -l 'anneal-dev' -g '*.md' -g '!dev-notes/**'`, `rg -l 'corpus.evolution'`, `rg -ln 're.render'`, `rg -ln 'method.kernel|kernel.independent'` over the framework repo (root-doc set converges to the 6 above; glossary/modules appear only on the re-render method-token).
- **D2 [OUTLINED]** Define the three paths cleanly (Q#1): name each + its input→output + the boundary between them. Committed boundary insight from F1: Path-1 = spec-DERIVATION (manual, domain expertise) → then HAND-OFF to the same build/evolve machinery as Path-2/3 at "spec settled" (`instantiation-guide.md` §6); so the real distinction is derivation-act vs evolution-act, not three parallel silos. — basis: F1 (the §6 hand-off sentence is the existing boundary marker). Concrete per-path input/output table not yet written → [OUTLINED], needs a cycle.
- **D3 [OUTLINED]** Route all three through anneal-dev as the single channel (Q#2): YES — design Path-1's derivation act as an anneal-dev entry (mode/extension), folding the standalone `instantiation-guide.md` procedure into the channel rather than leaving it parallel. — basis: F2 + F3 + F9 (two of three paths already route to anneal-dev; the third (instantiation derivation) is the lone holdout; one channel removes the fragmentation in F9). Rests on confirming the derivation act fits the investigate-design phase shape → sharpen next cycle.
- **D4 [PENDING]** Enforcement (Q#3): the channel needs a STRUCTURAL forcing function for the render/route path, not prose-only — the current hook enforces skill-craft-invocation but not anneal-dev-routing (F3), so re-render-routing is unenforced prose (Unenforced-rule). Committed direction: design a structural gate (shape TBD — e.g., extend the pre-edit hook to require a live anneal-dev run-context for `plugin/skills/*/` edits, or a render-provenance artifact). — basis: F3 + `development-process.md` practice 8 (load-bearing rule left as prose is under-prescribed). Concrete gate shape needs design → [PENDING].
- **D5 [CONDITIONAL]** Repo-merge (Q#4, the spine): MERGE anneal-dev into anneal-framework (anneal-framework becomes the marketplace host; anneal-dev becomes a tracked subtree) — the cross-repo boundary is the convolution's root (F6/F7) and the merge is ARCHITECTURALLY FREE (F5: no contract rests on repo count; kernel-independent-verify rests on render-lineage + outside-kernel checkers, both preserved under merge). — basis: F5 + F6 + F7. ASSUMPTION (operator-resolvable): operator accepts anneal-framework becoming a published plugin-marketplace repo + anneal-dev losing standalone independent distribution (low value — its only users already hold the framework spec). Concrete merge mechanics (subtree vs subdir; marketplace.json restructure; reconciling the unpushed 0.1.2) are a downstream decision, not yet designed.
  - considered: keep-separate-and-sharpen-the-boundary (rejected: papers the root cause (F6/F7) with prose discipline; `development-process.md` practice 8 + practice 7 "design-time placement wins" favor structural elimination of the boundary over recurring cross-repo discipline).
  - considered: anneal-dev-is-an-instance→instances-are-separate-repos uniformity (rejected: anneal-dev is already non-uniform — F6 shows its config/runstate/render-source live in the framework repo, not its own; the uniformity is already broken).

---

## Cycle 2 (append-only)

### F-track updates + new findings

- **F1 [VERIFIED — addressed]** Path-1 split observation addressed by D2 (the derivation-act-vs-evolution-act boundary names exactly this split). — basis: D2 (cites `instantiation-guide.md` §6 hand-off).
- **F2 [VERIFIED — addressed]** Path-2 two-regime routing addressed by D2+D3 (folded into the one-channel model). — basis: D2, D3.
- **F4 [VERIFIED — addressed]** Stale "(until anneal-dev is packaged)" parenthetical addressed by D2's routing-doc rewrite (the parenthetical is removed when `development-process.md` lines 9-18 are re-stated to the one-channel model; anneal-dev IS packaged). — basis: D2; `development-process.md` lines 17-18 located.
- **F5 [VERIFIED — non-issue]** The backlog premise "merge endangers the kernel-independent-verify rule" is contradicted by the rule's own basis: it rests on render-lineage + outside-kernel checkers, neither of which a git-repo merge touches. — basis: located read `development-process.md` lines 19-32 (rationale "a checker built from the kernel shares its blind spots" — render-lineage, fact: no repo-boundary clause) + `foundation.md` lines 10-40 (3 contracts, fact: zero repo-count reference).
- **F9 [VERIFIED — addressed]** Routing-fragmentation addressed by D2+D3 (one canonical channel statement; the 3 current homes become one home + cross-refs). — basis: D2, D3.
- **F10 [PENDING]** Re-render (Path-3) is ALREADY structurally inside the anneal-dev channel: verify battery check (a) render-fidelity (separate-context, clause-by-clause) + the `render-and-open-diff` on-verify-PASSED extension produce the re-render. Path-3 is the render-TAIL of any spec-changing run, not a separate path. — basis: located read `phases/verify.md` lines 58-67 (check (a)) + `anneal-dev/spec/extensions.md` lines 26-38 (the extension).
- **F11 [PENDING]** The `skill-craft-pre-edit.py` hook is registered in anneal-framework and scans the SESSION transcript; it fires for plugin edits in an anneal-framework-rooted session but NOT for edits made from a separate instance-repo-rooted session unless that instance installs the hook. Routing-enforcement for OTHER instances (clippy/daneel/…) needs per-instance hook deployment — and the merge does NOT fix that (clippy stays a separate repo regardless). — basis: located read `hooks/skill-craft-pre-edit.py` lines 1-36 (PreToolUse, transcript-scan) + the hook's home is anneal-framework/hooks.
- **F12 [PENDING]** `render-and-open-diff` derives affected renders from "the tracker's verified D-entries whose targets are rendered plugin clauses" — so a single run re-renders exactly the instances its decisions targeted. Multi-instance propagation of a framework-spec change requires the run's D-entries to target each affected instance's clauses (not automatic fan-out across all instances). — basis: located read `anneal-dev/spec/extensions.md` lines 32-33.

### D-track updates + new decisions

- **D2 [VERIFIED]** The three paths are THREE ENTRY-CONDITIONS into ONE channel (anneal-dev: investigate-design → implement → verify, with the render-fidelity battery + the `render-and-open-diff` extension + the release loop), NOT three parallel systems. Entry-conditions by starting state: (1) new-instantiation = no instance spec yet (derive spec, then build); (2) dev-on-anneal = a rule-change to make (corpus-evolution, or method-kernel + outside-kernel verify); (3) re-render = a spec change already committed, to propagate (the pure render-tail). Path-3 was never separate (F10); Path-1's derivation act (instantiation-guide §1-5) is the lone piece outside the channel, folded by D3. — basis: F10 + `phases/verify.md` lines 58-67 + `anneal-dev/spec/extensions.md` lines 26-38 + `instantiation-guide.md` §6.
- **D3 [VERIFIED]** Route all three entry-conditions through anneal-dev. The instantiation derivation act fits the channel: deriving an instance spec is a design task (investigate the domain → lock bindings + lens-set = investigate-design's "produce a locked design"), the plugin render is implement, render-fidelity is verify; and authoring spec files IS corpus-evolution, the domain anneal-dev already owns. — basis: `phases/investigate-design.md` lines 3-5 ("build understanding + produce a locked design") + `instantiation-guide.md` §6 (build already routed as corpus-evolution).
- **D6 [CONDITIONAL]** The `instantiation-guide.md` §1-5 domain-knowledge (domain-fit check, the closed slot set, Path-2 lens-set bootstrap) is PRESERVED and REFRAMED, not deleted: it stops being a "standalone manual procedure you follow by hand" and becomes the spec/input an anneal-dev instantiation-entry run is DRIVEN BY (as a clippy run is driven by a codebase). Minimal text change: §6 + the framing shift. — basis: D3 + `instantiation-guide.md` §1-5 (the domain-knowledge is valuable, not redundant). ASSUMPTION (operator-resolvable): operator prefers reference-in-place over folding §1-5 into anneal-dev's own spec.
- **D4 [PENDING]** Enforcement of the routing rule (Q#3) — TWO open sub-questions hold this short of locked: (i) **Is a new gate even warranted?** The existing hook (skill-craft gate + spec-origin reminder) + release-loop step-4 render-fidelity discharge already enforce isolated render-fidelity; a new anneal-dev-specific gate risks Additive-reflex (duplicating). (ii) **If warranted, what signal?** A naive "scan-for-anneal-dev-invocation" gate fails — anneal-dev's own implement subagents don't re-invoke anneal-dev (they're dispatched by it), so the scan would block the legitimate render. Candidate signals: an in-progress `.anneal-dev/runs/<run>.md` tracker (complication: multi-repo run-state location), or an orchestrator-passed marker in the dispatch brief. — basis: F3 + F11 + `hooks/skill-craft-pre-edit.py` lines 186-209 (the scan logic) + `development-process.md` release-loop step 4 (existing render-fidelity discharge). Concrete gate shape undesigned → [PENDING].
- **D5 [CONDITIONAL]** (mechanics now designed; recommendation unchanged = MERGE). Concrete mechanics IF operator accepts: move `anneal-dev/{plugin,spec,derivation-rationale.md,README.md}` into anneal-framework as a subdir (e.g. `anneal-framework/anneal-dev/`); anneal-framework hosts the marketplace manifest; render becomes intra-repo (`spec/` source → `anneal-dev/plugin/` output); the clean local `0.1.2` render is the merged state (reconciles F7's unpushed-render); git via subtree-merge to preserve anneal-dev history; operator re-points the marketplace clone + installed pin post-merge. EXECUTION is operator/infra git-work surfaced as a companion to the routing-doc edits, not an anneal-dev implement-unit (anneal-dev produces rule-text, not repo restructures). — basis: F5 + F6 + F7. ASSUMPTION (operator-resolvable, unchanged): operator accepts anneal-framework-as-marketplace + loss of standalone anneal-dev distribution.
  - coupling note: D5 does NOT break D2/D3 (the one-channel model is repo-count-independent). It DOES touch (a) incidental "anneal-dev repo, sibling to this one" phrasings (`development-process.md` line 11) — a Missed-dependents item for implement; (b) D4's gate scope (merged → one hook covers anneal-dev's render; separate instances unaffected either way per F11).

---

## Cycle 3 (append-only)

### F-track updates + new finding

- **F3 [VERIFIED — addressed]** "Re-render routing is unenforced prose" addressed by D4: the rule isn't under-prescribed-prose pretending to be a hard rule — its load-bearing sub-guarantees (render-fidelity, skill-craft form, spec-origin) ARE structurally gated (pre-edit hook + commit-msg discharge hook); routing-through-anneal-dev is the rigor-preferred channel, correctly classified. — basis: D4.
- **F6 [VERIFIED — addressed]** Asymmetric cross-repo coupling addressed by D5 (merge co-locates the parts). — basis: D5.
- **F7 [VERIFIED — addressed]** Unpushed-0.1.2 / stale-cache symptom addressed by D5 (merge makes the clean render the merged state; intra-repo render removes the cross-repo pin drift). Operational note: independent of the design, the operator should push 0.1.2 + reload OR fold it into the merge. — basis: D5.
- **F8 [VERIFIED — deferred]** Instance non-adoption of routing deferred to `adoption-instance-settlement` (existing backlog item); trigger = each instance's Phase-B re-render (a file-change event class re-firing the finding per instance). — basis: `dev-notes/backlog/adoption-instance-settlement.md` (the deferring item) + trigger condition (instance re-render).
- **F10 [VERIFIED — addressed]** Re-render-already-in-channel addressed by D2 (incorporated as the render-tail entry-condition). — basis: D2.
- **F11 [VERIFIED — addressed]** Hook-per-repo coverage gap addressed by D4 (the enforcement-layering names hook-deployment-coverage as the floor's precondition); the per-instance hook DEPLOYMENT is deferred to `adoption-instance-settlement`. — basis: D4 + `dev-notes/backlog/adoption-instance-settlement.md`.
- **F12 [VERIFIED — non-issue]** "Does one run auto-fan-out to all instances?" — no, and that is correct, not a gap: `render-and-open-diff` re-renders exactly the instances a run's D-entries target, which is the right scope. — basis: located read `anneal-dev/spec/extensions.md` lines 32-33 (targets = verified D-entries' rendered-clause targets).
- **F13 [VERIFIED — addressed]** The `commit-msg` discharge hook is a LITERAL ACTIVE git hook (`git config core.hooksPath = hooks/`), blocking rule-corpus commits without a complete Step-4 discharge — confirming the checkpoint-vs-discharge conflict is mechanically real (anneal-dev per-unit checkpoint commits touch rule-corpus + cannot produce a pre-verify discharge). Addressed by D7. — basis: located read `hooks/commit-msg` lines 99-230 (blocks rule-corpus commit lacking discharge) + `git config core.hooksPath` = `hooks/` (hook is active) + `implement.md` lines 304-318 (checkpoint = commit reference).

### D-track updates + new decisions

- **D4 [VERIFIED]** Enforcement (Q#3): NO new structural gate forcing "all corpus edits route through anneal-dev." The load-bearing guarantees a routed run provides are ALREADY structurally enforced independent of routing — (1) the pre-edit hook gates every plugin/spec edit on skill-craft-invocation + injects spec-origin (`hooks/skill-craft-pre-edit.py` 262-296); (2) the commit-msg discharge hook blocks any rule-corpus commit lacking the Step-4 discharge artifact — render-fidelity (separate-context) + skill-craft review + coherence — operator-gated (`hooks/commit-msg` 99-230 + `development-process.md` 540-642). A new anneal-dev-routing gate is Additive-reflex (duplicates the gated fidelity guarantee), unworkable (an invocation-scan blocks anneal-dev's own implement subagents — F11/hook 186-209), and disproportionate (forces the full machine on a typo-fix — practice 7). The redesign's prose STATES this layering: structural floor (the two hooks) + AI-discipline (the CLAUDE.md re-grounding routes substantial corpus work through anneal-dev) + operator commit-gate. Also resolves `anneal-dev-extension-render-gate`: a mechanical re-render still hits the pre-edit skill-craft gate + spec-origin reminder — appropriate (skill-craft carries the rendering-fidelity rule), no carve-out. — basis: `hooks/commit-msg` 99-230 + `hooks/skill-craft-pre-edit.py` 262-296 + `development-process.md` 540-642 (step-4 discharge) + practice 7 + practice 8 / skill-craft Additive-reflex.
  - considered: a new hard gate requiring an in-progress anneal-dev run for plugin/spec edits (rejected: Additive-reflex — the commit-msg discharge hook already forces the load-bearing fidelity/review guarantee; unworkable signal — blocks anneal-dev's own dispatched subagents; disproportionate — full machine on trivial edits, against practice 7).
- **D7 [CONDITIONAL]** Checkpoint-vs-discharge reconciliation (F13, folded from `anneal-dev-impl-checkpoint-vs-discharge-hook`): the commit-msg discharge hook gates the RELEASE commit (operator-approved, pushed, step 5); anneal-dev's per-unit checkpoint commits are working-progress saves carrying a recognized marker the hook SKIPS — parallel to its existing Merge/Revert/fixup/squash skip-list (`hooks/commit-msg` 202-204). `development-process.md` states checkpoint-save ≠ release-commit. Split of work: the dev-process prose statement is anneal-dev implement work; the commit-msg hook skip-marker edit is companion code-work (a .py edit, outside anneal-dev's rule-text domain — parallel to D5's git-work). — basis: F13 + `hooks/commit-msg` 202-204 (existing skip-list precedent) + `implement.md` 304-318 (checkpoint = commit reference, unchanged). ASSUMPTION (operator-resolvable): operator accepts the marker-skip shape over heavier alternatives.
  - considered: run-branch + squash-merge release (rejected now: changes anneal-dev's in-place integrity mechanism — method-kernel-heavier; hold unless marker-skip proves insufficient); checkpoint-save-as-non-commit (rejected: `implement.md` defines the persistence reference AS a commit reference + integrity reads HEAD — a method-kernel change to avoid a lighter hook fix).
- **D8 [VERIFIED]** Canonical routing home (closes F9 structurally): the one-channel routing statement lives canonically in `development-process.md` (already "the home of the shared framework-dev machinery", its line 34); the other routing-touching docs (`instantiation-guide.md` §6, `spec/README.md` :50-52, `README.md`, `instance-template/CLAUDE.md`) carry a one-line POINTER to it, not a restatement — so the corpus holds one statement + cross-refs, not 3+ drifting copies. — basis: located read `development-process.md` line 34 ("This document is the home of the shared framework-dev machinery") + F9.

---

## Cycle 4 — CONVERGENCE CYCLE (append-only)

### Investigation pass (new surfaces)
New file citations this cycle: `README.md`, `instance-template/CLAUDE.md` (read whole); new query `rg 'home of …framework-dev'`.

- **F14 [VERIFIED — addressed]** README.md:110-113 labels the discharge artifact "step-**5** discharge" while `hooks/commit-msg` + `development-process.md` call it "Step-**4** discharge" — a minor labeling drift the D8 canonicalization implement sweeps up (the implementer aligns README's dev-process description to the canonical statement). No new decision. — basis: located read `README.md` 110-113 ("step-5 discharge") vs `hooks/commit-msg` line 3 ("Step-4 discharge") + D8.
- (confirming, no new finding) README.md:99-104 ALREADY names development-process.md "the home of the framework-dev machinery" + corpus-evolution router → confirms D8 + shows README/template-CLAUDE are already pointer-shaped (minimal implement change). instance-template/CLAUDE.md carries the rendered-not-authored + route-through-anneal-dev seed, pointing to development-process.md.

### Falsification pass → outcome (artifact: `…cycle-4.falsification.md`)
D1, D2, D4, D8 HOLD against adversarial attack. **D3 FALSIFIED** (2 of 3 candidates): anneal-dev's investigate-design Scope machinery presupposes "the contract being changed" + dependents (an existing corpus), which greenfield instance-derivation lacks; and the current corpus boundary (instantiation-guide §6) places the §1-5 derivation act OUTSIDE the channel.

### D-track: the cascade re-resolution
- **D3 [INVALIDATED]** (falsified by cycle-4 convergence pass — basis: `…cycle-4.falsification.md`).
- **D3 [VERIFIED]** (re-resolved): Route the BUILD + ALL EVOLUTION through anneal-dev — entry-conditions 2 (dev-on-anneal) + 3 (re-render) fully, and entry-condition 1's BUILD half (instantiation-guide §6 onward). The instantiation DERIVATION act (§1-5: domain-fit, author the instance spec, bind, derive the lens set) is a **PRE-CHANNEL design step** that produces the instance spec the channel then builds from — it is NOT folded into anneal-dev's investigate-design, because that phase's Scope machinery presupposes an existing contract + dependents (`phases/investigate-design.md` 88-104, `spec/core.md` 285) which greenfield authoring lacks; forcing it would require a method-kernel change to the scope machinery for a rare bootstrap act (against `spec/README.md` 150 "deliberately resistant to extension" + prescription discipline + practice 7). The channel boundary is instantiation-guide §6, stated cleanly. The load-bearing discipline (render-fidelity, basis rule, lenses) is NOT bypassed: it applies to all rule-text production (build + evolution), all in-channel; derivation produces a spec that the in-channel build then verifies. — basis: `…cycle-4.falsification.md` (Scope presupposes existing-contract) + `instantiation-guide.md` §6 (the existing boundary) + `spec/README.md` 150 (extension-resistance).
  - considered: fold §1-5 derivation INTO anneal-dev's investigate-design (rejected: requires editing anneal-dev's Scope phase-spec to admit greenfield — a method-kernel change expanding the method for a rare act; the de-convolution win (re-render = render-tail; build+evolution = one channel) does not require it).
- **D2 [INVALIDATED]** (amended — the "Path-1's derivation act … folded by D3" sub-clause is contradicted by re-resolved D3).
- **D2 [VERIFIED]** (re-resolved): One channel, three entry-conditions — re-render is the render-tail, NOT a separate path (HOLDS, falsification-confirmed). Correction: entry-condition 1 (new instantiation) carries a PRE-CHANNEL derivation prefix (§1-5) before its build enters the channel; the derivation is a design step, not a fourth routing path and not folded into the channel (per D3). The de-convolution thesis is unchanged: the three "convoluted paths" were really ONE channel for build+evolution (re-render ≠ separate), plus a well-defined derivation design-step prefixing instantiation. — basis: `…cycle-4.falsification.md` (D2 core holds) + D3 (the derivation boundary).
- **D6 [CONDITIONAL]** (amended, lightened): `instantiation-guide.md` §1-5 STAYS as the pre-channel derivation procedure (largely unchanged — it is the design-step spec); §6's hand-off boundary to the channel is stated cleanly + the framing that all post-derivation work (build + evolution) runs in-channel. Lighter than the prior "reframe §1-5 as channel input." — basis: re-resolved D3 + `instantiation-guide.md` §6. ASSUMPTION (operator-resolvable): operator accepts keeping §1-5 as the canonical derivation procedure (vs folding into anneal-dev's spec).

### Convergence status
NOT clean — cycle 4 produced D-track deltas (D3 falsified+re-resolved; D2 amended; D6 amended). Per `phases/investigate-design.md`, [READY] requires a convergence cycle observed clean; the deltas feed the next cycle. D1, D4, D5, D7, D8 unaffected (re-resolved D3 is repo-independent and edit-discipline-independent). A re-attempt convergence cycle must re-falsify the changed D2/D3 (and confirm D6's assumption stands).

---

## Cycle 5 — RE-ATTEMPT CONVERGENCE CYCLE (append-only) → CLEAN

### Investigation pass (new surfaces)
New citations: `anneal-dev/spec/bindings.md`, `spec/core.md` §3.2 (line 285 read whole), the anneal-dev run-history scan.

- **F15 [VERIFIED — addressed]** anneal-dev's OWN domain bindings presuppose an existing corpus — scope binding = "the set of spots encoding **the contract being changed**" (`anneal-dev/spec/bindings.md` line 40), "existing work = the rule-corpus **as it currently stands**" (line 37); and all 8 anneal-dev runs in history are edit/re-render/method-kernel (ZERO greenfield derivation). Confirms D3′ at the instance-binding level + empirically. — basis: located read `anneal-dev/spec/bindings.md` lines 37,40 + run-history task scan (8 trackers, all edit/re-render). Addressed by D3′ (it is the confirming evidence).

### Falsification pass → outcome (artifact: `…cycle-5.falsification.md`)
ALL FIVE [VERIFIED] entries (D1, D2′, D3′, D4, D8) HOLD on FRESH candidates (query strings/reads distinct from cycle 4). D3′ residual ("does pre-channel derivation escape discipline?") failed to falsify: instance `spec/*.md` authoring matches BOTH hooks' patterns (executed against `coding-clippy/spec/bindings.md` etc.) → hits the structural floor where deployed; no corpus text claims derivation must run through anneal-dev; extension-resistance basis confirmed. Pre-existing F11 (per-instance hook deployment) noted, already deferred — not a new escape.

### Convergence verdict: CLEAN
New-surface investigation pass + falsification pass (5/5 hold) + ZERO D-track deltas. The convergence-cycle requirement (`phases/investigate-design.md`) is met.

### Fresh-session-implementability test: PASSED (per-implementer-step external evidence)
A session with only this tracker implements the design without surfacing a new design decision:
1. Edit `development-process.md` (U1) — the routing-intro rewrite. Evidence: located read `development-process.md` lines 9-38 (current two-regime block to re-state), lines 17-18 (stale parenthetical to remove), line 11 (sibling-repo phrasing), line 34 (machinery-home, grounds D8 canonical placement).
2. Edit `instantiation-guide.md` §6 boundary + framing (U2). Evidence: located read `instantiation-guide.md` lines 14-37 (spec-first process), §6 lines 428-438 (the hand-off boundary).
3. Edit `spec/README.md` re-render pointer (U3). Evidence: located read `spec/README.md` lines 50-52 (the re-render routing sentence → pointer).
4. Edit `README.md` + `instance-template/CLAUDE.md` + `CLAUDE.md` pointer alignment + F14 (U4). Evidence: located read `README.md` 99-104 (routing description) + 110-113 (the step-5 drift); `instance-template/CLAUDE.md` 13-15.
5. Companion: repo-merge git-work (C1, gated D5=merge); commit-msg skip-marker (C2). Evidence: `anneal-dev/.claude-plugin/marketplace.json` + `plugin/.claude-plugin/plugin.json` (the packaging to relocate); `hooks/commit-msg` lines 202-204 (the skip-list to extend).
Result: **PASSED** — each step's target + change is derivable from the locked decisions (D1-D8) without a new design decision; realization output (exact rule-text) is impl work per `tracker.md`.

### [READY] — design presented for operator next-phase decision
Tracker state: F1-F15 all [VERIFIED]; D1, D2′, D3′, D4, D8 [VERIFIED]; D5, D6′, D7 [CONDITIONAL] (auto-accept at next-phase). Standardized lens set accounted for whole; last cycle's pass clean. Convergence cycle clean. Impl plan: `…impl-plan.md`.

---

## Phase transition: investigate-design → implement (operator next-phase)

Operator selected `next phase` at the [READY] presentation without overriding any open [CONDITIONAL]. Per `references/tracker.md` / `foundations.md`, the three [CONDITIONAL] decisions become [AUTO-ACCEPTED]:

- **D5 [AUTO-ACCEPTED]** MERGE anneal-dev into anneal-framework (the assumption — operator accepts framework-as-marketplace + loss of standalone anneal-dev distribution — was not overridden). Surfaced for post-run review.
- **D6′ [AUTO-ACCEPTED]** Keep instantiation-guide §1-5 as the pre-channel derivation procedure (not folded into anneal-dev's spec).
- **D7 [AUTO-ACCEPTED]** Checkpoint ≠ release-commit via marker-skip (over the heavier alternatives).

Impl plan locked: `…impl-plan.md` (U1 sequential anchor → U2/U3/U4 parallel-eligible; C1 repo-merge + C2 hook-skip-marker companion). C1 gating-status: D5=merge → C1 runs.

---

## IMPLEMENT → loopback to investigate-design (actioned finding F16)

Implement executed C2 (commit `00374a5`, hook skip-marker) and C1a (the co-location subtree-add, commit `d5ae00d` — anneal-dev → `anneal-framework/anneal-dev/`, clean 0.1.2 carried, live install untouched). Verifying C1a surfaced an actioned finding → loopback (`implement.md`: inline-fix is malformed; loopback or defer).

- **F16 [PENDING]** (loopback-required) The merge relocated anneal-dev's rule-corpus to `anneal-dev/plugin/skills/…` + `anneal-dev/spec/…`, which the `commit-msg` discharge hook's `^`-anchored `RULE_CORPUS_PATTERN`/`INSTANCE_PLUGIN_PATTERN` do NOT match → the merged anneal-dev's rule-corpus commits bypass the discharge gate D4's floor rests on. (Pre-edit hook unaffected — it `re.search`es absolute paths, still matches.) The merge also has housekeeping dependents the design under-enumerated.
  - **trigger:** subtree-add commit `d5ae00d` added `anneal-dev/plugin/skills/*.md` + `anneal-dev/spec/*.md`; the commit passed commit-msg WITHOUT a discharge.
  - **scope:** D4's structural-floor coverage for the merged location (the commit-msg hook patterns); the merge's housekeeping dependents (development-process.md:10 "sibling repo" phrasing — already in U1; README.md anneal-dev link — U4; the standalone anneal-dev repo's now-duplicated status; the nested `anneal-dev/.gitignore`).
  - **basis:** executed `RULE_CORPUS_PATTERN.match` → False for `anneal-dev/plugin/skills/anneal-dev/SKILL.md`, `anneal-dev/spec/bindings.md`, `anneal-dev/.claude-plugin/…`; pre-edit `re.search` → True (unaffected); `rg 'anneal-dev repo|sibling'` → only development-process.md:10 merge-coupled.
  - **affected_decisions:** D5 (EXTENDED — its merge mechanics under-enumerated the commit-msg-hook-coverage + housekeeping dependents); D4 (its floor-coverage for the merged location is incomplete until the hook is fixed — D9 below restores it).

Work preserved (redo-inheritance): commits `00374a5` (C2) + `d5ae00d` (C1a merge) STAND — the co-location is correct; the loopback enumerates + fixes its dependents, it does not revert the merge. Run returns to investigate-design at cycle 6.

---

## Cycle 6 — investigate-design (loopback recovery for F16) → re-converged

### F-track
- **F16 [VERIFIED — addressed]** Merge-dependent gap addressed by D9 (hook coverage, the load-bearing fix) + D10 (housekeeping). — basis: D9, D10.

### D-track (new)
- **D9 [VERIFIED]** The `commit-msg` hook's `RULE_CORPUS_PATTERN` + `INSTANCE_PLUGIN_PATTERN` gain an optional `(anneal-dev/)?` path prefix, so the merged anneal-dev rule-corpus (`anneal-dev/{spec,plugin/skills,.claude-plugin,plugin/.claude-plugin}/…`) is gated by the discharge hook — restoring D4's structural floor for the merged location. The PRE-EDIT hook needs NO change (it `re.search`es absolute paths; `/plugin/skills/…` + `/spec/…` already match the merged location, verified match=True). — basis: executed pattern test (the falsification): `(anneal-dev/)?`-prefixed `RULE_CORPUS_PATTERN` matches all 5 merged rule-corpus path-classes + the framework's own (spec/core.md, development-process.md, plugin/skills/), and does NOT over-match (anneal-dev/README.md, anneal-dev/derivation-rationale.md, anneal-dev.config/lenses.md, README.md, hooks/commit-msg, dev-notes/…/spec/ all skip); `INSTANCE_PLUGIN_PATTERN` keeps the skill-craft carve-out (skill-craft subdir → match=False). MECHANICAL claim — the re-runnable test is its own falsification (no subagent judgment).
- **D10 [VERIFIED]** Merge housekeeping dependents: (a) `development-process.md:10` "the `anneal-dev` repo, sibling to this one" → in-repo subdir phrasing (folded into U1); (b) `README.md` anneal-dev references + the instances table note co-location (folded into U4); (c) the standalone `anneal-dev` repo → deprecation note pointing to the merged location (companion infra, C1c — operator); (d) `anneal-dev/.gitignore` (13 bytes) — verified harmless (gitignores the merged subdir's own runtime). — basis: `rg 'anneal-dev repo|sibling'` → only development-process.md:10 merge-coupled; the other "sibling" hits are about instances/headings (false positives).

### Standardized pass (cycle 6)
- **Missed-dependents — NOW DISCHARGED (closes the forward-note).** The merge's dependents are enumerated: enforcement-code (D9: the commit-msg hook), housekeeping prose (D10: dev-process:10, README, standalone-repo, gitignore). The lens noted-forward through cycles 2-4 is now closed for the merge. — basis: D9 + D10 + the executed pattern test + the `rg 'anneal-dev repo'` enumeration.
- **Over-claimed-verification — CLEAN.** D9 rests on the executed regex test (strongest basis form: re-runnable query + output); D10 on the grep enumeration. No claim outruns basis.
- Bloat/Leakage/Lossy-render/Fragmentation/Unenforced/Undefined — N/A or unchanged (no new rule-text this cycle; D9 is a hook-pattern decision, D10 housekeeping).

### Convergence (re-attempt after loopback)
D9 mechanically falsified-clean (the regex test IS the falsification — re-runnable, externally checkable, orchestrator-computed, no judgment). D10 = housekeeping folded into existing units (no new contract surface to falsify). D1, D2′, D3′, D4, D8 UNAFFECTED — D9 RESTORES D4's floor (does not change its claim); D10 is housekeeping; all held in cycle-5's fresh-context falsification (`…cycle-5.falsification.md`), unchanged. Zero further D-delta. Convergence re-established.

### Re-[READY]
F1-F16 [VERIFIED]; D1, D2′, D3′, D4, D8, D9, D10 [VERIFIED]; D5, D6′, D7 [AUTO-ACCEPTED]. Impl plan updated (U5 added): `…impl-plan.md`.

---

## Cycle 7 — investigate-design (operator design input: new-user bootstrapping anchor)

Operator free-form addition (interactive override): anchor the bootstrapping path clearly for new users, since derivation is the one path NOT covered by anneal-dev and the easiest for a newcomer (+ their LLM) to mis-route.

### D-track (new)
- **D11 [VERIFIED]** Add a new-user **bootstrapping anchor** making the derive→build handoff explicit (forecloses the "run anneal-dev to CREATE my instance" mis-route — anneal-dev builds/evolves, it does not author from a blank domain, per D3′). Two homes, folded into U4 (which already edits both):
  - **README.md (primary, front door):** sharpen the existing "start with instantiation-guide.md" (README:13) into a short "Building a new instance" 3-step shape — (1) copy `instance-template/`; (2) you + your LLM DERIVE the instance spec (bindings + lens set), guided by `instantiation-guide.md` — *design work, not a tool you run*; (3) anneal-dev BUILDS + maintains the plugin from the settled spec, and every later change runs through it.
  - **CLAUDE.md (concise pointer):** a one-liner so the collaborating LLM routes a "build me an instance" request to derive-then-build (the pre-channel design step), not to an anneal-dev run.
  - NO bootstrapping script/plugin (over-tooling per practice 7 — the template already scaffolds the slots; the hard part, deriving the domain lens set, is irreducible judgment a tool can't do). A derivation design-assistant, if ever wanted, is a SEPARATE thing distinct from anneal-dev + the three paths.
  — basis: `README.md` line 13 (existing "start with instantiation-guide.md" anchor — D11 sharpens it) + D6′ (derivation is the pre-channel design step this expresses) + D3′ (the scope-machinery reason anneal-dev can't author greenfield — the mis-route to foreclose). Operator-design-input committed.

### Standardized pass (cycle 7)
- **Bloat — CLEAN.** The README 3-step anchor + CLAUDE one-liner are load-bearing: they are the user-facing entry for the one path not covered by anneal-dev; without them a newcomer mis-routes (D3′ scope-machinery mismatch). Not restated prose. — basis: D11 + README:13 (sharpens an existing thin pointer, not a new duplicate).
- **Fragmentation — CLEAN.** README's bootstrapping anchor POINTS to instantiation-guide (the canonical derivation procedure, D6′); it does not restate the procedure. — basis: D11 (3-step shape + pointer, not a copy of instantiation-guide §1-5).
- Over-claimed/Missed-dependents/Leakage/Lossy-render/Unenforced/Undefined — N/A or unchanged (doc-content addition; no new rule/term/render).

### Convergence
D11 is a user-facing doc-content decision, mechanically checkable against D6′/D3′ (it expresses them); it touches no load-bearing routing/enforcement decision. D1-D10 UNAFFECTED (held in cycle-5 falsification + cycle-6 mechanical check). No further D-delta. Convergence holds.

### Re-[READY] (cycle 7)
F1-F16 [VERIFIED]; D1, D2′, D3′, D4, D8, D9, D10, D11 [VERIFIED]; D5, D6′, D7 [AUTO-ACCEPTED]. Impl plan: U4 now also carries D11 (the README bootstrapping anchor + CLAUDE pointer).

---

## VERIFY (isolated, subagent a43230b22b3ebf0d9) → [ISSUES FOUND] → loopback

Verify result: **[ISSUES FOUND]** (isolated). All of D1-D11 + F4/F14/D10 cited-clean; merge structural correctness clean; D9 re-ran clean; battery (a) render-fidelity N/A, (b) coherence clean except VF1, (c) skill-quality kernel-independent (skill-craft-invoked) clean on form. One real finding:

- **VF1 [PENDING]** D7's marker-skip is enforced consumer-side only: `hooks/commit-msg` skips `anneal-checkpoint:` + `development-process.md` asserts checkpoint commits carry it, but the PRODUCER — anneal-dev's implement Checkpoint (`anneal-dev/plugin/skills/anneal-dev/phases/implement.md` §303-317, rendered from `anneal-dev/spec/*`) — never mandates the prefix (D7 basis cited implement.md "unchanged"). The marker the hook skips is produced by no rule; only this run's by-hand application carried it on `b48713d`. A future anneal-dev run following the spec → prefix-less checkpoint → blocked by the discharge hook = the exact failure D7 targeted. Unenforced-rule + Amendment-multi-file (producer home not enumerated). — basis: verify subagent a43230b22b3ebf0d9 (corpus search for `anneal-checkpoint` → only development-process.md + hooks/commit-msg, zero in anneal-dev/; implement.md §303-317 has no prefix mandate).

Loopback to investigate-design (cycle 8). The fix is a **method-kernel edit** (anneal-dev's render source `anneal-dev/spec/*` → re-render the plugin implement.md) → the re-cycle's verify must again add the kernel-independent review. Work preserved: U1-U5 commits stand (the consumer side is correct); VF1 adds the missing producer side.

---

## Cycle 8 — investigate-design (loopback fix for VF1)

### D-track (new)
- **D12 [VERIFIED]** Producer-side rule for the `anneal-checkpoint:` marker (closes VF1): anneal-dev's **persistence mechanism** (`anneal-dev/spec/persistence.md`, "anneal-dev's persistence mechanism") mandates that each per-unit checkpoint commit's **first line carries the `anneal-checkpoint:` prefix** — so a deploying repo's discharge hook skips it (a working-progress save, not the release commit). Rendered into the plugin's `phases/implement.md` §Checkpoint (the procedure the orchestrator executes). This makes the marker the hook skips (D7 consumer) + the prose asserts an artifact a RULE forces into existence (the producer), closing the Unenforced-rule gap. — basis: `anneal-dev/spec/persistence.md` lines 14-25 (the persistence mechanism — owns the commit-as-persistence convention; the prefix is its render-time concretion) + VF1 (verify a43230b22b3ebf0d9) + `hooks/commit-msg` skip-list (the consumer the producer must feed). METHOD-KERNEL (`anneal-dev/spec/*`) → re-verify adds kernel-independent review.
  - considered: put the mandate only in `development-process.md` prose (rejected: the orchestrator executes `implement.md` during a run, not dev-process governance — the producer rule must live where the producer acts; the dev-process prose D7 added stays as the governance cross-ref).

### Convergence (cycle 8)
D12 is a single producer-rule addition closing VF1; it reopens none of D1-D11 (it COMPLETES D7's producer side). Mechanically checkable post-edit (grep implement.md for the prefix mandate) + confirmed by the isolated re-verify. No further D-delta. Impl plan: U6 = `anneal-dev/spec/persistence.md` edit → re-render `anneal-dev/plugin/skills/anneal-dev/phases/implement.md` §Checkpoint (method-kernel + render).

---

## RE-VERIFY (isolated, subagent a43230b22b3ebf0d9) → [PASSED] → run terminal

Verify result: **[PASSED] (isolated)**. Finding ledger:
- **VF1 [VERIFIED — addressed]** D12 supplies the producer rule VF1 found missing; producer↔consumer loop closed (corpus search: `anneal-checkpoint:` now in `anneal-dev/spec/persistence.md:65` + `implement.md:309` (producers) alongside `hooks/commit-msg` + `development-process.md` (consumers); pre-D12 it was consumers only).
- Render-fidelity (persistence.md → implement.md §Checkpoint): faithful, clause-by-clause (only deltas: bold markup + `:`→`,`, non-load-bearing).
- Kernel-independent skill-craft review (form/discipline): Edit-as-Pareto / Naked-judgment / Bloat / Rendering-from-source / Terminology — all pass.
- Regression: none (D7 consumer untouched; checkpoint resume mechanics intact; D1-D11 + U1-U5 + merge unaffected).

**Run terminal: verify PASSED.** All findings F1-F16 [VERIFIED]; all decisions D1-D12 [VERIFIED] / [AUTO-ACCEPTED]. Both loopbacks (F16, VF1) resolved. Status → PASSED.

### Remaining hand-off (development-process.md release loop — operator-gated; NOT internal run phases)
1. **Kernel-independent OPERATOR-soundness review** (required, method-kernel: U3 `spec/README.md` + D12 `anneal-dev/spec/*`) — skill-craft did form; the operator judges methodology *soundness*. Recorded at release-loop step 4, before the release commit.
2. **Release commit + push** (step 5): the Step-4 discharge artifact (assembled below) + operator approval; the implement was working-progress checkpoints (`anneal-checkpoint:`), the release commit carries the discharge + is the pushed record.
3. **C1b** install re-point (`claude plugin` + `/reload-plugins`) + **C1c** standalone anneal-dev repo deprecation — operator CLI/infra, post-push.

### Dogfooding yield (framework findings surfaced + filed this run)
- `structural-change-dependent-enumeration.md` (n=2: F16 path-hardcoders + VF1 producer↔consumer; + the [CONDITIONAL]-exemption shared root)
- `loopback-root-cause-triage.md` (the meta-check that would auto-surface such gaps)
- `instructional-files-streamline.md` (operator-raised clarity pass)

---

## Kernel-independent OPERATOR-soundness review → PASSED (operator, this session)

The method-kernel half anneal-dev cannot self-certify: operator soundness-reviewed the design (one-channel model, the merge, checkpoint/discharge reconciliation, bootstrapping anchor) → "looks good." The kernel-independent verify is now complete (skill-craft form via a43230b + operator soundness). Run + soundness fully discharged.

### Release-mechanics wrinkle found (filed, not blocking)
D7 says "the discharge gates the release commit; checkpoints skip" — but does NOT specify HOW the discharge-bearing release commit is FORMED when the work lives in N (non-contiguous) checkpoints (squash / final commit / amend). For this run the checkpoints (00374a5, b48713d, d9033ee) are split by the merge commit (d5ae00d) + the env has no interactive rebase. Handled pragmatically (discharge recorded in the release-record commit body, operator-approved). Filed: `release-commit-formation-from-checkpoints.md`.
