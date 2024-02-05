import time
from Utilities.scroll_util import *
from .BasePageSP import BasePageSP
from .ProfileServiceScreenSP import ProfileServicesScreenSP
from appium.webdriver.common.appiumby import AppiumBy
from .ProfileInfoScreenSP import ProfileInfoScreenSP
from .ProfilePortfolioScreenSP import ProfilePortfolioScreenSP

from Variables.variables import *


class ProfileDataScreenSP(BasePageSP):
    profile_info_tab = (AppiumBy.ACCESSIBILITY_ID, "account-information-button-text")
    profile_services_tab = (AppiumBy.ACCESSIBILITY_ID, "account-services-button-text")
    profile_work_mode_tab = (AppiumBy.ACCESSIBILITY_ID, "account-work-mode-button-text")
    profile_hours_tab = (AppiumBy.ACCESSIBILITY_ID, "account-hours-button-text")
    profile_gallery_tab = (AppiumBy.ACCESSIBILITY_ID, "account-gallery-button-text")
    profile_preview_button = (AppiumBy.ACCESSIBILITY_ID, "profile-preview-button-text")
    profile_submit_button = (AppiumBy.ACCESSIBILITY_ID, "profile-submit-button")
    back_button = (AppiumBy.ACCESSIBILITY_ID,"header-back-button")
    # ok_button = (AppiumBy.CLASS_NAME, "android.widget.Button")
    ok_button = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView")
    x_button = (AppiumBy.ACCESSIBILITY_ID,"account-close-button")

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
        self.click(self.profile_gallery_tab)
        return ProfilePortfolioScreenSP(self.driver)

    def click_profile_preview_tab(self):
        self.click(self.profile_preview_button)

    def click_profile_submit(self):
        ScrollUtil.scrollToAccessibilityIdByAndroidUIAutomator("profile-submit-button", self.driver)
        self.click(self.profile_submit_button)
        self.click(self.ok_button)

    def click_back_button(self):
        ScrollUtil.scrollToAccessibilityIdByAndroidUIAutomator("header-back-button", self.driver)
        self.click(self.back_button)

    def click_close_account(self):
        self.click(self.x_button)
