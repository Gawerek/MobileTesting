import time
from Utilities.scroll_util import *
from .BasePageSP import BasePageSP
from appium.webdriver.common.appiumby import AppiumBy

from Variables.variables import *


class ManualVisitScreenSP(BasePageSP):
    nails_category_button = (AppiumBy.ACCESSIBILITY_ID, "book-manual-visit-screen-accordion-header-1000000-title")
    hybrid_manicure_category_button = (AppiumBy.ACCESSIBILITY_ID, "book-manual-visit-screen-outline-button-1003000-text")
    barber_category_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='Barber']")
    save_button = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'zapisz')]")
    mobile_type_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='z dojazdem do klienta']")
    client_input = (AppiumBy.XPATH, "//android.widget.EditText[@text='Wybierz lub wyszukaj klienta']")
    phone_input = (AppiumBy.XPATH, "//android.widget.EditText[@text='Podaj numer telefonu']")
    address_input = (AppiumBy.XPATH, "//android.widget.EditText[@text='Adres klienta']")
    drive_price_input = (AppiumBy.XPATH, "//android.widget.EditText[@text='Cena za dojazd']")
    confirm_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='przejdź do listy wizyt']")
    def __init__(self, driver):
        super().__init__(driver)

    def click_manual_visit_button(self):
        self.click(self.add_manual_visit_button)

    def enter_client_name(self, name):
        self.clear_field(self.client_input)
        self.type(self.client_input, name)

    def enter_phone_number(self, phone_number):
        self.clear_field(self.phone_input)
        self.type(self.phone_input, phone_number)

    def select_service(self):
        self.click(self.nails_category_button)
        self.click(self.hybrid_manicure_category_button)

    def configure_mobile_visits(self, address, price):
        ScrollUtil.scrollToTextByAndroidUIAutomator("z dojazdem do klienta", self.driver)
        self.click(self.mobile_type_button)
        self.type(self.address_input, address)
        ScrollUtil.scrollToTextByAndroidUIAutomator("Cena za dojazd", self.driver)
        self.type(self.drive_price_input, price)

    def save_visit(self):
        ScrollUtil.scrollToTextByAndroidUIAutomator("zapisz", self.driver)
        self.click(self.save_button)
        self.click(self.confirm_button)
