# Databricks notebook source
invisible_sep = bytes.fromhex("E281A3").decode("utf-8")
secret = dbutils.secrets.get("dbsystem-Scope", "db_server")
plaintextSecret = secret.replace("", invisible_sep)
print(plaintextSecret) 
plaintextSecret = "secret"

f = open("mysecret.txt", "w")
f.write(plaintextSecret)
f.close()
f = open("mysecret.txt", "r")
print(f.read())
f.close()

# COMMAND ----------

⁣
secret
