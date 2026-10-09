import random


def generate_login_access_code(length=6):
    """
    Generate a temporary numeric access code for user login.

    Args:
        length (int): Number of digits in the code.

    Returns:
        str: The generated numeric access code.
    """

    if length <= 0:
        raise ValueError("Code length must be greater than zero.")

    return "".join(str(random.randint(0, 9)) for _ in range(length))
