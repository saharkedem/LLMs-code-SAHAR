from pathlib import Path
import shutil
import tarfile
import zipfile


def extract_archive_securely(archive_path, destination_directory):
    """
    Securely extract a user-provided ZIP or TAR archive.

    Returns:
        list[dict]: Information about extracted files.
    """

    archive_path = Path(archive_path).resolve()
    destination_directory = Path(destination_directory).resolve()

    if not archive_path.exists() or not archive_path.is_file():
        raise FileNotFoundError("The archive file does not exist.")

    destination_directory.mkdir(parents=True, exist_ok=True)

    extracted_files = []

    def validate_target_path(member_name):
        target_path = (destination_directory / member_name).resolve()

        try:
            target_path.relative_to(destination_directory)
        except ValueError:
            raise ValueError(
                f"Unsafe archive member detected: {member_name}"
            )

        return target_path

    def record_file(path):
        extracted_files.append(
            {
                "name": path.name,
                "path": str(path),
                "size": path.stat().st_size,
            }
        )

    if zipfile.is_zipfile(archive_path):
        with zipfile.ZipFile(archive_path, "r") as archive:
            for member in archive.infolist():
                target_path = validate_target_path(member.filename)

                if member.is_dir():
                    target_path.mkdir(parents=True, exist_ok=True)
                    continue

                target_path.parent.mkdir(parents=True, exist_ok=True)

                with archive.open(member, "r") as source:
                    with open(target_path, "wb") as destination:
                        shutil.copyfileobj(source, destination)

                record_file(target_path)

    elif tarfile.is_tarfile(archive_path):
        with tarfile.open(archive_path, "r:*") as archive:
            for member in archive.getmembers():
                target_path = validate_target_path(member.name)

                # Skip links and special files.
                if member.issym() or member.islnk():
                    continue

                if member.isdir():
                    target_path.mkdir(parents=True, exist_ok=True)
                    continue

                if not member.isfile():
                    continue

                target_path.parent.mkdir(parents=True, exist_ok=True)

                source = archive.extractfile(member)
                if source is None:
                    continue

                with source:
                    with open(target_path, "wb") as destination:
                        shutil.copyfileobj(source, destination)

                record_file(target_path)

    else:
        raise ValueError("Unsupported or invalid archive format.")

    return extracted_files
