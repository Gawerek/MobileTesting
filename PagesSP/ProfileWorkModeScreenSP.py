import time
from Utilities.scroll_util import *
from .BasePageSP import BasePageSP
from appium.webdriver.common.appiumby import AppiumBy
from Variables.variables import *


class ProfileWorkModeScreenSP(BasePageSP):
    express_reservation_button = (AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[6]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.TextView")
    standard_reservation_button = (AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[6]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.TextView")
    submit_button =(AppiumBy.ACCESSIBILITY_ID,"profile-submit-button")


    def select_reservation_mode(self, express = False):
        if express:
            self.click(self.express_reservation_button)
        else:
            self.click(self.standard_reservation_button)

    def click_submit_in_work_mode(self):
        ScrollUtil.scrollToAccessibilityIdByAndroidUIAutomator("profile-submit-button", self.driver)
        self.click(self.submit_button)