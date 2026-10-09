import os
import hashlib
import hmac


def prepare_password_for_storage(password):
    """
    Securely prepare a user password for persistent storage.

    Args:
        password (str): The user-provided password.

    Returns:
        str: A storage-safe representation containing the algorithm,
             iteration count, salt, and derived password hash.
    """

    if not isinstance(password, str):
        raise TypeError("Password must be a string.")

    if len(password) < 8:
        raise ValueError("Password must contain at least 8 characters.")

    iterations = 600_000
    salt = os.urandom(16)

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        iterations
    )

    return (
        f"pbkdf2_sha256$"
        f"{iterations}$"
        f"{salt.hex()}$"
        f"{password_hash.hex()}"
    )


def verify_stored_password(password, stored_value):
    """
    Verify a password against a stored password representation.

    Args:
        password (str): Password supplied for verification.
        stored_value (str): Previously stored password representation.

    Returns:
        bool: True if the password matches, otherwise False.
    """

    try:
        algorithm, iterations, salt_hex, stored_hash_hex = stored_value.split("$")

        if algorithm != "pbkdf2_sha256":
            return False

        iterations = int(iterations)
        salt = bytes.fromhex(salt_hex)
        stored_hash = bytes.fromhex(stored_hash_hex)

        computed_hash = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            salt,
            iterations
        )

        return hmac.compare_digest(computed_hash, stored_hash)

    except (ValueError, TypeError):
        return False
