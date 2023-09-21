from Utilities.scroll_util import ScrollUtil
import pytest
import time

from Pages.CodeScreen import CodeScreen
from Pages.HomeScreen import HomeScreen
from TestCases.BaseTest import BaseTest
from Utilities import dataProvider
from Variables.variables import *

class Test_BookAppointment(BaseTest):
    @pytest.mark.parametrize("phone_number_param,change_country,country_code, name", [
        ("365967654", False, None,"Magic Nails")])
    def test_book_appointment(self, phone_number_param, change_country, country_code, name):
        home = HomeScreen(self.driver)
        settings = home.go_to_settings_login()
        login_or_registration = settings.click_general_login_button()
        phone_number = login_or_registration.click_login_or_register()
        login_code_screen = phone_number.login_provide_phone_number_and_click_next(phone_number_param, change_country,
                                                                                   country_code)
        settings = login_code_screen.provide_code_and_click_next(assert_phone_number=phone_number_param, code=op_code)
        for x in range(1,11):
            search = home.go_to_search()
            map_screen = search.search_service_or_professional(name)
            map_screen.assert_name(name)
            sp_profile_screen = map_screen.click_on_check_services()
            book_visit_screen = sp_profile_screen.book_service()
            after_booking_screen = book_visit_screen.click_book_button()
            after_booking_screen.click_go_to_visit_list()

