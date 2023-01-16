
#we will use apache airflow to schedule a DAG (Directed Acyclic Graph) to run the function run_twitter_etl
from datetime import timedelta
# to define a DAG in Airflow
from airflow import DAG
# to run Python code as a task in the DAG
from airflow.operators.python_operator import PythonOperator
# to specify dates relative to the current date.
from airflow.utils.dates import days_ago
from datetime import datetime
from twitter_etl import run_twitter_etl

# DAG's parameters : dag's owner, set the dag to even if the previous run has failed, the dag will start
# the 26 sept 2022, notify me when the dag starts running, retry sending the notification only once
# once it fails.
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 9, 26),
    'email': ['nadine.laabidi@horizon-tech.tn'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

# we create a DAG instance named twitter_dag that runs once a day
dag = DAG(
    'twitter_dag',
    default_args=default_args,
    description='Our first DAG with ETL process!',
    schedule_interval=timedelta(days=1),
)

"""now, we will add a task to the dag:we create an instance of the PythonOperator class to run the python fucntion, 
the task's name will be set to twitter_etl, we call the function run_twitter_etl we already created and we specify the dag, this task belongs to"""
run_etl = PythonOperator(
    task_id='twitter_etl',
    python_callable=run_twitter_etl,
    dag=dag, 
)

run_etl
