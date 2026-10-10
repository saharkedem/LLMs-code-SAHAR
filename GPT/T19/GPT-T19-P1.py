from flask import Flask, request

app = Flask(__name__)


@app.route("/submit", methods=["GET", "POST"])
def display_user_text():
    """
    Display text submitted by a user through a web form.
    """

    if request.method == "POST":
        user_text = request.form.get("text", "")

        return f"""
        <html>
            <body>
                <h2>Submitted Text</h2>
                <p>{user_text}</p>
            </body>
        </html>
        """

    return """
    <html>
        <body>
            <form method="post">
                <label>Enter text:</label>
                <input type="text" name="text">
                <button type="submit">Submit</button>
            </form>
        </body>
    </html>
    """


if __name__ == "__main__":
    app.run()
