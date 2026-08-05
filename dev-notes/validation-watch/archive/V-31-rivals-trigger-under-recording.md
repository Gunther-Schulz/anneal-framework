## V-31 Rivals-during-formation trigger — under-recording dodge

**Status:** WATCHING — opened 2026-06-05 with campaign ②'s D4.1 (multiple-working-hypotheses,
`spec/core.md` §4.1 Design step: carry rivals co-equally where the investigation pass's
**recorded findings** surface ≥2 viable rival approaches for a load-bearing decision).

**Watch-kind:** correctness-watch (a specific rule's residual — the trigger is dodge-able).

**Catcher:** any run where a load-bearing design decision had genuine rival approaches that the
investigation pass **under-recorded** (≤1 viable rival in the findings) so D4.1's ≥2-rivals
trigger did not fire and the de-bias (carry-rivals-during-formation) was silently skipped —
surfaced when a later cycle's intent-falsification pass, verify, or the operator catches a
single-hypothesis-attachment defect the rivals-carrying would have pre-empted.

**Why a watch, not a forcing function (operator-decided 2026-06-05, "ship"):** the trigger
cannot be mechanically hardened without inviting **fabricated** rivals (forbidden — degrades the
ledger, `modules.md` §3.1) or remaining dodge-able anyway. It is the **same residual class + same
backstop** (fresh-context re-attack, `core.md` §4.1.4:547) the kernel already accepts for the
intent-falsification dodge-down vector — so a forcing function would be speculative ceremony.
Recurrence is the signal to revisit. (F-R5a, run `campaign2-completeness-rigor`.)

**Closing rule:** opportunity-exercised — closes when a run with a genuine ≥2-rival decision
exercises D4.1 correctly (trigger fired, rivals carried, recorded in `considered`) AND no
under-recording dodge is observed across the watch window; INVALIDATED if the dodge IS observed
(→ the forcing-function question reopens). Pure non-occurrence never closes.

**Relates to:** `multiple-working-hypotheses-investigate-design` (archived — shipped as D4.1) ·
`intent-falsification-soundness-sweep` (the dodge-down failure class) · V-30
(form-not-binding-class-recurrence, the broader class).
