from typing import List, Dict

import yaml
from appium.webdriver.common.mobileby import MobileBy
# from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _params = {}
    # 声明一个driver
    def __init__(self, driver:WebDriver = None):
        self.driver = driver

    # 定义方法find  一定要return
    def find(self, locator):
        return self.driver.find_element(MobileBy.XPATH, locator)


    # 定义查找点击
    def find_click(self, locator):
        self.find(locator).click()

    # 定义滑动
    def swip_click(self, text):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).'
                                 f'scrollIntoView(new UiSelector().text("{text}").instance(0));').click()

    # 定义sendkeys
    def sendkeys(self, locator, value):
        self.find(locator).send_keys(value)

    def parse_action(self, path,):
        with open(path, "r", encoding="UTF-8") as f:
            steps: List[Dict] = yaml.safe_load(f)

        for step in steps:
            if step["action"] == "find":
                self.find(step["locator"])
            elif step["action"] == "find_click":
                self.find_click(step["locator"])
            elif step["action"] == "swip_click":
                self.swip_click(step["locator"])
            elif step["action"] == "sendkeys":
                content: str = step["value"]
                for param in self._params:
                    content = content.replace('{%s}'%param, self._params[param])
                self.sendkeys(step["locator"],content)
