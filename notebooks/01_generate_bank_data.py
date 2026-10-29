# Databricks notebook source
from pyspark.sql import SparkSession
from datetime import date, timedelta
import random

random.seed(42)
print("Bank Data Pipeline - Starting...")

# COMMAND ----------

transactions = [
    (1, 101, "Deposit", 500.00, "2026-01-01"),
    (2, 102, "Payment", 35.50, "2026-01-01"),
    (3, 101, "Withdrawal", 100.00, "2026-01-02"),
    (4, 103, "Payment", 75.00, "2026-01-02"),
    (5, 102, "Deposit", 200.00, "2026-01-03")
]

columns = [
    "transaction_id",
    "customer_id",
    "transaction_type",
    "amount",
    "transaction_date"
]

print("Number of transactions:", len(transactions))

# COMMAND ----------

df = spark.createDataFrame(transactions, columns)
display(df)

# COMMAND ----------

df.printSchema()

# COMMAND ----------

print(df.count())

# COMMAND ----------

display(df)

# COMMAND ----------

df.write.format("delta").mode("overwrite").saveAsTable("bronze_transactions")

# COMMAND ----------

display(spark.table("bronze_transactions"))

# COMMAND ----------

