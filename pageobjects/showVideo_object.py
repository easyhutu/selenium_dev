"""
CREAt: 2017/4/21
AUTHOR: Hehahutu
"""
from test_case.page_object import Page
from selenium.webdriver.common.by import By
import time


class ShowVideo(Page):
    video_btn_loc = (By.CLASS_NAME, 'groupbtn-topnav')
    video_item_loc = (By.LINK_TEXT, '视频巡店')
    video_list_loc = (By.LINK_TEXT, '门店列表')
    shop_name_loc = (By.LINK_TEXT, 'AA自动化测试17.14')
    driver_name_loc = (By.LINK_TEXT, 'IPCamera')
    focus_time_loc = (By.CLASS_NAME, 'time')
    capture_loc = (By.CLASS_NAME, 'capture-btn')
    capture_info_loc = (By.CLASS_NAME, 'pic-des')

    def type_video_item(self):
        self.find_element(*self.video_btn_loc).click()

    def type_list_item(self):
        self.find_element(*self.video_item_loc).click()

    def type_shop_item(self):
        self.find_element(*self.video_list_loc).click()

    def type_shop(self):
        self.find_element(*self.shop_name_loc).click()

    def type_driver(self):
        self.find_element(*self.driver_name_loc).click()

    def type_focus_time(self):
        self.action_move_to(self.focus_time_loc)

    def type_capture(self):
        self.find_element(*self.capture_loc).click()

    def test_show_video(self):
        self.open_url()
        self.login_web()
        self.type_video_item()
        self.type_list_item()
        self.type_shop_item()
        self.type_shop()
        self.type_driver()
        self.switch_to_window(self.get_handles()[-1])
        time.sleep(10)

    def test_capture_video(self):
        self.test_show_video()
        self.type_focus_time()
        self.type_capture()
        time.sleep(10)
