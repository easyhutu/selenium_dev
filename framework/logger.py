"""
CREATE: 2018/1/31
AUTHOR: Hehahutu
"""

from config.settings import LOG_PATH, LOG_LEVEL
import logging as logger
import logging.config

CH_LEVEL = {
    'INFO': logger.INFO,
    'WARN': logger.WARN,
    'DEBUG': logger.DEBUG,
}

conf = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            'format': '%(asctime)s [%(name)s:%(lineno)d] [%(levelname)s]- %(message)s'
        },
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] %(filename)s [line:%(lineno)d] %(levelname)s %(message)s'
        },
    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        },

        "default": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": LOG_LEVEL,
            "formatter": "standard",
            "filename": LOG_PATH,
            'mode': 'w+',
            "maxBytes": 1024 * 1024 * 5,  # 5 MB
            "backupCount": 20,
            "encoding": "utf8"
        },
    },

    "root": {
        'handlers': ['default'],
        'level': LOG_LEVEL,
        'propagate': False
    }
}
logging.config.dictConfig(conf)
#################################################################################################
# logger.basicConfig(level=CH_LEVEL[LOG_LEVEL],
#                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                    datefmt='%a, %d %b %Y %H:%M:%S',
#                    filename=LOG_PATH,
#                    filemode='a')

# 定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logger.StreamHandler()
console.setLevel(LOG_LEVEL)
formatter = logger.Formatter('%(name)-5s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logger.getLogger('').addHandler(console)

#################################################################################################
