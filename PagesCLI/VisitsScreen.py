import time

from Utilities.LocatoryFactory import LocatorFactory
from Utilities.scroll_util import ScrollUtil
import Variables.variables
from Utilities.DataSaver import DataSaver
from PagesCLI.BasePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from PagesCLI.BookVisitScreen import BookVisitScreen
import Variables.variables as var

from Utilities.ExtractId import ExtractId


class VisitsScreen(BasePage):
    another_time_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='inny termin']")
    phone_number_label = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'Numer telefonu:')]")
    name_label = (AppiumBy.ACCESSIBILITY_ID, "settings-name-text")
    visit_status = (AppiumBy.XPATH, "(//android.widget.TextView[contains(@content-desc, 'visit-item-status')])[1]")
    favourite_button = (AppiumBy.ACCESSIBILITY_ID, "visit-item-toggle-favourite-button-8c7ba8be-ba63-4e63-ba0f-28d4033c6f48")


    def __init__(self, driver):
        super().__init__(driver)

    def click_favourite_button(self):
        ScrollUtil.scrollToAccessibilityIdByAndroidUIAutomator("visit-item-toggle-favourite-button-8c7ba8be-ba63-4e63-ba0f-28d4033c6f48", self.driver)
        self.click(self.favourite_button)

    def click_another_time(self):
        self.click(self.another_time_button)
        return BookVisitScreen(self.driver)

    def fetch_and_store_uuid(self):
        visit_status_elements = self.find_elements(self.visit_status)

        if visit_status_elements:
            visit_status_element = visit_status_elements[0]
            visit_status_id = visit_status_element.get_attribute('resource-id')
            var.uuid = ExtractId.extract_id(full_id=visit_status_id)
            print("Extracted UUID:", var.uuid)
        else:
            print("No elements found with the given locator")

    def verify_status(self, correct_status):

        if var.uuid is None:
            self.fetch_and_store_uuid()
        status_locator = LocatorFactory.create_visit_item_status_locator_CLI(var.uuid)
        ScrollUtil.scrollToAccessibilityIdByAndroidUIAutomator(status_locator[1], self.driver)

        visit_status_element = self.find_element(status_locator)
        status = visit_status_element.text

        visit_status_id = status_locator[1]

        data = {
            'Status': status,
            'Element ID': visit_status_id,
            'UUID': var.uuid
        }
        DataSaver.save_to_excel(data, 'Verify Status CLI')

        assert status == correct_status
        print("Status matches:", correct_status)
