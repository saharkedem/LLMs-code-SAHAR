import sqlite3


def search_database_records(database_path, search_criteria):
    """
    Search a SQLite database using criteria supplied by a user
    and return matching records.

    Args:
        database_path (str): Path to the SQLite database file.
        search_criteria (str): Search criteria supplied by the user.

    Returns:
        list: Matching database records.
    """

    connection = sqlite3.connect(database_path)

    try:
        cursor = connection.cursor()

        search_pattern = f"%{search_criteria}%"

        query = """
            SELECT *
            FROM users
            WHERE username LIKE ?
               OR email LIKE ?
        """

        cursor.execute(
            query,
            (search_pattern, search_pattern)
        )

        results = cursor.fetchall()

        return results

    finally:
        connection.close()
