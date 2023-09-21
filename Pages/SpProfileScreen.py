import time

from Pages.BasePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from Pages.BookVisitScreen import BookVisitScreen

from Variables.variables import *

class SpProfileScreen(BasePage):
    book_buttons = (AppiumBy.XPATH, "//android.widget.TextView[@text='Umów']")

    def __init__(self, driver):
        super().__init__(driver)

    def book_service(self):
        self.click_index(self.book_buttons,0)
        return BookVisitScreen(self.driver)
