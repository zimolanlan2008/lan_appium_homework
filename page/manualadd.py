"""
手动添加联系人输入页面
"""
from appium.webdriver.common.mobileby import MobileBy

from page.basepage import BasePage


class ManualAdd(BasePage):
    def adding(self, username, phonenum, address):
        self._params["username"] = username
        self._params["phonenum"] = phonenum
        self._params["address"] = address

        self.parse_action("../page/manualadd_page.yaml")
        # 进入到手动添加页面，页面元素操作，姓名
        # self.sendkeys("//*[@resource-id='com.tencent.wework:id/b7m']","lantest06")
        # # self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/b7m']").send_keys("lantest04")
        #
        #
        # # 性别点击，之后选择男  android.widget.FrameLayout
        # # self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/b8p']").click()
        # # self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/eso']").click()
        # # self.driver.find_element(MobileBy.XPATH, "(//*[@resource-id='com.tencent.wework:id/bp9'])[2]").click()
        # self.find_click("//*[@resource-id='com.tencent.wework:id/eso']")
        # self.find_click("(//*[@resource-id='com.tencent.wework:id/bp9'])[2]")
        #
        # # 输入手机号
        # # self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/fwi']").send_keys(
        # #     "13200000004")
        # self.sendkeys("//*[@resource-id='com.tencent.wework:id/fwi']","13200000006")
        #
        # # 点击地址 多个元素
        # # print(self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/b8p']"))
        # # self.driver.find_element(MobileBy.XPATH, "(//*[@resource-id='com.tencent.wework:id/b8p'])[2]").click()
        # self.find_click("(//*[@resource-id='com.tencent.wework:id/b8p'])[2]")
        #
        # # 地址栏输入惠康家园
        # # self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/js']").send_keys("惠康家园")
        # self.sendkeys("//*[@resource-id='com.tencent.wework:id/js']","惠康家园")
        #
        # # 对某个结果点击
        # # self.driver.find_element(MobileBy.XPATH,
        # #                          "//*[@resource-id='com.tencent.wework:id/ilc' and @text = '北京市门头沟区上园路']").click()
        # self.find_click("//*[@resource-id='com.tencent.wework:id/ilc' and @text = '北京市门头沟区上园路']")
        #
        # # 点击确定
        # # self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/igh"]').click()
        # self.find_click('//*[@resource-id="com.tencent.wework:id/igh"]')
        # # 点击保存
        # # self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/aj_"]').click()
        # self.find_click('//*[@resource-id="com.tencent.wework:id/aj_"]')

        # 结果页面进行校验,消息弹框
        # message = self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'添加成功')]").text
        # message = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        # message = self.find("//*[@class='android.widget.Toast']").text
        message = self.find("//*[contains(@text,'添加成功')]").text
        print(message)
        assert message == "添加成功"
