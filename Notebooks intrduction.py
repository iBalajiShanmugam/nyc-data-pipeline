# Databricks notebook source
# MAGIC %md 
# MAGIC ## Notebook
# MAGIC ### learn magic commands

# COMMAND ----------

msg = "welcome to Databricks"

# COMMAND ----------

msg

# COMMAND ----------

# MAGIC %sql
# MAGIC select 'hello'

# COMMAND ----------

# MAGIC %scala
# MAGIC val msg ="welcome to scall"
# MAGIC print(msg)

# COMMAND ----------

# MAGIC %fs
# MAGIC ls

# COMMAND ----------

# MAGIC %sh
# MAGIC ps

# COMMAND ----------

display(dbutils.fs.ls('/'))

# COMMAND ----------

# MAGIC %fs
# MAGIC ls /databricks-datasets/

# COMMAND ----------


