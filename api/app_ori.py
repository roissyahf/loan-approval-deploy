import time
import logging
from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

# ---------------------
# Logging Setup
# ---------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ---------------------
# Load Model on Startup
# ---------------------
MODEL_PATH = os.path.join("model", "model.pkl")
try:
    model = joblib.load(MODEL_PATH)
    logger.info(f"✅ Model loaded from {MODEL_PATH}")
except Exception as e:
    logger.error(f"❌ Failed to load model: {e}")
    raise

# ---------------------
# Flask Setup
# ---------------------
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Welcome to the Loan Approval Prediction API!"), 200

@app.route('/health', methods=['GET'])
def health():
    return jsonify(status="ok"), 200

@app.route('/predict', methods=['POST'])
def predict():
    try:
        start_time = time.time()

        # Parse input
        data = request.get_json()
        logger.info(f"📦 Received input: {data}")

        # Extract features in expected order
        features = [
            data.get("person_age"),
            data.get("person_income"),
            data.get("loan_amnt"),
            data.get("loan_int_rate"),
            data.get("loan_percent_income"),
            data.get("credit_score"),
            data.get("previous_loan_defaults_on_file")
        ]

        features = np.array(features).reshape(1, -1)

        # Predict and return result
        prediction = model.predict(features)[0]
        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba(features)[0].tolist()
        else:
            probabilities = []

        latency = time.time() - start_time
        logger.info(f"✅ Prediction: {prediction} | Latency: {latency:.3f}s")

        return jsonify({
            "prediction": int(prediction),
            "probabilities": probabilities,
            "latency": latency
        })

    except Exception as e:
        logger.exception("❌ Prediction error")
        return jsonify({"error": str(e)}), 500

# ---------------------
# Run the App
# ---------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
    #app.run(host='127.0.0.1', port=8000, debug=True)