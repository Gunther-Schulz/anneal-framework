def ensure_prefix(path):
    return path if path.startswith("/api/") else "/api/" + path
