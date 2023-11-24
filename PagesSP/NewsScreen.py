import time


from .BasePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy


from Variables.variables import *
class NewsScreen(BasePage):
    accept_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='Akceptuj']")
    more_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='Więcej']")
    reject_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='Odrzuć']")
    reschedule_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='Zmień termin']")
    cancel_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='Odwołaj']")

    def __init__(self, driver):
        super().__init__(driver)
    def accept_visit(self):
        self.click_index(self.accept_button, 0)

    def click_more(self, index):
        self.click_index(self.more_button, index)

    def reject_visit(self):
        self.click(self.reject_button)

    def cancel_visit(self):
        self.click(self.cancel_button)
