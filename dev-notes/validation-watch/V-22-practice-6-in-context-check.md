## V-22. Practice-6 in-context check — corpus-appeal vulnerability under recursive N/A

**Status: WATCHING.**

**Decision (`development-process.md` release loop step 4, "in-
context check artifact (practice-6 specific)"; commit
`e4190ef` + subsequent sharpening).** The practice-6 in-context
check artifact requires (a) section-heading hierarchy
before/after the edit, and (b) first sentence of (containing +
immediate-preceding + immediate-following sibling) sections.
Both anchors are mechanically observable from the document
state. Prose self-attestation alone is insufficient — explicit
in dev-process.md release loop step 4.

**Why uncertain.** Cycle D.1 audit F10 flagged a residual
structural-precarity: the mechanical artifact requirement
itself rests on the AI applying the check correctly per
discharge. A recursive failure shape — AI rationalizes N/A on
practice-6 specifically ("the edit is too small to need
hierarchy citation", "the neighborhood sentences are obvious")
— would skip the artifact without producing any observable
gap until downstream re-organization breaks the unchecked
neighborhood. The N/A discipline (anti-patterns.md
Skip-rationalization, dev-process.md "doubt-voicing IS
evidence") is the counter-mechanism, but its effectiveness
against the recursive case is empirically unmeasured.

**Production signal to watch.** A commit where (a) practice-6
in-context check was marked PASS / N/A with thin artifact
(missing or weak neighborhood-sentence citation), AND (b) the
section's argument flow was subsequently observed broken by
downstream re-organization OR an operator-side catch.
Observable: the discharge artifact's neighborhood-sentence
citation lines vs. the actual subsequent section state.

Closing criterion (WATCHING → FIX-SHIPPED): observed n=1
instance of the production signal; sharpen the in-context
check artifact further OR escalate to mandatory subagent
dispatch on practice-6 (Tier-1 mechanical instead of Tier-2
structural). FIX-SHIPPED → RESOLVED on first subsequent edit
where the strengthened check catches what the prior shape
would have missed.

Per `development-process.md` practice 8, this V-N is
legitimate: the fix-shape (mechanical artifact requirement) IS
shipped; the open question is whether the recursive
self-application case requires further structural enforcement
(operator-detectable empirically, not classifiable in
advance).

---

