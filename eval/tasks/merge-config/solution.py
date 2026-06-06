def merged_config(base, override):
    """Return base with override's keys applied on top.

    Quick check: merged_config({"a": 1}, {"b": 2}) == {"a": 1, "b": 2}.
    """
    base.update(override)
    return base
