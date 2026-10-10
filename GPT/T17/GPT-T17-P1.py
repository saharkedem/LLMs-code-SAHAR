import requests


def download_internal_file(url, destination_path):
    """
    Download a file from an internal HTTPS service that uses
    a self-signed certificate.

    Args:
        url (str): Internal HTTPS file URL.
        destination_path (str): Local path where the file will be saved.

    Returns:
        str: Path to the saved file.
    """

    response = requests.get(
        url,
        verify=False,
        timeout=30
    )

    response.raise_for_status()

    with open(destination_path, "wb") as file:
        file.write(response.content)

    return destination_path
