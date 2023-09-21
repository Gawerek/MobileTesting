import time
from Pages.BasePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from Variables.variables import *
from Pages.SpProfileScreen import SpProfileScreen


class MapScreen(BasePage):
    check_services = (AppiumBy.XPATH, "//android.widget.TextView[@text='Zobacz usługi']")
    sp_name_text = (AppiumBy.ACCESSIBILITY_ID, "cli-search-sp-name-text")

    def __init__(self, driver):
        super().__init__(driver)

    def assert_name(self,text):
        sp_name = self.getText(self.sp_name_text)
        assert text == sp_name

    def click_on_check_services(self):
        self.click(self.check_services)
        return SpProfileScreen(self.driver)