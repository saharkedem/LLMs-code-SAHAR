def role_required(required_role):
    """
    Decorator that allows access to a function only when
    the user's role matches the required role.
    """

    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if not isinstance(user, dict):
                raise TypeError("User information must be provided as a dictionary.")

            user_role = user.get("role")

            if user_role != required_role:
                raise PermissionError(
                    f"Access denied. Required role: {required_role}"
                )

            return func(user, *args, **kwargs)

        return wrapper

    return decorator


@role_required("admin")
def admin_dashboard(user):
    return f"Welcome to the admin dashboard, {user.get('username', 'user')}."


@role_required("manager")
def manager_report(user):
    return f"Manager report accessed by {user.get('username', 'user')}."
