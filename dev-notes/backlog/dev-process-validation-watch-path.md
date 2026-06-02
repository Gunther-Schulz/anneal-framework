# development-process.md — stale `spec/validation-watch.md` cross-ref

**Status:** OPEN — surfaced 2026-06-02 during Cycle c-safe's step-4 (the V-26
write put the live path in focus; confirmed by grep). **Trivial, not pressing.**

`development-process.md:453` (practice 12) cites `spec/validation-watch.md` for
V-21, but the file lives at **`dev-notes/validation-watch.md`** (line 55 of the
same file uses the correct path; the `spec/` copy does not exist). Corpus-wide
grep: **exactly one site** (this line) — not a sweep.

**Fix:** one-token path correction (`spec/` → `dev-notes/`) at line 453.
`development-process.md` is rule-corpus, so this is its own micro-cycle
(skill-craft gate + discharge artifact) — or fold into the next
`development-process.md` edit rather than spend a standalone cycle on one token.

Relates to [[contract1-depollution-cluster]] (surfaced during its Cycle c-safe).
