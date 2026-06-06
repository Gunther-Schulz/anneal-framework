# Task: review `most_common_word` for correctness

`solution.py` defines `most_common_word(text)` — it should return the most
frequently occurring word in `text` (words are whitespace-separated).

**Requirement (load-bearing):** word counting is **case-insensitive** — `"The"`,
`"the"`, and `"THE"` are the same word and their counts combine. The returned
word must be lowercase.

A quick check passes: `most_common_word("a a b") == "a"`.

Review the function for correctness and fix any issues you find. Edit
`solution.py` in place; keep the signature `most_common_word(text)`. Do not add
tests or other files.
