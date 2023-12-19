from appium.webdriver.common.appiumby import AppiumBy
from Utilities.Globals import uuid  # Import the global uuid variable

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

    @staticmethod
    def create_dashboard_status_locator_SP(uuid):
        return (AppiumBy.ACCESSIBILITY_ID, f"dashboard-dynamic-card-{uuid}-visit-status")

    @staticmethod
    def create_dashboard_visit_modal_locator_SP(uuid):
        return (AppiumBy.ACCESSIBILITY_ID, f"dashboard-visit-modal-{uuid}-visit-status")
