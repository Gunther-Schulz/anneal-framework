## V-13. Minimal verbatim content scope — sufficient or polluting?

**Status: FIX-SHIPPED (2026-05-27, commit [pending]).** Basis form
revised — verbatim content dropped entirely. Basis is now (a) a
re-runnable executable query OR (b) a file:line range citation
paired with one observable fact (count, identifier, type,
structural shape). Un-fakeability shifts to verifier-side: verify
(`core.md` §4.3) and convergence cycles (`core.md` §4.1.4) re-open
citations to check both location AND observable fact. The
"minimal" naked qualifier — flagged as Naked-judgment per
skill-craft `anti-patterns.md` — is gone; the operational form
(citation + one fact) replaces it. Trackers no longer contain
code-shaped content as basis.

**Production signal that triggered the fix.** Unit-11
dynamic-bet-sizing tracker (beat-the-books, 2026-05-26):
8.6% of tracker lines exceed 500 chars; basis records quote 5-15+
lines of Python/SQL per claim; tracker bulk dominated by code-
quote rather than analysis. Pollution flag tripped clearly.

**Closing criterion (FIX-SHIPPED → RESOLVED).** A post-run review
identifies a run where the new basis form was load-bearing —
either grounded a claim cleanly without producing code-quote
pollution, OR verify/convergence caught a fabricated citation
under the new form. One observed instance is sufficient.

**Original observation preserved below for audit trail.**

---

**Decision (`core.md` §3.2).** The basis form for a located read
was *"minimal verbatim content from the cited range that grounds
the claim"* — the load-bearing excerpt, not the entire range.
Adopted to avoid tracker pollution from full-range citations
(e.g., 59-line class bodies pasted as basis records).

**Why uncertain.** The "minimal" qualifier introduces bounded
judgment: the AI selects which lines from the cited range
ground the claim. The selection is artifact-checkable (does
the cited verbatim match source at the cited location, and
does it ground the stated claim?), but the selection moment
is naked-judgment. Three possible failure shapes:

- *Under-grounding*: AI cites too little; the excerpt doesn't
  actually contain enough text to verify the claim. Operator
  catch or downstream verify catch.
- *Pollution*: AI cites too much; basis bloats with surrounding
  context that doesn't ground the specific claim. Tracker
  becomes dominated by code bulk rather than analysis.
- *Right-sized*: AI cites the load-bearing excerpt at the
  intended scope. The target case.

**Production signal to watch.** Tracker review after runs:
- Pollution flag: any single point claim's basis exceeds ~5
  lines of verbatim, OR the tracker becomes dominated by
  code-quote bulk
- Under-grounding flag: any finding whose basis doesn't contain
  enough verbatim text to verify the stated claim

**Closing criterion (WATCHING → RESOLVED).** Three consecutive
runs produce tracker-clean, sufficiently-grounded basis records
with no under-grounding catches and no pollution flags. The
minimal-text qualifier is empirically sufficient.

**Alternative closure (WATCHING → SHARPENED).** A run shows
either consistent under-grounding (operator catches insufficient
basis repeatedly) or consistent pollution (tracker becomes
unwieldy with verbatim bulk). Sharpen §3.2 — either toward
fuller citation (accept pollution as the price of safety) or
toward a more mechanical scope criterion (e.g., "cite N lines
max around the load-bearing point").

---

