"""
CREAT: 2018/1/30
AUTHOR:　HEHAHUTU
"""
import sys
import os
import time
import dotenv
from getenv import env

from outputdata.logs import LOG_BASE_PATH
from tools.driver import ENV_DRIVER, ENV_PLATFORM

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
ROOT_PATH = os.path.abspath(os.path.join(PROJECT_PATH, os.pardir))

# 尝试读取环境变量配置
try:
    dotenv_path = os.path.join(ROOT_PATH, '.env')
    dotenv.read_dotenv(dotenv_path)
except Exception as e:
    raise Exception('读取环境变量失败！！！')

# 日志配置
# 日志保存路径
LOG_PATH = os.path.abspath(os.path.join(LOG_BASE_PATH, f'{ENV_PLATFORM}_{int(time.time())}.log'))
# 日志级别
LOG_LEVEL = 'INFO'  # INFO ; WARN ; DEBUG

# 浏览器驱动配置
CHROME_DRIVER = ENV_DRIVER['CHROME']
FIREFOX_DRIVER = ENV_DRIVER['FIREFOX']
IE_DRIVER = ENV_DRIVER.get('IE')

# 测试数据配置，使用mongodb
# db.createUser({user: "selenium", pwd: "selenium123", roles: [{role:"readWrite",db: "selenium"}]})

MONGO_HOST = env('MONGO_HOST')
MONGO_PORT = env('MONGO_PORT')
MONGO_USERNAME = env('MONGO_USERNAME')
MONGO_PASSWORD = env('MONGO_PASSWORD')
MONGO_DBNAME = env('MONGO_DBNAME')

MONGO_URI = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DBNAME}?authSource=selenium"
