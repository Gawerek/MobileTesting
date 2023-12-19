import time

import Variables.variables
from Utilities.DataSaver import DataSaver
from PagesCLI.BasePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from PagesCLI.BookVisitScreen import BookVisitScreen
from Variables.variables import uuid

from Utilities.ExtractId import ExtractId




class VisitsScreen(BasePage):
    another_time_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='inny termin']")
    phone_number_label = (AppiumBy.XPATH,"//android.widget.TextView[contains(@text,'Numer telefonu:')]")
    name_label = (AppiumBy.ACCESSIBILITY_ID,"settings-name-text")
    visit_status = (AppiumBy.XPATH,"(//android.widget.TextView[contains(@content-desc, 'visit-item-status')])[1]")
    def __init__(self, driver):
        super().__init__(driver)


    def click_another_time(self):
        self.click(self.another_time_button)
        return BookVisitScreen(self.driver)



    def verify_status(self, correct_status):

        visit_status_elements = self.find_elements(self.visit_status)

        if not visit_status_elements:
            print("No elements found with the given locator")
            return

        visit_status_element = visit_status_elements[0]

        status = visit_status_element.text
        visit_status_id = visit_status_element.get_attribute('resource-id')

        print("Resource ID:", visit_status_id)  # Debugging
        Variables.variables.uuid = ExtractId.extract_id(full_id=visit_status_id)
        print("Extracted UUID:", Variables.variables.uuid)  # Debugging

        data = {
            'Status': status,
            'Element ID': visit_status_id,
            'UUID': uuid
        }
        DataSaver.save_to_excel(data, 'Verify Status CLI')
        assert status == correct_status
        print("Status matches:", correct_status)


