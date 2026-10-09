import sqlite3


def create_or_update_record(database_path, user_data):
    """
    Create a new user record or update an existing one.

    Args:
        database_path (str): Path to the SQLite database file.
        user_data (dict): User-supplied data containing:
                          id (optional), username, and email.

    Returns:
        int: The ID of the created or updated record.
    """

    connection = sqlite3.connect(database_path)

    try:
        cursor = connection.cursor()

        user_id = user_data.get("id")
        username = user_data.get("username")
        email = user_data.get("email")

        if user_id is None:
            cursor.execute(
                """
                INSERT INTO users (username, email)
                VALUES (?, ?)
                """,
                (username, email)
            )

            connection.commit()
            return cursor.lastrowid

        cursor.execute(
            """
            UPDATE users
            SET username = ?, email = ?
            WHERE id = ?
            """,
            (username, email, user_id)
        )

        connection.commit()
        return user_id

    finally:
        connection.close()
