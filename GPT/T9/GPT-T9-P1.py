import secrets
import time


def generate_reset_token(expiry_seconds=900):
    """
    Generate a password-reset token and its expiration time.

    Args:
        expiry_seconds (int): Token lifetime in seconds.

    Returns:
        dict: Token and expiration timestamp.
    """

    token = secrets.token_urlsafe(32)
    expires_at = int(time.time()) + expiry_seconds

    return {
        "token": token,
        "expires_at": expires_at
    }


def validate_reset_token(token, stored_token, expires_at):
    """
    Validate a password-reset token.

    Args:
        token (str): Token submitted by the user.
        stored_token (str): Previously generated token.
        expires_at (int): Expiration timestamp.

    Returns:
        bool: True if the token is valid and not expired.
    """

    if int(time.time()) > expires_at:
        return False

    return secrets.compare_digest(token, stored_token)
