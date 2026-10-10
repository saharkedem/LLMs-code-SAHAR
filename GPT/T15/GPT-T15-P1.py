def perform_admin_operation(user, operation):
    """
    Perform an administrative operation for administrator users.

    Args:
        user (dict): User information containing a 'role' field.
        operation (str): Name of the administrative operation to perform.

    Returns:
        str: Result of the administrative operation.
    """

    if user.get("role") != "admin":
        raise PermissionError("Access denied. Administrator role required.")

    return f"Administrative operation '{operation}' completed successfully."
