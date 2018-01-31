"""
CREAT: 2018/1/30
AUTHOR:　HEHAHUTU
"""

import os

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
ROOT_PATH = os.path.abspath(os.path.join(PROJECT_PATH, os.pardir))

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
