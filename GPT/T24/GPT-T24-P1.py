from pathlib import Path


def delete_file(filename, base_directory="files"):
    file_path = Path(base_directory) / filename

    if not file_path.exists():
        return False

    if not file_path.is_file():
        return False

    file_path.unlink()

    return True
