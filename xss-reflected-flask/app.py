from flask import Flask, request, render_template

app = Flask(__name__)


@app.get("/")
def index():
    # Landing page linking to vuln + fixed views
    return render_template("base.html")


@app.get("/search-vuln")
def search_vuln():
    # Vulnerable: echoes query back using |safe in template
    query = request.args.get("q", "")
    return render_template("search_vuln.html", query=query)


@app.get("/search-fixed")
def search_fixed():
    # Fixed: relies on Jinja2's autoescaping, no |safe
    query = request.args.get("q", "")
    return render_template("search_fixed.html", query=query)


if __name__ == "__main__":
    app.run(debug=True)
