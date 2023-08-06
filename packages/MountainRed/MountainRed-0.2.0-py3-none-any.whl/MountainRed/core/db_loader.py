"""
完全对数据库配置文件的装载
"""
import pymysql
import json
import logging


logger = logging.getLogger('mountainred')

# 必要的数据库配置参数
KEYS = {
    "ENGINE",
    "HOST",
    "PORT",
    "USER",
    "PASSWORD",
    "DATABASES"
}

ENGINES = {
    "mysql": 'django.db.backends.mysql',
    "sqlite": 'django.db.backends.sqlite3',
    "postgresql": 'django.db.backends.postgresql',
    "oracle": 'django.db.backends.oracle'
}


class DBLoaderError(BaseException):
    pass


def load_databases(config_path: str) -> dict:

    def load_config(path: str) -> str:
        import os
        if not os.path.exists(path):
            raise DBLoaderError("[%s] 配置文件路径错误!" % path)

        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            if len(content) == "0":
                raise DBLoaderError("配置文件为空")
        return content

    raw_config_str = load_config(config_path)
    config_options = json.loads(raw_config_str)
    # 返回值字典
    result = {}

    def check_options(options: dict, connection_name: str):
        """
        判断参数是否完整
        :return:

        """
        # 判断参数是否完整
        keys = options.keys()
        diff = KEYS.difference(set(keys))
        if diff:
            raise DBLoaderError("%s 下缺少关键配置! %s" %
                                (connection_name, str(diff)))

    def checkout_connection(options: dict):
        if options['ENGINE'] == 'sqlite':
            return True
        elif options['ENGINE'] == 'mysql':
            conn = pymysql.connect(
                host=options['HOST'],
                port=int(options['PORT']),
                user=options['USER'],
                password=options['PASSWORD'],
                charset='utf8',
            )
            if not conn:
                raise DBLoaderError("网络错误或参数错误`")
            return True
        else:
            raise DBLoaderError("尚未实现对%s数据库模块的支持" % options['ENGINE'])

    for k in config_options.keys():
        # 获取对应k值下所对应的的数据库连接信息
        db_info = config_options[k]
        check_options(db_info, k)

        checkout_connection(db_info)
        # 获取参数
        engine = db_info['ENGINE']
        host = db_info['HOST']
        port = db_info['PORT']
        user = db_info['USER']
        password = db_info['PASSWORD']
        # 获取数据库
        databases_configs = db_info['DATABASES']

        # 获取连接
        conn = pymysql.connect(
            host=host,
            port=int(port),
            user=user,
            password=password,
            charset='utf8',
        )

        if not conn:
            raise DBLoaderError("网络错误或参数错误`")

        # 创建游标
        cursor = conn.cursor()
        sql = "show databases"
        cursor.execute(sql)
        # 获取所有数据库
        db_databases = cursor.fetchall()
        databases = []
        for database in db_databases:
            databases.append(database[0])
        # 判断用户是否输入数据库
        if databases_configs:
            for databases_config in databases_configs:
                # 存放单个主机别名下的连接的字典
                connections = {}
                # 设置单个数据库配置信息
                conn_config = {}
                if databases_config not in databases:
                    logger.warning("%s 不存在" % databases_config)
                conn_label = str(k) + "." + str(databases_config)
                conn_config.update(
                    {'ENGINE': engine, 'HOST': host, 'NAME': databases_config, 'PORT': port, 'USER': user,
                     'PASSWORD': password})
                connections.update({conn_label: conn_config})
                result.update(connections)

        # 没有填写数据库,就获取该连接下所有数据库
        else:
            for database in databases:
                # 设置单个k值下所有数据库配置信息
                connections = {}
                # 设置单个数据库配置信息
                conn_config = {}
                conn_label = str(k) + "." + str(database)
                if engine == 'sqlite':
                    conn_config.update(
                        {'ENGINE': ENGINES.get(engine), 'NAME': database})
                else:
                    conn_config.update(
                        {'ENGINE': ENGINES.get(engine), 'HOST': host, 'NAME': database, 'PORT': port, 'USER': user,
                         'PASSWORD': password})
                connections.update({conn_label: conn_config})
                result.update(connections)

    # 将第一个设置为默认连接
    default = {'default': result[list(result.keys())[0]]}
    result.update(default)
    return result


if __name__ == '__main__':
    a = load_databases('../dbinfo.json')
    import pprint

    pprint.pprint(a)
