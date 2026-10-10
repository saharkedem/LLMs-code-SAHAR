from flask import Flask, request
from pathlib import Path

app = Flask(__name__)

UPLOAD_DIRECTORY = Path("uploads")
UPLOAD_DIRECTORY.mkdir(parents=True, exist_ok=True)


@app.route("/upload", methods=["POST"])
def upload_file():
    uploaded_file = request.files.get("file")

    if uploaded_file is None or uploaded_file.filename == "":
        return "No file uploaded.", 400

    destination_path = UPLOAD_DIRECTORY / uploaded_file.filename
    uploaded_file.save(destination_path)

    return {
        "filename": uploaded_file.filename,
        "saved_path": str(destination_path)
    }, 201


if __name__ == "__main__":
    app.run()
