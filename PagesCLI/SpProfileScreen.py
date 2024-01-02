import time

from Utilities.scroll_util import *
from PagesCLI.BasePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from PagesCLI.BookVisitScreen import BookVisitScreen
from Utilities.LocatoryFactory import LocatorFactory
from .SpProfileInfoTabScreen import SpProfileInfoTabScreen

from Variables.variables import *

class SpProfileScreen(BasePage):
    japan_manicure = (AppiumBy.ACCESSIBILITY_ID, "sp-profile-services-select-button-1003000")
    classic_massage_category = (AppiumBy.ACCESSIBILITY_ID, "sp-profile-services-select-button-1003000")
    classic_massage_1h = (AppiumBy.ACCESSIBILITY_ID, "profile-schedule-button-10001002")
    sp_profile_tab_services = (AppiumBy.ACCESSIBILITY_ID, "sp-profile-tab-services")
    sp_profile_tab_info = (AppiumBy.ACCESSIBILITY_ID, "sp-profile-tab-info")
    sp_profile_tab_portfolio = (AppiumBy.ACCESSIBILITY_ID, "sp-profile-tab-portfolio")
    sp_profile_tab_reviews = (AppiumBy.ACCESSIBILITY_ID, "sp-profile-tab-reviews")
    sp_profile_name = (AppiumBy.ACCESSIBILITY_ID, "sp-profile-name")


    def __init__(self, driver):
        super().__init__(driver)

    def click_sp_profile_tab_info(self):
        self.click(self.sp_profile_tab_info)
        return SpProfileInfoTabScreen(self.driver)


    def select_service_category(self, category):
        if category == "classic_massage_category":
            self.click(self.classic_massage_category)
        # Add more categories as needed
        return self

    def verify_sp_name(self, name):
        ScrollUtil.scrollToAccessibilityIdByAndroidUIAutomator("sp-profile-name", self.driver)
        profile_name_element = self.find_element(self.sp_profile_name)
        assert name == profile_name_element.text


    def book_service(self, service=None):
        service_locator = LocatorFactory.create_service_locator(service)

        self.click(service_locator)

        return BookVisitScreen(self.driver)