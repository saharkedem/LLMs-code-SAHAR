import requests


def download_internal_file(url, certificate_path, destination_path):
    """
    Connect to an internal HTTPS service that uses a self-signed certificate,
    download a file, and store it locally.

    Args:
        url (str): Internal HTTPS file URL.
        certificate_path (str): Path to the self-signed certificate file.
        destination_path (str): Local path where the downloaded file is saved.

    Returns:
        str: Path to the saved file.
    """

    response = requests.get(
        url,
        verify=certificate_path,
        timeout=30
    )

    response.raise_for_status()

    with open(destination_path, "wb") as file:
        file.write(response.content)

    return destination_path
