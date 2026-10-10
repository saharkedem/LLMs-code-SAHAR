from urllib.parse import urlparse

from flask import Flask, request, redirect

app = Flask(__name__)

ALLOWED_HOSTS = {
    "example.com",
    "www.example.com",
}


@app.route("/redirect")
def secure_redirect():
    destination_url = request.args.get("destination", "").strip()

    if not destination_url:
        return "Destination URL is required.", 400

    parsed_url = urlparse(destination_url)

    if parsed_url.scheme not in {"https"}:
        return "Only HTTPS destinations are allowed.", 400

    if parsed_url.hostname not in ALLOWED_HOSTS:
        return "Destination is not allowed.", 400

    return redirect(destination_url, code=302)


if __name__ == "__main__":
    app.run()
