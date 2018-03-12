"""
CREAt: 2017/3/22
AUTHOR: Hehahutu
"""

from selenium import webdriver
import os
import json
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import json
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from config.settings import DEFAULT_DRIVER, DEFAULT_WEB_URL, CAPTURE_PATH
from framework.logger import logger

from bs4 import BeautifulSoup


class Page:
    def __init__(self, path='/', wait=30):

        self.driver_path = DEFAULT_DRIVER
        logger.info(self.driver_path)
        self.url = DEFAULT_WEB_URL
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.driver.implicitly_wait(wait)
        self.path = path
        self.By = By


    # 打开网址
    def open_base_url(self):
        self.driver.maximize_window()
        url = self.url + self.path
        self.driver.get(url)
        logger.info(f'open url: {url}')

    def open_url(self, url):
        self.driver.get(url)
        logger.info(f'open url: {url}')

    def open_url_path(self, path='/'):
        url = f'{self.url}/index.html?#{path}'
        self.driver.get(url)
        logger.info(f'open url: {url}')

    # 定位元素
    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    # 登录
    def login_web(self, user_info: list = ['username', 'password']):
        self.driver.maximize_window()
        self.driver.get(self.url)
        username_loc = (By.ID, 'username')
        password_loc = (By.ID, 'password')
        login_btn_loc = (By.CLASS_NAME, 'login-btn')
        try:
            self.find_element(*username_loc).clear()
            self.find_element(*username_loc).send_keys(user_info[0])
            self.find_element(*password_loc).clear()
            self.find_element(*password_loc).send_keys(user_info[1])
            self.find_element(*login_btn_loc).click()
            logger.info(f'login success')
            time.sleep(1)

        except Exception as e:
            logger.error(f'login failed, error code: {e}')

    # 退出
    def quit_web(self):
        nav_loc = (By.CLASS_NAME, 'nav-username')
        quit_loc = (By.CLASS_NAME, 'sys-logout')
        try:
            self.find_element(*nav_loc).click()
            self.find_element(*quit_loc)
            logger.info(f'logout success')
        except Exception as e:
            logger.error(f'logout error, error code: {e}')

    # 获取当前页面网址
    def get_url(self):
        current_url = self.driver.current_url
        logger.debug(f'get current url: {current_url}')
        return current_url

    # 获取当前页面标题
    def get_title(self):
        current_title = self.driver.title
        logger.debug(f'get current title: {current_title}')
        return current_title

    def capture_page(self, filename: str = '001.png'):
        try:
            file_path = os.path.join(CAPTURE_PATH, filename)
            self.driver.execute_script("""
                        (function () {
                          var y = 0;
                          var step = 100;
                          window.scroll(0, 0);

                          function f() {
                            if (y < document.body.scrollHeight) {
                              y += step;
                              window.scroll(0, y);
                              setTimeout(f, 50);
                            } else {
                              window.scroll(0, 0);
                              document.title += "scroll-done";
                            }
                          }

                          setTimeout(f, 1000);
                        })();
                        """)
            time.sleep(2)
            self.driver.save_screenshot(filename=file_path)
            logger.info(f'save screenshot success, save path: {file_path}')
        except Exception as e:
            logger.error(f'save screenshot failed, error code: {e}')

    # 获取所有标签
    def get_handles(self):
        return self.driver.window_handles

    def switch_to_window(self, handel=''):
        return self.driver.switch_to.window(handel)

    def action_move_to(self, loc=''):
        action = ActionChains(self.driver)
        action.move_to_element(self.find_element(*loc))
        action.perform()

    def action_move_to_click(self, loc=''):
        action = ActionChains(self.driver)
        action.click(self.find_element(*loc))
        action.perform()

    def try_tag_title(self, loc):
        try:
            data = self.find_element(*loc).text
            return data
        except ElementNotVisibleException:
            return None

    def try_find_dom_text(self, loc):
        elet = self.find_element(*loc)
        html = elet.get_attribute('innerHTML')
        return BeautifulSoup(html, 'html.parser').text

    # 退出浏览器
    def dispose(self):
        return self.driver.quit()
