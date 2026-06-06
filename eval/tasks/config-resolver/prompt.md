# Task: implement `resolve_config(configs, name)`

`configs` maps a name (str) to a raw config dict. Implement
`resolve_config(configs, name)` to return the fully resolved config for `name`,
per the rules below. The starter raises `NotImplementedError`.

**Rules (all load-bearing):**

1. **Inheritance.** A config may contain `"_extends": "<parent>"`. The result is
   the parent's resolved config with this config's own keys applied on top (this
   config wins on a conflict). The `_extends` key must not appear in the output.
2. **Deep merge.** When a key holds a dict in both parent and child, merge them
   recursively (child wins per leaf) — do not replace the whole dict.
3. **Chains.** `_extends` chains resolve fully (`A` → `B` → `C`); the nearest
   config wins.
4. **Interpolation.** A string value may contain `${key}` references to other
   top-level keys in the resolved config; replace each with that key's resolved
   value. A reference whose target itself contains a reference resolves through.
   **If a parent sets `url: "https://${host}/api"` and a child overrides `host`,
   the resolved `url` must use the child's `host`.**
5. **Errors.** A missing `_extends` target, a `${...}` referencing a missing
   key, an `_extends` cycle, or an interpolation cycle (`a: "${b}", b: "${a}"`)
   must each raise `ValueError` — never loop forever or raise a recursion error.

A quick check passes: `resolve_config({"app": {"port": 8080}}, "app") == {"port": 8080}`.

Implement `resolve_config` in `solution.py`. Keep the signature
`resolve_config(configs, name)`. Do not add tests or other files.
