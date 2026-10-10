import requests


def call_rest_api_securely(url, api_token):
    """
    Send an authenticated request to a REST API while following
    secure token-handling practices.

    Args:
        url (str): HTTPS REST API endpoint.
        api_token (str): Authentication token.

    Returns:
        dict | str: Parsed JSON response if available,
                    otherwise the raw response text.
    """

    if not isinstance(url, str) or not url.startswith("https://"):
        raise ValueError("The API URL must use HTTPS.")

    if not isinstance(api_token, str) or not api_token.strip():
        raise ValueError("A valid API token is required.")

    headers = {
        "Authorization": f"Bearer {api_token}",
        "Accept": "application/json",
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=(5, 15),
            allow_redirects=False,
        )

        response.raise_for_status()

        content_type = response.headers.get("Content-Type", "")

        if "application/json" in content_type.lower():
            return response.json()

        return response.text

    except requests.RequestException as exc:
        raise RuntimeError("The API request failed.") from exc
