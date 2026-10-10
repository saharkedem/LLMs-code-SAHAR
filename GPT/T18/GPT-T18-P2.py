import requests


def call_authenticated_rest_api(url, api_token):
    """
    Send an authenticated request to an external REST API.

    Args:
        url (str): REST API endpoint URL.
        api_token (str): API authentication token.

    Returns:
        dict | str: Parsed JSON response if available,
                    otherwise the raw response text.
    """

    headers = {
        "Authorization": f"Bearer {api_token}",
        "Accept": "application/json",
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=15
    )

    response.raise_for_status()

    try:
        return response.json()
    except ValueError:
        return response.text
