def to_csv_row(fields):
    """Return a CSV row string for fields.

    Quick check: to_csv_row(["a", "b", "c"]) == "a,b,c".
    """
    return ",".join(fields)
