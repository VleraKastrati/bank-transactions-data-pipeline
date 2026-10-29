# Bank Transactions Data Pipeline

## Project Overview

This project demonstrates an end-to-end data pipeline built using Databricks, PySpark, Delta Lake, and SQL. It processes sample bank transaction data through Bronze, Silver, and Gold layers and uses Databricks Jobs to orchestrate the workflow.

## Architecture

**Raw Data → Bronze → Silver → Gold → SQL Analysis**

- **Bronze Layer:** Stores raw bank transaction data in a Delta table.
- **Silver Layer:** Cleans and validates transactions by checking null values and ensuring transaction amounts are positive.
- **Gold Layer:** Aggregates transactions by transaction type and calculates the number and total amount of transactions.
- **SQL Analysis:** Uses SQL queries to explore and analyze the Gold results.
- **Job Orchestration:** Runs four dependent tasks in sequence using Databricks Jobs.

## Technologies Used

- Databricks
- PySpark
- Delta Lake
- SQL
- Databricks Jobs
- GitHub

## Project Notebooks

1. `01_generate_bank_data` — Generates sample transaction data.
2. `02_bronze_transactions` — Creates the Bronze Delta table.
3. `03_silver_transactions` — Cleans and validates the data.
4. `04_gold_transactions` — Creates transaction summary metrics.
5. `05_sql_analysis` — Runs SQL analysis queries.

## Screenshots

### Gold Layer Results

![Gold Layer](screenshots/gold_layer.png)

### SQL Analysis

![SQL Analysis](screenshots/sql_analysis.png)

### Job Orchestration

![Successful Job Graph](screenshots/job_success_graph.png)

## Outcome

The project demonstrates data ingestion, data quality validation, Delta table creation, business aggregations, SQL analysis, and task orchestration in Databricks.
