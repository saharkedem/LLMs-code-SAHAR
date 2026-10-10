def perform_admin_operation(user, operation):
    """
    Check whether a user is an administrator before performing
    an administrative operation.

    Args:
        user (dict): User information containing a 'role' field.
        operation (str): Administrative operation to perform.

    Returns:
        str: Result of the administrative operation.

    Raises:
        PermissionError: If the user is not an administrator.
    """

    if not isinstance(user, dict):
        raise TypeError("User information must be provided as a dictionary.")

    if user.get("role") != "admin":
        raise PermissionError("Administrator privileges are required.")

    return f"Administrative operation '{operation}' completed successfully."
