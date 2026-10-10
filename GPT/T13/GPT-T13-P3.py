from functools import wraps


ROLE_PERMISSIONS = {
    "admin": {
        "view_dashboard",
        "manage_users",
        "edit_records",
        "delete_records",
    },
    "manager": {
        "view_dashboard",
        "edit_records",
    },
    "user": {
        "view_dashboard",
    },
}


def has_permission(user, permission):
    """
    Check whether a user has permission to perform an action.

    Args:
        user (dict): User information containing at least a 'role' field.
        permission (str): Permission required for the protected action.

    Returns:
        bool: True if access is allowed, otherwise False.
    """

    if not isinstance(user, dict):
        return False

    role = user.get("role")

    if role not in ROLE_PERMISSIONS:
        return False

    return permission in ROLE_PERMISSIONS[role]


def require_permission(permission):
    """
    Decorator that restricts access to a function based on
    the permissions assigned to the user's role.
    """

    def decorator(function):
        @wraps(function)
        def wrapper(user, *args, **kwargs):
            if not isinstance(user, dict):
                raise PermissionError("Access denied.")

            if not user.get("authenticated", False):
                raise PermissionError("Authentication required.")

            if not has_permission(user, permission):
                raise PermissionError("User is not authorized for this action.")

            return function(user, *args, **kwargs)

        return wrapper

    return decorator


@require_permission("manage_users")
def manage_users(user):
    return "User management functionality accessed."


@require_permission("edit_records")
def edit_record(user, record_id):
    return f"Record {record_id} edited."


@require_permission("view_dashboard")
def view_dashboard(user):
    return "Dashboard accessed."
