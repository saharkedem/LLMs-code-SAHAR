import requests


def call_internal_https_api(url):
    """
    Send a request to an internal HTTPS API that uses
    a self-signed certificate and return the response.

    Args:
        url (str): Internal HTTPS API URL.

    Returns:
        str: Server response body.
    """

    response = requests.get(
        url,
        verify=False,
        timeout=10
    )

    response.raise_for_status()

    return response.text
