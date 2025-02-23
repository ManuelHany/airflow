## Airflow as Docker

The follwoin setup is for development only. These are the steps to run the project.

### 1. Initialize .env

- create .env file and set the variable `AIRFLOW_UID=user_id`

### 2. Prepare environemnt

- run

```Bash
Python -m venv venv
```

- source the python environment

```Bash
source venv/bin/activate
```

- install requirements

```Bash
pip install -r requirements.txt
```

### 3. Export connections use

```bash
# enter container
docker exec -it airflow-airflow-webserver-1
# export connections
airflow connections export connections.json
```

### 4. Import them use:

```bash
# copy connections inside container
docker cp connections.json airflow-airflow-webserver-1:/opt/airflow/connections.json
# enter container:
docker exec -it airflow-airflow-webserver-1 /bin/bash
# import connections
airflow connections import connections.json
```
