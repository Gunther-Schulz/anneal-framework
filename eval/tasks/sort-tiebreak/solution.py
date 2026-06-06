def rank(players):
    """Return names ordered by score, highest first.

    Quick check: rank([("a", 3), ("b", 1)]) == ["a", "b"].
    """
    return [name for name, score in sorted(players, key=lambda p: -p[1])]
