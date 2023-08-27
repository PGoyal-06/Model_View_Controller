from flask import Flask, jsonify, request
from classifier import get_predictions

app = Flask(__name__)

@app.route("/predict-alphabet", methods=["POST"])

def predict_data():
    image = request.files.get("alphabet")
    prediction = get_predictions(image)
    return jsonify({
        "prediction": prediction
    },200)