"""
CREATE: 2018/2/1
AUTHOR: Hehahutu
"""
from tools.logger import logger
from config.settings import CHROME_DRIVER, FIREFOX_DRIVER, IE_DRIVER
import time
from selenium import webdriver


class BrowserDriver:
    @staticmethod
    def chrome():
        try:
            driver = webdriver.Chrome(executable_path=CHROME_DRIVER)
            driver.maximize_window()
            driver.close()
            logger.info('chrome driver ok')
        except Exception as e:
            logger.error(f'chrome driver failed;  error code: {e}')

    @staticmethod
    def firefox():
        try:
            driver = webdriver.Firefox(executable_path=FIREFOX_DRIVER)
            driver.maximize_window()
            driver.close()
            logger.info('firefox driver ok')
        except Exception as e:
            logger.error(f'firefox driver failed; {e}')

    @staticmethod
    def ie():
        try:
            driver = webdriver.Ie(executable_path=IE_DRIVER)
            driver.maximize_window()
            driver.close()
            logger.info('ie driver ok')
        except Exception as e:
            logger.error(f'ie driver failed; {e}')


if __name__ == '__main__':
    print(CHROME_DRIVER, FIREFOX_DRIVER, IE_DRIVER)
    bs = BrowserDriver()
    bs.chrome()
    bs.firefox()
    bs.ie()
