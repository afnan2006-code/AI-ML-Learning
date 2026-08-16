# E-Commerce Sales — Exploratory Data Analysis

## Project Overview

This project performs Exploratory Data Analysis (EDA) on an e-commerce
sales dataset containing 10,000 records and 26 columns.

The main objective is to clean the dataset, explore its structure,
analyze statistical patterns, visualize important relationships, and
extract meaningful business insights.

## Objectives

- Load and inspect the raw dataset
- Check and handle missing values
- Detect and remove duplicate records
- Check and correct data types
- Perform statistical analysis
- Analyze numerical feature distributions
- Create a correlation heatmap
- Analyze revenue, profit, customers, regions, and order statuses
- Extract meaningful business insights
- Export the cleaned dataset

## Dataset

The dataset contains e-commerce sales information including:

- Order information
- Customer information
- Product categories
- Pricing and quantity
- Discounts
- Revenue
- Cost
- Profit
- Shipping information
- Payment methods
- Order status

The dataset contains **10,000 records and 26 columns**.

## Data Cleaning

The following checks were performed:

- Missing values were checked
- Duplicate records were checked
- Data types were inspected
- The `Order_Date` column was converted to datetime format
- The cleaned dataset was exported as:

`cleaned_ecommerce_sales.csv`

## Exploratory Data Analysis

The following visualizations and analyses were performed:

1. Revenue by Category
2. Profit by Region
3. Revenue by Customer Segment
4. Yearly Revenue
5. Order Status Distribution
6. Discount vs Profit
7. Distribution plots for important numerical features
8. Correlation Heatmap

## Key Findings

### 1. Category Performance

Electronics generated the highest total revenue at approximately
3.38 million, making it the strongest revenue-generating category.

### 2. Regional Profitability

The Middle East generated the highest total profit among the analyzed
regions, followed by North America, Asia, and Europe.

### 3. Customer Segment Revenue

The Regular customer segment generated the highest total revenue,
while the VIP segment generated the lowest revenue.

### 4. Yearly Revenue

Revenue increased from 506,060.36 in 2021 to 2,308,640.02 in 2023,
which was the strongest revenue-performing year. Revenue then declined
to 1,147,842.31 in 2024.

### 5. Order Status

Delivered orders represented the largest portion of orders in the
dataset. Returned orders were the second most common status, while
Processing and Cancelled orders occurred less frequently.

### 6. Discount and Profit

The correlation between Discount and Profit was approximately -0.25,
indicating a weak-to-moderate negative relationship. Higher discounts
are generally associated with lower profit, although correlation does
not imply causation.

## Conclusion

The EDA provided useful insights into the business performance of the
e-commerce dataset. Electronics was the strongest revenue-generating
category, the Middle East recorded the highest regional profit, and
2023 was the strongest revenue-performing year.

The analysis also showed that Regular customers contributed the most
revenue and that most orders were successfully delivered. The negative
relationship between discount and profit suggests that discount
strategies should be monitored carefully to maintain profitability.

Overall, the project demonstrates how data cleaning, statistical
analysis, and visualization can be used to discover meaningful business
patterns and support data-driven decision-making.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy
- Jupyter Notebook
