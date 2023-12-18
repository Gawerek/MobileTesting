import time

from PagesCLI.BasePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from PagesCLI.ConfirmationScreen import ConfirmationScreen


from Variables.variables import *
from Utilities.scroll_util import ScrollUtil

class BookVisitScreen(BasePage):
    book_button = (AppiumBy.ACCESSIBILITY_ID, "booking-button")
    selected_service = (AppiumBy.ACCESSIBILITY_ID,"booking-choosen-service-text")
    service_price = (AppiumBy.ACCESSIBILITY_ID,"booking-price-of-service-text")
    service_duration = (AppiumBy.ACCESSIBILITY_ID, "booking-time-of-service-text" )
    time_slot_locator = (AppiumBy.ACCESSIBILITY_ID, "booking-time-slot-button-")
    show_more_button = (AppiumBy.ACCESSIBILITY_ID, "booking-calendar-toggle-expand-button")
    mobile_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='usługi mobilne']")
    change_time_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='zmień termin']")
    address_input = (AppiumBy.XPATH, "//android.widget.EditText[@text='adres']")
    def __init__(self, driver):
        super().__init__(driver)



    def click_book_button(self):
        duration = self.getText(self.service_duration)
        service = self.getText(self.selected_service)
        price = self.getText(self.service_price)
        result = (f"czas ={duration},\n"
               f"serwis = {service},\n"
               f"cena = {price}\n")
        print(f"Booking result -{result}")


        ScrollUtil.scrollToTextByAndroidUIAutomator("zarezerwuj", self.driver)
        self.click(self.book_button)
        return ConfirmationScreen(self.driver)

    def click_change_time_button(self):
        ScrollUtil.scrollToTextByAndroidUIAutomator("zmień termin", self.driver)
        self.click(self.change_time_button)
        return ConfirmationScreen(self.driver)

    def configure_mobile_visits(self, address):
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
