# foundation-invariants-register — cycle 2 standardized pass

- **Fragmentation:** RESOLVED (F3) — the exclusion/loopback/falsification overlap
  resolves to distinct entries by distinct anchor: loopback/not-settled (Platt
  recycle + Quine-Duhem) vs exclusion-via-named-falsifier (Platt exclusion + Gunter).
  Each register entry is keyed to one external anchor grounding one invariant; no
  two entries point at the same {invariant, anchor} pair.
- **Bloat:** clean — D2's 5 entries each carry a distinct load-bearing function (a
  distinct kernel invariant + its distinct external anchor); the membership rule
  (anchor-gated, anneal-only-anchorable EXCLUDED) is the standing anti-bloat gate.
  D3's §2 edit adds one leg (the foundation-invariant check) — load-bearing (it is
  what focuses the soundness pass).
- **Leakage:** clean + reinforced (F4) — D6 places the new terms in the register
  README (dev-notes companion), NOT the rendered spec/glossary.md; this is the
  leakage-avoiding choice (a dev-process-specific concept kept out of the
  domain-general rendered spec). D3's §2 edit carries no domain concretion.
- **Missed-dependents:** clean — D3 touches the verify discipline at its 3 located
  homes (§2 lines 25-36, step-4 template lines 567-579) + CLAUDE.md restatement
  (D1 dependent); D3b/D4 touch hooks/commit-msg. No paraphrased restatement of the
  discipline outside D1's enumerated set (F1 search).
- **Unenforced-rule:** clean — D3's foundation-invariant check is enforced by D3b
  (commit-msg requires the discharge line on kernel-source commits, same shape as
  the 7 existing REQUIRED_CHECKS); D4's protection is enforced by the git-observable
  Invariant-change-ratified marker on M/D of invariant files. Neither is
  prose-suggestion-only.
- **Undefined-shorthand:** RESOLVED (F4/D6) — "foundation invariant",
  "foundation-invariants register", "anchor-gated", "Invariant-change-ratified
  marker" gain definitions in the register README (the companion's own definitional
  home, per the validation-watch precedent).
- **Over-claimed-verification:** clean — cycle-2 [VERIFIED] tags (F3,F4,F6,D2,D3,D3b,D6)
  each cite a located read or a re-runnable search introduced this run; the anchor
  citations name external works (Zave-Jackson, Gunter ICRE2000, Platt, Quine-Duhem,
  SGV) traced to their sources in dev-notes/research/. No completeness claim rests
  on recall.
- **Lossy-render:** N/A — no plugin render/paraphrase committed (spec-only cadence).
