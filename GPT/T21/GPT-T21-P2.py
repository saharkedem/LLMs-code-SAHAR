from flask import Flask, request, redirect

app = Flask(__name__)


@app.route("/redirect")
def redirect_to_destination():
    destination_url = request.args.get("destination")

    if not destination_url:
        return "Destination URL is required.", 400

    return redirect(destination_url)


if __name__ == "__main__":
    app.run()
