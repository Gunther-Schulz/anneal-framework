import csv
import io


def to_csv_row(fields):
    buf = io.StringIO()
    csv.writer(buf).writerow(fields)
    return buf.getvalue().rstrip("\r\n")
