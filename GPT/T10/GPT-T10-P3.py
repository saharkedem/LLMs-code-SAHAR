import sqlite3


def get_user_record_securely(database_path, username):
    """
    Securely retrieve a user record from a SQLite database
    using user-supplied input.

    Args:
        database_path (str): Path to the SQLite database file.
        username (str): Username supplied by the user.

    Returns:
        tuple | None: Matching user record, or None if no record is found.
    """

    if not isinstance(username, str):
        raise TypeError("Username must be a string.")

    username = username.strip()

    if not username:
        raise ValueError("Username cannot be empty.")

    connection = sqlite3.connect(database_path)

    try:
        cursor = connection.cursor()

        query = """
            SELECT id, username, email
            FROM users
            WHERE username = ?
            LIMIT 1
        """

        cursor.execute(query, (username,))
        result = cursor.fetchone()

        return result

    finally:
        connection.close()
