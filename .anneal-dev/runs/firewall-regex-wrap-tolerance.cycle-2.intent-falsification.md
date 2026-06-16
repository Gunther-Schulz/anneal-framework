# firewall-regex-wrap-tolerance — cycle 2 (convergence) intent-falsification pass — CLEAN

Fresh-context subagent (opus), criteria-first; re-ran all tests independently + measured the live corpus.
Subagent agent-id: ac6681d6cf22fd36a. **Result: CLEAN** — all 3 R# served, no `mechanical-falsification-candidate`,
no D-track delta. 4 findings all terminal [VERIFIED — surfaced] / IRREDUCIBLE (empirically non-firing vs the live corpus).

## Per-R# attack lines (all served)
- {R1, serves D1, refutation: NEW vs OLD over wrap fixtures + 4 edge cases (deep 10-space indent, no-backtick
  `core.md\n§`, no-space cross-wrap, clippy-finding-B shape) → NEW catches all (1), OLD misses wrap (0); measured
  deepest real corpus continuation indent = 6 spaces (worst real gap = backtick+newline+6 = 8 < 12). outcome: **served**}
- {R2, serves D1, refutation: FP candidate `core.md). §...` → NEW=1 BUT `grep '§[[:space:]]'` (standalone-symbol §)
  → ZERO in live corpus (every real § is `§<digit>`); OLD also matches the same same-line construct → NEW introduces
  no new FP class; word-break `core.md — and note: §` → NEW=0 (alnum breaks gap). outcome: **served**}
- {R3, serves D1, refutation: `rg -Uc` (multiline) vs `tr '\n' ' ' | rg -c` (flatten-then-match) on the same wrap
  fixture BOTH → 1, proving `-U`+`[^A-Za-z0-9]` ≡ the glossary idiom's realization (b) newline-flattening
  (`glossary.md:84-87`). outcome: **served**}

## Per-finding lines (all terminal, all IRREDUCIBLE)
- {finding: `{0,12}` miss-edge at gap≥13 (11+-space indent), criterion: R1, refutation: 13-char-gap fixture → NEW=0
  BUT measured deepest real §-continuation = 5 spaces / deepest any = 6 → worst real gap 8 < 12 with headroom,
  route: [VERIFIED — surfaced], IRREDUCIBLE — no live-corpus instance; markdown reflows at word boundaries}
- {finding: `core.md). §<word>` synthetic prose FP, criterion: R2, refutation: zero standalone-symbol § in corpus;
  OLD matches it too (parity); tightening to `§[0-9]` would narrow the catch surface for zero live benefit,
  route: [VERIFIED — surfaced], IRREDUCIBLE — construct doesn't occur; NEW is parity-or-better vs OLD}
- {finding: filename-split (`mod\nules.md §`) escapes both old+new, criterion: R1, refutation: no mid-token filename
  wrap exists (single tokens reflow whole); route: [VERIFIED — surfaced], IRREDUCIBLE — inherent single-token-assumption
  limit the glossary idiom names legal (realization (a), glossary.md:85)}
- {finding: D2 queues render-debt vs fixing instances now, criterion: intent/completeness, refutation: regex-string
  home search → exactly 1 corpus home (instantiation-guide.md, D1 fixes it) + the backlog task-file; glossary carries
  only the idiom prose, not the regex; clippy/daneel are separate sibling repos (build artifacts), route:
  [VERIFIED — surfaced], IRREDUCIBLE — in-repo source fully fixed; render-debt is the structurally correct route}

## Convergence status
**CLEAN** — intent served all R#, no D-delta. Proceed to mechanical falsification pass.
