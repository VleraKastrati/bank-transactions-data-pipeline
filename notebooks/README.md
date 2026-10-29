# Bank Transactions Data Pipeline

## Project Overview

This project demonstrates an end-to-end data pipeline built using Databricks, PySpark, Delta Lake, and SQL. It processes sample bank transaction data through Bronze, Silver, and Gold layers.

## Project Notebooks

### 1. 01_generate_bank_data.py
Generates sample bank transaction data, including transaction IDs, account IDs, transaction types, amounts, and transaction dates.

### 2. 02_bronze_transactions.py
Loads raw bank transaction data into a Spark DataFrame and stores it as a Delta table in the Bronze layer.

### 3. 03_silver_transactions.py
Cleans and validates bank transactions by checking null values and ensuring transaction amounts are positive. Stores the cleaned data in the Silver Delta table.

### 4. 04_gold_transactions.py
Aggregates cleaned transactions by transaction type, calculates transaction counts and total transaction amounts, and stores the results in the Gold layer.

### 5. 05_sql_analysis.py
Uses SQL queries to analyze the Gold transaction data, including transaction counts and total amounts by transaction type.

## Technologies Used

- Databricks
- PySpark
- Delta Lake
- SQL
- Databricks Jobs
- GitHub

## Architecture

Raw Data → Bronze → Silver → Gold → SQL Analysis

- **Bronze Layer:** Stores raw bank transaction data.
- **Silver Layer:** Cleans and validates transaction records.
- **Gold Layer:** Creates aggregated transaction metrics.
- **SQL Analysis:** Explores the Gold results using SQL queries.
- **Job Orchestration:** Runs dependent tasks in sequence using Databricks Jobs.

## Project Outcome

This project demonstrates data ingestion, data cleaning, data quality validation, Delta table creation, business aggregations, SQL analysis, and job orchestration in Databricks.
