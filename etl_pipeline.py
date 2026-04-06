from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from src.extract.from_api import fetch_api
from src.transform.clean import clean_data
from src.load.to_db import load

def etl():
    df = fetch_api()
    df = clean_data(df)
    load(df)

default_args = {"start_date": datetime(2024, 1, 1)}

with DAG("etl_pipeline", schedule_interval="@daily", default_args=default_args, catchup=False) as dag:
    task = PythonOperator(
        task_id="run_etl",
        python_callable=etl
    )
