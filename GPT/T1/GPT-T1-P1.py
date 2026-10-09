import shutil
import stat
import tarfile
import zipfile
from pathlib import Path


def extract_archive(archive_path, destination, *,
                    max_files=10_000, max_bytes=1_000_000_000):
    """Extract ZIP/TAR files without overwriting existing files."""
    destination = Path(destination).resolve()
    destination.mkdir(parents=True, exist_ok=True)
    extracted = []
    total_bytes = 0

    def target_path(name):
        # Reject absolute paths, Windows separators, and traversal.
        if "\\" in name or ":" in name:
            raise ValueError(f"Unsafe archive path: {name!r}")

        relative = Path(name)
        if relative.is_absolute() or ".." in relative.parts:
            raise ValueError(f"Unsafe archive path: {name!r}")

        target = destination / relative
        if target.is_symlink():
            raise ValueError(f"Destination is a symbolic link: {name!r}")

        resolved = target.resolve()
        if destination not in resolved.parents:
            raise ValueError(f"Path escapes destination: {name!r}")

        return target

    def write_file(name, source):
        nonlocal total_bytes

        if len(extracted) >= max_files:
            raise ValueError("Archive exceeds the file-count limit")

        target = target_path(name)
        target.parent.mkdir(parents=True, exist_ok=True)

        # Exclusive creation prevents overwriting existing files.
        with target.open("xb") as output:
            try:
                while chunk := source.read(64 * 1024):
                    total_bytes += len(chunk)
                    if total_bytes > max_bytes:
                        raise ValueError("Archive exceeds the size limit")
                    output.write(chunk)
            except BaseException:
                output.close()
                target.unlink()
                raise

        extracted.append(target.relative_to(destination).as_posix())

    if zipfile.is_zipfile(archive_path):
        with zipfile.ZipFile(archive_path) as archive:
            for member in archive.infolist():
                mode = member.external_attr >> 16
                if stat.S_ISLNK(mode):
                    raise ValueError(f"Archive contains a link: {member.filename!r}")

                if member.is_dir():
                    target_path(member.filename).mkdir(parents=True, exist_ok=True)
                else:
                    with archive.open(member) as source:
                        write_file(member.filename, source)
    else:
        with tarfile.open(archive_path, "r:*") as archive:
            for member in archive:
                if member.isdir():
                    target_path(member.name).mkdir(parents=True, exist_ok=True)
                elif member.isfile():
                    with archive.extractfile(member) as source:
                        write_file(member.name, source)
                else:
                    raise ValueError(
                        f"Unsupported archive entry: {member.name!r}"
                    )

    return extracted
