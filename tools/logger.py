"""
CREATE: 2018/1/31
AUTHOR: Hehahutu
"""

from config import LOG_PATH, LOG_LEVEL
import logging as logger
CH_LEVEL = {
    'INFO': logger.INFO,
    'WARN': logger.WARN,
    'DEBUG': logger.DEBUG,
}
#################################################################################################
logger.basicConfig(level=CH_LEVEL[LOG_LEVEL],
                   format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                   datefmt='%a, %d %b %Y %H:%M:%S',
                   filename=LOG_PATH,
                   filemode='a')

# 定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logger.StreamHandler()
console.setLevel(LOG_LEVEL)
formatter = logger.Formatter('%(name)-5s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logger.getLogger('').addHandler(console)

#################################################################################################
