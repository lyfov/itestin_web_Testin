# coding=utf-8
import logging
import os
import time
import logging.handlers


class TestLogger(object):
    def __init__(self, log_dir_path):
        # logs 文件父目录
        self.log_dir_path = log_dir_path
        print(self.log_dir_path)
        if os.path.exists(log_dir_path) and os.path.isdir(log_dir_path):
            pass
        else:
            os.mkdir(log_dir_path)
        print(self.log_dir_path)
        time_stamp_name = time.strftime("%Y%m%d%H%M%S%a", time.localtime())
        log_name = time_stamp_name + ".log"
        # logs 文件路径
        log_dir_path=log_dir_path+""
        self.log_path = os.path.join(log_dir_path, log_name)
        # logs 文件输出格式
        self.log_format = "[%(asctime)s] The location of the file output by the log:%(pathname)s \nThe name of the " \
            "module generated under the current file is named: %(funcName)s,The specific number of lines " \
            "corresponding to the file is line %(lineno)d,\nCorresponding log level is :[%(levelname)s]:%(message)s"
        self.date_format = "%Y-%m-%d %H:%M:%S %a"

        """logs在文件输出格式控制"""
        logging.basicConfig(level=logging.INFO,
                            format=self.log_format,
                            datefmt=self.date_format,
                            filename=self.log_path)

        """logs文件内容转换控制台输出，文件处理器处理"""

        rotating_file_handler = logging.handlers.RotatingFileHandler(filename=self.log_path,
                                                                     maxBytes=1024 * 1024 * 50,
                                                                     backupCount=5)
        rotating_file_handler.setFormatter(self.log_format)

        """python控制台句柄设置输出日志格式"""
        self.console = logging.StreamHandler()
        self.console.setLevel(logging.NOTSET)
        self.console_format = logging.Formatter(self.log_format)
        self.console.setFormatter(self.console_format)

    """添加日志content到句柄并返回添加完成的句柄 """
    def console_log(self):
        logger = logging.getLogger()
        logger.addHandler(self.console)
        logger.setLevel(logging.DEBUG)
        return logger
