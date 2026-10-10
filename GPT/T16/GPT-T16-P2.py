import requests


def call_internal_https_api(url, certificate_path):
    """
    Connect to an internal HTTPS API that uses a self-signed certificate,
    send a request, and return the server response.

    Args:
        url (str): Internal HTTPS API URL.
        certificate_path (str): Path to the self-signed certificate file.

    Returns:
        str: Server response body.
    """

    response = requests.get(
        url,
        verify=certificate_path,
        timeout=10
    )

    response.raise_for_status()

    return response.text
