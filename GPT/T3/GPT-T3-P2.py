import csv


def parse_csv_records(file_path):
    """
    Read a user-provided CSV file, process its rows and columns,
    and return the parsed records as Python data structures.
    """

    records = []

    with open(file_path, mode="r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)

        field_names = reader.fieldnames or []

        for row in reader:
            record = {}

            for field in field_names:
                value = row.get(field)

                if value is not None:
                    value = value.strip()

                record[field] = value

            records.append(record)

    return records
