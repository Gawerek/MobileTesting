import time

from Pages.BasePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from Pages.ConfirmationScreen import ConfirmationScreen

from Variables.variables import *
from Utilities.scroll_util import ScrollUtil

class BookVisitScreen(BasePage):
    book_button = (AppiumBy.ACCESSIBILITY_ID, "booking-button")
    general_time_slot = (AppiumBy.ACCESSIBILITY_ID, "booking-time-slot-button-")
    mobile_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='usługi mobilne']")
    change_time_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='zmień termin']")
    address_input = (AppiumBy.XPATH, "//android.widget.EditText[@text='adres']")
    def __init__(self, driver):
        super().__init__(driver)




    def click_book_button(self):
        ScrollUtil.scrollToTextByAndroidUIAutomator("zarezerwuj", self.driver)
        self.click(self.book_button)
        return ConfirmationScreen(self.driver)

    def click_change_time_button(self):
        ScrollUtil.scrollToTextByAndroidUIAutomator("zmień termin", self.driver)
        self.click(self.change_time_button)
        return ConfirmationScreen(self.driver)

    def configure_mobile_visits(self, address):
        self.click(self.mobile_button)
        self.type(self.address_input, address)