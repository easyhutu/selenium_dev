"""
CREAT: 2018/1/30
AUTHOR:　HEHAHUTU
"""
import sys
import os
import time
from pprint import pprint

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
ROOT_PATH = os.path.abspath(os.path.join(PROJECT_PATH, os.pardir))
ENV_PLATFORM = sys.platform

# 日志配置
LOG_PATH = f'{ENV_PLATFORM}_{int(time.time())}.log'
LOG_LEVEL = 'INFO'  # INFO ; WARN ; DEBUG

BROWSER_DRIVER = {
    'CHROME': {
        'LINUX': os.path.abspath(os.path.join(ROOT_PATH, 'tools/driver/chrome/linux/chromedriver')),
        'WINDOWS': os.path.abspath(os.path.join(ROOT_PATH, 'tools/driver/chrome/win32/chromedriver.exe'))

    },
    'FIREFOX': {
        'LINUX': os.path.abspath(os.path.join(ROOT_PATH, 'tools/driver/firefox/linux/geckodriver')),
        'WINDOWS': os.path.abspath(os.path.join(ROOT_PATH, 'tools/driver/firefox/win32/geckodriver.exe'))

    },
    'IE': {
        'WINDOWS': os.path.abspath(os.path.join(ROOT_PATH, 'tools/driver/ie/win32/IEDriverServer.exe'))

    }
}

try:
    ENV_DRIVER = {}

    print(f'检测到当前环境是 {ENV_PLATFORM}')
    if ENV_PLATFORM == 'linux':
        ENV_DRIVER['CHROME'] = BROWSER_DRIVER['CHROME']['LINUX']
        ENV_DRIVER['FIREFOX'] = BROWSER_DRIVER['FIREFOX']['LINUX']
    else:
        ENV_DRIVER['CHROME'] = BROWSER_DRIVER['CHROME']['WINDOWS']
        ENV_DRIVER['FIREFOX'] = BROWSER_DRIVER['FIREFOX']['WINDOWS']
        ENV_DRIVER['IE'] = BROWSER_DRIVER['IE']['WINDOWS']


except Exception as e:

    raise Exception(f'加载配置文件失败！  code: {e}')

# 浏览器驱动配置
CHROME_DRIVER = ENV_DRIVER['CHROME']
FIREFOX_DRIVER = ENV_DRIVER['FIREFOX']
IE_DRIVER = ENV_DRIVER.get('IE')
pprint(f'成功加载驱动配置如下：')
print(f'chrome path: {CHROME_DRIVER}')
print(f'firefox path: {FIREFOX_DRIVER}')
print(f'ie path: {IE_DRIVER}')
