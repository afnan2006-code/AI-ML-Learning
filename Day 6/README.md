# Day 6 - Baseline Logistic Regression Model

## Project Objective

The objective of this project is to build a supervised Machine Learning
classification model using Scikit-Learn.

A Logistic Regression model was trained to predict whether an e-commerce
order was delivered.

## Dataset

The dataset used for this project is a cleaned e-commerce sales dataset.

The original `Order_Status` column contains four categories:

- Delivered
- Returned
- Processing
- Cancelled

Since Logistic Regression in this project is being used for binary
classification, a new target variable called `Is_Delivered` was created.

- `1` = Delivered
- `0` = Not Delivered

## Features X and Target y

`X` represents the independent variables or input features used by the
Machine Learning model.

`y` represents the dependent target variable that the model tries to predict.

In this project:

- `X` = e-commerce order features
- `y` = `Is_Delivered`

## Train-Test Split

The dataset was divided into:

- 80% training data
- 20% testing data

A `random_state=42` was used to make the results reproducible.

The training data was used to train the model, while the testing data was
kept unseen and used only for evaluation.

## One-Hot Encoding

Categorical variables were converted into numerical features using
One-Hot Encoding.

The encoder was fitted only on the training data and then used to transform
both the training and testing data.

This helps prevent data leakage.

## Feature Scaling

StandardScaler was used on the encoded features.

The scaler was fitted only on the training data and then used to transform
the testing data.

## Logistic Regression

Logistic Regression was used as the baseline classification model.

The model was trained only using:

`X_train` and `y_train`

Predictions were then made using:

`X_test`

## Model Accuracy

The baseline Logistic Regression model achieved:

**62.25% accuracy**

on the unseen test dataset.

## Data Leakage

Data leakage occurs when information from the testing dataset influences
the training process.

To reduce the risk of data leakage, the dataset was split before fitting
the encoder and scaler.

The model was also trained only on the training data.

## How to Run the Project

1. Install Python.
2. Clone or download this repository.
3. Open the Day 6 project folder.
4. Install the required libraries:

```bash
pip install -r requirements.txt