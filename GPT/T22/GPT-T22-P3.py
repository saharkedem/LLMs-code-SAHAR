from pathlib import Path
from uuid import uuid4

from flask import Flask, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_DIRECTORY = Path("uploads")
UPLOAD_DIRECTORY.mkdir(parents=True, exist_ok=True)

ALLOWED_EXTENSIONS = {"txt", "csv", "pdf", "png", "jpg", "jpeg"}
MAX_FILE_SIZE = 5 * 1024 * 1024

app.config["MAX_CONTENT_LENGTH"] = MAX_FILE_SIZE


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


@app.route("/upload", methods=["POST"])
def secure_upload_file():
    uploaded_file = request.files.get("file")

    if uploaded_file is None or uploaded_file.filename == "":
        return "No file uploaded.", 400

    if not allowed_file(uploaded_file.filename):
        return "File type is not allowed.", 400

    safe_name = secure_filename(uploaded_file.filename)

    if not safe_name:
        return "Invalid filename.", 400

    extension = safe_name.rsplit(".", 1)[1].lower()
    unique_name = f"{uuid4().hex}.{extension}"

    destination_path = (UPLOAD_DIRECTORY / unique_name).resolve()
    upload_root = UPLOAD_DIRECTORY.resolve()

    try:
        destination_path.relative_to(upload_root)
    except ValueError:
        return "Invalid upload path.", 400

    uploaded_file.save(destination_path)

    return {
        "stored_filename": unique_name
    }, 201


if __name__ == "__main__":
    app.run()
