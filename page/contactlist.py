"""
通讯录列表页
"""


from appium.webdriver.common.mobileby import MobileBy

from page.addmemberlist import AddMemberList
from page.basepage import BasePage


class Contactlist(BasePage):
    def goto_addmemberlist(self):
        self.parse_action("../page/contactlist_page.yaml.yaml")
        # 通讯录页面滑动找添加成员按钮，找到后点击
        # ele = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                                'new UiScrollable(new UiSelector().scrollable(true).instance(0)).'
        #                                'scrollIntoView(new UiSelector().text("添加成员").instance(0));')
        # ele.click()
        # self.swip_click("添加成员")
        return AddMemberList(self.driver)

