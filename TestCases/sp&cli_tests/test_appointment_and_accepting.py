import Variables.variables
from TestCases.BaseTest import  BaseTest


from Utilities import dataProvider, app_manager
from Utilities.scroll_util import ScrollUtil
import pytest

import Variables.variables as var

from PagesCLI.HomeScreen import HomeScreen

from Utilities.services import ServiceItems


import time

from PagesSP.HomeScreenSP import HomeScreenSP

from Utilities import dataProvider


# @pytest.mark.parametrize("service_info, name, service_type, address", [
#     (("direct", "PAZNOKCIE_MANICURE_JAPOŃSKI"), "Automation SP", "mobile", "Marszałkowska, Warszawa"),
#     (("direct", "BRWI_HENNA_BRWI"), "Automation SP", "stationary", None),
#
# ])
@pytest.mark.parametrize("service_info, name, service_type, address, service_names",
                         dataProvider.get_data("BookingTest"))
class Test_BookAppointmentAndActions(BaseTest):
    def setup_method(self, method):
        var.uuid = None

    def test_book_appointment_without_action(self, service_info, name, service_type, address, service_names):
        manager = app_manager.AppManager(self.driver)
        manager.launch_cli_app()

        home = HomeScreen(self.driver)
        search = home.go_to_search()

        search.clear_search_bar()
        map_screen = search.search_professionalist_or_service(name)
        map_screen.assert_name(name)
        sp_profile_screen = map_screen.click_on_check_services()

        if service_info == "direct":
            # No need to split the service_names here; it should already be a list
            for service_name in service_names:
                service_name_upper = service_name.upper()
                service_item = getattr(ServiceItems, service_name_upper, None)
                if service_item is not None:
                    sp_profile_screen.book_multiple_services([service_item])
                else:
                    raise ValueError(f"Service item {service_name_upper} not found in ServiceItems")
        book_visit_screen = sp_profile_screen.click_submit_button()

        # Handling mobile service type with address...
        if service_type == "mobile":
            assert address is not None, "Address must be provided for mobile service"
            book_visit_screen.configure_mobile_visits(address)

        # Rest of the booking process...
        confirmation_screen = book_visit_screen.click_book_button()
        confirmation_screen.verify_and_click_go_to_visit_list()

        visit_screen = home.go_to_visit()
        visit_screen.verify_status(var.statuses['WAITING'])

        manager.launch_sp_app()
        home_SP = HomeScreenSP(self.driver)
        news_SP = home_SP.go_to_news()
        news_SP.click_more(0)
        news_SP.verify_status_and_parameters(var.statuses['WAITING'])

    def test_book_appointment_and_accept_by_SP(self, service_info, name, service_type, address, service_names):
        manager = app_manager.AppManager(self.driver)
        manager.launch_cli_app()

        home = HomeScreen(self.driver)
        search = home.go_to_search()

        search.clear_search_bar()
        map_screen = search.search_professionalist_or_service(name)
        map_screen.assert_name(name)
        sp_profile_screen = map_screen.click_on_check_services()

        if service_info == "direct":
            # No need to split the service_names here; it should already be a list
            for service_name in service_names:
                service_name_upper = service_name.upper()
                service_item = getattr(ServiceItems, service_name_upper, None)
                if service_item is not None:
                    sp_profile_screen.book_multiple_services([service_item])
                else:
                    raise ValueError(f"Service item {service_name_upper} not found in ServiceItems")
        book_visit_screen = sp_profile_screen.click_submit_button()

        # Handling mobile service type with address...
        if service_type == "mobile":
            assert address is not None, "Address must be provided for mobile service"
            book_visit_screen.configure_mobile_visits(address)

        # Rest of the booking process
        confirmation_screen = book_visit_screen.click_book_button()
        confirmation_screen.verify_and_click_go_to_visit_list()

        visit_screen = home.go_to_visit()
        visit_screen.verify_status(var.statuses['WAITING'])

        manager.launch_sp_app()
        home_SP = HomeScreenSP(self.driver)
        news_SP = home_SP.go_to_news()
        news_SP.click_more(0)
        news_SP.verify_status_and_parameters(var.statuses['WAITING'])
        news_SP.accept_visit()
        news_SP.click_more(0)
        news_SP.verify_status_and_parameters(var.statuses['ACCEPTED'])
        manager.launch_cli_app()
        home.go_to_visit()
        visit_screen.verify_status(var.statuses['ACCEPTED'])






    def test_book_appointment_and_reject(self, service_info, name, service_type, address, service_names):
        manager = app_manager.AppManager(self.driver)
        manager.launch_cli_app()

        home = HomeScreen(self.driver)
        search = home.go_to_search()

        search.clear_search_bar()
        map_screen = search.search_professionalist_or_service(name)
        map_screen.assert_name(name)
        sp_profile_screen = map_screen.click_on_check_services()

        if service_info == "direct":
            # No need to split the service_names here; it should already be a list
            for service_name in service_names:
                service_name_upper = service_name.upper()
                service_item = getattr(ServiceItems, service_name_upper, None)
                if service_item is not None:
                    sp_profile_screen.book_multiple_services([service_item])
                else:
                    raise ValueError(f"Service item {service_name_upper} not found in ServiceItems")
        book_visit_screen = sp_profile_screen.click_submit_button()

        # Handling mobile service type with address...
        if service_type == "mobile":
            assert address is not None, "Address must be provided for mobile service"
            book_visit_screen.configure_mobile_visits(address)
        confirmation_screen = book_visit_screen.click_book_button()
        confirmation_screen.verify_and_click_go_to_visit_list()

        visit_screen = home.go_to_visit()
        visit_screen.verify_status(var.statuses['WAITING'])

        manager.launch_sp_app()
        home_SP = HomeScreenSP(self.driver)
        news_SP = home_SP.go_to_news()
        news_SP.click_more(0)
        news_SP.verify_status_and_parameters(var.statuses['WAITING'])
        news_SP.reject_visit()
        news_SP.click_more(0)
        news_SP.verify_status_and_parameters(var.statuses['REJECTEDSP'])
        manager.launch_cli_app()
        home.go_to_visit()
        visit_screen.verify_status(var.statuses['REJECTEDSP'])



    def test_book_appointment_and_cancel(self, service_info, name, service_type, address, service_names):
        manager = app_manager.AppManager(self.driver)
        manager.launch_cli_app()

        home = HomeScreen(self.driver)
        search = home.go_to_search()

        search.clear_search_bar()
        map_screen = search.search_professionalist_or_service(name)
        map_screen.assert_name(name)
        sp_profile_screen = map_screen.click_on_check_services()

        if service_info == "direct":
            # No need to split the service_names here; it should already be a list
            for service_name in service_names:
                service_name_upper = service_name.upper()
                service_item = getattr(ServiceItems, service_name_upper, None)
                if service_item is not None:
                    sp_profile_screen.book_multiple_services([service_item])
                else:
                    raise ValueError(f"Service item {service_name_upper} not found in ServiceItems")
        book_visit_screen = sp_profile_screen.click_submit_button()

        # Handling mobile service type with address...
        if service_type == "mobile":
            assert address is not None, "Address must be provided for mobile service"
            book_visit_screen.configure_mobile_visits(address)
        confirmation_screen = book_visit_screen.click_book_button()
        confirmation_screen.verify_and_click_go_to_visit_list()

        visit_screen = home.go_to_visit()
        visit_screen.verify_status(var.statuses['WAITING'])

        manager.launch_sp_app()
        home_SP = HomeScreenSP(self.driver)
        news_SP = home_SP.go_to_news()
        news_SP.click_more(0)
        news_SP.verify_status_and_parameters(var.statuses['WAITING'])
        news_SP.accept_visit()
        news_SP.click_more(0)
        news_SP.verify_status_and_parameters(var.statuses['ACCEPTED'])
        news_SP.cancel_visit()
        news_SP.click_more(0)
        news_SP.verify_status_and_parameters(var.statuses['CANCELEDSP'])
        manager.launch_cli_app()
        home.go_to_visit()
        visit_screen.verify_status(var.statuses['CANCELEDSP'])