def get_user_resource(user_id, resource_id, resources):
    """
    Retrieve a resource using a user ID and resource ID.

    Args:
        user_id (int | str): Identifier of the user.
        resource_id (int | str): Identifier of the resource.
        resources (list[dict]): Collection of resource records.

    Returns:
        dict | None: Matching resource, or None if no match is found.
    """

    for resource in resources:
        if (
            resource.get("user_id") == user_id
            and resource.get("resource_id") == resource_id
        ):
            return resource

    return None
