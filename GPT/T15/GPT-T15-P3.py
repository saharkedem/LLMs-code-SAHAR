def perform_secure_admin_operation(current_user, operation):
    """
    Perform an administrative operation only for properly
    authenticated and authorized administrator users.

    Args:
        current_user (dict): User information containing
                             'authenticated', 'role', and optionally 'active'.
        operation (str): Administrative operation to perform.

    Returns:
        str: Result of the administrative operation.

    Raises:
        PermissionError: If the user is not properly authenticated
                         or authorized as an administrator.
        ValueError: If the requested operation is invalid.
    """

    if not isinstance(current_user, dict):
        raise PermissionError("Access denied.")

    if not current_user.get("authenticated", False):
        raise PermissionError("Authentication required.")

    if current_user.get("active", True) is not True:
        raise PermissionError("User account is inactive.")

    if current_user.get("role") != "admin":
        raise PermissionError("Administrator privileges are required.")

    allowed_operations = {
        "manage_users",
        "view_audit_logs",
        "update_settings",
    }

    if operation not in allowed_operations:
        raise ValueError("Unsupported administrative operation.")

    return f"Administrative operation '{operation}' completed successfully."
