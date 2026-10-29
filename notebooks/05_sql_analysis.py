# Databricks notebook source
# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM gold_transaction_summary;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC transaction_type,
# MAGIC total_transactions,
# MAGIC total_amount
# MAGIC FROM gold_transaction_summary
# MAGIC ORDER BY total_amount DESC;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM gold_transaction_summary
# MAGIC WHERE total_amount > 500;

# COMMAND ----------

