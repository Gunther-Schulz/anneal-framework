## V-18. 5-part design-decision body shape — trivial decisions over-structured?

**Status: WATCHING.**

**Decision (`core.md` §5.2, commit e12eec5).** Design decision
body specifies (a) target, (b) shape, (c) acceptance criteria,
(d) side effects/failure modes, (e) basis. Adopted to prevent
code-block pollution in design decisions (Unit-11 tracker showed
D2/D8/D11 with full Python/SQL bodies).

**Why uncertain.** The 5-part structure is sized for complex
decisions (Unit-11 D2 four-reducer signature; D5 calibration repo
contract; D8 validator spec). For trivial decisions — deferrals
("defer X to Unit Y because Z"), single-line acknowledgments,
version-pin assertions — the 5 named slots read heavy; risk of
checklist-driven slot-filling rather than thinking-driven
body-shaping.

Two mitigation paths considered but rejected:

- Trivial-decisions exception ("5 slots when non-trivial; basis
  alone for trivial") → introduces Naked-judgment qualifier
  ("trivial") — the anti-pattern this corpus has been sharpening
  against
- "Content not format" clarification → defensible but
  Additive-reflex default ("do nothing on ambiguous rule-need")
  and the rule's "specifies" wording is already loose

Cross-session reasoning (2026-05-27): "the 5-part shape is more
often a help than a hindrance, so the net is positive even with
the over-structuring tax."

**Production signal to watch.** Future tracker runs — do trivial
decisions naturally compress to one sentence (all 5 slots present
implicitly), or do they get boilerplate-filled (5 sequential
paragraphs even when content is trivial)?

- Compression flag: one run shows trivial decisions in
  one-sentence form with all 5 slots present implicitly → R2
  working as designed → RESOLVED.
- Boilerplate flag: one run shows trivial decisions with 5
  sequential mostly-empty paragraphs → R2 needs sharpening →
  candidate fix is the "content not format" clarification, OR a
  trivial-decision exception with mechanical criterion (not
  naked-judgment "trivial").

Per `development-process.md` practice 8, this V-N is legitimate
(Y not classifiable upfront — fix form depends on whether
boilerplate or compression dominates), not deferral-journal.

