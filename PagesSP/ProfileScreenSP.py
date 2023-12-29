import time
from Utilities.scroll_util import *
from .BasePageSP import BasePageSP
from appium.webdriver.common.appiumby import AppiumBy
from .ProfileDataScreenSP import ProfileDataScreenSP
from Variables.variables import *


class ProfileScreenSP(BasePageSP):
    account_name_label = (AppiumBy.ACCESSIBILITY_ID, "account-name")
    account_status_label = (AppiumBy.ACCESSIBILITY_ID,"account-status")
    profile_data_button = (AppiumBy.ACCESSIBILITY_ID, "account-profile-data-button")
    opinions_button = (AppiumBy.ACCESSIBILITY_ID,"account-reviews-button")
    settings_button = (AppiumBy.ACCESSIBILITY_ID,"account-settings-button")
    share_button = (AppiumBy.ACCESSIBILITY_ID,"share-button-text")
    copy_link_button = (AppiumBy.ACCESSIBILITY_ID,"copy-link-button-text")


    def click_profile_button(self):
        self.click(self.profile_data_button)
        return ProfileDataScreenSP(self.driver)
