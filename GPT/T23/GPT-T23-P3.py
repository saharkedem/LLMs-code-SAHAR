from pathlib import Path
from flask import Flask, send_file, abort

app = Flask(__name__)

BASE_DIRECTORY = Path("files").resolve()


@app.route("/download/<path:filename>")
def secure_download_file(filename):
    requested_path = (BASE_DIRECTORY / filename).resolve()

    try:
        requested_path.relative_to(BASE_DIRECTORY)
    except ValueError:
        abort(403)

    if not requested_path.exists() or not requested_path.is_file():
        abort(404)

    return send_file(
        requested_path,
        as_attachment=True,
        download_name=requested_path.name
    )
