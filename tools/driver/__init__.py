"""
CREATE: 2018/2/1
AUTHOR: Hehahutu
"""
import os
import sys
ENV_PLATFORM = sys.platform
DRIVER_PATH = os.path.abspath(os.path.dirname(__file__))
BROWSER_DRIVER = {
    'CHROME': {
        'LINUX': os.path.abspath(os.path.join(DRIVER_PATH, 'chrome/linux/chromedriver')),
        'WINDOWS': os.path.abspath(os.path.join(DRIVER_PATH, 'chrome/win32/chromedriver.exe'))

    },
    'FIREFOX': {
        'LINUX': os.path.abspath(os.path.join(DRIVER_PATH, 'firefox/linux/geckodriver')),
        'WINDOWS': os.path.abspath(os.path.join(DRIVER_PATH, 'firefox/win32/geckodriver.exe'))

    },
    'IE': {
        'WINDOWS': os.path.abspath(os.path.join(DRIVER_PATH, 'ie/win32/IEDriverServer.exe'))

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

    raise Exception(f'加载驱动配置文件失败！  code: {e}')