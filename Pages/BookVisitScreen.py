import time

from Pages.BasePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from Pages.AfterBookingScreen import AfterBookingScreen

from Variables.variables import *


class BookVisitScreen(BasePage):
    book_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='Zarezerwuj']")

    def __init__(self, driver):
        super().__init__(driver)



    def click_book_button(self):
        self.click(self.book_button)
        return AfterBookingScreen(self.driver)