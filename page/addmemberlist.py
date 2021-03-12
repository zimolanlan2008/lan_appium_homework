"""
添加方式列表页面
"""
from appium.webdriver.common.mobileby import MobileBy

from page.basepage import BasePage
from page.manualadd import ManualAdd


class AddMemberList(BasePage):
    def goto_manualadd(self):
        self.parse_action("../page/main.yaml")

        # self.find_click("//*[@text = '手动输入添加']")
        # self.driver.find_element(MobileBy.XPATH, "//*[@text = '手动输入添加']").click()
        return ManualAdd(self.driver)
