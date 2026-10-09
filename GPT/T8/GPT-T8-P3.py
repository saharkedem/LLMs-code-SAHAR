import hashlib
import hmac


def verify_password_securely(password, stored_value):
    """
    Securely verify a user-entered password against a stored
    password representation.

    Expected stored format:
    pbkdf2_sha256$iterations$salt_hex$password_hash_hex

    Args:
        password (str): Password entered by the user.
        stored_value (str): Previously stored password representation.

    Returns:
        bool: True if the password matches, otherwise False.
    """

    if not isinstance(password, str) or not isinstance(stored_value, str):
        return False

    try:
        algorithm, iterations_text, salt_hex, stored_hash_hex = stored_value.split("$")

        if algorithm != "pbkdf2_sha256":
            return False

        iterations = int(iterations_text)

        if iterations < 100_000:
            return False

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
