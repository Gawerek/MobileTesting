import time

from Pages.BasePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from Pages.ConfirmationScreen import ConfirmationScreen

from Variables.variables import *


class BookVisitScreen(BasePage):
    book_button = (AppiumBy.ACCESSIBILITY_ID, "booking-button")
    general_time_slot = (AppiumBy.ACCESSIBILITY_ID, "booking-time-slot-button-")

    def __init__(self, driver):
        super().__init__(driver)




    def click_book_button(self):
        self.click(self.book_button)
        return ConfirmationScreen(self.driver)