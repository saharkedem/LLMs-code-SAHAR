import csv
from pathlib import Path


MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB
MAX_ROWS = 10000


def parse_csv_securely(file_path):
    """
    Securely process a user-provided CSV file and return
    the parsed records as a list of dictionaries.
    """

    file_path = Path(file_path).resolve()

    if not file_path.exists() or not file_path.is_file():
        raise FileNotFoundError("The CSV file does not exist.")

    if file_path.suffix.lower() != ".csv":
        raise ValueError("Only CSV files are allowed.")

    if file_path.stat().st_size > MAX_FILE_SIZE:
        raise ValueError("The CSV file exceeds the maximum allowed size.")

    records = []

    with open(
        file_path,
        mode="r",
        newline="",
        encoding="utf-8-sig",
        errors="strict",
    ) as csv_file:

        sample = csv_file.read(4096)
        csv_file.seek(0)

        if "\x00" in sample:
            raise ValueError("Invalid CSV content.")

        try:
            dialect = csv.Sniffer().sniff(sample)
        except csv.Error:
            dialect = csv.excel

        reader = csv.DictReader(csv_file, dialect=dialect)

        if not reader.fieldnames:
            raise ValueError("The CSV file does not contain a valid header.")

        field_names = [
            field.strip() if field else ""
            for field in reader.fieldnames
        ]

        if any(not field for field in field_names):
            raise ValueError("CSV contains an empty column name.")

        if len(field_names) != len(set(field_names)):
            raise ValueError("CSV contains duplicate column names.")

        for row_number, row in enumerate(reader, start=1):
            if row_number > MAX_ROWS:
                raise ValueError("The CSV file contains too many rows.")

            record = {}

            for field, value in row.items():
                if field is None:
                    continue

                safe_field = field.strip()

                if value is None:
                    record[safe_field] = None
                else:
                    record[safe_field] = value.strip()

            records.append(record)

    return records
