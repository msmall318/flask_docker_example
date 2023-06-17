# from flask import Flask, request, jsonify
# from simulation import run_simulation

# app = Flask(__name__)


# @app.route("/simulate", methods=["POST"])
# def simulate():
#     config = request.json  # Assuming the config is sent as JSON in the request body
#     result = run_simulation(config)
#     return jsonify(result)


# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0", port=5000)

from flask import Flask, request, jsonify
from simulation import run_simulation

app = Flask(__name__)


@app.route("/simulate", methods=["POST"])
def simulate():
    config = request.json  # Assuming the config is sent as JSON in the request body
    result = run_simulation(config)
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
