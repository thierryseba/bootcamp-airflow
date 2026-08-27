from datetime import datetime
from airflow.sdk import DAG, Asset
from airflow.operators.bash import BashOperator

mon_fichier = Asset("file:///tmp/mon_asset.txt")

with DAG(
    dag_id="producteur_asset_bash",
    start_date=datetime (2026, 8, 27, tz='UTC'),
    schedule=None,
    catchup=False,
    tags=["dataset"],

) as dag:
    @task(outlets=[mon_fichier])
    tache1 = BashOperator(
        task_id="produire_fichier",
        bash_command= "echo 'hello' > /tmp/mon_asset.txt'",
    )

with DAG(
    dag_id="consommateur_asset_bash",
    start_date=datetime (2026, 8, 27, tz=3Zurope/Paris'),
    schedule=[mon_fichier],
    catchup=False,
    tags=["dataset_consume"],

) as dag:
    tache2 = BashOperator(
        task_id="lire_fichier",
        bash_command= "cat /tmp/mon_asset.txt",

    )


 
