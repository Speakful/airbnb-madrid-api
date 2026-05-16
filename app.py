from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)
model = joblib.load('model/model.pkl')

@app.route('/health', methods = ['GET'])
def health():
    return jsonify({'status': 'ok', 'model': 'loaded'})

@app.route('/predict/<neighbourhood>', methods = ['GET'])
def predict_by_neighbourhood(neighbourhood):
    return jsonify({'neighbourhood': neighbourhood, 'message': 'Use POST /predict for full prediction'})

@app.route('/listings', methods = ['GET'])
def listings():
    room_type = request.args.get('room_type', 'all')
    return jsonify({'room_type': room_type, 'message': f'Listings filtered by room_type: {room_type}'})

@app.route('/predict', methods = ['POST'])
def predict():
    data = request.get_json()
    
    input_df = pd.DataFrame([data])
    input_encoded = pd.get_dummies(input_df)
    
    # align columns with training data
    model_columns = model.feature_names_in_
    input_encoded = input_encoded.reindex(columns = model_columns, fill_value = 0)
    
    prediction = model.predict(input_encoded)
    
    return jsonify({'predicted_price': round(float(prediction[0]), 2)})

if __name__ == '__main__':
    app.run(debug = True)