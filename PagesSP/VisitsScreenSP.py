import time

from .BasePageSP import BasePageSP
from appium.webdriver.common.appiumby import AppiumBy
from .ManualVisitScreenSP import ManualVisitScreenSP
from Variables import variables as var
from Utilities.LocatoryFactory import LocatorFactory

from Variables.variables import *
class VisitsScreenSP(BasePageSP):
    add_manual_visit_button = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Dodaj') and contains(@text, 'wizytę')]")
    first_visits_date_roll_out_button = (AppiumBy.ACCESSIBILITY_ID, "visit-dates-header-text-0")
    def click_manual_visit_button(self):
        self.click(self.add_manual_visit_button)
        return ManualVisitScreenSP(self.driver)

    # def verify_status_and_parameters(self, correct_status):
    #     print("uuid from variables " + var.uuid)
    #     # Create locators with dynamic id
    #     dashboard_status_locator = LocatorFactory.create_dashboard_visit_modal_locator_SP(var.uuid)
    #     phone_number_locator = LocatorFactory.create_dashboard_visit_modal_visit_info_service_client_phone_number_locator_SP(var.uuid)
    #     duration_locator = LocatorFactory.create_dashboard_visit_modal_visit_info_service_duration_locator_SP(var.uuid)
    #     original_date_locator = LocatorFactory.create_dashboard_visit_modal_visit_info_original_date_locator_SP(var.uuid)
    #     cost_locator = LocatorFactory.create_dashboard_visit_modal_visit_info_service_cost_locator_SP(var.uuid)
    #     client_name_locator = LocatorFactory.create_dashboard_visit_modal_visit_info_client_name_locator_SP(var.uuid)
    #     original_time_locator = LocatorFactory.create_dashboard_visit_modal_visit_info_original_time_locator_SP(var.uuid)
    #     service_name_locator =  LocatorFactory.create_dashboard_visit_modal_visit_info_service_name_locator_SP(var.uuid)
    #
    #     # Create elements with dynamic locators
    #     status_element = self.find_element(dashboard_status_locator)  # Use the dynamic locator
    #     phone_number_element = self.find_element(phone_number_locator)
    #     duration_element = self.find_element(duration_locator)
    #     original_date_element = self.find_element(original_date_locator)
    #     cost_element = self.find_element(cost_locator)
    #     client_name_element = self.find_element(client_name_locator)
    #     original_time_element = self.find_element(original_time_locator)
    #     service_name_element = self.find_element(service_name_locator)
    #
    #     element_id = status_element.get_attribute('resource-id')
    #
    #     phone_number = phone_number_element.text
    #     status = status_element.text
    #     duration = duration_element.text
    #     original_date = original_date_element.text
    #     cost = cost_element.text
    #     client_name = client_name_element.text
    #     original_time = original_time_element.text
    #     service_name = service_name_element.text
    #
    #     data = {
    #         'Status': status,
    #         'Element ID': element_id,
    #         'UUID': var.uuid,
    #         'Phone': phone_number,
    #         'Duration': duration,
    #         'Date':original_date,
    #         'Price': cost,
    #         'ClientName':client_name,
    #         'OriginalTime':original_time,
    #         'Service':service_name
    #
    #     }
    #
    #
    #     DataSaver.save_to_excel(data, 'Verify Status SP')
    #     assert status_element.text == correct_status
    #     print("Status matches:", correct_status)