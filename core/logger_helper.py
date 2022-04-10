import logging
from logging import Logger
from logging.handlers import TimedRotatingFileHandler

""" 日志管理类 """


def init_logger(logger_name):
    if logger_name not in Logger.manager.loggerDict:
        logger1 = logging.getLogger(logger_name)
        logger1.setLevel(logging.INFO)  # 设置最低级别
        # logger1.setLevel(logging.DEBUG)  # 设置最低级别
        df = '%Y-%m-%d %H:%M:%S'
        format_str = '[%(asctime)s]: %(name)s %(levelname)s %(lineno)s %(message)s'
        formatter = logging.Formatter(format_str, df)
        # handle all
        try:
            handle1 = TimedRotatingFileHandler('/usr/wechat/log/all.log', when='D', interval=1, backupCount=7)
        except Exception:
            handle1 = TimedRotatingFileHandler('D:/wechat/core/log\/all.log', when='D', interval=1, backupCount=7)

        handle1.setFormatter(formatter)
        handle1.setLevel(logging.DEBUG)
        logger1.addHandler(handle1)

        # handle error
        try:
            handle2 = TimedRotatingFileHandler('/usr/wechat/log/error.log', when='D', interval=1, backupCount=7)
        except Exception:
            handle2 = TimedRotatingFileHandler('D:/wechat/core/log\/error.log', when='D', interval=1, backupCount=7)

        handle2.setFormatter(formatter)
        handle2.setLevel(logging.DEBUG)
        logger1.addHandler(handle2)

        # console
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        # 设置日志打印格式
        console.setFormatter(formatter)
        # 将定义好的console日志handle添加到root logger
        logger1.addHandler(console)

    logger1 = logging.getLogger(logger_name)
    return logger1


logger = init_logger('runtime-log')

if __name__ == '__main__':
    logger.debug('test-debug')
    logger.info('test-info')
    logger.warn('test-warn')
    logger.error('test-error')
