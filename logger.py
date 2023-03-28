import logging
import os

import colorlog

# 日志级别
console_level = logging.DEBUG
file_level = logging.INFO

# 日志颜色配置
log_colors_config = {
    'DEBUG': 'white',
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'bold_red',
}

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def _get_logger():
    logger = logging.getLogger('logger')
    logger.setLevel(logging.DEBUG)

    # 设置控制台句柄
    console_handler = logging.StreamHandler()
    console_formatter = colorlog.ColoredFormatter(
        fmt='%(log_color)s[%(levelname)s]: %(message)s',
        log_colors=log_colors_config
    )
    console_handler.setFormatter(console_formatter)
    console_handler.setLevel(console_level)
    logger.addHandler(console_handler)

    # 设置文件句柄
    file_handler = logging.FileHandler('log.txt', encoding='utf8')
    file_formatter = logging.Formatter(
        fmt='[%(asctime)s] %(filename)s -> %(funcName)s line:%(lineno)d [%(levelname)s]: %(message)s',
    )
    file_handler.setFormatter(file_formatter)
    file_handler.setLevel(file_level)
    logger.addHandler(file_handler)
    return logger


logger = _get_logger()
