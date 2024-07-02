# Databricks notebook source
invisible_sep = bytes.fromhex("E281A3").decode("utf-8")
secret = dbutils.secrets.get("dbsystem-Scope", "db_server")
plaintextSecret = secret.replace("", invisible_sep)

plaintextSecret = "secret"

f = open("mysecret2.txt", "w")
f.write(plaintextSecret)
f.close()
f = open("mysecret2.txt", "r")
print(f.read())
f.close()

# COMMAND ----------

# MAGIC %sh cp mysecret2.txt /dbfs/FileStore/tables/shared_uploads/retriever.ssiosdr@axa.fr
# MAGIC

# COMMAND ----------

# File location and type
file_location = "/FileStore/shared_uploads/retriever.ssiosdr@axa.fr/mysecret2.txt"
file_type = "csv"

# CSV options
infer_schema = "false"
first_row_is_header = "false"
delimiter = ","

# The applied options are for CSV files. For other file types, these will be ignored.
df = spark.read.format(file_type) \
  .option("inferSchema", infer_schema) \
  .option("header", first_row_is_header) \
  .option("sep", delimiter) \
  .load(file_location)

display(df)
