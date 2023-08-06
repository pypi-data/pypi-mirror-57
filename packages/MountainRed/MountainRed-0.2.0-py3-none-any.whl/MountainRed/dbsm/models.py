"""
该模块实现了数据库的配置文件读写, 配置装载
Author: singein
E-mail: singein@outlook.com
"""

import osprofile
import os
import json
import abc
import logging
from MountainRed.dbsm.loaders import get_loaders
from MountainRed.dbsm.writers import get_writers

logger = logging.getLogger('dbsm')


APP_NAME = 'MountainRed'
PROFILE = 'databases.json'
OPTIONS = {}
EXTRA_ALIAS = ['default', 'auth', 'sessions', 'admin', 'contenttypes']


class DataBasesWriterError(BaseException):
    pass


class DataBasesLoaderError(BaseException):
    pass


class DataBasesSettingsManager(osprofile.OSProfile):

    def __init__(self, appname=APP_NAME, profile=PROFILE, options=OPTIONS):
        super().__init__(appname=appname, profile=profile, options=options)

    def update_or_create(self, options: dict):
        """
        更新数据库配置
        """
        dbtype = options['ENGINE']
        name = options['NAME']
        writer = get_writers(dbtype, name, options)
        updates = writer.writedown()
        if updates:
            self.update_profile(updates)

    def delete_option(self, option: str):
        """
        删除配置选项
        """
        options = self.read_profile()
        try:
            del options[option]
            with open(os.path.join(self.path, self.profile), 'w') as f:
                f.write(json.dumps(options))
        except KeyError:
            logger.warning('Option [%s] does not exist!' % option)

    def get_db_settings(self) -> dict:
        logger.info('DBSM start to load database settings...')
        databases = {}
        options = self.read_profile()

        for key in options.keys():
            loader = get_loaders(options[key]['ENGINE'], key, options[key])
            databases.update(loader.load())

        default = {}
        if len(list(databases.keys())) > 0:
            for app in EXTRA_ALIAS:
                default[app] = databases[list(databases.keys())[0]]

        else:
            for app in EXTRA_ALIAS:
                default[app] = {
                    'NAME': 'sqlite.db',
                    'ENGINE': 'django.db.backends.sqlite3'
                }
        databases.update(default)
        return databases


class DataBasesWriter(metaclass=abc.ABCMeta):

    def __init__(self, name: str, options: dict):
        """初始化构造数据库配置写入对象

        Arguments:
            name {str} -- 数据库连接名
            options {str} -- 数据库配置参数
        """
        self.name = name
        # self.engine = options['ENGINE']
        self.options = options

    @abc.abstractmethod
    def is_options_legal(self) -> bool:
        pass

    def writedown(self) -> dict:
        """组装, 校验数据库数据库配置

        Returns:
            dict -- 经过组装并校验后的配置
        """
        if self.is_options_legal():
            return {self.name: self.options}
        return None


class DataBasesLoader(metaclass=abc.ABCMeta):
    ENGINES = {
        "mysql": 'django.db.backends.mysql',
        "sqlite": 'django.db.backends.sqlite3',
        "postgresql": 'django.db.backends.postgresql',
        "oracle": 'django.db.backends.oracle'
    }

    def get_engine(self):
        return self.ENGINES[self.options['ENGINE']]

    def __init__(self, name: str, options: dict):
        """初始化装载对象

        Arguments:
            name {str} -- 配置文件中读出的数据库连接别名
            options {dict} -- 配置信息
        """
        self.name = name
        self.options = options

    @abc.abstractmethod
    def is_options_legal(self) -> bool:
        """
        检查参数
        """
        pass

    @abc.abstractmethod
    def test_connection(self) -> bool:
        """检查数据库连接
        """
        pass

    @abc.abstractmethod
    def loading(self):
        """
        根据数据库配置生成Django的DataBase配置
        """
        pass

    def load(self) -> dict:
        logger.info('Start loading connection [%s]' % self.name)
        if self.is_options_legal():
            if self.test_connection():
                return self.loading()
            return {}
        return {}
