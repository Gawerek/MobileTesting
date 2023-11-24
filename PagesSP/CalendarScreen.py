import time

from .BasePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from .ManualVisitScreen import ManualVisitScreen
from Variables.variables import *


class CalendarScreen(BasePage):
    add_manual_visit_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='Dodaj wizytę']")


    def __init__(self, driver):
        super().__init__(driver)


    def click_manual_visit_button(self):
        self.click(self.add_manual_visit_button)
        return ManualVisitScreen(self.driver)
