from airflow import dag
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

def _task_a():
    print("Bonjour")

with DAG(
    dag_id='hello_airflow',
    start_date=datetime(2026, 8, 27),
    schedule='@daily',
    catchup=False
):

   task_a = BashOperator(
    task_id='task_a',
    bash_callable=_task_a,
   )

   task_a
    