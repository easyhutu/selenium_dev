"""
CREAt: 2017/12/18
AUTHOR: Hehahutu
"""
from helper.page_object import Page
from selenium.webdriver.common.by import By
import time
from settings import DEPARTMENT_CONFIG
from selenium.webdriver.common.keys import Keys


class DepartmentCase(Page):
    department_name = DEPARTMENT_CONFIG['门店名称'] + 'test'
    de_path = '/xtgl/mdgl/manager'
    de_tag_path = '/xtgl/mdgl/label'
    xp_add_btn = (By.XPATH, '//*[@id="xtglmdglindex"]/div[2]/div[1]/div/div[3]/div[1]')
    xp_first_dep = (By.XPATH, '//*[@id="xtglmdglindex"]/div[2]/div[2]/div[2]/ol')
    xp_first_tag = (
        By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/ol/li/div/div/span[1]')

    xp_first_dep_two = (By.XPATH, '//*[@id="xtglmdglindex"]/div[2]/div[2]/div[2]/ol/li[1]')

    # 　门店名称
    xp_dep_name = (By.XPATH, '//*[@id="xtglmdglindex"]/div[3]/div/div[1]/div[1]/div[1]/input')
    # 　店铺ID
    xp_dep_id_name = (By.XPATH, '//*[@id="xtglmdglindex"]/div[3]/div/div[1]/div[1]/div[3]/input')
    xp_zzjg_name = (By.XPATH, '//*[@id="xtglmdglindex"]/div[3]/div/div[1]/div[1]/div[4]/input')
    xp_zzjg_detail_name = (By.XPATH, '//*[@id="organTree_1_span"]')

    xp_dep_submit_btn = (By.XPATH, '//*[@id="xtglmdglindex"]/div[3]/div/table/tbody/tr[1]/td[2]/span')

    xp_dep_delete_btn = (By.XPATH, '//*[@id="xtglmdglindex"]/div[3]/div/table/tbody/tr[1]/td[1]/span')

    xp_dep_delete_btn_rel = (By.XPATH, '//*[@id="okBtn"]')

    xp_dep_tag_input = (By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div[1]/input')
    xp_dep_tag_submit_btn = (By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div/span[1]')
    xp_dep_tag_delete_btn = (By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div/span[2]')
    xp_dep_tag_select_btn = (
        By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/ol/li/div/div/span[1]')

    # xp_dep_tag_delete_btn_re = (By.XPATH, '//*[@id="okBtn"]')

    def type_add_btn(self):
        self.find_element(*self.xp_add_btn).click()

    def type_edit_dep_btn(self):
        self.find_element(*self.xp_first_dep).click()

    def type_dep_name(self, department_name):
        self.find_element(*self.xp_dep_name).clear()
        self.find_element(*self.xp_dep_name).send_keys(department_name)

    def type_dep_id_name(self, department_id):
        self.find_element(*self.xp_dep_id_name).clear()
        self.find_element(*self.xp_dep_id_name).send_keys(department_id)

    def type_zzjg_name(self):
        self.find_element(*self.xp_zzjg_name).click()
        self.find_element(*self.xp_zzjg_detail_name).click()

    def type_submit_btn(self):
        self.find_element(*self.xp_dep_submit_btn).click()

    def type_delete_dep(self):
        self.find_element(*self.xp_dep_delete_btn).click()
        time.sleep(1)
        self.find_element(*self.xp_dep_delete_btn_rel).click()

    def event_department(self, department_name, department_id):
        self.login_web()
        self.open_url_path(self.de_path)
        # self.action_move_to_click(self.xp_add_btn)
        time.sleep(1)
        self.type_add_btn()
        time.sleep(1)
        self.type_add_btn()
        self.type_dep_name(department_name)
        self.type_dep_id_name(department_id)
        self.type_zzjg_name()
        self.type_submit_btn()

    def event_department_delete(self, department_name):
        self.login_web()
        self.open_url_path(self.de_path)
        time.sleep(1)
        self.find_element(*self.xp_first_dep).click()
        self.type_delete_dep()

    def event_department_tag(self, department_tag):
        self.login_web()
        self.open_url_path(self.de_tag_path)
        self.find_element(*self.xp_dep_tag_input).send_keys(department_tag)
        self.find_element(*self.xp_dep_tag_input).send_keys(Keys.ENTER)
        time.sleep(2)
        self.find_element(*self.xp_dep_tag_submit_btn).click()

    def event_department_tag_delete(self):
        self.login_web()
        self.open_url_path(self.de_tag_path)
        self.find_element(*self.xp_dep_tag_select_btn).click()
        self.find_element(*self.xp_dep_tag_delete_btn).click()
        self.find_element(*self.xp_dep_delete_btn_rel).click()


if __name__ == '__main__':
    lp = DepartmentCase()
    lp.event_department()
    lp.event_department_delete()
