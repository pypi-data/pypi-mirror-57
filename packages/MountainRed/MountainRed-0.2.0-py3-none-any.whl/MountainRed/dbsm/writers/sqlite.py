from MountainRed.dbsm import DataBasesWriter, logger


class Writer(DataBasesWriter):

    def is_options_legal(self) -> bool:
        """
        sqlite 必须的字段有:
        engine, name
        """
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
