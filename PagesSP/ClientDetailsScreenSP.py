import time

from .BasePageSP import BasePageSP

from appium.webdriver.common.appiumby import AppiumBy



class ClientDetailsScreen(BasePageSP):
    client_profile_name_locator = (AppiumBy.ACCESSIBILITY_ID, "client-profile-name")
    client_profile_input_locator = (AppiumBy.ACCESSIBILITY_ID, "client-profile-name-input")
    phone_number_prefix_picker = (AppiumBy.ACCESSIBILITY_ID,"client-profile-phone-number-input-picker-select-react-native-picker-select")
    client_phone_number_input = (AppiumBy.ACCESSIBILITY_ID,"client-profile-phone-number-input-phone-number")
    client_birth_date_input = (AppiumBy.ACCESSIBILITY_ID, "add-client-birth-date-input")
    client_address_input = (AppiumBy.ACCESSIBILITY_ID, "client-profile--address-input-location-input-autocomplete")
    client_note_input = (AppiumBy.ACCESSIBILITY_ID, "add-client-note-input")

    def verify_profile_details(self, client_name, client_address, client_phone):
        profile_name_element = self.find_element(self.client_profile_name_locator)
        profile_input_element = self.find_element(self.client_profile_input_locator)
        profile_phone_element = self.find_element(self.client_phone_number_input)
        profile_address_element = self.find_element(self.client_address_input)
        standardized_client_address = ' '.join(client_address.split())
        standardized_profile_address = ' '.join(profile_address_element.text.split())


        assert client_phone == profile_phone_element.text
        assert standardized_client_address == standardized_profile_address
        assert profile_input_element.text, profile_name_element.text == client_name
