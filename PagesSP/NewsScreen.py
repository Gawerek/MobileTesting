import time
from .VisitsScreen import VisitsScreen

from .BasePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy

from Variables.variables import *
class NewsScreen(BasePage):
    accept_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='Akceptuj']")
    more_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='Więcej']")
    reject_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='Odrzuć']")
    reschedule_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='Zmień termin']")

    def accept_visit(self):
        self.click_index(self.accept_button, 1)