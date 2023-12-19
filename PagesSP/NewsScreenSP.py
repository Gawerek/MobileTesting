import time
import re
from Utilities.DataSaver import DataSaver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .BasePageSP import BasePageSP
from appium.webdriver.common.appiumby import AppiumBy
from Utilities.ExtractId import ExtractId


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
       # Find the first element with content-desc that matches the pattern
        status_element = self.driver.find_element(AppiumBy.XPATH, "//*[contains(@content-desc, 'dashboard-visit-modal-') and contains(@content-desc, '-visit-status')]")
        element_id = status_element.get_attribute('resource-id')
        uuid = ExtractId.extract_id(full_id=element_id)
        status = status_element.text
        data = {
            'Status': status,
            'Element ID': element_id,
            'UUID': uuid
        }
        DataSaver.save_to_excel(data, 'Verify Status SP')
        assert status_element.text == correct_status
        print("Status matches:", correct_status)


