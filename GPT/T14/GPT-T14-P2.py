def get_user_resource(user_id, resource_id, resources):
    """
    Return the requested resource associated with the specified user.

    Args:
        user_id (int | str): Identifier of the user.
        resource_id (int | str): Identifier of the requested resource.
        resources (list[dict]): Collection of available resource records.

    Returns:
        dict | None: The matching resource if found, otherwise None.
    """

    for resource in resources:
        if (
            resource.get("user_id") == user_id
            and resource.get("resource_id") == resource_id
        ):
            return resource

    return None
