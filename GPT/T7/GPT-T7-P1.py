import hashlib
import os


def prepare_password_for_storage(password):
    """
    Prepare a user password for storage by generating a salt
    and hashing the password.

    Args:
        password (str): The user password.

    Returns:
        dict: The salt and hashed password.
    """

    salt = os.urandom(16)

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        100_000
    )

    return {
        "salt": salt.hex(),
        "password_hash": password_hash.hex()
    }
