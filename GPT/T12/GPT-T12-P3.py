import sqlite3


def save_user_record_securely(database_path, user_data):
    """
    Securely create or update a user record in a SQLite database.

    Args:
        database_path (str): Path to the SQLite database file.
        user_data (dict): User-provided data containing:
                          id (optional), username, and email.

    Returns:
        int: The ID of the created or updated record.
    """

    if not isinstance(user_data, dict):
        raise TypeError("user_data must be a dictionary.")

    username = user_data.get("username")
    email = user_data.get("email")
    user_id = user_data.get("id")

    if not isinstance(username, str) or not username.strip():
        raise ValueError("A valid username is required.")

    if not isinstance(email, str) or not email.strip():
        raise ValueError("A valid email address is required.")

    username = username.strip()
    email = email.strip()

    connection = sqlite3.connect(database_path)

    try:
        cursor = connection.cursor()

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

        if not isinstance(user_id, int) or user_id <= 0:
            raise ValueError("User ID must be a positive integer.")

        cursor.execute(
            """
            UPDATE users
            SET username = ?, email = ?
            WHERE id = ?
            """,
            (username, email, user_id)
        )

        if cursor.rowcount == 0:
            raise ValueError("No matching user record was found.")

        connection.commit()
        return user_id

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()
