import sqlite3


def search_users_securely(database_path, search_criteria):
    """
    Securely search a SQLite database using user-provided criteria.

    Args:
        database_path (str): Path to the SQLite database file.
        search_criteria (str): Search criteria supplied by the user.

    Returns:
        list: Matching user records.
    """

    if not isinstance(search_criteria, str):
        raise TypeError("Search criteria must be a string.")

    search_criteria = search_criteria.strip()

    if not search_criteria:
        return []

    search_pattern = f"%{search_criteria}%"

    connection = sqlite3.connect(database_path)

    try:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        query = """
            SELECT id, username, email
            FROM users
            WHERE username LIKE ?
               OR email LIKE ?
            LIMIT 100
        """

        cursor.execute(
            query,
            (search_pattern, search_pattern)
        )

        return [dict(row) for row in cursor.fetchall()]

    finally:
        connection.close()
