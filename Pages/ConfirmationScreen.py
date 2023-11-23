import time

from Pages.BasePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy

from Variables.variables import *
class ConfirmationScreen(BasePage):
    visit_list_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='przejdź do listy wizyt']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_go_to_visit_list(self):
        self.click(self.visit_list_button)
