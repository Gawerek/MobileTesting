import time
import re

import Variables.variables
from Utilities.DataSaver import DataSaver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .BasePageSP import BasePageSP
from appium.webdriver.common.appiumby import AppiumBy
from Utilities.ExtractId import ExtractId
from Utilities.LocatoryFactory import LocatorFactory
import Variables.variables as var


from Variables.variables import *
class NewsScreenSP(BasePageSP):
    accept_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='Akceptuj']")
    more_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='Więcej']")
    reject_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='Odrzuć']")
    reschedule_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='Zmień termin']")
    cancel_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='Odwołaj']")
    visit_status = (AppiumBy.XPATH,"//*[contains(@id,'dashboard-visit-modal') and contains(@id,'-visit-status')]")
    dashboard_status = (AppiumBy.XPATH, "//*[contains(@id,'dashboard-dynamic-card-') and contains(@id,'-visit-status')]")

    def __init__(self, driver):
        super().__init__(driver)
    def accept_visit(self):
        self.click_index(self.accept_button, 0)

    def click_more(self, index):
        self.click_index(self.more_button, index)

    def reject_visit(self):
        self.click(self.reject_button)

    def cancel_visit(self):
        self.click(self.cancel_button)


    def verify_status(self, correct_status):
        print("uuid from variables " + var.uuid)
        dashboard_status_locator = LocatorFactory.create_dashboard_visit_modal_locator_SP(Variables.variables.uuid)
        status_element = self.find_element(dashboard_status_locator)  # Use the dynamic locator
        element_id = status_element.get_attribute('resource-id')
        status = status_element.text
        data = {
            'Status': status,
            'Element ID': element_id,
            'UUID': var.uuid
        }
        DataSaver.save_to_excel(data, 'Verify Status SP')
        assert status_element.text == correct_status
        print("Status matches:", correct_status)
