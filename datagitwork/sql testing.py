# Databricks notebook source
# MAGIC %sql
# MAGIC create table demo
# MAGIC (Message varchar(256) )

# COMMAND ----------

# MAGIC %sql
# MAGIC   insert into demo
# MAGIC select 'Hi World!........ How are you' as Message
# MAGIC

# COMMAND ----------


