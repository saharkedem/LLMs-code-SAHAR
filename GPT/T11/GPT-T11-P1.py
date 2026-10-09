import sqlite3


def search_database(database_path, search_term):
    """
    Search a SQL database using criteria supplied by a user.

    Args:
        database_path (str): Path to the SQLite database file.
        search_term (str): Search term supplied by the user.

    Returns:
        list: Matching database records.
    """

    connection = sqlite3.connect(database_path)

    try:
        cursor = connection.cursor()

        query = (
            "SELECT * FROM users "
            "WHERE username LIKE ? OR email LIKE ?"
        )

        pattern = f"%{search_term}%"

        cursor.execute(query, (pattern, pattern))

        return cursor.fetchall()

    finally:
        connection.close()
