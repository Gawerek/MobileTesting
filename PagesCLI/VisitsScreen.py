import time

from PagesCLI.BasePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from PagesCLI.BookVisitScreen import BookVisitScreen
from Variables.variables import *


class VisitsScreen(BasePage):
    another_time_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='inny termin']")
    phone_number_label = (AppiumBy.XPATH,"//android.widget.TextView[contains(@text,'Numer telefonu:')]")
    name_label = (AppiumBy.ACCESSIBILITY_ID,"settings-name-text")
    def __init__(self, driver):
        super().__init__(driver)


    def click_another_time(self):
        self.click(self.another_time_button)
        return BookVisitScreen(self.driver)

