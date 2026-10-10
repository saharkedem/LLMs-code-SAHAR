class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role


def assign_role(user, role):
    """
    Assign a role to a user.

    Args:
        user (User): The user object.
        role (str): The role to assign.

    Returns:
        User: The updated user object.
    """

    user.role = role
    return user


def has_role(user, required_role):
    """
    Check whether a user has the required role.

    Args:
        user (User): The user object.
        required_role (str): Role required to access the function.

    Returns:
        bool: True if the user has the required role, otherwise False.
    """

    return user.role == required_role


def protected_function(user, required_role):
    """
    Allow access to protected functionality only if
    the user has the required role.

    Args:
        user (User): The user requesting access.
        required_role (str): Required role for access.

    Returns:
        str: Access result.
    """

    if not has_role(user, required_role):
        raise PermissionError("Access denied.")

    return f"Access granted to {user.username}."


# Example usage
admin_user = User("alice", "admin")
regular_user = User("bob", "user")

print(protected_function(admin_user, "admin"))
# print(protected_function(regular_user, "admin"))  # Raises PermissionError
