import xgboost
import pickle
from flask import Flask, request, app, jsonify, render_template
import pandas as pd
import time
import os
import logging

# ---------------------
# Logging Setup
# ---------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ---------------------
# Load the model
# ---------------------
MODEL_PATH = os.path.join("model", "model.pkl")

try:
    model = pickle.load(open(MODEL_PATH, 'rb'))
    logger.info(f"✅ Model loaded from {MODEL_PATH}")
except Exception as e:
    logger.error(f"❌ Failed to load model: {e}")
    raise

# ---------------------
# Flask Setup
# ---------------------
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html") 

@app.route('/health', methods=['GET'])
def health():
    return jsonify(status="ok"), 200

@app.route('/predict', methods=['POST'])
def predict_api():
    start_time = time.time()
    data = request.get_json()
    logger.info(f"Received input: {data}")

    # Convert  input data to expected format
    input_data = pd.DataFrame([data])
    # Extract features in expected order
    feature_extract = input_data[[
            "person_age",
            "person_income",
            "loan_amnt",
            "loan_int_rate",
            "loan_percent_income",
            "credit_score",
            "previous_loan_defaults_on_file"
        ]]

    # Predict and return result
    prediction = model.predict(feature_extract)[0]
    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(feature_extract)[0].tolist()
    else:
        probabilities = []

    latency = time.time() - start_time
    return jsonify({
            "prediction": int(prediction),
            "probabilities": probabilities,
            "latency": latency
        })

# ---------------------
# Run the App
# ---------------------
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
