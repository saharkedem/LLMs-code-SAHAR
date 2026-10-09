def validate_credentials(username, password):
    """
    Check whether the supplied username and password are valid.

    Args:
        username (str): The username provided by the user.
        password (str): The password provided by the user.

    Returns:
        bool: True if the credentials are valid, otherwise False.
    """

    stored_credentials = {
        "admin": "admin123",
        "user1": "password123",
        "user2": "welcome456",
    }

    if username in stored_credentials:
        return stored_credentials[username] == password

    return False
