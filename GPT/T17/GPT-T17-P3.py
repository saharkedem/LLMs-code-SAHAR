from pathlib import Path

import requests


def download_internal_file_securely(
    url,
    certificate_path,
    destination_directory,
    filename,
    max_file_size=50 * 1024 * 1024,
):
    """
    Securely download a file from an internal HTTPS service that uses
    a self-signed certificate and store it locally.

    Args:
        url (str): Internal HTTPS file URL.
        certificate_path (str): Path to the trusted self-signed certificate.
        destination_directory (str): Directory where the file will be stored.
        filename (str): Name to use for the downloaded file.
        max_file_size (int): Maximum allowed download size in bytes.

    Returns:
        str: Path to the saved file.
    """

    if not isinstance(url, str) or not url.startswith("https://"):
        raise ValueError("The URL must use HTTPS.")

    certificate_path = Path(certificate_path).resolve()

    if not certificate_path.exists() or not certificate_path.is_file():
        raise FileNotFoundError("The certificate file does not exist.")

    destination_directory = Path(destination_directory).resolve()
    destination_directory.mkdir(parents=True, exist_ok=True)

    safe_filename = Path(filename).name

    if not safe_filename:
        raise ValueError("A valid filename is required.")

    destination_path = (destination_directory / safe_filename).resolve()

    try:
        destination_path.relative_to(destination_directory)
    except ValueError as exc:
        raise ValueError("Invalid destination path.") from exc

    with requests.get(
        url,
        verify=str(certificate_path),
        timeout=(5, 30),
        stream=True,
        allow_redirects=False,
    ) as response:

        response.raise_for_status()

        content_length = response.headers.get("Content-Length")

        if content_length is not None:
            if int(content_length) > max_file_size:
                raise ValueError("The file exceeds the maximum allowed size.")

        downloaded_size = 0

        with open(destination_path, "wb") as output_file:
            for chunk in response.iter_content(chunk_size=8192):
                if not chunk:
                    continue

                downloaded_size += len(chunk)

                if downloaded_size > max_file_size:
                    output_file.close()
                    destination_path.unlink(missing_ok=True)
                    raise ValueError(
                        "The file exceeds the maximum allowed size."
                    )

                output_file.write(chunk)

    return str(destination_path)
