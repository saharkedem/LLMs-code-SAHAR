import requests


def call_rest_api(url, token):
    """
    Send a request to a REST API using an authentication token.

    Args:
        url (str): REST API endpoint.
        token (str): Authentication token.

    Returns:
        dict | str: Parsed JSON response when available,
                    otherwise the raw response text.
    """

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=10
    )

    response.raise_for_status()

    try:
        return response.json()
    except ValueError:
        return response.text
