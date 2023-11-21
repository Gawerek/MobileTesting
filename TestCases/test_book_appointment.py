from Utilities.scroll_util import ScrollUtil
import pytest
import time

from Pages.CodeScreen import CodeScreen
from Pages.HomeScreen import HomeScreen
from TestCases.BaseTest import BaseTest
from Utilities import dataProvider
from Variables.variables import *

class Test_BookAppointment(BaseTest):
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
    @pytest.mark.parametrize("service_info, name", [
        (("direct", "japan_manicure"), "Magic Nails SP")
        # (("category_subcategory", "classic_massage_category", "classic_massage_1h"), "Magic Nails")
    ])
    def test_book_appointment(self, service_info, name):
        home = HomeScreen(self.driver)
        search = home.go_to_search()
        map_screen = search.search_professionalist_or_service(name)
        map_screen.assert_name(name)
        sp_profile_screen = map_screen.click_on_check_services()

        # Handling different types of service booking
        if service_info[0] == "direct":
            service = service_info[1]
            book_visit_screen = sp_profile_screen.book_service(service)
        elif service_info[0] == "category_subcategory":
            category = service_info[1]
            subcategory = service_info[2]
            ScrollUtil.swipeDown(2, self.drvier)
            sp_profile_screen.select_service_category(category)
            book_visit_screen = sp_profile_screen.book_service(subcategory)

        # Rest of the booking process
        ScrollUtil.scrollToTextByAndroidUIAutomator("zarezerwuj", self.driver)
        confirmation_screen = book_visit_screen.click_book_button()
        confirmation_screen.click_go_to_visit_list()







    # def test_book_appointment(self):
    #     for x in range(1,11):
    #         home = HomeScreen(self.driver)
    #         search = home.go_to_search()
    #         map_screen = search.select_service()


