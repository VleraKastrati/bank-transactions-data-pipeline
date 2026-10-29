# Databricks notebook source
silver_df = spark.table("silver_transactions")

display(silver_df)

# COMMAND ----------

from pyspark.sql.functions import sum, count

gold_df = silver_df.groupBy("transaction_type").agg(
    count("*").alias("total_transactions"),
    sum("amount").alias("total_amount")
)

display(gold_df)

# COMMAND ----------

gold_df.write.format("delta").mode("overwrite").saveAsTable(
    "gold_transaction_summary"
)

# COMMAND ----------

display(spark.table("gold_transaction_summary"))

# COMMAND ----------

