from pathlib import Path
import zipfile
import tarfile


def extract_archive(archive_path, destination_directory):
    archive_path = Path(archive_path)
    destination_directory = Path(destination_directory)
    destination_directory.mkdir(parents=True, exist_ok=True)

    extracted_files = []

    def safe_path(member_name):
        target = (destination_directory / member_name).resolve()
        base = destination_directory.resolve()

        if not str(target).startswith(str(base)):
            raise ValueError(f"Unsafe archive path detected: {member_name}")

        return target

    if zipfile.is_zipfile(archive_path):
        with zipfile.ZipFile(archive_path, "r") as archive:
            for member in archive.infolist():
                target = safe_path(member.filename)

                if member.is_dir():
                    target.mkdir(parents=True, exist_ok=True)
                    continue

                target.parent.mkdir(parents=True, exist_ok=True)

                with archive.open(member) as source, open(target, "wb") as output:
                    output.write(source.read())

                extracted_files.append({
                    "name": target.name,
                    "path": str(target),
                    "size": target.stat().st_size
                })

    elif tarfile.is_tarfile(archive_path):
        with tarfile.open(archive_path, "r:*") as archive:
            for member in archive.getmembers():
                if not member.isfile():
                    continue

                target = safe_path(member.name)
                target.parent.mkdir(parents=True, exist_ok=True)

                source = archive.extractfile(member)

                if source is not None:
                    with source, open(target, "wb") as output:
                        output.write(source.read())

                    extracted_files.append({
                        "name": target.name,
                        "path": str(target),
                        "size": target.stat().st_size
                    })

    else:
        raise ValueError("Unsupported or invalid compressed archive.")

    return extracted_files
