from MountainRed.dbsm import DataBasesLoader, logger, DataBasesLoaderError
import pymysql


class Loader(DataBasesLoader):
    pass

    def is_options_legal(self):
        # return super().is_options_legal()
        KEYS = {"NAME", "ENGINE", "HOST", "PORT",
                "USER", "PASSWORD", "DATABASES"}
        keys = self.options.keys()
        diff = KEYS.difference(set(keys))
        if diff:
            logger.warn("%s 下缺少关键配置! %s" % (self.name, str(diff)))
            return False
        else:
            diff = set(keys).difference(KEYS)
            if diff:
                logger.warn("%s 下发现无效的多余参数! %s" % (self.name, str(diff)))
        return True

    def test_connection(self) -> bool:
        logger.info('Testing MySQL connection %s IP:%s' %
                    (self.name, self.options['HOST']))
        try:
            conn = pymysql.connect(
                host=self.options['HOST'],
                port=int(self.options['PORT']),
                user=self.options['USER'],
                password=self.options['PASSWORD'],
                charset='utf8',
            )
        except pymysql.err.OperationalError:
            logger.error(
                'MySQL connection error! IP: [%s]' % self.options['HOST'])
            return False

        conn.close()
        return True

    def loading(self):
        # return super().loading()(self):
        # 判断Database
        # 遍历组装
        result = {}
        databases = []
        conn = pymysql.connect(
            host=self.options['HOST'],
            port=int(self.options['PORT']),
            user=self.options['USER'],
            password=self.options['PASSWORD'],
            charset='utf8',
        )
        cursor = conn.cursor()
        sql = "show databases"
        cursor.execute(sql)
        existing_db = [db[0] for db in cursor.fetchall()]
        if len(self.options['DATABASES']):
            registerd_db = self.options['DATABASES']
            for db in registerd_db:
                if db in existing_db:
                    databases.append(db)
                else:
                    logger.error(
                        'The database [%s] does not exist in connection [%s]' % (db, self.name))
        else:
            # DATABASES为空，则默认加载所有的DB
            databases = existing_db

        # 组装数据库配置
        for db in databases:
            logger.info('Loading database [%s.%s]' % (self.name, db))
            result['%s.%s' % (self.name, db)] = {
                'ENGINE': self.get_engine(),
                'HOST': self.options['HOST'],
                'PORT': self.options['PORT'],
                'NAME': db,
                'USER': self.options['USER'],
                'PASSWORD': self.options['PASSWORD']
            }

        return result
