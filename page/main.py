"""
主页面
"""
from appium.webdriver.common.mobileby import MobileBy

from page.basepage import BasePage
from page.contactlist import Contactlist


class Main(BasePage):
    def goto_contactlist(self):
        # 点击通讯录
        self.parse_action("../page/main.yaml")
        # self.find_click("//*[@text='通讯录']")
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return Contactlist(self.driver)

