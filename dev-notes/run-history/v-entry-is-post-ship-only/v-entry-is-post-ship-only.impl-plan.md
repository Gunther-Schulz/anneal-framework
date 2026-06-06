# Impl plan — v-entry-is-post-ship-only (revised post-D4-drop, 2026-06-06)

3 units, scope-disjoint (distinct files) → parallel-eligible (disjointness basis: distinct file
paths, no shared file). Small + locked → implemented in the working context (self-hosting: the
repo-level integrity clean-precondition is N/A because in-tree backlog captures predate this run;
path-level attribution used — `self-hosting-inplace-integrity-clean-precondition`). D4 dropped (F17).

- **U1 — D2** · `dev-notes/validation-watch/README.md` · first (no deps). (i) preamble: add the
  canonical post-ship/backlog exclusion; (ii) WATCHING def (`:42-45`): re-word to anchor
  "already-shipped decision" (resolves the F1 pre-ship contradiction); (iii) Vocab state-line
  (`:127-134`): → pointer to the Entry-lifecycle canonical def (resolves the `:42`/`:128` drift).
- **U2 — D3** · `CLAUDE.md` filing-shape · parallel with U1/U3. Sharpen the V-entry line:
  post-ship effect-watch on a shipped fix/choice; never an un-implemented change; fires → spawns
  backlog. **Shown to operator before commit** (operator-instructions file).
- **U3 — D6** · new `dev-notes/backlog/validation-watch-entry-conformance-sweep.md` · parallel.
  The per-entry conformance audit (folds F9 closing-rule-vs-table + F13 accepted-residual
  discriminator).

Post-implement check (D2 acceptance / F12): `grep -nE "no (structural )?fix shipped yet"
dev-notes/validation-watch/README.md` must be EMPTY (both `:42` def + Vocab `:128` rewritten).
Verify (isolated subagent): skill-craft form review + cross-doc coherence (README ↔ practice 8 ↔
CLAUDE.md, no contradiction; the 28 V-entry labels unaffected).
