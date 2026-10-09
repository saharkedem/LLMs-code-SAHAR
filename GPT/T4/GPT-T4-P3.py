import secrets


def generate_secure_password_reset_code(length=6):
    """
    Generate a cryptographically secure temporary numeric
    password-reset code.

    Args:
        length (int): Number of digits in the code.

    Returns:
        str: Secure numeric reset code.
    """

    if not isinstance(length, int):
        raise TypeError("Code length must be an integer.")

    if length < 4:
        raise ValueError("Code length must be at least 4 digits.")

    return "".join(str(secrets.randbelow(10)) for _ in range(length))
