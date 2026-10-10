from pathlib import Path


def secure_delete_file(filename, base_directory="files"):
    base_path = Path(base_directory).resolve()
    requested_path = (base_path / filename).resolve()

    try:
        requested_path.relative_to(base_path)
    except ValueError:
        raise PermissionError("Invalid file path.")

    if not requested_path.exists():
        return False

    if not requested_path.is_file():
        return False

    if requested_path.is_symlink():
        raise PermissionError("Symbolic links are not allowed.")

    requested_path.unlink()

    return True
