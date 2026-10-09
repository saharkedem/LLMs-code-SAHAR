import hashlib
import os


def prepare_password_for_storage(password):
    """
    Transform a password into a representation suitable
    for persistent storage.

    Args:
        password (str): The user-provided password.

    Returns:
        str: A string containing the salt and password hash.
    """

    if not isinstance(password, str):
        raise TypeError("Password must be a string.")

    salt = os.urandom(16)

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        100_000
    )

    stored_value = f"{salt.hex()}${password_hash.hex()}"

    return stored_value
