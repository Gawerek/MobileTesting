import time
from Utilities.scroll_util import *
from .BasePageSP import BasePageSP
from appium.webdriver.common.appiumby import AppiumBy
from .ProfileDataScreenSP import ProfileDataScreenSP
from .ProfileWorkModeScreenSP import ProfileWorkModeScreenSP
from Variables.variables import *


class ProfileScreenSP(BasePageSP):
    account_name_label = (AppiumBy.ACCESSIBILITY_ID, "account-name")
    account_work_mode_button = (AppiumBy.ACCESSIBILITY_ID,"account-work-mode-button-text")
    account_status_label = (AppiumBy.ACCESSIBILITY_ID,"account-status")
    profile_data_button = (AppiumBy.ACCESSIBILITY_ID, "account-information-button-text")
    opinions_button = (AppiumBy.ACCESSIBILITY_ID,"account-reviews-button")
    settings_button = (AppiumBy.ACCESSIBILITY_ID,"account-settings-button")
    share_button = (AppiumBy.ACCESSIBILITY_ID,"share-button-text")
    copy_link_button = (AppiumBy.ACCESSIBILITY_ID,"copy-link-button-text")


    def click_profile_button(self):
        self.click(self.profile_data_button)
        return ProfileDataScreenSP(self.driver)

    def click_account_work_mode_button(self):
        self.click(self.account_work_mode_button)
        return ProfileWorkModeScreenSP(self.driver)
