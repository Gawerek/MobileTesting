import time

from Pages.BasePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from Pages.BookVisitScreen import BookVisitScreen

from Variables.variables import *

class SpProfileScreen(BasePage):
    japan_manicure = (AppiumBy.ACCESSIBILITY_ID, "profile-schedule-button-1003000")
    classic_massage_category = (AppiumBy.ACCESSIBILITY_ID, "profile-schedule-button-10000000")
    classic_massage_1h = (AppiumBy.ACCESSIBILITY_ID, "profile-schedule-button-10001002")

    def __init__(self, driver):
        super().__init__(driver)

    def select_service_category(self, category):
        if category == "classic_massage_category":
            self.click(self.classic_massage_category)
        # Add more categories as needed
        return self


    def book_service(self, service=None):
        if service == "japan_manicure":
            self.click(self.japan_manicure)
        if service == "classic_massage_1h":
            self.click(self.classic_massage_subcategory)
        return BookVisitScreen(self.driver)