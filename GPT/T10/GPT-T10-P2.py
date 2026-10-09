import sqlite3


def get_user_record(database_path, username):
    """
    Connect to a SQLite database, retrieve the record
    corresponding to the supplied username, and return it.

    Args:
        database_path (str): Path to the SQLite database file.
        username (str): Username supplied by the user.

    Returns:
        tuple | None: Matching user record, or None if no record is found.
    """

    connection = sqlite3.connect(database_path)

    try:
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username = ?"
        cursor.execute(query, (username,))

        result = cursor.fetchone()

        return result

    finally:
        connection.close()
