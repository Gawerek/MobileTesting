# LocatorFactory.py
from appium.webdriver.common.appiumby import AppiumBy

class LocatorFactory:
    @staticmethod
    def create_category_locator(category_id):
        return (AppiumBy.ACCESSIBILITY_ID, f"search-service-type-item-accordion-{category_id}")

    @staticmethod
    def create_service_locator(service_id):
        return (AppiumBy.ACCESSIBILITY_ID, f"sp-profile-services-select-button-{service_id}")

    @staticmethod
    def create_schedule_button_locator(service_id):
        return (AppiumBy.ACCESSIBILITY_ID, f"profile-schedule-button-{service_id}")


    @staticmethod
    def create_toggle_expand_button_locator(service_id):
        return (AppiumBy.ACCESSIBILITY_ID, f"sp-profile-services-toggle-expand-button-{service_id}")