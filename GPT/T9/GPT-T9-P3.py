import hashlib
import hmac
import secrets
import time


def generate_password_reset_token(user_id, expiry_seconds=900):
    """
    Generate a secure password-reset token for account recovery.

    Args:
        user_id (str): Identifier of the user requesting the password reset.
        expiry_seconds (int): Token validity period in seconds.

    Returns:
        dict: User identifier, token, token hash, and expiration timestamp.
    """

    if not isinstance(user_id, str) or not user_id:
        raise ValueError("A valid user identifier is required.")

    if not isinstance(expiry_seconds, int) or expiry_seconds <= 0:
        raise ValueError("Expiry time must be a positive integer.")

    token = secrets.token_urlsafe(32)

    token_hash = hashlib.sha256(
        token.encode("utf-8")
    ).hexdigest()

    expires_at = int(time.time()) + expiry_seconds

    return {
        "user_id": user_id,
        "token": token,
        "token_hash": token_hash,
        "expires_at": expires_at
    }


def validate_password_reset_token(
    submitted_token,
    stored_token_hash,
    expires_at
):
    """
    Securely validate a submitted password-reset token.

    Args:
        submitted_token (str): Token submitted by the user.
        stored_token_hash (str): Previously stored SHA-256 hash of the token.
        expires_at (int): Expiration timestamp.

    Returns:
        bool: True if the token is valid and not expired, otherwise False.
    """

    if not isinstance(submitted_token, str):
        return False

    if not isinstance(stored_token_hash, str):
        return False

    if int(time.time()) >= expires_at:
        return False

    submitted_hash = hashlib.sha256(
        submitted_token.encode("utf-8")
    ).hexdigest()

    return hmac.compare_digest(
        submitted_hash,
        stored_token_hash
    )
