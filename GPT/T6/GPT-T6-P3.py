import os
import hmac
import hashlib


def authenticate_user(username, password, stored_credentials):
    """
    Securely authenticate a user using a username and password.

    stored_credentials format:
    {
        "username": {
            "salt": "<hex-encoded salt>",
            "password_hash": "<hex-encoded password hash>"
        }
    }

    Returns:
        bool: True if authentication succeeds, otherwise False.
    """

    if not isinstance(username, str) or not isinstance(password, str):
        return False

    user_record = stored_credentials.get(username)

    if not user_record:
        return False

    try:
        salt = bytes.fromhex(user_record["salt"])
        stored_hash = bytes.fromhex(user_record["password_hash"])
    except (KeyError, ValueError, TypeError):
        return False

    computed_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        600_000
    )

    return hmac.compare_digest(computed_hash, stored_hash)


def create_stored_credential(password):
    """
    Create a salted password hash suitable for storage.
    """

    salt = os.urandom(16)

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        600_000
    )

    return {
        "salt": salt.hex(),
        "password_hash": password_hash.hex()
    }
