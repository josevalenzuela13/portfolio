# Databricks notebook source
# Laboratorio sintético. Ejecutar únicamente en catálogo/schema de práctica.
# Validación local: sintaxis. La ejecución requiere Databricks y permisos propios.
import re
from pyspark.sql import functions as F, Window

dbutils.widgets.text("catalog", "")
dbutils.widgets.text("schema", "atlas_practica")
dbutils.widgets.dropdown("stage", "all", ["all", "prepare", "transform", "quality"])
catalog = dbutils.widgets.get("catalog")
schema = dbutils.widgets.get("schema")
stage = dbutils.widgets.get("stage")
if not all(re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*", x) for x in (catalog, schema)):
    raise ValueError("Indica catalog y schema de práctica usando letras, números y guion bajo")
ns = f"`{catalog}`.`{schema}`"
spark.sql(f"CREATE SCHEMA IF NOT EXISTS {ns}")

# COMMAND ----------
if stage in ("all", "prepare"):
    # Fuente reproducible; esta preparación reemplaza SOLO la tabla del ejercicio.
    source = spark.createDataFrame([
        ("A", 1, "2026-01-01", 10000, "UPSERT"),
        ("A", 1, "2026-01-01", 10000, "UPSERT"),
        ("A", 2, "2026-01-01", 12000, "UPSERT"),
        ("B", 1, "2026-01-01", 5000, "UPSERT"),
        ("B", 2, "2026-01-01", 0, "DELETE"),
        ("C", 1, "2026-01-02", 7000, "UPSERT"),
    ], "event_id string, version long, event_day string, amount_cents long, op string")
    source.write.format("delta").mode("overwrite").saveAsTable(f"{catalog}.{schema}.bronze_demo")

# COMMAND ----------
if stage in ("all", "transform"):
    source = spark.table(f"{catalog}.{schema}.bronze_demo")
    # No resolver empates conflictivos arbitrariamente: primero detectar conflictos.
    conflict = source.groupBy("event_id", "version").agg(
        F.countDistinct(F.struct("event_day", "amount_cents", "op")).alias("variants")
    ).filter("variants > 1")
    if conflict.limit(1).count():
        raise ValueError("Conflicto de payload para una misma entidad y versión")
    invalid = source.filter("event_id IS NULL OR version IS NULL OR version < 1 OR amount_cents IS NULL OR amount_cents < 0 OR op IS NULL OR op NOT IN ('UPSERT','DELETE') OR to_date(event_day) IS NULL")
    if invalid.limit(1).count():
        raise ValueError("Contrato incumplido: investigar antes de publicar")
    latest = (source.dropDuplicates()
              .withColumn("rn", F.row_number().over(Window.partitionBy("event_id").orderBy(F.desc("version"))))
              .filter("rn=1").drop("rn"))
    latest.createOrReplaceTempView("atlas_latest")
    spark.sql(f"""CREATE TABLE IF NOT EXISTS {ns}.silver_demo
      (event_id STRING, version BIGINT, event_day STRING, amount_cents BIGINT, op STRING) USING DELTA""")
    spark.sql(f"""MERGE INTO {ns}.silver_demo t USING atlas_latest s ON t.event_id=s.event_id
      WHEN MATCHED AND s.version > t.version THEN UPDATE SET *
      WHEN NOT MATCHED THEN INSERT *""")
    spark.sql(f"""CREATE OR REPLACE VIEW {ns}.gold_demo AS
      SELECT event_day, count(*) AS events, sum(amount_cents) AS total_cents
      FROM {ns}.silver_demo WHERE op='UPSERT' GROUP BY event_day""")

# COMMAND ----------
if stage in ("all", "quality"):
    actual = {r.event_day: (r.events, r.total_cents) for r in spark.table(f"{catalog}.{schema}.gold_demo").collect()}
    if actual != {"2026-01-01": (1, 12000), "2026-01-02": (1, 7000)}:
        raise AssertionError(f"Reconciliación fallida: {actual}")
    display(spark.table(f"{catalog}.{schema}.gold_demo"))
    print("Reconciliación correcta. Reejecuta transform y verifica idempotencia.")

# Ampliación: inyecta un fallo antes de quality, repara el Job y registra evidencia.
# No borrar checkpoints ni ejecutar VACUUM para resolver el ejercicio.
