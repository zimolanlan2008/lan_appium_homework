"""
启动app
启动方法
打开APP主页面

"""

from appium import webdriver

from page.basepage import BasePage
from page.main import Main


class App(BasePage):
    _package = "com.tencent.wework"
    _activity = ".launch.WwMainActivity"
    # def __init__(self):
    #     self.driver = None
    #     self.app_start()

    def app_start(self):
        # 每次启动时候不用都初始化
        if self.driver is None:
            desire_cap = {}
            desire_cap['platformName'] = 'android'
            desire_cap['deviceName'] = '127.0.0.1:7555'
            desire_cap['appPackage'] = self._package
            desire_cap["appActivity"] = self._activity
            desire_cap['automationName'] = 'uiautomator2'
            desire_cap["ensureWebviewsHavePages"] =True
            desire_cap["settings[waitForIdleTimeout]"] =0
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        else:
            self.driver.start_activity(self._package,self._activity)

        self.driver.implicitly_wait(6)
        return self

    def goto_main(self):
        # 把driver传给Main   返回到main
        return Main(self.driver)


