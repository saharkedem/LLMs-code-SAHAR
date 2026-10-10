from pathlib import Path


def get_server_file(filename, base_directory="files"):
    base_path = Path(base_directory)
    file_path = base_path / filename

    if not file_path.exists() or not file_path.is_file():
        return None

    return file_path.read_bytes()
