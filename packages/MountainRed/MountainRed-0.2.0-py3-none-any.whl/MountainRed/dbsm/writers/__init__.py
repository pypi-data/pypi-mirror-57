import importlib
import logging

logger = logging.getLogger('dbsm')


def get_writers(dbtype: str, name: str, options: dict):
    try:
        writer = importlib.import_module(
            'MountainRed.dbsm.writers.%s' % dbtype).Writer
    except ImportError:
        logger.error('Cannot find module Writer [%s]' % dbtype)
        raise NotImplementedError

    return writer(name, options)
