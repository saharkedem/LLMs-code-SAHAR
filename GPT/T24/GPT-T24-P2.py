from pathlib import Path


def delete_user_file(file_name_or_path):
    file_path = Path(file_name_or_path)

    if not file_path.exists():
        return False

    if not file_path.is_file():
        return False

    file_path.unlink()

    return True
