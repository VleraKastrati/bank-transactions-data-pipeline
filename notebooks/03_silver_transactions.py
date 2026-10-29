# Databricks notebook source
from pyspark.sql.functions import col
bronze_df = spark.table("bronze_transactions")

display(bronze_df)

# COMMAND ----------

silver_df = bronze_df.filter(
    col("amount").isNotNull() &
    (col("amount") > 0) &
    col("transaction_id").isNotNull() &
    col("customer_id").isNotNull()
)

display(silver_df)

# COMMAND ----------

silver_df.write.format("delta").mode("overwrite").saveAsTable("silver_transactions")

print("Bronze rows:", bronze_df.count())
print("Silver rows:", silver_df.count())

# COMMAND ----------

