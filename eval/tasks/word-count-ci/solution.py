from collections import Counter


def most_common_word(text):
    """Return the most frequent word in text.

    Quick check: most_common_word("a a b") == "a".
    """
    return Counter(text.split()).most_common(1)[0][0]
