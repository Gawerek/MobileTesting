import time
from Utilities.scroll_util import *
from .BasePageSP import BasePageSP
from .ProfileServiceScreenSP import ProfileServicesScreenSP
from appium.webdriver.common.appiumby import AppiumBy
from .ProfileInfoScreenSP import ProfileInfoScreenSP
from .ProfilePortfolioScreenSP import ProfilePortfolioScreenSP

from Variables.variables import *


class ProfileDataScreenSP(BasePageSP):
    profile_info_tab = (AppiumBy.ACCESSIBILITY_ID, "profile-info-tab")
    profile_services_tab = (AppiumBy.ACCESSIBILITY_ID, "profile-services-tab")
    profile_location_tab = (AppiumBy.ACCESSIBILITY_ID, "profile-location-tab")
    profile_hours_tab = (AppiumBy.ACCESSIBILITY_ID, "profile-hours-tab")
    profile_gallery_tab = (AppiumBy.ACCESSIBILITY_ID, "profile-gallery-tab")
    profile_preview_button = (AppiumBy.ACCESSIBILITY_ID, "profile-preview-button-text")
    profile_submit_button = (AppiumBy.ACCESSIBILITY_ID, "profile-submit-button-text")
    back_button = (AppiumBy.ACCESSIBILITY_ID,"header-back-button")
    ok_button = (AppiumBy.CLASS_NAME, "android.widget.Button")



    def click_profile_info_tab(self):
        self.click(self.profile_info_tab)
        return ProfileInfoScreenSP(self.driver)

    def click_services_tab(self):
        self.click(self.profile_services_tab)
        return ProfileServicesScreenSP(self.driver)
    def click_profile_location_tab(self):
        self.click(self.profile_location_tab)

    def click_profile_hours_tab(self):
        self.click(self.profile_hours_tab)

    def click_profile_gallery_tab(self):
        ScrollUtil.scrollToAccessibilityIdByAndroidUIAutomator("profile-gallery-tab",self.driver, horizontal=True)
        self.click(self.profile_gallery_tab)
        return ProfilePortfolioScreenSP(self.driver)

    def click_profile_preview_tab(self):
        self.click(self.profile_preview_button)

    def click_profile_submit(self):
        self.click(self.profile_submit_button)
        self.click(self.ok_button)

    def click_back_button(self):
        self.click(self.back_button)