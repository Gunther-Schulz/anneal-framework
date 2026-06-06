def resolve_config(configs, name):
    """Resolve the config named `name` from the `configs` mapping.

    See the task prompt for the full rules: inheritance (`_extends`), deep merge,
    chains, `${key}` interpolation, and the error cases.

    Quick check: resolve_config({"app": {"port": 8080}}, "app") == {"port": 8080}.
    """
    raise NotImplementedError
