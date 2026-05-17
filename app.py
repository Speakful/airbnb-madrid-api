<<<<<<< HEAD
# Importamos pickle para poder cargar el archivo model.pkl
import pickle

# Importamos Flask para crear la API,
# jsonify para devolver respuestas en formato JSON,
# y request para leer datos que envía el usuario
from flask import Flask, jsonify, request
=======
# Flask API with 4 endpoints:

from flask import Flask, request, jsonify
import joblib
import numpy as np
>>>>>>> 242027fbafe57f5db4a552099bdf789bf2434148
import pandas as pd

# Creamos la aplicación Flask
# __name__ le indica a Flask dónde está el archivo principal
app = Flask(__name__)

<<<<<<< HEAD
# Esto activa el modo debug, muestra errores más detallados cuando estoy programando
app.config["DEBUG"] = False

#app.config["DEBUG"] = True


# Cargamos el "modelo" al iniciar la aplicación
# Esto hace que el modelo se lea una sola vez al arrancar la API
# y no en cada petición
with open("model.pkl", "rb") as f:
    model = pickle.load(f)


FEATURES = [
    "neighbourhood_cleansed",
    "room_type",
    "accommodates",
    "bathrooms",
    "bedrooms",
    "beds",
    "price",
    "minimum_nights",
    "number_of_reviews",
    "review_scores_rating",
    "availability_365"
]

# Ruta principal de la API
# Se ejecuta cuando alguien entra a la URL raíz "/"
# En la terminal bash:   http://localhost:5000/
# En render:  https://tu-api.onrender.com/

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "API Flask para prediccion de apartamentos",
        "endpoints": ["/health", "/predict_query", "/predict"]
    })


# Para comprobar rápidamente si la API está funcionando
# Sólo significa que el proceso Flask está vivo y puede responder una petición HTTP en esa ruta
@app.route("/health", methods=["GET"])
=======
# 1) /health (GET) — checks the API is running and the model is loaded
@app.route('/health', methods = ['GET'])
>>>>>>> 242027fbafe57f5db4a552099bdf789bf2434148
def health():
    return jsonify({
        "status": "ok",
        "service": "running"
    })

<<<<<<< HEAD

# Ruta con parámetro en el path, para recibir por ejemplo el nombre de un barrio
# Ejemplo: /neighbourhood/Sol
# El valor "Sol" se guarda en la variable name

# @pie sintax
# Es un decorado de una función o un objeto, se utiliza para modificar su comportamiento
@app.route("/neighbourhood/<string:name>", methods=["GET"])
def get_neighbourhood(name):
    return jsonify({
        "neighbourhood_cleansed": name,
        "message": f"Barrio recibido correctamente: {name}"
    })


# RUTA CON PARÁMETROS DE LA QUERY PARA USAR LA FUNCIÓN DE PREDICCIÓN
# Recibe los datos que necesita el modelo para hacer las predicciones
# Variables del modelo:
'''
'neighbourhood_cleansed', 
'room_type', 
'accommodates',
'bathrooms', 
'bedrooms', 
'beds', 
'price',
'minimum_nights', 
'number_of_reviews',
 'review_scores_rating', 
 'availability_365'

variable objetivo: price 
'''

def build_input(data_source):
    return {
        "neighbourhood_cleansed": data_source.get("neighbourhood_cleansed"),
        "room_type": data_source.get("room_type"),
        "accommodates": float(data_source.get("accommodates")),
        "bathrooms": float(data_source.get("bathrooms")),
        "bedrooms": float(data_source.get("bedrooms")),
        "beds": float(data_source.get("beds")),
        "price": float(data_source.get("price")),
        "minimum_nights": float(data_source.get("minimum_nights")),
        "number_of_reviews": float(data_source.get("number_of_reviews")),
        "review_scores_rating": float(data_source.get("review_scores_rating")),
        "availability_365": float(data_source.get("availability_365"))
    }


# PREDICCION DE RESULTADOS
# /predict_query?neighbourhood=Sol&room_type=Entire%20home/apt&minimum_nights=5...
@app.route("/predict_query", methods=["GET"])
def predict_query():
    try:
        input_data = build_input(request.args)
        df = pd.DataFrame([input_data], columns=FEATURES)
        prediction = model.predict(df)[0]

        return jsonify({
            "predicted_price": float(prediction),
            "input": input_data
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/predict", methods=["POST"])
=======
# 2) /predict/<neighbourhood> (GET) — path parameter endpoint, redirects to POST for full prediction
@app.route('/predict/<neighbourhood>', methods = ['GET'])
def predict_by_neighbourhood(neighbourhood):
    return jsonify({'neighbourhood': neighbourhood, 'message': 'Use POST /predict for full prediction'})

# 3) /listings (GET) — query parameter endpoint, filters listings by room type
@app.route('/listings', methods = ['GET'])
def listings():
    room_type = request.args.get('room_type', 'all')
    return jsonify({'room_type': room_type, 'message': f'Listings filtered by room_type: {room_type}'})

# 4) /predict (POST) — main endpoint: receives listing data as JSON, encodes it,
#                   aligns it with the training columns and returns a predicted nightly price
@app.route('/predict', methods = ['POST'])
>>>>>>> 242027fbafe57f5db4a552099bdf789bf2434148
def predict():
    try:
        data = request.get_json()
        input_data = build_input(data)
        df = pd.DataFrame([input_data], columns=FEATURES)
        prediction = model.predict(df)[0]

        return jsonify({
            "predicted_price": float(prediction),
            "input": input_data
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400



# Manejador de error 404
# Se activa cuando el usuario entra en una ruta que no existe
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "error": "Ruta no encontrada"
    }), 404


# Manejador de error 500
# Se activa cuando ocurre un error interno en el servidor
@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        "error": "Error interno del servidor"
    }), 500

