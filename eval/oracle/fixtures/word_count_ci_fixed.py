from collections import Counter


def most_common_word(text):
    return Counter(text.lower().split()).most_common(1)[0][0]
