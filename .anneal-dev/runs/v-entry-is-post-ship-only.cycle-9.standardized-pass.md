# Cycle 9 — standardized inspection pass

Run: `v-entry-is-post-ship-only` · cycle 9 (D2 reverted to minimal). Scope: edits to
`dev-notes/validation-watch/README.md`. The minimal delta is strictly LESS surface than
cycle-7's (no discriminator clause, no 3-way enumeration) — the cycle-7 pass was already
clean; removing prose only shrinks the attack surface.

- **Bloat** — clean, improved. Net-new prose vs the live README = the WATCHING re-word
  (post-ship anchor) + one exclusion sentence. Both R1/R2-load-bearing. The cycle-7
  discriminator + 3-way enumeration are REMOVED (F14/F15) — a net reduction. basis: D2-minimal (b).
- **Fragmentation** — clean. The exclusion echoes practice-8 Entry-hygiene (`:310-315`) with
  a cross-reference, not a restatement; Vocab→pointer keeps one canonical state def. basis:
  practice 8 `:310-315` + D2-minimal (b).
- **Unenforced-rule** — clean (filing-shape judgment, backstopped by self-review/operator/Q7).
- **Undefined-shorthand** — clean. No coined term; "already-shipped decision" descriptive.
  The cycle-7 "accepted residual" elaboration (a near-term) is gone. basis: D2-minimal (b).
- **Missed-dependents** — clean. State refs by name (transitions/RESOLVED/INVALIDATED) →
  unbroken; Vocab→pointer; Q7 no-edit (F5); 28 labels preserved; D3/D4 consistent. basis: D0 + F5.
- **Leakage / Lossy-render / Over-claimed** — N/A.
