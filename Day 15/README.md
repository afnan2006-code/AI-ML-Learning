# Day 15 — ML Model Deployment with FastAPI

## Project Overview

This project demonstrates how to move a trained machine learning model from a notebook environment into a production-style REST API using FastAPI.

The trained Random Forest model from Week 2 is serialized as a `.pkl` file and loaded into the FastAPI application.

## Project Structure

- main.py — FastAPI application
- production_rf_model.pkl — Serialized trained ML model
- requirements.txt — Python dependencies
- README.md — Project documentation

## API Endpoints

### Health Check

GET /health-check

Returns:

{
  "status": "API is live"
}

### Prediction

POST /predict

Currently accepts a JSON payload and prints it to the terminal. Actual prediction logic will be implemented in the next stage.

Example:

{
  "test": "hello"
}

## Running the API

Install dependencies:

pip install -r requirements.txt

Start the API:

uvicorn main:app --reload

Swagger documentation:

http://127.0.0.1:8000/docs

## Pickle Security Note

Pickle/joblib model files should only be loaded from trusted sources because deserialization of untrusted files can execute arbitrary code.

## Day 15 Learning Outcomes

- Model serialization and persistence
- Loading a trained .pkl model
- FastAPI application structure
- REST API endpoints
- JSON request handling
- Swagger API documentation
- Local virtual environment isolation
