import random


def generate_password_reset_code(length=6):
    """
    Generate a temporary numeric password-reset code.

    Args:
        length (int): Number of digits in the code.

    Returns:
        str: The generated numeric reset code.
    """

    if length <= 0:
        raise ValueError("Code length must be greater than zero.")

    return "".join(str(random.randint(0, 9)) for _ in range(length))
