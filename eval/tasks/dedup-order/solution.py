def dedupe(items):
    """Remove duplicate values from items.

    Quick check: set(dedupe([1, 2, 2, 3])) == {1, 2, 3}.
    """
    return list(set(items))
