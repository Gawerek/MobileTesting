import time
from Utilities.scroll_util import *
from .BasePageSP import BasePageSP
from appium.webdriver.common.appiumby import AppiumBy
from .ProfileInfoScreenSP import ProfileInfoScreenSP

from Variables.variables import *


class ProfileDataScreenSP(BasePageSP):
    profile_info_tab = (AppiumBy.ACCESSIBILITY_ID, "profile-info-tab")
    profile_services_tab = (AppiumBy.ACCESSIBILITY_ID, "profile_services_tab")
    profile_location_tab = (AppiumBy.ACCESSIBILITY_ID, "profile_location_tab")
    profile_hours_tab = (AppiumBy.ACCESSIBILITY_ID, "profile_hours_tab")
    profile_gallery_tab = (AppiumBy.ACCESSIBILITY_ID, "profile_gallery_tab")
    profile_preview_button = (AppiumBy.ACCESSIBILITY_ID, "profile-preview-button-text")
    profile_submit_button = (AppiumBy.ACCESSIBILITY_ID, "profile-submit-button-text")



    def click_profile_info_tab(self):
        self.click(self.profile_info_tab)
        return ProfileInfoScreenSP(self.driver)

    def click_services_tab(self):
        self.click(self.profile_services_tab)

    def click_profile_location_tab(self):
        self.click(self.profile_location_tab)

    def click_profile_hours_tab(self):
        self.click(self.profile_hours_tab)

    def click_profile_gallery_tab(self):
        self.click(self.profile_gallery_tab)

    def click_profile_preview_tab(self):
        self.click(self.profile_preview_button)

    def click_profile_submit(self):
        self.click(self.profile_submit_button)
