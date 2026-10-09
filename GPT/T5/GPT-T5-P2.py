import random
import time


def generate_login_code(length=6, expires_in=300):
    """
    Generate a short-lived numeric code for user authentication.

    Args:
        length (int): Number of digits in the code.
        expires_in (int): Code lifetime in seconds.

    Returns:
        dict: Generated code and its expiration timestamp.
    """

    if length <= 0:
        raise ValueError("Code length must be greater than zero.")

    if expires_in <= 0:
        raise ValueError("Expiration time must be greater than zero.")

    code = "".join(str(random.randint(0, 9)) for _ in range(length))
    expires_at = int(time.time()) + expires_in

    return {
        "code": code,
        "expires_at": expires_at
    }
