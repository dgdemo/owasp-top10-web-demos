from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)
app.secret_key = "dev-only-secret-key"  # for session handling if you add it later

# Super simple in-memory "account"
ACCOUNT = {
    "alice": {"balance": 1000}
}


@app.route("/")
def index():
    """
    Simulate a logged-in user (alice) via cookie.
    In a real app, the user would have logged in earlier.
    """
    username = request.cookies.get("user", "alice")

    # If cookie not set yet, set it.
    if not request.cookies.get("user"):
        resp = make_response(
            render_template(
                "csrf_vuln_form.html",
                username=username,
                balance=ACCOUNT[username]["balance"],
            )
        )
        resp.set_cookie("user", username)  # vulnerable: cookie-based session
        return resp

    return render_template(
        "csrf_vuln_form.html",
        username=username,
        balance=ACCOUNT[username]["balance"],
    )


@app.route("/transfer", methods=["POST"])
def transfer():
    """
    Vulnerable endpoint:
    - Relies on cookie-based "user" to identify the account
    - Performs state-changing action with NO CSRF protection
    """
    username = request.cookies.get("user", "alice")
    to_account = request.form.get("to_account", "attacker")
    amount_str = request.form.get("amount", "0")

    try:
        amount = int(amount_str)
    except ValueError:
        amount = 0

    if amount <= 0:
        return "Invalid amount", 400

    # Deduct from user balance
    ACCOUNT[username]["balance"] -= amount

    return render_template(
        "transfer_success.html",
        username=username,
        to_account=to_account,
        amount=amount,
        balance=ACCOUNT[username]["balance"],
        mode="vuln",
    )


if __name__ == "__main__":
    # Run on a slightly different port if you like, to keep demos isolated
    app.run(debug=True, port=5002)
