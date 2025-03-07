import time
from PagesCLI.BasePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from Variables.variables import *
from PagesCLI.SpProfileScreen import SpProfileScreen
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MapScreen(BasePage):
    check_services = (AppiumBy.ACCESSIBILITY_ID, "map-choose-sp-button")
    sp_name_text = (AppiumBy.ACCESSIBILITY_ID, "map-sp-preview-card-name-text")
    back_button = (AppiumBy.ACCESSIBILITY_ID, "map-back-button")

    def __init__(self, driver):
        super().__init__(driver)

    def assert_name(self, text):
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(self.sp_name_text, text)
        )
        sp_name = self.getText(self.sp_name_text)
        assert text == sp_name

    def click_on_check_services(self):
        self.click(self.check_services)
        return SpProfileScreen(self.driver)

    def click_back_button(self):
        self.click(self.back_button)

