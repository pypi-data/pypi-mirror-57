"""
日志文件类
主要用于把出现错误的地方捕捉后存放到./result/logs文件夹下面
"""
import logging.config
from logging.handlers import RotatingFileHandler


class MyLog:

    # 初始化 先有实例，才能初始化
    def __init__(self, format, log_level, log_path, max_bytes, backup_count, file_level, console_level):
        """
        初始化日志
        :param format: 日志输出的格式
        :param log_level: 日志的级别
        :param log_path: 日志的存放位置，路径拼接到.log
        :param max_bytes: 最大
        :param backup_count: 数量
        :param file_level: 文件输出log的级别
        :param console_level: 控制台打印log的级别
        """
        self.format = format
        self.log_level = log_level
        self.log_path = log_path
        self.max_bytes = max_bytes
        self.backup_count = backup_count
        self.file_level = file_level
        self.console_level = console_level

    def logger(self):
        """
        典型的日志记录的步骤是这样的：
        创建logger
        创建handler
        定义formatter
        给handler添加formatter
        给logger添加handler
        """
        # 创建一个logger
        logger = logging.getLogger()
        logger.setLevel(self.log_level)
        if not logger.handlers:
            # 控制台显示 日志处理器
            console_handler = logging.StreamHandler()
            # 创建一个handler,用于写入文件
            file_handler = RotatingFileHandler(self.log_path, maxBytes=self.max_bytes, backupCount=self.backup_count,
                                               encoding='utf-8')
            # 设置处理器日志级别
            file_handler.setLevel(self.file_level)
            console_handler.setLevel(self.console_level)
            # 这里来设置日志的级别
            # CRITICAl    50
            # ERROR    40
            # WARNING    30
            # INFO    20
            # DEBUG    10
            # NOSET    0

            # 定义handler的输出格式
            log_format = logging.Formatter(self.format)
            # 给handler添加formatter
            file_handler.setFormatter(log_format)
            console_handler.setFormatter(log_format)
            # 给logger添加handler
            logger.addHandler(file_handler)
            # 日志收集器添加处理器
            logger.addHandler(console_handler)
        return logger


# if __name__ == '__main__':
#     print('************')
#     logger = MyLog('%(asctime)s-%(name)s-%(levelname)s-%(filename)s-%(lineno)d-%(message)s', 20, 'D:\\python36\\srm_test\\2019-12-04_16_07_25.log', 104857600, 5, 'DEBUG')
#     logger.logger().info('测试logger日志类')
