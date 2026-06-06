def rank(players):
    return [name for name, score in sorted(players, key=lambda p: (-p[1], p[0]))]
