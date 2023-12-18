import time

from PagesCLI.BasePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy

from Variables.variables import *


class SettingsScreen(BasePage):
    delete_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='usuń konto']")
    log_out_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='wyloguj się']")
    confirmation_yes_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='tak']")
    confirmation_no_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='nie']")
    phone_number_label = (AppiumBy.XPATH,"//android.widget.TextView[contains(@text,'Numer telefonu:')]")
    name_label = (AppiumBy.ACCESSIBILITY_ID,"settings-name-text")
    def __init__(self, driver):
        super().__init__(driver)



    def assert_phone_number(self,assert_phone_number):
        phone_number_text = self.getText(self.phone_number_label)
        print(phone_number_text)
        assert assert_phone_number in phone_number_text

    def assert_name(self,assert_name):
        name_text = self.getText(self.name_label)
        print(name_text)
        assert assert_name in name_text

    def delete_account(self, delete=True):
        self.click(self.delete_button)
        if delete:
            self.click(self.confirmation_yes_button)
        else:
            self.click(self.confirmation_no_button)
        time.sleep(2)

    def log_out_account(self, log_out=True):
        self.click(self.log_out_button)
        if log_out:
            self.click(self.confirmation_yes_button)
            time.sleep(3)
        else:
            self.click(self.confirmation_no_button)

