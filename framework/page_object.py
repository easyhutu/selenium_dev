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
from settings import Config
from bs4 import BeautifulSoup


class Page:
    def __init__(self, path='/', wait=30):

        self.conf = Config
        self.url = self.conf['url']
        self.username = self.conf['username']
        self.password = self.conf['password']

        option = webdriver.ChromeOptions()
        option.add_argument('--user-data-dir={}'.format(self.conf['browser_conf']))
        if self.conf['driver_type'] == 'Chrome':

            self.driver = webdriver.Chrome(chrome_options=option) if self.conf['EN_CONFIG'] else webdriver.Chrome()

        elif self.conf['driver_type'] == 'Firefox':
            self.driver = webdriver.Firefox(executable_path='E:\\gecker\\geckodriver.exe')

        self.driver.implicitly_wait(wait)
        self.path = path
        self.By = By

    # 打开网址
    def open_base_url(self):
        self.driver.maximize_window()
        self.driver.get(self.url + self.path)
        print(self.url + self.path)

    def open_url(self, url):
        self.driver.get(url)
        print(url)

    def open_url_path(self, path='/'):
        url = f'{self.url}/index.html?#{path}'
        self.driver.get(url)
        print(url)

    # 定位元素
    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    # 登录
    def login_web(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        username_loc = (By.ID, 'username')
        password_loc = (By.ID, 'password')
        login_btn_loc = (By.CLASS_NAME, 'login-btn')

        self.find_element(*username_loc).clear()
        self.find_element(*username_loc).send_keys(self.username)
        self.find_element(*password_loc).clear()
        self.find_element(*password_loc).send_keys(self.password)
        self.find_element(*login_btn_loc).click()
        time.sleep(1)

    # 退出
    def quit_web(self):
        nav_loc = (By.CLASS_NAME, 'nav-username')
        quit_loc = (By.CLASS_NAME, 'sys-logout')
        time.sleep(2)
        self.find_element(*nav_loc).click()
        self.find_element(*quit_loc)

    # 获取当前页面网址
    def get_url(self):
        return self.driver.current_url

    # 获取当前页面标题
    def get_title(self):
        return self.driver.title

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
