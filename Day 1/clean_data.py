"""
Day 1 Internship Project
Data Cleaning using Pandas and NumPy

Objective:
- Load corrupted dataset
- Handle missing values
- Clean inconsistent data
- Handle outliers using IQR
- Export cleaned dataset
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==================================================
# Load Dataset
# ==================================================

df = pd.read_csv("corrupted_dataset.csv")

print("=" * 60)
print("DATASET LOADED SUCCESSFULLY")
print("=" * 60)

print("\nFirst 5 Rows:\n")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# ==================================================
# Remove Duplicate Rows
# ==================================================

df = df.drop_duplicates()

# ==================================================
# Clean Text Columns
# ==================================================

text_columns = ["Name", "Sex", "Ticket", "Cabin", "Embarked"]

existing_text = [c for c in text_columns if c in df.columns]

df[existing_text] = df[existing_text].apply(
    lambda col: col.astype(str)
    .str.strip()
    .str.replace(r"\s+", " ", regex=True)
)

# Standardize Gender
if "Sex" in df.columns:
    df["Sex"] = (
        df["Sex"]
        .str.lower()
        .replace(
            {
                "male": "Male",
                "female": "Female"
            }
        )
    )

# ==================================================
# Handle Missing Values
# ==================================================

if "Age" in df.columns:
    df["Age"] = df["Age"].fillna(df["Age"].median())

if "Fare" in df.columns:
    df["Fare"] = df["Fare"].fillna(df["Fare"].median())

if "Embarked" in df.columns:
    df["Embarked"] = df["Embarked"].fillna(
        df["Embarked"].mode()[0]
    )

if "Cabin" in df.columns:
    df["Cabin"] = df["Cabin"].fillna("Unknown")

# ==================================================
# Handle Outliers using IQR
# ==================================================

def clip_iqr(series):
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)

    iqr = q3 - q1

    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    return series.clip(lower, upper)

numeric_columns = [
    "Age",
    "Fare",
    "SibSp",
    "Parch"
]

existing_numeric = [
    c for c in numeric_columns
    if c in df.columns
]

df[existing_numeric] = df[existing_numeric].apply(clip_iqr)

# ==================================================
# Missing Values After Cleaning
# ==================================================

print("\nMissing Values After Cleaning:\n")
print(df.isnull().sum())

# ==================================================
# Save Clean Dataset
# ==================================================

df.to_csv("cleaned_dataset.csv", index=False)

print("\nCleaned dataset saved successfully.")

# ==================================================
# Visualization
# ==================================================

missing = df.isnull().sum()

plt.figure(figsize=(10, 5))
missing.plot(kind="bar")

plt.title("Missing Values After Cleaning")
plt.xlabel("Columns")
plt.ylabel("Missing Values")

plt.tight_layout()

plt.savefig("missing_values_after_cleaning.png")

print("Chart saved as missing_values_after_cleaning.png")

print("\nPROJECT COMPLETED SUCCESSFULLY")
