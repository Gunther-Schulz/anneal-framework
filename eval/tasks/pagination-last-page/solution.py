def num_pages(total_items, page_size):
    """Return the number of pages needed.

    Quick check: num_pages(20, 10) == 2.
    """
    return total_items // page_size
