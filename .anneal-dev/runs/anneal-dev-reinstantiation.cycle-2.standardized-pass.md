# Standardized-pass artifact — anneal-dev-reinstantiation, cycle 2

Cycle 2 touched only the reinstall-mechanism design (D8 amendment) + F10/F11
investigation; no plugin rule-text rendered yet. In-scope lenses:

- **Over-claimed-verification** [in scope] — CLEAN: F10's [VERIFIED — non-issue]
  rests on three cited config files (known_marketplaces / installed_plugins /
  marketplace.json), each a located read with an observable fact (github source;
  version+sha; `./anneal-dev/plugin` source); F11 on a located read of
  verify.md:32-57. Neither over-claims. basis: F10/F11 basis fields (this cycle).
- **Missed-dependents** [in scope] — CLEAN: D8's amendment enumerates the full
  activation chain (commit → push → plugin-update-to-0.1.3); no activation step
  omitted now that the github-coupling is named. basis: F10 chain + D8
  [CONDITIONAL] body.
- **Bloat / Fragmentation / Leakage / Unenforced-rule / Undefined-shorthand /
  Lossy-render** [out of scope this cycle] — cited reason: cycle 2 rendered no
  plugin rule-text (design-only: reinstall mechanism); these fire on
  added/amended rule-text, none this cycle. They were in scope cycle 1 (render
  design) and re-fire at impl on realized text. basis: cycle-2 change-set =
  D8 amendment + F10/F11 (no plugin file touched).
