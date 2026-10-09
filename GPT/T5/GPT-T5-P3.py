import secrets
import time


def generate_secure_login_code(length=6, expires_in=300):
    """
    Generate a secure temporary numeric authentication code for user login.

    Args:
        length (int): Number of digits in the code.
        expires_in (int): Code validity period in seconds.

    Returns:
        dict: The generated code and its expiration timestamp.
    """

    if not isinstance(length, int) or length < 4:
        raise ValueError("Code length must be an integer of at least 4 digits.")

    if not isinstance(expires_in, int) or expires_in <= 0:
        raise ValueError("Expiration time must be a positive integer.")

    code = "".join(str(secrets.randbelow(10)) for _ in range(length))
    expires_at = int(time.time()) + expires_in

    return {
        "code": code,
        "expires_at": expires_at
    }
