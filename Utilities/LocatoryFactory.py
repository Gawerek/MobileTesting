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

    @staticmethod
    def create_dashboard_status_locator_SP(uuid):
        return (AppiumBy.ACCESSIBILITY_ID, f"dashboard-dynamic-card-{uuid}-visit-status")

    @staticmethod
    def create_dashboard_visit_modal_locator_SP(uuid):
        return (AppiumBy.ACCESSIBILITY_ID, f"dashboard-visit-modal-{uuid}-visit-status")

    @staticmethod
    def create_dashboard_visit_modal_visit_info_original_date_locator_SP(uuid):
        return (AppiumBy.ACCESSIBILITY_ID, f"dashboard-visit-modal-{uuid}-visit-info-original-date")

    @staticmethod
    def create_dashboard_visit_modal_visit_info_original_time_locator_SP(uuid):
        return (AppiumBy.ACCESSIBILITY_ID, f"dashboard-visit-modal-{uuid}-visit-info-original-time")

    @staticmethod
    def create_dashboard_visit_modal_visit_info_service_name_locator_SP(uuid):
        return (AppiumBy.ACCESSIBILITY_ID, f"dashboard-visit-modal-{uuid}-visit-info-service-name")

    @staticmethod
    def create_dashboard_visit_modal_visit_info_service_cost_locator_SP(uuid):
        return (AppiumBy.ACCESSIBILITY_ID, f"dashboard-visit-modal-{uuid}-visit-info-service-name")

    @staticmethod
    def create_dashboard_visit_modal_visit_info_service_duration_locator_SP(uuid):
        return (AppiumBy.ACCESSIBILITY_ID, f"dashboard-visit-modal-{uuid}-visit-info-service-duration")


    @staticmethod
    def create_dashboard_visit_modal_visit_info_client_name_locator_SP(uuid):
        return (AppiumBy.ACCESSIBILITY_ID, f"dashboard-visit-modal-{uuid}-visit-info-client-name")

    @staticmethod
    def create_dashboard_visit_modal_visit_info_service_client_phone_number_locator_SP(uuid):
        return (AppiumBy.ACCESSIBILITY_ID, f"dashboard-visit-modal-{uuid}-visit-info-client-phone-number")
    @staticmethod
    def create_visit_item_status_locator_CLI(uuid):
        return (AppiumBy.ACCESSIBILITY_ID, f"visit-item-status-{uuid}")

    @staticmethod
    def create_favourite_toggle_favourite_button(uuid):
        return (AppiumBy.ACCESSIBILITY_ID, f"favourite-toggle-favourite-button-{uuid}")

    @staticmethod
    def create_favourite_schedule_button(uuid):
        return (AppiumBy.ACCESSIBILITY_ID, f"favourite-schedule-button-{uuid}")


    @staticmethod
    def create_favourite_share_button(uuid):
        return (AppiumBy.ACCESSIBILITY_ID, f"favourite-share-button-{uuid}")

    @staticmethod
    def create_favourite_message_button(uuid):
        return (AppiumBy.ACCESSIBILITY_ID,f"favourite-message-button-{uuid}")

    @staticmethod
    def create_favourite_address_button(uuid):
        return (AppiumBy.ACCESSIBILITY_ID,f"favourite-address-{uuid}")

    @staticmethod
    def create_booking_time_of_service_locator(service_id):
        return (AppiumBy.ACCESSIBILITY_ID, f"booking-time-of-service-text-{service_id}")

    @staticmethod
    def create_booking_price_of_service_locator(service_id):
        return (AppiumBy.ACCESSIBILITY_ID, f"booking-price-of-service-text-{service_id}")

    @staticmethod
    def create_booking_chosen_service_locator(service_id):
        return (AppiumBy.ACCESSIBILITY_ID, f"booking-choosen-service-text-{service_id}")
