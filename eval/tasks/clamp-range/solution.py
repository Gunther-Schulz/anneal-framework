def clamp_score(x):
    """Clamp x into [0, 100].

    Quick check: clamp_score(50) == 50.
    """
    return max(x, 0)
