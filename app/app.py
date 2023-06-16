from flask import Flask, render_template, request, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Used to keep the session


@app.route("/", methods=["GET", "POST"])
def index():
    if "number" not in session:
        session["number"] = 0

    if request.method == "POST":
        session["number"] += 1
    return render_template("index.html", number=session["number"])


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
