from fastapi import FastAPI
import joblib

# Load the trained machine learning model
model = joblib.load("production_rf_model.pkl")

# Create FastAPI application
app = FastAPI(title="ML Model API")


@app.get("/health-check")
def health_check():
    return {"status": "API is live"}


@app.post("/predict")
def predict(data: dict):
    print("Incoming JSON payload:", data)
    return {"message": "Prediction endpoint received the payload"}
