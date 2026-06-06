def ensure_prefix(path):
    """Return path prefixed with /api/.

    Quick check: ensure_prefix("users") == "/api/users".
    """
    return "/api/" + path
