import time

from .BasePageSP import BasePageSP
from appium.webdriver.common.appiumby import AppiumBy
from Variables.variables import *


class AddClientScreenSP(BasePageSP):
    client_name_input = (AppiumBy.ACCESSIBILITY_ID, "add-client-name-input-name-input")
    phone_number_prefix_picker = (AppiumBy.ACCESSIBILITY_ID,"add-client-phone-number-input-picker-select-react-native-picker-select")
    client_phone_number_input = (AppiumBy.ACCESSIBILITY_ID,"add-client-phone-number-input-phone-number")
    client_birth_date_input = (AppiumBy.ACCESSIBILITY_ID, "add-client-birth-date-input")
    client_address_input = (AppiumBy.XPATH, "//android.widget.EditText[@text='adres']")
    client_note_input = (AppiumBy.ACCESSIBILITY_ID, "add-client-note-input")
    next_button = (AppiumBy.ACCESSIBILITY_ID,"add-client-submit-button-text")
    success_button = (AppiumBy.ACCESSIBILITY_ID, "add-client-success-navigate-to-clients-button-text")


    def __init__(self, driver):
        super().__init__(driver)

    def add_new_client(self, name, address, phone):
        self.type(self.client_name_input, name)
        self.type(self.client_address_input, address)
        self.type(self.client_phone_number_input, phone)
        self.click(self.next_button)
        self.click(self.success_button)



