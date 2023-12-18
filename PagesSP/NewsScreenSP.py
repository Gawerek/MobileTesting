import time
import re

from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .BasePageSP import BasePageSP
from appium.webdriver.common.appiumby import AppiumBy


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

    def extract_id(self):
        full_id = self.get_element_id(self.dashboard_status)
        # Use regex to extract the UUID from the resourceId
        match = re.search(r'dashboard-visit-modal-(.*?)-visit-status', full_id)
        if match:
            dynamic_id = match.group(1)
            print(dynamic_id)
            return dynamic_id
        else:
            print("ID pattern not found")
            return None

    def verify_status(self, correct_status):
       # Find the first element with content-desc that matches the pattern
        status_element = self.driver.find_element(AppiumBy.XPATH, "//*[contains(@content-desc, 'dashboard-visit-modal-') and contains(@content-desc, '-visit-status')]")
        element_id = status_element.get_attribute('resource-id')

        print("Element ID:", element_id)

        assert status_element.text == correct_status
        print("Status matches:", correct_status)

