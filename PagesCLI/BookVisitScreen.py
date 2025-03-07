import time

from PagesCLI.BasePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from PagesCLI.ConfirmationScreen import ConfirmationScreen


from Variables.variables import *
from Utilities.scroll_util import ScrollUtil


from Utilities.DataSaver import DataSaver

class BookVisitScreen(BasePage):
    book_button = (AppiumBy.ACCESSIBILITY_ID, "booking-button-text")
    selected_service = (AppiumBy.ACCESSIBILITY_ID,"booking-choosen-service-text-")
    total_cost = (AppiumBy.ACCESSIBILITY_ID, "booking-total-cost")
    total_duration = (AppiumBy.ACCESSIBILITY_ID, "booking-total-duration")
    time_slot_locator = (AppiumBy.ACCESSIBILITY_ID, "booking-time-slot-button-")
    show_more_button = (AppiumBy.ACCESSIBILITY_ID, "booking-calendar-toggle-expand-button")
    mobile_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='z dojazdem do klienta']")
    change_time_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='zmień termin']")
    address_input = (AppiumBy.XPATH, "//android.widget.EditText[@text='adres']")
    def __init__(self, driver):
        super().__init__(driver)



    def click_book_button(self):
        duration = self.getText(self.total_duration)
        # service = self.getText(self.selected_service) - add logic to create locator in LocatoryFactory
        price = self.getText(self.total_cost)

        data = {
            'Duration': duration,
            # 'Service': service,
            'Price': price
        }

        for key, item in data.items():
            print(item)
        DataSaver.save_to_excel(data, 'Book Visit Screen Data')



        ScrollUtil.scrollToAccessibilityIdByAndroidUIAutomator("booking-button-text", self.driver)
        self.click(self.book_button)
        return ConfirmationScreen(self.driver)

    def click_change_time_button(self):
        ScrollUtil.scrollToTextByAndroidUIAutomator("zmień termin", self.driver)
        self.click(self.change_time_button)
        return ConfirmationScreen(self.driver)

    def configure_mobile_visits(self, address):
        ScrollUtil.scrollToTextByAndroidUIAutomator("z dojazdem do klienta", self.driver)
        self.click(self.mobile_button)
        self.type(self.address_input, address)



    def get_available_time_slots(self):
        return self.driver.find_elements(*self.time_slot_locator)

    def select_first_available_time_slot(self):
        available_time_slots = self.get_available_time_slots()

        for slot in available_time_slots:
            if slot.is_enabled():
                slot.click()
                return slot.get_attribute("content-desc")  # Return the selected time slot description
        return None  # Return None if no available slot is found

    def select_specific_time_slot(self, time):
        available_time_slots = self.get_available_time_slots()

        for slot in available_time_slots:
            if slot.get_attribute("content-desc") == time and slot.is_enabled():
                slot.click()
                return True
        return False  # Return False if the specified time slot is not found or not available
