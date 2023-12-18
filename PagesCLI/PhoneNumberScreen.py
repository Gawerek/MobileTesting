import time

from PagesCLI.BasePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from PagesCLI.CodeScreen import CodeScreen
from Variables.variables import *


class PhoneNumberScreen(BasePage):
    country_dropdown = (AppiumBy.XPATH, "//android.widget.EditText[contains(@text, '+48')]")
    # phone_number_input = (AppiumBy.ACCESSIBILITY_ID, "auth-phone-input")
    phone_number_input = (AppiumBy.ACCESSIBILITY_ID, "auth-phone-number-input")
    # name_input = (AppiumBy.ACCESSIBILITY_ID, "-name-input") android.widget.EditText
    name_input = (AppiumBy.XPATH, "//android.widget.EditText[@text='Imię i nazwisko']")
    next_button = (AppiumBy.ACCESSIBILITY_ID, "auth-next-button")
    back_button = (AppiumBy.ACCESSIBILITY_ID, "auth-back-button")
    country_prefix_buttons = {
        '48': (AppiumBy.XPATH, "//android.widget.CheckedTextView[contains(@text, '+48')]"),
        '49': (AppiumBy.XPATH,
               "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[3]"),
        '380': (AppiumBy.XPATH,
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[4]"),
        '421': (AppiumBy.XPATH,
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[5]"),
        '43': (AppiumBy.XPATH,
               "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[6]")
    }

    def __init__(self, driver):
        super().__init__(driver)

    def registration_provide_phone_number_and_click_next(self, phone_number=login_number, change_country=False,
                                                         country_code=None,
                                                         name=None):
        if change_country:

            self.click(self.country_dropdown)

            if country_code and country_code in self.country_prefix_buttons:
                self.click(self.country_prefix_buttons[country_code])

        if name:
            self.type(self.name_input, name)

        self.type(self.phone_number_input, phone_number)

        self.click(self.next_button)
        return CodeScreen(self.driver)

    def login_provide_phone_number_and_click_next(self, phone_number=login_number, change_country=False,
                                                  country_code=None,
                                                  ):
        if change_country:

            self.click(self.country_dropdown)

            if country_code and country_code in self.country_prefix_buttons:
                self.click(self.country_prefix_buttons[country_code])

        self.type(self.phone_number_input, phone_number)

        self.click(self.next_button)
        return CodeScreen(self.driver)
