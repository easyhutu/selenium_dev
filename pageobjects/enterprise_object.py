"""
CREAt: 2017/12/13
AUTHOR: Hehahutu
"""
from helper.page_object import Page
import time
from selenium.webdriver.common.by import By
from settings import ENTERPRISE_CONFIG


class EnterpriseCase(Page):
    xp_edit_en = (By.XPATH, '//*[@id="enterpriseindex"]/div[1]/div[2]/div[1]/ol/li')
    xp_enterprise_name = (By.XPATH, '//*[@id="enterpriseindex"]/div[2]/div[1]/div[1]/div[1]/div[1]/input')
    xp_phone = (By.XPATH, '//*[@id="enterpriseindex"]/div[2]/div[1]/div[1]/div[1]/div[4]/input')
    xp_system_name = (By.XPATH, '//*[@id="enterpriseindex"]/div[2]/div[1]/div[1]/div[1]/div[6]/input')
    xp_connect_user = (By.XPATH, '//*[@id="enterpriseindex"]/div[2]/div[1]/div[1]/div[1]/div[7]/input')

    xp_submit_btn = (By.XPATH, '//*[@id="enterpriseindex"]/div[2]/div[1]/span[2]')

    def type_btn_edit(self):
        self.find_element(*self.xp_edit_en).click()

    def type_enterprise_name_edit(self):
        self.find_element(*self.xp_enterprise_name).clear()
        self.find_element(*self.xp_enterprise_name).send_keys(ENTERPRISE_CONFIG['企业名称'])

    def type_phone_edit(self):
        self.find_element(*self.xp_phone).clear()
        self.find_element(*self.xp_phone).send_keys(ENTERPRISE_CONFIG['手机号码'])

    def type_system_name_edit(self):
        self.find_element(*self.xp_system_name).clear()
        self.find_element(*self.xp_system_name).send_keys(ENTERPRISE_CONFIG['系统名称'])

    def type_connect_user_edit(self):
        self.find_element(*self.xp_connect_user).clear()
        self.find_element(*self.xp_connect_user).send_keys(ENTERPRISE_CONFIG['联系人'])

    def type_submit_edit(self):
        self.find_element(*self.xp_submit_btn).click()

    def test_enterprise(self):
        self.open_base_url()
        self.login_web()
        self.open_url_path('/xtgl/qygl')
        time.sleep(5)
        self.type_btn_edit()
        time.sleep(1)
        self.type_enterprise_name_edit()
        self.type_phone_edit()
        self.type_system_name_edit()
        self.type_connect_user_edit()
        self.type_submit_edit()
        time.sleep(5)
        self.type_btn_edit()
        time.sleep(1)

    def get_enterprise_name(self):
        return self.find_element(*self.xp_enterprise_name).get_attribute('value')


if __name__ == '__main__':
    te = EnterpriseCase()
    te.test_enterprise()
