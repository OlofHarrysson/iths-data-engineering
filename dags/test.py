from datetime import datetime

from airflow.decorators import dag, task

from newsfeed import dag_start


@task(task_id="hello")
def hello() -> None:
    print("HELLO suuup")
    print(dag_start.get_name())


@dag(
    dag_id="test_pipeline",
    start_date=datetime(2023, 6, 2),
    schedule="*/5 * * * *",
    catchup=False,
)
def test_pipeline() -> None:
    hello()


# register DAG
test_pipeline()
