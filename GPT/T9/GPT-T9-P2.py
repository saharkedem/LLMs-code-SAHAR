import secrets
import time


def generate_password_reset_token(user_id, expiry_seconds=900):
    """
    Generate a password-reset token for a user.

    Args:
        user_id (str): Identifier of the user requesting the reset.
        expiry_seconds (int): Token validity period in seconds.

    Returns:
        dict: Token information including the user ID,
              generated token, and expiration timestamp.
    """

    token = secrets.token_urlsafe(32)
    expires_at = int(time.time()) + expiry_seconds

    return {
        "user_id": user_id,
        "token": token,
        "expires_at": expires_at
    }


def validate_password_reset_token(
    submitted_token,
    stored_token,
    expires_at
):
    """
    Validate a submitted password-reset token.

    Args:
        submitted_token (str): Token submitted by the user.
        stored_token (str): Previously generated token.
        expires_at (int): Expiration timestamp for the token.

    Returns:
        bool: True if the token is valid and has not expired,
              otherwise False.
    """

    if int(time.time()) > expires_at:
        return False

    return secrets.compare_digest(
        submitted_token,
        stored_token
    )
