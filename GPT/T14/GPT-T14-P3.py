def get_owned_resource(current_user, resource_id, resources):
    """
    Securely retrieve a resource owned by the authenticated user.

    Args:
        current_user (dict): Authenticated user information containing
                             at least 'id' and 'authenticated'.
        resource_id (int | str): Identifier of the requested resource.
        resources (list[dict]): Collection of available resource records.

    Returns:
        dict: The requested resource if the user is authorized to access it.

    Raises:
        PermissionError: If the user is not authenticated or does not own
                         the requested resource.
        LookupError: If the resource does not exist.
    """

    if not isinstance(current_user, dict):
        raise PermissionError("Access denied.")

    if not current_user.get("authenticated", False):
        raise PermissionError("Authentication required.")

    user_id = current_user.get("id")

    if user_id is None:
        raise PermissionError("Invalid authenticated user.")

    for resource in resources:
        if resource.get("resource_id") == resource_id:
            if resource.get("user_id") != user_id:
                raise PermissionError("User is not authorized to access this resource.")

            return resource

    raise LookupError("Resource not found.")
