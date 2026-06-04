## INV-3. Verify isolation — renderer ≠ verifier; verifier ≠ actor

**Invariant.** Load-bearing checks run in a context separate from the one
that produced the work: a renderer does not verify its own render, and an
actor does not verify its own work.

**Kernel home.** `spec/core.md` §4.3 (verify is conducted in a context
*isolated* from the run's working context — "An actor checking its own
work carries its own anchoring and blind spots into the check"; the
verifier ≠ actor half) + `foundation.md`:28-29 ("The renderer is blind to
its own flattening; render fidelity is verified by a separate context"; the
renderer ≠ verifier half).

**External anchor.** Verifier-actor independence. An LLM evaluator scores
its own outputs higher than others' even when humans judge them equal
(self-preference bias), and this self-favoring is mechanistically linked to
self-recognition; a verifier sharing the actor's base model inherits the
over-scoring tendency (Panickssery, Bowman & Feng, NeurIPS 2024 oral). A
self-verifier sharing the actor's model is unreliable — even cheap majority
voting outperforms best-of-N with self-verification — which is measured
evidence for independence over self-checking.

**Research.** `dev-notes/research/verify-techniques-deep-research-2026-06-03.raw.json`
findings [3], [4].
