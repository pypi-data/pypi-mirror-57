from MountainRed.dbsm import DataBasesLoader, logger, DataBasesLoaderError
import os


class Loader(DataBasesLoader):
    pass

    def is_options_legal(self):
        KEYS = {"ENGINE", "NAME"}
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
        path = self.options['NAME']
        if not os.path.exists(path):
            logger.warn(
                'SQLite: [%s] not found. this will be autocreated by MountainRed.' % path)

        return True

    def loading(self):

        result = {
            self.name: {
                "ENGINE": self.get_engine(),
                "NAME": self.options['NAME']
            }
        }

        return result
