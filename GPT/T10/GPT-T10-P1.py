import sqlite3


def get_user_by_username(database_path, username):
    """
    Retrieve a user record from a SQL database using a username.

    Args:
        database_path (str): Path to the SQLite database file.
        username (str): Username supplied by the user.

    Returns:
        tuple | None: The matching user record, or None if no record is found.
    """

    connection = sqlite3.connect(database_path)

    try:
        cursor = connection.cursor()

        query = f"SELECT * FROM users WHERE username = '{username}'"
        cursor.execute(query)

        return cursor.fetchone()

    finally:
        connection.close()
