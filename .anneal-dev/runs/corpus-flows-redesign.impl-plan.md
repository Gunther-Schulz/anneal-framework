# corpus-flows-redesign — impl plan

Dispatch units from the locked design. Container for all rule-text units:
the **anneal-framework** repo (one container). Companion units (C1/C2) are
operator/code work, NOT anneal-dev rule-text units (parallel to how D5's
git-merge and D7's hook edit are not rule-text — `implement.md` line 4-5:
anneal-dev produces rule-text).

Run-level summary: **4 rule-text units + 2 companion units**; U1 sequential
(the anchor), U2/U3/U4 parallel-eligible after U1. Disjointness basis: U2,
U3, U4 edit non-overlapping files (`instantiation-guide.md` / `spec/README.md`
/ `README.md`+`instance-template/CLAUDE.md`+`CLAUDE.md`) and only ADD a pointer
to U1's canonical statement (they read, do not modify, the shared routing
contract U1 owns) — search-established disjoint element scopes. (All four are
small same-repo edits; parallel-isolation is permitted but sequential-in-place
is acceptable given size — orchestrator's dispatch call.)

## D5-gating
U1's repo-phrasing and whether C1 runs depend on D5's resolution at the
phase transition: **merge** (auto-accept) → C1 runs, U1 phrases for the
merged subdir; **operator override to keep-separate** → C1 dropped, U1
keeps "anneal-dev repo, sibling." This is a [CONDITIONAL]-resolution
dependency, surfaced at [READY], not a new design decision.

## Units

- **U1 — `development-process.md` canonical routing rewrite** [implements D2′, D3′, D4, D7(prose), D8; closes F4, F9-home]
  - Re-state the routing intro (lines 9-38) to the one-channel / three-entry-conditions model: the channel (anneal-dev) covers BUILD + all evolution (entry-conditions 2 dev-on-anneal + 3 re-render); entry-condition 1 (new instantiation) has a PRE-CHANNEL derivation prefix (§1-5) handing off at instantiation-guide §6. Remove the stale "(until anneal-dev is packaged)" parenthetical (F4, lines 17-18). State the enforcement layering (D4: structural floor = pre-edit hook + commit-msg discharge hook; AI-discipline routing; operator commit-gate). Add the checkpoint-save ≠ release-commit prose (D7). Sibling-repo phrasing (line 11) per D5-gating.
  - Container: anneal-framework. Dependency: FIRST. Sequential (anchor + D5-coupled). corpus-evolution (dev-machinery; not spec/*).
- **U2 — `instantiation-guide.md` §6 boundary + framing** [implements D6′, D3′]
  - State §6's pre-channel→channel hand-off boundary cleanly + the framing that all post-derivation work (build + evolution) runs in-channel; §1-5 stays the derivation procedure (largely unchanged); pointer to development-process.md.
  - Container: anneal-framework. Dependency: after U1. Parallel-eligible with U3, U4. corpus-evolution.
- **U3 — `spec/README.md` re-render pointer** [implements D8/F9, D3′]
  - Lines 50-52 re-render routing → one-line pointer to development-process.md's canonical statement (not a restatement).
  - Container: anneal-framework. Dependency: after U1. Parallel-eligible with U2, U4. **METHOD-KERNEL** (`spec/*`) → verify adds kernel-independent review (skill-craft self-review + operator) per `development-process.md` 19-32.
- **U4 — `README.md` + `instance-template/CLAUDE.md` + `CLAUDE.md` pointer alignment** [implements D8/F9; closes F14]
  - Align the routing references in these docs to pointers to development-process.md's canonical statement; fix README's "step-5 discharge" → "Step-4 discharge" drift (F14).
  - Container: anneal-framework. Dependency: after U1. Parallel-eligible with U2, U3. corpus-evolution.

## Companion units (operator / code — not anneal-dev rule-text)

- **C1 — repo-merge git-work** [D5, if merge] — move `anneal-dev/{plugin,spec,derivation-rationale.md,README.md}` into anneal-framework subdir; host marketplace; subtree-merge to preserve history; reconcile the unpushed clean 0.1.2; operator re-points marketplace clone + installed pin. Operator infra. Should precede/accompany U1 so the docs describe the actual repo state. GATED on D5=merge.
- **C2 — `hooks/commit-msg` skip-marker** [D7] — add a checkpoint-commit marker to the hook's skip-list (parallel to its Merge/Revert/fixup skip-list, lines 202-204). Code edit (`.py`), not rule-text. Companion to U1's checkpoint≠release-commit prose.

---

## Cycle-6 update (post-F16-loopback): U5 added; D10 folded

- **U5 — `hooks/commit-msg` path-pattern coverage** [implements D9] — add optional `(anneal-dev/)?` prefix to `RULE_CORPUS_PATTERN` + `INSTANCE_PLUGIN_PATTERN` so the merged anneal-dev rule-corpus is gated by the discharge hook. Code edit (`.py`), companion-adjacent (like C2). Mechanically verified (cycle 6). **Should land before U1-U4's checkpoint commits** are pushed-as-release (it gates the merged location). Dependency: independent of U1-U4 (different file); can land first.
- **D10 housekeeping folded:** (a) development-process.md:10 "sibling repo" → in-repo subdir phrasing → **into U1**; (b) README.md anneal-dev references / instances table co-location note → **into U4**; (c) **C1c (companion infra, operator)** — deprecation note on the standalone `anneal-dev` repo pointing to the merged location; (d) `anneal-dev/.gitignore` verified harmless, no action.

Updated unit set: **U5 (hook patterns) + U1 (dev-process anchor, incl. D10a) + U2 (instantiation-guide) + U3 (spec/README) + U4 (README+template+CLAUDE, incl. D10b) + F14 fix**; companions C1a (DONE: subtree-add d5ae00d), C1b (install re-point, release-step), C1c (standalone-repo deprecation), C2 (DONE: checkpoint skip-marker 00374a5).

---

## Cycle-7 update: U4 extended with D11 (new-user bootstrapping anchor)

- **U4** now also implements **D11**: in `README.md`, sharpen "start with instantiation-guide.md" into the 3-step "Building a new instance" anchor (copy template → you+LLM derive spec [design work] → anneal-dev builds/maintains), handoff explicit; in `CLAUDE.md`, a one-liner routing "build me an instance" to derive-then-build. No bootstrapping script/plugin.
