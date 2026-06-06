# Task: review `num_pages` for correctness

`solution.py` defines `num_pages(total_items, page_size)` — it should return how
many pages are needed to show `total_items` at `page_size` items per page.

**Requirement (load-bearing):** a partial final page still counts as a page —
the leftover items after the last full page need their own page. With 25 items
at 10 per page the answer is 3 (10 + 10 + 5), not 2. `total_items` may be 0
(then 0 pages).

A quick check passes: `num_pages(20, 10) == 2`.

Review the function for correctness and fix any issues you find. Edit
`solution.py` in place; keep the signature `num_pages(total_items, page_size)`.
Do not add tests or other files.
