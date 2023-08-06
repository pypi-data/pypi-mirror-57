import datetime
import logging
import os
import subprocess
import urllib.parse
from typing import Dict

import pandas as pd
import pytest

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

AF_HOME = "AIRFLOW_HOME"

assert AF_HOME in os.environ and os.path.exists(
    os.environ[AF_HOME]
), f"env-variable {AF_HOME} needs to be set properly"

NECESSARY_DATA_STORE_PATHS = (
    "archive",
    "ingest",
    "ready",
    "staging",
    "staging/intermediate",
    "staging/ready",
    "staging/pickedup",
    "ingest/archive",
    "ingest/landing",
)


def make_test_db_path() -> str:
    return os.path.join(os.environ[AF_HOME], "airtunnel_test.db")


@pytest.fixture(scope="session")
def test_db_path() -> str:
    db_path = make_test_db_path()
    logger.info(f"Using test-database: {db_path}")
    yield db_path


def update_airflow_cfg(test_db_path: str) -> None:
    test_folder_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), os.pardir
    )
    cfg_path = os.path.join(test_folder_path, "airflow_home/airflow.cfg")

    cfg_path_template = os.path.join(
        test_folder_path, "airflow_home/airflow.template.cfg"
    )

    dags_folder_path = os.path.join(test_folder_path, "test_airtunnel/testdags")

    decls_folder_path = os.path.join(test_folder_path, "test_airtunnel/declarations")

    data_store_folder_path = os.path.join(test_folder_path, "data_store")

    # pre-caution: ensure data store folders all exist (i.e. for docker container)
    os.makedirs(data_store_folder_path, exist_ok=True)

    for data_store_subfolder_path in NECESSARY_DATA_STORE_PATHS:
        os.makedirs(
            os.path.join(data_store_folder_path, data_store_subfolder_path),
            exist_ok=True,
        )

    scripts_folder_path = os.path.join(test_folder_path, "scripts")

    with open(cfg_path_template, "r") as cfgfile_template:
        cfg_template = cfgfile_template.read()

    airflow_test_cfg = cfg_template.format(
        dags_folder=dags_folder_path,
        sqlite_path=test_db_path,
        decls_folder=decls_folder_path,
        data_store_folder=data_store_folder_path,
        scripts_folder=scripts_folder_path,
    )

    with open(cfg_path, "w") as cfgfile:
        cfgfile.write(airflow_test_cfg)

    logger.info(f"Updated test airflow.cfg at: {cfg_path}")


@pytest.fixture(scope="session", autouse=True)
def provide_airflow_cfg(test_db_path: str) -> None:
    update_airflow_cfg(test_db_path)

    if not os.path.exists(test_db_path):
        logger.info(f"SQLite DB is missing – initializing it at: {test_db_path}")
        # initialize the airflow db
        subprocess.run("airflow initdb", shell=True, check=True)
    else:
        logger.info(f"SQLite DB exists at: {test_db_path}")
        subprocess.run("airflow resetdb -y", shell=True, check=True)


@pytest.fixture(scope="session")
def test_db_hook(test_db_path, provide_airflow_cfg):
    from airflow.hooks.sqlite_hook import SqliteHook

    os.environ[
        "AIRFLOW_CONN_SQLITE"
    ] = f"sqlite:///{urllib.parse.quote_plus(test_db_path)}"
    return SqliteHook("sqlite")


def test_setup_airflow_cfg(provide_airflow_cfg):
    # pseudo-test we can call before collecting all other tests,
    # this will trigger an initial setup of airflow.cfg
    # (if airflow.cfg is not correctly in-place, no other test-cases can safely import anything from "airflow"
    #  which unfortunately happens on pytest collect...)
    pass


@pytest.fixture(scope="session")
def iris() -> pd.DataFrame:
    return pd.read_csv(
        "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    )


@pytest.fixture(scope="session")
def fake_airflow_context() -> Dict:
    from airflow.models import TaskInstance
    from airflow.operators.dummy_operator import DummyOperator

    fake_context = {
        "task_instance": TaskInstance(
            task=DummyOperator(task_id="dummy_tas_id"),
            execution_date=datetime.datetime.now(),
        )
    }
    return fake_context
