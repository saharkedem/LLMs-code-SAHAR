import requests


def call_internal_https_service(url, certificate_path):
    """
    Securely communicate with an internal HTTPS service that uses
    a self-signed certificate.

    Args:
        url (str): Internal HTTPS service URL.
        certificate_path (str): Path to the trusted self-signed CA
                                or server certificate.

    Returns:
        str: Response body returned by the server.

    Raises:
        ValueError: If the URL does not use HTTPS.
        requests.RequestException: If the request fails.
    """

    if not isinstance(url, str) or not url.startswith("https://"):
        raise ValueError("The service URL must use HTTPS.")

    if not isinstance(certificate_path, str) or not certificate_path:
        raise ValueError("A valid certificate path is required.")

    response = requests.get(
        url,
        verify=certificate_path,
        timeout=10
    )

    response.raise_for_status()

    return response.text
