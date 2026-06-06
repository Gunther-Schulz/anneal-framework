"""Reference correct solution for the design-surface task `config-resolver`.

The design crux (the thing a coherent design surfaces up front): two phases.
  Phase 1 — resolve inheritance FULLY into a merged dict (with deep merge,
            chains, and _extends-cycle detection).
  Phase 2 — interpolate ${key} against that FINAL merged dict (with
            interpolation-cycle detection).
Doing interpolation eagerly during the merge breaks C5 (a child override must
change what a parent's ${...} resolves to). Skipping the cycle sets breaks
C7/C8.
"""
import re

_REF = re.compile(r"\$\{([^}]+)\}")


def _deep_merge(base, over):
    result = dict(base)
    for k, v in over.items():
        if k in result and isinstance(result[k], dict) and isinstance(v, dict):
            result[k] = _deep_merge(result[k], v)
        else:
            result[k] = v
    return result


def _resolve_extends(configs, name, seen):
    if name not in configs:
        raise ValueError(f"missing config: {name!r}")
    if name in seen:
        raise ValueError(f"_extends cycle at {name!r}")
    cfg = configs[name]
    parent = cfg.get("_extends")
    base = _resolve_extends(configs, parent, seen + (name,)) if parent is not None else {}
    own = {k: v for k, v in cfg.items() if k != "_extends"}
    return _deep_merge(base, own)


def _resolve_key(root, key, stack):
    if key not in root:
        raise ValueError(f"missing interpolation key: {key!r}")
    if key in stack:
        raise ValueError(f"interpolation cycle at {key!r}")
    val = root[key]
    if isinstance(val, str):
        return _interpolate_str(val, root, stack + (key,))
    return val


def _interpolate_str(s, root, stack):
    m = _REF.fullmatch(s)
    if m:  # whole string is a single ref — preserve the resolved value's type
        return _resolve_key(root, m.group(1), stack)
    return _REF.sub(lambda mo: str(_resolve_key(root, mo.group(1), stack)), s)


def _interpolate_node(node, root):
    if isinstance(node, dict):
        return {k: _interpolate_node(v, root) for k, v in node.items()}
    if isinstance(node, list):
        return [_interpolate_node(v, root) for v in node]
    if isinstance(node, str):
        return _interpolate_str(node, root, ())
    return node


def resolve_config(configs, name):
    merged = _resolve_extends(configs, name, ())   # phase 1
    return _interpolate_node(merged, merged)        # phase 2
