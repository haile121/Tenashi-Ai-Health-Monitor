# Flask API exposing endpoints for current metrics and anomaly detection
from flask import Flask, jsonify, request
from flask_cors import CORS

from model import train_model, load_model, predict_anomaly
from data_simulator import generate_dataframe, generate_sample

app = Flask(__name__)
CORS(app)

# Try to load model, otherwise train new model
model = load_model()
if model is None:
    seed_df = generate_dataframe(300)     # Simulated training dataset
    model = train_model(seed_df)          # Train new model


@app.route("/api/metrics", methods=["GET"])
def get_metrics():
    sample = generate_sample()     # Create 1 simulated reading
    is_anom = predict_anomaly(
        model,
        sample["heart_rate"],
        sample["blood_oxygen"]
    )
    sample["anomaly"] = is_anom
    return jsonify(sample)


@app.route("/api/score", methods=["POST"])
def score():
    data = request.get_json()
    hr = data.get("heart_rate")
    spo2 = data.get("blood_oxygen")

    if hr is None or spo2 is None:
        return jsonify({"error": "missing fields"}), 400

    result = predict_anomaly(model, hr, spo2)
    return jsonify({"anomaly": result})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
