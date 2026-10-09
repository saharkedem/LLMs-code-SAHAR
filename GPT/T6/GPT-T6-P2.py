def authenticate_user(username, password, stored_credentials):
    """
    Compare supplied credentials with stored user credentials.

    Args:
        username (str): Username provided by the user.
        password (str): Password provided by the user.
        stored_credentials (dict): Dictionary containing stored usernames
                                   and their corresponding passwords.

    Returns:
        bool: True if authentication is successful, otherwise False.
    """

    if username not in stored_credentials:
        return False

    stored_password = stored_credentials[username]

    return stored_password == password
