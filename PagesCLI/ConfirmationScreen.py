import time
from Utilities.DataSaver import DataSaver
from PagesCLI.BasePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy

from Variables.variables import *
class ConfirmationScreen(BasePage):
    visit_list_button = (AppiumBy.ACCESSIBILITY_ID, "visit-confirmation-button")
    visit_date = (AppiumBy.ACCESSIBILITY_ID, "visit-confirmation-info-visit-date")
    visit_service = (AppiumBy.ACCESSIBILITY_ID, "visit-confirmation-info-service-name")
    visit_address = (AppiumBy.ACCESSIBILITY_ID, "visit-confirmation-info-provider-address")
    visit_type = (AppiumBy.ACCESSIBILITY_ID, "visit-confirmation-info-visit-type")
    def __init__(self, driver):
        super().__init__(driver)



    def verify_and_click_go_to_visit_list(self):
        type = self.getText(self.visit_type)
        service = self.getText(self.visit_service)
        date = self.getText(self.visit_date)
        address = self.getText(self.visit_address)
        data = {
            'Type': type,
            'Service': service,
            'Date': date,
            'Address': address
        }
        for key, item in data.items():
            print(item)
        DataSaver.save_to_excel(data, 'Confirmation Screen Data')
        self.click(self.visit_list_button)
