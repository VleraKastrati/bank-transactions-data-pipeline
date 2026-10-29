# Databricks notebook source
df = spark.table("bronze_transactions")
display(df)

# COMMAND ----------

print("Total transactions:", df.count())

df.printSchema()