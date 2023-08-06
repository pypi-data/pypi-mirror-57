import logging
import os
import sys

from test_airtunnel.conftest import make_test_db_path, update_airflow_cfg

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def _remove_airflow_db():
    db_path = make_test_db_path()

    if os.path.exists(db_path):
        logger.info(f"Removing SQLite DB at: {db_path}")
        os.remove(db_path)
        logger.info(f"Done.")
    else:
        logger.info(f"No SQLite DB exists at: {db_path}")

    exit(0)


def _update_airflow_cfg():
    update_airflow_cfg(make_test_db_path())

    exit(0)


if __name__ == "__main__":
    usage = "Usage: python test_cli_utils.py remove_db|update_airflow_cfg"

    if len(sys.argv) > 1 and sys.argv[1] == "remove_db":
        _remove_airflow_db()

    if len(sys.argv) > 1 and sys.argv[1] == "update_airflow_cfg":
        _update_airflow_cfg()

    logger.error(usage)
