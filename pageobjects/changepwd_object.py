"""
CREAt: 2017/3/23
AUTHOR: Hehahutu
"""
from test_case.page_object import Page
# from test_scripts.login_object import Login
from selenium.webdriver.common.by import By
import time


class ChangePwd(Page):

    nav_btn_loc = (By.XPATH, '//*[@id="top"]/div[2]/span[1]')
    changepwd_btn_loc = (By.XPATH, '//*[@id="top"]/div[2]/div/ul/li[2]/label')
    oldpwd_input_loc = (By.XPATH, '//*[@id="changePwdDlg"]/table/tbody/tr[1]/td[2]/input')
    newpwd_input_loc = (By.XPATH, '//*[@id="changePwdDlg"]/table/tbody/tr[2]/td[2]/input')
    renewpwd_input_loc = (By.XPATH, '//*[@id="changePwdDlg"]/table/tbody/tr[3]/td[2]/input')
    submit_loc = (By.XPATH, '//*[@id="okBtn"]')
    login_info_loc = (By.CLASS_NAME, 'nav-username')

    def type_navbtn(self):
        self.find_element(*self.nav_btn_loc).click()

    def type_changepwd_btn(self):
        self.find_element(*self.changepwd_btn_loc).click()
        time.sleep(1)

    def type_oldpwd_input(self):
        self.find_element(*self.oldpwd_input_loc).send_keys(self.password)

    def type_newpwd_input(self):
        self.find_element(*self.newpwd_input_loc).send_keys(self.password)

    def type_renewpwd_input(self):
        self.find_element(*self.renewpwd_input_loc).send_keys(self.password)

    def type_submit(self):
        self.find_element(*self.submit_loc).click()
        time.sleep(6)

    def test_change_pwd(self):
        self.open_base_url()
        self.login_web()
        time.sleep(2)
        self.type_navbtn()
        self.type_changepwd_btn()
        self.type_oldpwd_input()
        self.type_newpwd_input()
        self.type_renewpwd_input()
        self.type_submit()
        self.login_web()
        time.sleep(2)
