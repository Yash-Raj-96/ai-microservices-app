from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

PREDICTION_SERVICE_URL = 'http://prediction-service:5000/predict'

@app.route('/process', methods=['POST'])
def process():
    data = request.json['data']
    # Perform preprocessing (e.g., scaling, normalization)
    processed_data = preprocess(data)
    
    # Forward to Prediction Service
    response = requests.post(PREDICTION_SERVICE_URL, json={'data': processed_data})
    return response.json()

def preprocess(data):
    # Add your preprocessing logic here
    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
