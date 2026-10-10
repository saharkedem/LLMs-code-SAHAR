from flask import Flask, request, render_template_string, abort
from flask_wtf.csrf import CSRFProtect
from markupsafe import escape
import os

app = Flask(__name__)

# Secure application configuration
app.config.update(
    SECRET_KEY=os.environ["FLASK_SECRET_KEY"],
    MAX_CONTENT_LENGTH=16 * 1024,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_SAMESITE="Lax"
)

csrf = CSRFProtect(app)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Secure Text Submission</title>
</head>
<body>
    <h1>Submit Your Text</h1>

    <form method="POST">
        <input type="hidden"
               name="csrf_token"
               value="{{ csrf_token() }}">

        <textarea name="text"
                  maxlength="1000"
                  required></textarea>

        <button type="submit">Submit</button>
    </form>

    {% if submitted_text is not none %}
        <h2>Submitted Text:</h2>
        <p>{{ submitted_text }}</p>
    {% endif %}
</body>
</html>
"""

@app.after_request
def set_security_headers(response):
    response.headers["Content-Security-Policy"] = (
        "default-src 'none'; "
        "style-src 'none'; "
        "form-action 'self'; "
        "base-uri 'none'; "
        "frame-ancestors 'none'"
    )
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Referrer-Policy"] = "no-referrer"
