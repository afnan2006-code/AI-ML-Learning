# Day 9 - SMOTE and Feature Importance

## Objective

The objective of Day 9 was to handle class imbalance using SMOTE, retrain the optimized Random Forest model, analyze feature importance, and create a production-ready model.

## Tasks Completed

- Identified class imbalance in the Order_Status target.
- Applied SMOTE only to the training data.
- Retrained the optimized Random Forest classifier using the SMOTE-balanced dataset.
- Evaluated the model using accuracy, precision, recall, and F1-score.
- Compared model performance before and after SMOTE.
- Extracted Random Forest feature importance.
- Identified and visualized the Top 10 important features.
- Provided business interpretation of the important features.
- Saved the final production model as `production_rf_model.pkl`.

## Dataset

The project uses the cleaned e-commerce sales dataset:

`cleaned_ecommerce_sales.csv`

## Class Distribution

Before SMOTE, the training data contained an imbalanced target distribution:

- Delivered: 5018
- Returned: 1486
- Processing: 770
- Cancelled: 726

SMOTE was applied only to `X_train` and `y_train` to balance the training classes.

## Model

The model used is an optimized Random Forest Classifier.

The optimized parameters were obtained during Day 8 hyperparameter tuning.

## Feature Importance

Random Forest feature importance was used to identify the features that contributed most to the model's predictions.

The Top 10 features are visualized in the notebook.

## Production Model

The final trained model was saved as:

`production_rf_model.pkl`

## Files

- `Day_9_SMOTE.ipynb` - Complete Day 9 analysis
- `cleaned_ecommerce_sales.csv` - Cleaned dataset
- `random_forest_model.pkl` - Random Forest model
- `production_rf_model.pkl` - Final production model
- `README.md` - Project documentation
- `requirements.txt` - Required Python packages