import csv


def read_csv_records(file_path):
    """
    Read a CSV file and return its records as a list of dictionaries.
    """

    records = []

    with open(file_path, mode="r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            records.append(dict(row))

    return records
