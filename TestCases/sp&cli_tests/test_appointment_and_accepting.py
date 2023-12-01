from Utilities.scroll_util import ScrollUtil
import pytest
import time
from TestCases.BaseTest import BaseTestSP
from TestCases.BaseTest import CombinedBaseTest
from PagesSP.HomeScreenSP import HomeScreenSP

from Utilities import dataProvider
from Utilities.scroll_util import ScrollUtil
import pytest
import time

from Pages.CodeScreen import CodeScreen
from Pages.HomeScreen import HomeScreen

from Utilities import dataProvider
from Variables.variables import *

import time

from PagesSP.HomeScreenSP import HomeScreenSP

from Utilities import dataProvider




class Test_BookAppointmentAndAccept:


    @pytest.mark.parametrize("service_info, name, service_type, address", [
        (("direct", "japan_manicure"), "Magic Nails SP", "mobile", "Marszałkowska, Warszawa"),
        (("direct", "japan_manicure"), "Magic Nails SP", "stationary", None),

    ])
    def test_book_appointment(self, service_info, name, service_type, address, appium_driver, appium_driver_SP):
        home = HomeScreen(self.appium_driver)
        search = home.go_to_search()

        search.clear_search_bar()
        map_screen = search.search_professionalist_or_service(name)
        # map_screen.assert_name(name)
        sp_profile_screen = map_screen.click_on_check_services()

        # Handling different types of service booking
        if service_info[0] == "direct":
            service = service_info[1]
            book_visit_screen = sp_profile_screen.book_service(service)
        elif service_info[0] == "category_subcategory":
            category = service_info[1]
            subcategory = service_info[2]
            ScrollUtil.swipeDown(2, self.driver_cli)
            sp_profile_screen.select_service_category(category)
            book_visit_screen = sp_profile_screen.book_service(subcategory)

        # Handling mobile service type with address
        if service_type == "mobile":
            assert address is not None, "Address must be provided for mobile service"
            ScrollUtil.scrollToTextByAndroidUIAutomator("usługi mobilne", self.driver_cli)
            book_visit_screen.configure_mobile_visits(address)

        # Rest of the booking process
        confirmation_screen = book_visit_screen.click_book_button()
        confirmation_screen.click_go_to_visit_list()
        time.sleep(1)
        home.go_to_search()
        home_SP = HomeScreenSP(self.appium_driver_SP)
        news_SP = home_SP.go_to_news()

        news_SP.accept_visit()

        news_SP.click_more(1)
        news_SP.reject_visit()

        news_SP.click_more(0)
        news_SP.cancel_visit()




