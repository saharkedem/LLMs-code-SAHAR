from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Text Submission</title>
</head>
<body>
    <h1>Submit Your Text</h1>

    <form method="POST">
        <textarea name="text" rows="5" cols="40" required></textarea>
        <br>
        <button type="submit">Submit</button>
    </form>

    {% if submitted_text is not none %}
        <h2>Submitted Text:</h2>
        <p>{{ submitted_text }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def submit_text():
    submitted_text = None

    if request.method == "POST":
        submitted_text = request.form.get("text", "")

    return render_template_string(
        HTML,
        submitted_text=submitted_text
    )

if __name__ == "__main__":
    app.run()
