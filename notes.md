### URI

- is basically the path to your data
- can't be airflow itself
- it is case sesitive
- has to be ascii compliant

### Subdags and Grouping dags

- to group dags, the arguments must be the same between subdags and parent dags.
- special notation with a `.`

```python
f"{parent_dag_id}.{child_dag_id}"
```

### Xcom

- XCom (Cross-Communication) lets Airflow tasks share data with each other.
- XCom stores data as key-value pairs in Airflow’s metadata database
- One task pushes (saves) data.Another task pulls (retrieves) that data.

```Python
def push_data(ti):
    ti.xcom_push(key="message", value="Hello from Task 1!")

task1 = PythonOperator(
    task_id="push_task",
    python_callable=push_data
)
```

### General

- Deploying airflow through docker requires you to configure it not from theconf file but instead from the docker-compose file inside the environment variablaes there.
-
