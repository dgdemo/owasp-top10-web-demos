import secrets
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    make_response,
    session,
    abort,
)

app = Flask(__name__)
app.secret_key = "dev-only-secret-key-fixed-version"

ACCOUNT = {
    "alice": {"balance": 1000}
}


def get_or_set_user_cookie(response=None):
    """
    Ensure a 'user' cookie exists. In a real app this would be a session cookie
    set at login time after authentication.
    """
    username = request.cookies.get("user")
    if not username:
        username = "alice"

    if response is None:
        response = make_response()

    response.set_cookie("user", username, httponly=True, samesite="Lax")
    return response, username


def generate_csrf_token():
    token = session.get("csrf_token")
    if not token:
        token = secrets.token_urlsafe(16)
        session["csrf_token"] = token
    return token


# Make the token generator available in templates as csrf_token()
app.jinja_env.globals["csrf_token"] = generate_csrf_token


@app.route("/")
def index():
    username = request.cookies.get("user")
    if not username:
        # First visit: set cookie
        resp = make_response(
            render_template(
                "csrf_fixed_form.html",
                username="alice",
                balance=ACCOUNT["alice"]["balance"],
            )
        )
        resp.set_cookie("user", "alice", httponly=True, samesite="Lax")
        return resp

    return render_template(
        "csrf_fixed_form.html",
        username=username,
        balance=ACCOUNT[username]["balance"],
    )


@app.route("/transfer", methods=["POST"])
def transfer():
    # 1. Enforce cookie-based "auth" (simulated)
    username = request.cookies.get("user")
    if not username:
        return redirect(url_for("index"))

    # 2. Validate CSRF token
    form_token = request.form.get("csrf_token")
    session_token = session.get("csrf_token")

    if not session_token or not form_token or form_token != session_token:
        abort(400, description="Invalid CSRF token")

    # 3. Proceed with the state-changing action
    to_account = request.form.get("to_account", "attacker")
    amount_str = request.form.get("amount", "0")

    try:
        amount = int(amount_str)
    except ValueError:
        amount = 0

    if amount <= 0:
        return "Invalid amount", 400

    ACCOUNT[username]["balance"] -= amount

    return render_template(
        "transfer_success.html",
        username=username,
        to_account=to_account,
        amount=amount,
        balance=ACCOUNT[username]["balance"],
        mode="fixed",
    )


if __name__ == "__main__":
    app.run(debug=True, port=5003)
# Note: This code is for educational purposes only. In a production environment,
# use established libraries and frameworks to handle CSRF protection.