# Validation-watch as a folder of single-entry files + archive/ (like the backlog)

**✅ SHIPPED + CLOSED 2026-06-04** — anneal-dev run `kernel-consolidation-batch`, release `e6abcc8`/`d008afe` on `main`. `dev-notes/validation-watch.md` is now `dev-notes/validation-watch/` (README = preamble + the relocated vocabulary home + archival convention; one file per watch-entry; `archive/V-5`). All kernel references repointed (validation-watch [PASSED] verify; byte-for-byte round-trip verified). Archived per convention.

**Status:** OPEN — framework hygiene, operator-raised + **design-set 2026-06-04**: "v-entries should be
just like backlog items: single files with an archive folder. much better than one huge file." **Not
urgent** (see data) but real. **Corpus-evolution → runs through anneal-dev** (spec-only; instance-render
citations deferred to the batch) — splitting the file changes every reference to it as a file, and
those references live in the kernel (`post-run-review.md` Q7, `development-process.md`, `glossary.md`)
+ the clippy/daneel rendered rules. (Supersedes the earlier "one big file + stub + single archive file"
half-measure — the folder model retires entries the way the backlog does.) **QUEUED — tier-2 F3,
batched with `kernel-consolidation-glossary-hygiene`** (operator: "batch", 2026-06-04). Both touch
`glossary.md` + kernel structure; one anneal-dev run amortizes the ceremony (the V-27 cost concern) —
not run standalone now. Low urgency (the file's length is mostly legitimate active watches, not cruft).

## The gap
`dev-notes/validation-watch.md` has **logical** retirement but no **physical** retirement:
- **Logical (exists):** the `RESOLVED` status. A `FIX-SHIPPED` entry → `RESOLVED` on the first
  load-bearing instance; once `RESOLVED` it is dormant and Q7 (`post-run-review.md`) skips it.
- **Physical (missing):** `RESOLVED`/`INVALIDATED` entries stay **inline forever**. No `archive/`
  equivalent (the backlog has one — `backlog/archive/`). The file only grows.

## Why it's not urgent yet (but is real)
Status distribution 2026-06-04: **23 WATCHING + 4 FIX-SHIPPED + 1 RESOLVED** (28 entries, 1552 lines).
So ~27 of 28 are *genuinely active* — the current length is real watching, not un-retired cruft; only
1 entry is archival-eligible today. The length is **mostly legitimate**, so this is future-proofing,
not a cleanup backlog.

**Where it bites regardless:** Q7 loads + walks the **whole** file on **every** post-run-review, on
**every** instance (clippy/daneel/anneal-dev — each renders its own `post-run-review.md` Q7 pointing at
the one shared file). So file length is a recurring **context + walk tax** paid on every review across
every instance, scaling with the file — independent of how many entries are still live. Archival caps
that tax at the active set.

## Hard constraint — V-N numbers are stable spec-cited references
`V-5`, `V-9`, `V-21` are cited **by number** inside `development-process.md` (V-21 cadence),
`spec/glossary.md`, and clippy/daneel rendered rules (V-5/V-9 in their `investigate-design.md` +
`SKILL.md`). The number is a permanent reference — **cannot renumber or delete it**, only relocate the
body. (basis: `grep -rhoE 'V-[0-9]+' spec/ development-process.md ../coding-clippy/plugin ../daneel/plugin`
→ V-5, V-9, V-21.)

## Design — folder of single-entry files + archive/ (the backlog model)
Restructure `dev-notes/validation-watch.md` (one ~1550-line file) into `dev-notes/validation-watch/`:
- **One file per entry**, named for identity like the backlog (e.g. `V-5-ready-self-assessment.md`).
  The **V-N number is the stable key** (spec-cited — see Hard constraint); the slug is for humans.
- **`README.md`** in the folder = the current preamble (purpose, n=1 convention, Entry lifecycle).
  `ls` is the index (active set at a glance), exactly like `backlog/`.
- **`archive/`** subfolder — a RESOLVED (or superseded INVALIDATED) entry's file is `git mv`d here.
  No stub needed in the live folder: the **number lives in the filename**, and citations resolve to
  "the V-N entry in `dev-notes/validation-watch/` (or its `archive/`)" — the folder is the referent,
  not a line in a monolith. (This is cleaner than the superseded stub approach — the filename IS the
  durable handle; reopening on recurrence is `git mv` back, like un-archiving a backlog item.)
- **Migration:** split the 28 current entries into files; `V-5` (the one RESOLVED) lands in `archive/`.

**The reference updates this forces (the corpus-evolution part):** every "in `validation-watch.md`"
becomes "in `validation-watch/`":
- `post-run-review.md` Q7 — "For each V-N in `dev-notes/validation-watch.md`" → "for each entry file in
  `dev-notes/validation-watch/` (+ `archive/` only on a recurrence re-walk)". The Q7 *logic* (per-state
  classify) is unchanged.
- `development-process.md` — the ~5 path references.
- `spec/glossary.md` — "validation-watch.md preamble" → "validation-watch/ README".
- **clippy/daneel rendered rules** — the V-5/V-9 citations + their post-run-review Q7. **DEFERRED** to
  the batch re-render (render-cadence policy) — a transient spec↔instance path mismatch, tracked.

Secondary length driver (note, out of scope): per-entry **verbosity** (~40-50 ln each). Per-file form
makes over-long entries individually visible — a softer follow-on, not this change.

## Level — corpus-evolution, runs through anneal-dev
NOT a dev-notes-only edit: it changes kernel files (`post-run-review.md`, `development-process.md`,
`spec/glossary.md`) that render to instances. So per the repo discipline it is an **anneal-dev cycle**,
**spec-only** (the dev-notes restructure + the 3 kernel reference-updates land now; the clippy/daneel
citation re-points defer to the batch re-render — queued in `instance-reinstantiation`). The Q7/lifecycle
*rules* don't change — only where entries live and the paths that point at them — so it should be a light
cycle, but it carries the method-kernel kernel-independent review (touches `glossary.md`).

## Relates to
- `backlog/README.md` Convention — the `archive/` model this borrows.
- `development-process.md` validation-watch governance + practice 8 (when a V-N is legitimate).
- `spec/glossary.md` (Validation-watch lifecycle definition) + `post-run-review.md` Q7 (the consumer).
- `kernel-consolidation-glossary-hygiene` — sibling corpus-hygiene cluster, but distinct (that is
  glossary/triage homes; this is validation-watch file growth).
