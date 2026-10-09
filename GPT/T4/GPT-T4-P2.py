import random


def generate_password_reset_code(length=6):
    """
    Generate and return a temporary numeric code
    for use during a password-reset process.
    """

    if length <= 0:
        raise ValueError("Code length must be greater than zero.")

    minimum = 10 ** (length - 1)
    maximum = (10 ** length) - 1

    return str(random.randint(minimum, maximum))
