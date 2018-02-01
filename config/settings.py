"""
CREAT: 2018/1/30
AUTHOR:　HEHAHUTU
"""
import sys
import os
import time
from outputdata.logs import LOG_BASE_PATH
from tools.driver import ENV_DRIVER, ENV_PLATFORM

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
ROOT_PATH = os.path.abspath(os.path.join(PROJECT_PATH, os.pardir))


# 日志配置
# 日志保存路径
LOG_PATH = os.path.abspath(os.path.join(LOG_BASE_PATH, f'{ENV_PLATFORM}_{int(time.time())}.log'))
# 日志级别
LOG_LEVEL = 'INFO'  # INFO ; WARN ; DEBUG

# 浏览器驱动配置
CHROME_DRIVER = ENV_DRIVER['CHROME']
FIREFOX_DRIVER = ENV_DRIVER['FIREFOX']
IE_DRIVER = ENV_DRIVER.get('IE')

