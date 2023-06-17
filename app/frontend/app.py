from flask import Flask, request, render_template
import requests

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # The user has submitted the form. Send a request to the backend
        # to perform the simulation.

        # Extract the form data. This could be parameters for the simulation.
        form_data = request.form

        # Send a request to the backend to perform the simulation.
        # For simplicity, let's not send any data to the backend.
        response = requests.post("http://backend:5000/simulate", json={})

        # Extract the result of the simulation from the response.
        result = response.json()["result"]

        # Render the result page.
        return render_template("result.html", result=result)

    # Render the form page.
    return render_template("form.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
