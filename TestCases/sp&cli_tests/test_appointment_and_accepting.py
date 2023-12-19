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




class Test_BookAppointmentAndAccept(BaseTest):


    @pytest.mark.parametrize("service_info, name, service_type, address", [
        (("direct", "PAZNOKCIE_MANICURE_JAPOŃSKI"), "Automation SP", "mobile", "Marszałkowska, Warszawa"),
        (("direct", "BRWI_HENNA_BRWI"), "Automation SP", "stationary", None),

    ])
    def test_book_appointment_and_accept_by_SP(self, service_info, name, service_type, address):
        manager = app_manager.AppManager(self.driver)

        home = HomeScreen(self.driver)
        manager.launch_cli_app()
        search = home.go_to_search()

        search.clear_search_bar()
        map_screen = search.search_professionalist_or_service(name)
        map_screen.assert_name(name)
        sp_profile_screen = map_screen.click_on_check_services()

        if service_info[0] == "direct":
            # Use getattr to dynamically access the service item
            service_name = service_info[
                1].upper()  # Convert to uppercase to match the class attribute naming convention
            service_item = getattr(ServiceItems, service_name, None)
            print(service_item)
            if service_item is not None:
                book_visit_screen = sp_profile_screen.book_service(service_item)
            else:
                raise ValueError(f"Service item {service_name} not found in ServiceItems")


        elif service_info[0] == "category_subcategory":
            category = service_info[1]
            subcategory = service_info[2]
            ScrollUtil.swipeDown(2, self.driver)
            sp_profile_screen.select_service_category(category)
            book_visit_screen = sp_profile_screen.book_service(subcategory)

        # Handling mobile service type with address
        if service_type == "mobile":
            assert address is not None, "Address must be provided for mobile service"
            ScrollUtil.scrollToTextByAndroidUIAutomator("usługi mobilne", self.driver)
            book_visit_screen.configure_mobile_visits(address)

        # if book_visit_screen.select_specific_time_slot("14:30"):
        #     ScrollUtil.scrollToTextByAndroidUIAutomator("14:30", self.driver)
        #     print("Selected time slot: 13:30")
        # else:
        #     print("Time slot 13:30 is not available or not found.")
        #     book_visit_screen.select_first_available_time_slot()

        # Rest of the booking process
        confirmation_screen = book_visit_screen.click_book_button()
        confirmation_screen.verify_and_click_go_to_visit_list()

        visit_screen = home.go_to_visit()
        visit_screen.verify_status(var.statuses['WAITING'])

        manager.launch_sp_app()
        home_SP = HomeScreenSP(self.driver)
        news_SP = home_SP.go_to_news()
        news_SP.click_more(0)
        news_SP.verify_status(var.statuses['WAITING'])
        news_SP.accept_visit()
        time.sleep(5)

        # news_SP.click_more(1)
        # news_SP.reject_visit()
        #
        # news_SP.click_more(0)
        # news_SP.cancel_visit()




