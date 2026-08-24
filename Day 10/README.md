# Day 10 — Loan Classification with SMOTE

## 📌 Project OverviewGet

This project focuses on building a **Random Forest Classification model** for loan classification and handling class imbalance using **SMOTE (Synthetic Minority Over-sampling Technique)**.

The objective is to develop a reliable classification workflow that includes data preprocessing, class-imbalance handling, model training, evaluation, feature-importance analysis, and production model saving.

---

## 🎯 Objectives

* Identify class imbalance in the dataset.
* Separate numerical and categorical features.
* Preprocess numerical and categorical data.
* Apply SMOTE to the training data.
* Train a Random Forest Classifier.
* Evaluate the model using multiple classification metrics.
* Analyze feature importance.
* Identify the Top 10 important features.
* Save the trained production model.
* Save the preprocessing pipeline for future predictions.

---

## 📊 Dataset Features

### Numerical Features

* Age
* Income
* LoanAmount
* CreditScore
* MonthsEmployed
* NumCreditLines
* InterestRate
* LoanTerm
* DTIRatio

### Categorical Features

* Education
* EmploymentType
* MaritalStatus
* HasMortgage
* HasDependents
* LoanPurpose
* HasCoSigner

After preprocessing, the dataset contained **31 features**.

---

## ⚙️ Machine Learning Workflow

```text
Dataset
   ↓
Train/Test Split
   ↓
Feature Identification
   ↓
Numerical Feature Scaling
   ↓
Categorical Feature Encoding
   ↓
SMOTE on Training Data
   ↓
Random Forest Classifier
   ↓
Model Prediction
   ↓
Model Evaluation
   ↓
Feature Importance Analysis
   ↓
Production Model Saving
```

---

## 🔄 Data Preprocessing

Numerical features were standardized using **StandardScaler**.

Categorical features were converted into numerical representations using **OneHotEncoder** with:

```python
OneHotEncoder(handle_unknown='ignore')
```

A **ColumnTransformer** was used to apply the appropriate preprocessing to numerical and categorical features.

The preprocessing pipeline was fitted only on the training data and then applied to the test data.

---

## ⚖️ Handling Class Imbalance with SMOTE

The training target distribution was examined to identify class imbalance.

SMOTE was applied **only to the training data**:

```python
smote = SMOTE(random_state=42)

X_train_smote, y_train_smote = smote.fit_resample(
    X_train_processed,
    y_train
)
```

The test data was not oversampled.

This approach helps avoid data leakage and ensures that the final evaluation is performed on unseen test data.

---

## 🌲 Random Forest Classifier

A Random Forest Classifier was trained using the SMOTE-balanced training dataset.

```python
RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    min_samples_split=2,
    random_state=42,
    n_jobs=-1
)
```

The trained model was then evaluated on the original processed test dataset.

---

## 📈 Model Evaluation

The model was evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* Classification Report
* Confusion Matrix

### Final Results

Replace the following values with the **actual results from the notebook**:

| Metric    |            Score |
| --------- | ---------------: |
| Accuracy  |  `YOUR_ACCURACY` |
| Precision | `YOUR_PRECISION` |
| Recall    |    `YOUR_RECALL` |
| F1 Score  |  `YOUR_F1_SCORE` |

---

## 🔍 Feature Importance

Random Forest feature importance was used to identify the features that contributed most to the model's predictions.

The model produced **31 processed features**, and the Top 10 features were extracted based on their importance scores.

Feature importance provides insight into which variables the model relied on most when making predictions.

> Feature importance indicates predictive contribution within the trained model and should not be interpreted as proof of a causal relationship.

---

## 💼 Business Interpretation

The feature-importance analysis can help identify characteristics that are particularly useful for loan classification.

Important factors may include:

* Creditworthiness
* Income and repayment capacity
* Loan amount
* Debt burden
* Employment stability
* Existing credit exposure
* Interest rate
* Loan duration

These insights can support data-driven risk assessment and help financial institutions better understand patterns in loan applications.

However, machine learning predictions should be treated as **decision-support information** rather than the sole basis for financial decisions.

---

## 💾 Production Model

The following production files were successfully created:

```text
production_rf_model.pkl
preprocessor.pkl
```

### `production_rf_model.pkl`

Contains the trained Random Forest classification model.

### `preprocessor.pkl`

Contains the preprocessing pipeline used to transform numerical and categorical features.

Both files are required to reproduce the same preprocessing and prediction workflow on future data.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Imbalanced-learn
* Matplotlib
* Joblib
* Jupyter Notebook

---

## 📁 Project Structure

```text
Day 10/
│
├── Day_10_SMOTE.ipynb
├── production_rf_model.pkl
├── preprocessor.pkl
├── README.md
└── requirements.txt
```

---

## 📚 Key Learning Outcomes

Through this project, I learned:

* How to identify class imbalance.
* How SMOTE balances minority classes.
* Why SMOTE should only be applied to training data.
* How to preprocess numerical and categorical features.
* How to train a Random Forest classifier.
* How to evaluate classification models using multiple metrics.
* How to analyze feature importance.
* How to save a trained machine learning model.
* How to save and reuse a preprocessing pipeline.
* How to prepare a machine learning model for production use.

---

## ✅ Conclusion

This project demonstrates a complete machine learning classification workflow for loan prediction.

The workflow covers data preprocessing, class-imbalance handling with SMOTE, Random Forest training, model evaluation, feature-importance analysis, and production model serialization.

The final **Random Forest model** and **preprocessing pipeline** were successfully saved for future predictions.
