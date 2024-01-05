from Utilities.scroll_util import ScrollUtil
import pytest
import time

from PagesCLI.CodeScreen import CodeScreen
from PagesCLI.HomeScreen import HomeScreen
from TestCases.BaseTest import BaseTest
from Utilities import dataProvider
from Utilities.services import ServiceItems
from Variables.variables import *


class Test_BookAppointment(BaseTest):

    # @pytest.mark.parametrize("service_info, name, service_type, address", [
    #     (("direct", "japan_manicure"), "Magic Nails", "mobile", "Marszałkowska, Warszawa"),
    #     (("direct", "japan_manicure"), "Magic Nails", "stationary", None),
    #
    # ])

    @pytest.mark.parametrize("service_info, name, service_type, address, service_name", dataProvider.get_data("BookingTest"))
    def test_book_appointment(self, service_info, name, service_type, address, service_name):
        home = HomeScreen(self.driver)
        search = home.go_to_search()
        for x in range(0, 2):
            print(x)
            search.clear_search_bar()
            map_screen = search.search_professionalist_or_service(name)
            # map_screen.assert_name(name)
            sp_profile_screen = map_screen.click_on_check_services()

            # Handling different types of service booking
            if service_info[0] == "direct":
                # Use getattr to dynamically access the service item
                service_name = service_info[1].upper()  # Convert to uppercase to match the class attribute naming convention
                service_item = getattr(ServiceItems, service_name, None)
                print(service_item)
                if service_item is not None:
                    book_visit_screen = sp_profile_screen.book_multiple_services(service_item)
                else:
                    raise ValueError(f"Service item {service_name} not found in ServiceItems")

            # elif service_info == "category_subcategory":
            #     subcategory = service_info[2]
            #     ScrollUtil.swipeDown(2, self.drvier)
            #     sp_profile_screen.select_service_category(category)
            #     book_visit_screen = sp_profile_screen.book_service(subcategory)

            # Handling mobile service type with address
            if service_type == "mobile":
                assert address is not None, "Address must be provided for mobile service"
                ScrollUtil.scrollToTextByAndroidUIAutomator("usługi mobilne", self.driver)
                book_visit_screen.configure_mobile_visits(address)

            # Rest of the booking process
            confirmation_screen = book_visit_screen.click_book_button()
            confirmation_screen.verify_and_click_go_to_visit_list()
            time.sleep(1)
            home.go_to_search()





    # def test_book_appointment(self, service_info, name, service_type, address):
    #     home = HomeScreen(self.driver_cli)
    #     search = home.go_to_search()
    #
    #     search.clear_search_bar()
    #     map_screen = search.search_professionalist_or_service(name)
    #     # map_screen.assert_name(name)
    #     sp_profile_screen = map_screen.click_on_check_services()
    #
    #     # Handling different types of service booking
    #     if service_info[0] == "direct":
    #         service = service_info[1]
    #         book_visit_screen = sp_profile_screen.book_service(service)
    #     elif service_info[0] == "category_subcategory":
    #         category = service_info[1]
    #         subcategory = service_info[2]
    #         ScrollUtil.swipeDown(2, self.driver_cli)
    #         sp_profile_screen.select_service_category(category)
    #         book_visit_screen = sp_profile_screen.book_service(subcategory)
    #
    #     # Handling mobile service type with address
    #     if service_type == "mobile":
    #         assert address is not None, "Address must be provided for mobile service"
    #         ScrollUtil.scrollToTextByAndroidUIAutomator("usługi mobilne", self.driver_cli)
    #         book_visit_screen.configure_mobile_visits(address)
    #
    #     # Rest of the booking process
    #     confirmation_screen = book_visit_screen.click_book_button()
    #     confirmation_screen.click_go_to_visit_list()
    #     time.sleep(1)
    #     home.go_to_search()
    #



    # @pytest.mark.parametrize("phone_number_param,change_country,country_code, name", [
    #     ("365967654", False, None,"Magic Nails")])
    # def test_book_appointment(self, phone_number_param, change_country, country_code, name):
    #     home = HomeScreen(self.driver)
    #     settings = home.go_to_settings_login()
    #     login_or_registration = settings.click_general_login_button()
    #     phone_number = login_or_registration.click_login_or_register()
    #     login_code_screen = phone_number.login_provide_phone_number_and_click_next(phone_number_param, change_country,
    #                                                                                country_code)
    #     settings = login_code_screen.provide_code_and_click_next(assert_phone_number=phone_number_param, code=op_code)
    # Add more test cases as needed
