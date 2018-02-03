"""
CREATE: 2018/2/3
AUTHOR: Hehahutu
"""
from pymongo import MongoClient
from config.settings import MONGO_URI
from datetime import datetime

try:
    mongo = MongoClient(MONGO_URI)
    connect_test = mongo.selenium.connect_test
    connect_test.insert({'time': datetime.now()})
    mongo.close()
    print('mongo 服务正常')
except Exception as e:
    raise Exception(f'mongodb服务器异常 {e}')


