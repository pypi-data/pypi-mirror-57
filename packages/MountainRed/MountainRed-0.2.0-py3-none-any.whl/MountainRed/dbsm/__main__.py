

from MountainRed.dbsm import DataBasesSettingsManager as DBSM
from MountainRed.dbsm import get_loaders, get_writers, logger
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))


if __name__ == "__main__":
    dbsm = DBSM()
    mysql_options = {
        "NAME": "auth",
        "ENGINE": "mysql",
        "HOST": "127.0.0.1",
        "DATABASES": ['chaos'],
        "PORT": "3306",
        "USER": "root",
        "PASSWORD": "mysql123"
    }

    sqlite_options = {
        "ENGINE": "sqlite",
        "NAME": "db.sqlite"
    }

    # mysql_writer = get_writers('mysql', 'localhost', mysql_options)
    # sqlite_writer = get_writers('sqlite', 'sqlite', sqlite_options)
    # dbsm.update_or_create(mysql_options)
    # dbsm.update_or_create(sqlite_options)
    dbsm.delete_option('db.sqlite')
    logger.info(dbsm.get_db_settings())
