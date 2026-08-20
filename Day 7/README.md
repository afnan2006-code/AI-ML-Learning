# Day 7 - Random Forest Classifier

## Project Objective

The objective of Day 7 was to build a Random Forest Classifier and compare its performance with the baseline model developed previously.

The project focuses on ensemble learning and advanced classification evaluation metrics rather than relying on Accuracy alone.

## Model Configuration

The Random Forest Classifier was initialized with:

- `n_estimators = 100`
- `random_state = 42`

The existing Day 6 training and testing split was reused for this experiment.

## Methodology

The following workflow was performed:

1. Reused the existing `X_train`, `X_test`, `y_train`, and `y_test` datasets from Day 6.
2. Encoded categorical input features so they could be used by the Random Forest model.
3. Initialized a `RandomForestClassifier`.
4. Trained the model using only the training dataset.
5. Generated predictions on the unseen testing dataset.
6. Evaluated the model using:
   - Accuracy
   - Precision
   - Recall
   - F1-Score
7. Generated a Classification Report.
8. Generated and displayed a Confusion Matrix.
9. Compared Random Forest performance with the previous baseline model.
10. Saved the trained model using Joblib.

## Random Forest

Random Forest is an ensemble learning algorithm that combines multiple Decision Trees to produce predictions.

Instead of relying on a single Decision Tree, Random Forest combines many trees. This ensemble approach can provide more robust predictions and can model nonlinear relationships in tabular datasets.

In this project, 100 Decision Trees were used.

## Evaluation Metrics

Accuracy measures the overall proportion of correct predictions.

Precision measures how many predicted class instances were actually correct.

Recall measures how many actual class instances were correctly identified.

F1-Score combines Precision and Recall using their harmonic mean:

`F1 = 2 × (Precision × Recall) / (Precision + Recall)`

F1-Score was emphasized because Accuracy alone may not fully represent classification performance, especially when the class distribution is imbalanced.

## Random Forest Results

The Random Forest model achieved the following results on the testing dataset:

| Metric | Score |
|---|---:|
| Accuracy | 60.85% |
| Precision | 52.48% |
| Recall | 60.85% |
| F1-Score | 50.94% |

## Confusion Matrix

The Random Forest confusion matrix was:

```text
[[  46, 699],
 [  84, 1171]]