# KEYWORDS / TAGS
- AIRFLOW
- APACHE AIRFLOW
- ORCHESTRATION
- WORKFLOW MANAGEMENT
- DAG
- DIRECTED ACYCLIC GRAPH
- TASK
- OPERATOR
- DEPENDENCY MANAGEMENT
- SCHEDULING
- RETRY
- MONITORING
- LOGGING
- TRIGGER
- PYTHON OPERATOR
- BASH OPERATOR
- EMAIL OPERATOR
- SQL OPERATOR
- SENSOR OPERATOR
- BRANCH OPERATOR
- ETL PIPELINE
- DAG CREATION
- AIRFLOW INSTALLATION
- AIRFLOW WEB UI


# TAG / ABBREVIATION REFERENCE
- [LIB] = Library
- [USA] = Usage (Example Code)
- [PAR] = Parameters
- [SYN] = Syntax
- [WHY] = Why this is used
- [EXA] = Example
- [MET] = Methods
- [CAT] = Cannot have it
- [ALI] = Alias
- [RES] = Expected Result
- [OPT] = Optional
- [ANE] = Another Example
- [FUN] = Functions Used
- [DAM] = Data Members
- [TYS] = Types
- [VER] = Python Version
- [USC] = Use Cases
- [COM] = CLI Command
- [INS] = Install this library
- [STE] = Steps


> **Date** = (29/7/2026)


# AIRFLOW
==========

## Definition

Airflow is available in Python alone.

Orchestration is the automated coordination, scheduling, monitoring, and management of multiple tasks that have dependencies.

Airflow is an orchestration tool.


# CORE ORCHESTRATION CONCEPTS
==============================

## 1. Workflow

A complete sequence of related tasks.


## 2. DAG (Directed Acyclic Graph)

Defines task flow with no cycles or loops.


## 3. Task

A single unit of work in a workflow.

Task execution can be managed using:

- Downstream:
    - Task that should be executed after another task.

- Upstream:
    - Task that should be executed before another task.


## 4. Operator

Defines the action a task performs.


## 5. Dependency

Specifies the execution order of tasks.


## 6. Scheduling

Runs workflows automatically at set times.


## 7. Retry

Re-runs failed tasks automatically.


## 8. Monitoring

Tracks workflow and task execution status.


## 9. Logging

Records execution details for debugging.


## 10. Trigger

Starts a workflow or task based on a schedule or event.


---

# AIRFLOW OPERATORS
===================

## Python Operator

Executes a Python function or script.


## Bash Operator

Runs Bash or shell commands.


## Email Operator

Sends emails from an Airflow workflow.


## SQL Operator

Executes SQL queries on a database.


## Transform Operators

Perform data transformation and processing tasks.


## Sensor Operators

Wait until a specific condition or event is met.


## Branch Operators

Choose one execution path based on conditions.


## Trigger Operators

Trigger another DAG or workflow execution.


## LatestOnly Operator

Runs tasks only for the most recent DAG execution.


---

# AIRFLOW INSTALLATION
======================


## [USA]


## [STE]

### 1. Create a virtual environment

```bash
python3 -m venv airflow_venv
````

---

## [STE]

### 2. Activate the virtual environment

```bash
source airflow_venv/bin/activate
```

---

## [STE]

### 3. Upgrade pip

```bash
pip install --upgrade pip
```

---

## [INS]

### 4. Install Apache Airflow

```bash
pip install apache-airflow
```

---

## [STE]

### 5. Set the Airflow home directory

```bash
export AIRFLOW_HOME=~/airflow
```

### Note

`export AIRFLOW_HOME=~/airflow` sets the directory where Airflow stores:

* airflow.cfg configuration file
* logs
* plugins
* database

If it is not set, Airflow uses:

```
~/airflow
```

as the default location.

This step is optional unless a custom location is required.

---

## [STE]

### 6. Verify Airflow installation

```bash
airflow --version
```

---

## [STE]

### 7. Initialize the Airflow database

```bash
airflow db migrate
```

---

## [STE]

### 8. Create an Admin User

```bash
airflow users create \
  --username admin \
  --firstname Admin \
  --lastname User \
  --role Admin \
  --email admin@example.com
```

Password:

```
admin123
```

---

## [STE]

### 9. Start Airflow Scheduler

```bash
airflow scheduler
```

---

## [STE]

### 10. Start Airflow Webserver

```bash
airflow webserver --port 8080
```

---

## [STE]

### 11. Open Airflow UI

```
http://localhost:8080
```

Login:

```
Username: admin
Password: admin123
```

---

# WRITING DAG FOR AIRFLOW

=========================

> **Date** = (30/7/2026)

## [USA]

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


# Function to execute
def print_message():
    print("Hi DAG")


# Create DAG
with DAG(
    dag_id="first_dag",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["example"],
) as dag:


    # Define task
    task1 = PythonOperator(
        task_id="print_message_task",
        python_callable=print_message,
    )


    # Task execution order
    task1
```

---

# DAG PARAMETERS

================

## [PAR]

| Parameter               | Description                                |
| ----------------------- | ------------------------------------------ |
| dag_id                  | Unique name of the DAG                     |
| start_date              | Date from which the DAG starts scheduling  |
| schedule                | Defines how often the DAG runs             |
| catchup                 | If False, skips missed past runs           |
| end_date                | Stops scheduling after this date           |
| default_args            | Default settings shared by all tasks       |
| description             | Brief description of the DAG               |
| tags                    | Labels used to organize DAGs in the UI     |
| max_active_runs         | Maximum DAG runs allowed at the same time  |
| max_active_tasks        | Maximum tasks running concurrently         |
| is_paused_upon_creation | Creates the DAG in a paused state          |
| template_searchpath     | Directory for Jinja template files         |
| doc_md                  | Markdown documentation displayed in the UI |

---

# ETL DAG EXAMPLE

=================

## [ANE]

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


# Extract
def extract():
    print("Reading data from source...")


# Transform
def transform():
    print("Cleaning and transforming data...")


# Load
def load():
    print("Loading data into database...")


with DAG(
    dag_id="etl_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:


    extract_task = PythonOperator(
        task_id="extract",
        python_callable=extract,
    )


    transform_task = PythonOperator(
        task_id="transform",
        python_callable=transform,
    )


    load_task = PythonOperator(
        task_id="load",
        python_callable=load,
    )


    # ETL execution order

    extract_task >> transform_task >> load_task
```

---

# KEY POINTS

=============

* Airflow is an orchestration tool.
* Orchestration manages scheduling, monitoring, and execution of dependent tasks.
* DAG defines the workflow execution sequence.
* A DAG should not contain cycles or loops.
* Tasks represent individual units of work.
* Operators define what action a task performs.
* Dependencies control task execution order.
* Scheduler executes workflows automatically.
* Retry automatically reruns failed tasks.
* Logging helps in debugging workflow execution.
* Airflow supports ETL pipeline creation.
* PythonOperator executes Python functions.
* Task dependency can be created using:

```python
task1 >> task2
```

* Airflow UI is available through:

```
http://localhost:8080
```
