🏠 Airbnb Madrid — Price Predictor API
A Flask REST API that predicts Airbnb nightly prices in Madrid using a Random Forest Regressor trained on Inside Airbnb data.

👥 Team

Edu
Ariela


🤖 Model

Algorithm: Random Forest Regressor (sklearn)
Dataset: Inside Airbnb — Madrid (detailed listings)
Features: neighbourhood, room type, accommodates, bathrooms, bedrooms, beds, minimum nights, number of reviews, review scores rating, availability
R² Score: 0.61 | MAE: €27 | RMSE: €37


🚀 API Endpoints
MethodRouteTypeDescriptionGET/health—Returns API status and model load confirmationGET/predict/<neighbourhood>Path paramQuick price estimate for a given neighbourhoodGET/listings?room_type=entireQuery paramReturns listings filtered by room typePOST/predictJSON bodyFull price prediction using all features

📨 Example Request
bashPOST /predict
Content-Type: application/json

{
  "neighbourhood_cleansed": "Embajadores",
  "room_type": "Entire home/apt",
  "accommodates": 2,
  "bathrooms": 1,
  "bedrooms": 1,
  "beds": 1,
  "minimum_nights": 2,
  "number_of_reviews": 45,
  "review_scores_rating": 4.8,
  "availability_365": 180
}
📨 Example Response
json{
  "predicted_price": 116.11
}

🛠️ Run Locally

Clone the repository

bashgit clone https://github.com/Speakful/airbnb-madrid-api.git
cd airbnb-madrid-api

Install dependencies

bashpip install -r requirements.txt

Run the app

bashpython app.py

API will be available at http://127.0.0.1:5000


☁️ Deployment
Deployed on Render and AWS EC2.

Render: https://online-ds-bridge-proyects-arielaastorga.onrender.com
AWS: http://13.60.90.39


🧰 Tech Stack

Python
Flask
scikit-learn
pandas
joblib
gunicorn
Render / AWS EC2