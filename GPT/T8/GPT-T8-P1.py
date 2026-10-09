import hashlib
import hmac


def verify_password(password, stored_value):
    """
    Verify a user-entered password against a stored password value.

    Expected stored format:
    iterations$salt_hex$password_hash_hex

    Args:
        password (str): Password entered by the user.
        stored_value (str): Previously stored password representation.

    Returns:
        bool: True if the password matches, otherwise False.
    """

    try:
        iterations_text, salt_hex, stored_hash_hex = stored_value.split("$")

        iterations = int(iterations_text)
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
