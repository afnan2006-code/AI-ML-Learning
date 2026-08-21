# Day 8 — Hyperparameter Tuning with GridSearchCV

## Objective

The objective of Day 8 was to optimize the Day 7 Random Forest Classifier using Hyperparameter Tuning and 5-Fold Cross-Validation.

The goal was to find a suitable balance between Bias and Variance while reducing the risk of overfitting.

## Techniques Used

- Random Forest Classifier
- GridSearchCV
- 5-Fold Cross-Validation
- Hyperparameter Optimization
- Confusion Matrix
- Classification Report
- Accuracy
- Precision
- Recall
- F1-Score

## Hyperparameter Grid

The following parameters were tested:

```python
param_grid = {
    "n_estimators": [50, 100, 150],
    "max_depth": [10, 20, 30],
    "min_samples_split": [2, 5]
}