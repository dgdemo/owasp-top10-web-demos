from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory “database”
comments = []

@app.route("/", methods=["GET", "POST"])
def index():
    mode = request.args.get("mode", "vuln")  # "vuln" or "fixed"

    if request.method == "POST":
        text = request.form.get("comment", "")
        comments.append(text)
        return redirect(url_for("index", mode=mode))

    # Pick the template version
    if mode == "fixed":
        template_name = "index_fixed.html"
    else:
        template_name = "index_vuln.html"

    return render_template(template_name, comments=comments, mode=mode)


if __name__ == "__main__":
    app.run(debug=True)
