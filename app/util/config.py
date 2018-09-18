import logging


class Logger(object):

    def __init__(self, log_formatter=None, name='logger', log_file='test.log'):
        # 创建一个logger
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        # 创建一个handler，用于写入日志文件
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)
        # 再创建一个handler，用于输出到控制台
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        # 定义handler的输出格式
        if log_formatter:
            formatter = logging.Formatter(log_formatter)
        else:
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        # 给logger添加handler
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        self.logger = logger

    def debug(self, msg):
        self.logger.debug(msg)

    def log(self, msg):
        self.logger.info(msg)

    def info(self, msg):
        self.log(msg)

    def warn(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)
