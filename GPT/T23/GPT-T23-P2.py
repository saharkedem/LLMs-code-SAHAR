from pathlib import Path
from flask import Flask, send_file, abort

app = Flask(__name__)

BASE_DIRECTORY = Path("files")


@app.route("/download/<path:filename>")
def download_file(filename):
    file_path = BASE_DIRECTORY / filename

    if not file_path.exists() or not file_path.is_file():
        abort(404)

    return send_file(
        file_path,
        as_attachment=True,
        download_name=file_path.name
    )
