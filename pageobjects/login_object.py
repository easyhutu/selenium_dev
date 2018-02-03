"""
CREAt: 2017/3/22
AUTHOR: Hehahutu
"""
from test_case.page_object import Page
from selenium.webdriver.common.by import By
import time


class Login(Page):
    username_loc = (By.ID, 'username')
    password_loc = (By.ID, 'password')
    login_btn_loc = (By.CLASS_NAME, 'login-btn')
    login_info_loc = (By.CLASS_NAME, 'nav-username')

    def type_username(self):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(self.username)

    def type_password(self):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(self.password)

    def login_submit(self):
        self.find_element(*self.login_btn_loc).click()
        time.sleep(2)

    def test_user_login(self):
        self.login_web()

