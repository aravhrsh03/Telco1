# SCENARIO: Incomplete Dashboard Data & Partial Ingestion Failure

> **The Challenge:** The daily network dashboard at 8:00 AM displays incomplete figures—showing abnormally low traffic for certain regions and missing expected regional summaries entirely—leaving operations uncertain if network load actually dropped or if the pipeline failed.

---

## 🔍 Diagnosis: Upstream Pipeline Partial Failure or Ingestion Delay

Because the dashboard loaded without crashing, the failure is **non-fatal and partial**. This typically occurs when batch processing completes on schedule but silent upstream data delivery failures, delayed log aggregation, or schema variations prevent full data partition inclusion.

### Key Red Flags to Check First:

* **Partial Ingestion / Late-Arriving Data:** CDR (Call Detail Record) collectors, tower log aggregators, or local edge nodes in missing/low-traffic regions failed to upload logs before the daily batch run window closed.
* **Partition Skew & Silent Drop-Offs:** The transformation or ETL job dropped records silently (e.g., failed parsing, unhandled null values, or key mismatches) without triggering a fatal error, leading to partial table updates.

---

## 🛠️ Investigation, Information Needed, & Fix Plan

To quickly resolve the root cause and ensure data integrity, execute this phased incident response:

### 1. Information Needed from Your Team

* **Pipeline Architecture:** Is this an orchestration job (e.g., Airflow, Prefect) running a SQL/Spark job, or a streaming pipeline (e.g., Kafka to Snowflake/BigQuery)?
* **Execution Logs & Row Counts:** What do the run logs, row counts, and data volume metrics look like for yesterday's batch run compared to historical averages?
* **Upstream Health:** Are edge storage buckets/SFTP endpoints for the missing regions populated with raw files, or are the incoming files undersized/absent?

### 2. Immediate Remediation & Fix

* **Audit Raw Storage vs. Staging:** Query raw staging tables to check if data for the missing regions arrived after the ingestion window or failed parsing due to schema/timestamp format shifts.
* **Isolate & Backfill:** Once upstream files are verified, rerun the extraction and transformation tasks specifically for the affected regional partitions.
* **Dashboard Status Banner:** Place a temporary banner on the NOC dashboard indicating that yesterday's data is undergoing an active backfill to prevent erroneous operational decisions.

### 3. Long-Term Prevention Measures

* **SLA & Freshness Alerts:** Set up automated alerts (e.g., Great Expectations, Monte Carlo) to validate total row volume and expected region key counts before updating production tables.
* **Circuit Breakers:** Prevent dashboard downstream updates if mandatory region partitions are missing, failing the job explicitly rather than publishing incomplete figures.
* **Late-Arriving Data Handling:** Configure dynamic backfill scripts and SLA windows that automatically process delayed logs into the appropriate historic partition upon late arrival.