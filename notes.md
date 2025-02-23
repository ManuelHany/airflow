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

- You can save (push) data to XCOm database either through the return value of the `python_callable` attribute of task. Or using the `xcom_push` which allow us to set the key value of the data.

```Python
def _t1(ti):
    t1.xcom_push(key='my_key', value=42)

def _t2(ti):
    retrieved_data = ti.xcom_pull(key='my_key', task_ids='t1)
```

### Trigger Rules

1. all_success – Task runs when all upstream tasks succeed (default).
2. all_failed – Task runs when all upstream tasks fail.
3. all_done – Task runs when all upstream tasks are finished (success, failure, or skipped).
4. one_success – Task runs if at least one upstream task succeeds.
5. one_failed – Task runs if at least one upstream task fails.
6. none_failed – Task runs if no upstream task fails (success or skipped).
7. none_failed_or_skipped – Task runs if no upstream task fails or is skipped.
8. none_skipped – Task runs if no upstream task is skipped (all must be success or fail).
9. always – Task runs regardless of upstream task status.
10. dummy (Deprecated in Airflow 2.0+) – Same as always, used for placeholder tasks.

### General

- Deploying airflow through docker requires you to configure it not from theconf file but instead from the docker-compose file inside the environment variablaes there.
- to export connections use

```bash
docker exec -it airflow-airflow-webserver-1 airflow connections list --output json > connections.json
```

- while to import them use:

```bash
# copy connections inside container
docker cp connections.json airflow-airflow-webserver-1:/connections.json
# run inside container:
docker exec -it airflow-airflow-webserver-1 sh -c "
jq -c '.[]' /connections.json | while read -r conn; do
    airflow connections add \
    --conn-id \"\$(echo \$conn | jq -r '.conn_id')\" \
    --conn-type \"\$(echo \$conn | jq -r '.conn_type')\" \
    --conn-host \"\$(echo \$conn | jq -r '.host')\" \
    --conn-login \"\$(echo \$conn | jq -r '.login')\" \
    --conn-password \"\$(echo \$conn | jq -r '.password')\" \
    --conn-schema \"\$(echo \$conn | jq -r '.schema')\" \
    --conn-port \"\$(echo \$conn | jq -r '.port')\" \
    --conn-extra \"\$(echo \$conn | jq -r '.extra')\"
done"
```
