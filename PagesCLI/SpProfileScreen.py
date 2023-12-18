import time

from PagesCLI.BasePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from PagesCLI.BookVisitScreen import BookVisitScreen
from Utilities.LocatoryFactory import LocatorFactory

from Variables.variables import *

class SpProfileScreen(BasePage):
    japan_manicure = (AppiumBy.ACCESSIBILITY_ID, "sp-profile-services-select-button-1003000")
    classic_massage_category = (AppiumBy.ACCESSIBILITY_ID, "sp-profile-services-select-button-1003000")
    classic_massage_1h = (AppiumBy.ACCESSIBILITY_ID, "profile-schedule-button-10001002")

    def __init__(self, driver):
        super().__init__(driver)

    def select_service_category(self, category):
        if category == "classic_massage_category":
            self.click(self.classic_massage_category)
        # Add more categories as needed
        return self


    def book_service(self, service=None):
        service_locator = LocatorFactory.create_service_locator(service)
        self.click(service_locator)

        return BookVisitScreen(self.driver)