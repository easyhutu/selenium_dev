"""
CREAT: 2018/1/30
AUTHOR:　HEHAHUTU
"""
import sys
import os
import time
from datetime import datetime
import dotenv
from getenv import env

from output.logs.out_logs import LOG_BASE_PATH
from output.test_report import TEST_REPORT_PATH
from output.logs.capture import CAPTURE_PATH
from testsuites import TEST_SUITES_PATH

from tools.driver import ENV_DRIVER, ENV_PLATFORM

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
ROOT_PATH = os.path.abspath(os.path.join(PROJECT_PATH, os.pardir))
TIME_TAG = datetime.now().strftime('%Y%m%d_%H%M%S')
TEST_REPORT_PATH = TEST_REPORT_PATH
TEST_SUITES_PATH = TEST_SUITES_PATH

# 尝试读取环境变量配置
try:
    dotenv_path = os.path.join(ROOT_PATH, '.env')
    dotenv.read_dotenv(dotenv_path)
except Exception as e:
    raise Exception('读取环境变量失败！！！')

# 日志配置
# 日志保存路径
LOG_PATH = os.path.abspath(os.path.join(LOG_BASE_PATH, f'{ENV_PLATFORM}_{TIME_TAG}.log'))
# 日志级别
LOG_LEVEL = 'INFO'  # INFO ; WARN ; DEBUG

# 浏览器驱动配置
CHROME_DRIVER = ENV_DRIVER['CHROME']
FIREFOX_DRIVER = ENV_DRIVER['FIREFOX']
IE_DRIVER = ENV_DRIVER.get('IE')
# TODO 当前测试调用的浏览器，这里配置后期需要优化
DEFAULT_DRIVER = CHROME_DRIVER

# 测试数据配置，使用mongodb
# db.createUser({user: "", pwd: "", roles: [{role:"readWrite",db: "selenium"}]})

MONGO_HOST = env('MONGO_HOST')
MONGO_PORT = env('MONGO_PORT')
MONGO_USERNAME = env('MONGO_USERNAME')
MONGO_PASSWORD = env('MONGO_PASSWORD')
MONGO_DBNAME = env('MONGO_DBNAME')

MONGO_URI = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DBNAME}?authSource=selenium"

# 测试根路径
PRO_WEB_URL = 'http://www.ovopark.com'
TEST_WEB_URL = 'http://121.43.123.76'
DEFAULT_WEB_URL = PRO_WEB_URL

# 截屏路径

try:
    CAPTURE_PATH = os.path.join(CAPTURE_PATH, TIME_TAG)
    os.mkdir(CAPTURE_PATH)
except:
    raise Exception('截屏路径初始化失败！')

# 邮件发送服务配置

MAIL_HOST = "smtphm.qiye.163.com"  # 设置服务器
MAIL_SMTP_PORT = 465

SENDER = 'mengjianhua@ovopark.com'
MAIL_USER = "mengjianhua@ovopark.com"  # 用户名
MAIL_PASS = "xxxxxxxxxx"  # 口令
"""
    'guzijian@ovopark.com',
    'zhangqing@ovopark.com',
"""
MAIL_RECEIVER = [

    'mengjianhua@ovopark.com',
]
