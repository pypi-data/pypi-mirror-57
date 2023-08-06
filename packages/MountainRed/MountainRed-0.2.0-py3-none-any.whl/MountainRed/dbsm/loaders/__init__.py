import importlib
import logging

logger = logging.getLogger('dbsm')


def get_loaders(dbtype: str, name: str, options: dict):
    try:
        loader = importlib.import_module(
            'MountainRed.dbsm.loaders.%s' % dbtype).Loader
    except ImportError:
        logger.error('Cannot find module from [%s]' % dbtype)
        raise NotImplementedError
    return loader(name, options)
