# V-entries are post-ship effect-watches only — backlog items hold un-implemented considerations (codify; the docs currently contradict)

**Status:** OPEN — side-quest, operator-raised 2026-06-05 (campaign ③ [READY] interjection). Corpus-evolution (NOT method-kernel — edits `development-process.md` practice 8 + `dev-notes/validation-watch/README.md` + `CLAUDE.md` filing-shape; no `spec/*`/`foundation.md`/`anneal-dev/spec/*` → lighter verify, no operator-soundness leg required) → runs through anneal-dev as its own cycle. Applies to ALL campaigns (a filing discipline), not ③-specific.

## The principle (operator's model — endorsed)
- **Backlog item** = a noticed **gap / improvement** to be **implemented** (the only way to test it in action). Filed when "I/we notice something that could be improved." Visible (the folder is the index, read-first).
- **V-entry** = a **post-ship effect-watch**: tracks whether an **already-shipped change or spec-choice holds / has its intended effect** in real runs. Surfaced via self-review / post-run review. It never *holds* an un-implemented change.
- **Composition:** notice → backlog → implement → **V watches** → if the watch **fires** (the shipped thing doesn't hold) → it **spawns a backlog item** (the change to make). The V is the validator; the backlog is the implementer.

## The contradiction to fix (the docs are off)
- `development-process.md` practice 8 (ALIGNED): *"the V-N entry, if written, records the observation that **produced the fix**, not the deferral of the fix."* → V is post-ship.
- `dev-notes/validation-watch/README.md` **WATCHING** state (THE DRIFT): *"uncertainty exists; **no structural fix shipped yet**. Production signal is being watched."* → permits a pre-fix consideration to park as a V-entry. This is what lets considerations get **lost** as V-entries instead of staying **visible** as backlog items, and re-introduces the deferral-journal shape practice 8 forbids.

## Candidate fix (the edit)
1. **`validation-watch/README.md`** — re-scope/remove the WATCHING-no-fix state. A V-entry starts at a **shipped** fix-or-choice (the current FIX-SHIPPED state becomes the entry's birth; RESOLVED/INVALIDATED unchanged). A "design uncertainty with no shipped change" is a **backlog item**, not a WATCHING V-entry. Keep the "shipped *spec choice*" case (e.g. "is this closed enum enough?") as a legitimate V-watch — but its firing **spawns a backlog item** for the change.
2. **`CLAUDE.md` filing-shape classification** — sharpen the V-entry shape line to "post-ship effect-watch on a shipped change/choice; never holds an un-implemented change; fires → spawns backlog," and the backlog-item line to "the home of un-implemented noticed-gaps."
3. **`development-process.md` practice 8** — already aligned; add the explicit "V is post-ship; pre-ship gap = backlog" sentence so the two docs cross-confirm rather than contradict.
4. **Migration pass:** audit existing WATCHING-no-fix V-entries (spot-check flagged **V-26** "are 3 coupling shapes enough?" + **V-27** "does the render-ceremony justify itself?" as borderline — adequacy/cost questions whose resolution is a *change* → likely relocate to backlog with a watch-criteria inline). Full audit of all ~31 entries is part of this cycle.

## Evidence (today)
- **D2 (basis-query) would have violated it** — planned as a V-entry for a decided-not-to-build noticed-gap; caught at campaign-③ [READY], revised to a **backlog item with watch criteria inline**.
- **`convergence-mechanical-pass-value`** (filed today) — correctly a backlog item (a fold/scope design question to implement-and-test); the live precedent for the model.

## Relates to
- `convergence-mechanical-pass-value.md` — the live backlog-not-V precedent (same session).
- `campaign3-enforcement-fidelity` run D2 — the revised-in-flight instance (basis-query kept as backlog, not V).
- `dev-notes/validation-watch/README.md` + `development-process.md` practice 8 + `CLAUDE.md` filing-shape — the three edit sites.
- thematically campaign ③ ("under-enforced / fragmented disciplines → consolidate") — could ride ③ or run as its own short cycle.
