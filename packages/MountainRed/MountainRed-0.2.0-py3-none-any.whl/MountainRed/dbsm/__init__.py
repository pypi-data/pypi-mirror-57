"""
该模块实现了数据库的配置文件读写, 配置装载
Author: singein
E-mail: singein@outlook.com
"""

import osprofile
import os
import json
import abc
from MountainRed.dbsm.models import DataBasesLoader
from MountainRed.dbsm.models import DataBasesWriter
from MountainRed.dbsm.models import DataBasesLoaderError
from MountainRed.dbsm.models import DataBasesLoaderError
from MountainRed.dbsm.models import DataBasesSettingsManager
# from MountainRed.dbsm.models import logger
from MountainRed.dbsm.loaders import get_loaders
from MountainRed.dbsm.writers import get_writers
import time

import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)s %(levelname)s %(message)s',
                    datefmt=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
logger = logging.getLogger('dbsm')

__all__ = [
    'DataBasesSettingsManager',
    'DataBasesWriterError',
    'DataBasesWriter',
    'DataBasesLoaderError',
    'DataBasesLoader',
    'logger',
    'get_loaders',
    'get_writers'
]
