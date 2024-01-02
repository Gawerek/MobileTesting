import time
from Utilities.scroll_util import *
from .BasePageSP import BasePageSP
from appium.webdriver.common.appiumby import AppiumBy
from Variables.variables import *


class ProfileServicesScreenSP(BasePageSP):
    profile_add_service = (AppiumBy.ACCESSIBILITY_ID, "profile-services-add-service-button-text")
    lashes_code = (AppiumBy.ACCESSIBILITY_ID, "undefined-4000000")
    lashes_henna_code = (AppiumBy.ACCESSIBILITY_ID, "profile-services-service-tag-4001000-text")
    profile_submit_button = (AppiumBy.ACCESSIBILITY_ID, "profile-submit-button-text")
    profile_description_input = (AppiumBy.ACCESSIBILITY_ID, "profile-description-input")
    profile_services_header = (AppiumBy.ACCESSIBILITY_ID, "profile-services-accordion-header-11")
    profile_services_header2 = (AppiumBy.ACCESSIBILITY_ID, "profile-services-accordion-header-4")

    profile_service_edit_button =(AppiumBy.ACCESSIBILITY_ID,"profile-services-edit-button-4001000")
    profile_service_duration_increment = (AppiumBy.ACCESSIBILITY_ID, "profile-services-service-duration-increment-4001000")
    profile_service_price_increment = (AppiumBy.ACCESSIBILITY_ID, "profile-services-service-price-increment-4001000")
    profile_service_delete_button = (AppiumBy.ACCESSIBILITY_ID, "profile-services-delete-button-4001000")

    def add_service(self):
        self.click(self.profile_add_service)
        self.click(self.lashes_code)
        self.click(self.lashes_henna_code)
        self.click(self.profile_submit_button)

    def configure_service(self):
        self.click(self.profile_services_header)
        self.click(self.profile_service_edit_button)
        self.click(self.profile_service_duration_increment)
        self.click(self.profile_service_price_increment)

    def delete_service(self):
        self.click(self.profile_services_header2)
        self.click(self.profile_service_delete_button)


