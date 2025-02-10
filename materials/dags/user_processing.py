from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

from datetime import datetime

with DAG(
    "user_processing",
    start_date=datetime(2022, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    pass
