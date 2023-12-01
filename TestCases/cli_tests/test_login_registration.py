import pytest
import time

from Pages.CodeScreen import CodeScreen
from Pages.HomeScreen import HomeScreen
from TestCases.BaseTest import BaseTest
from Utilities import dataProvider
from Variables.variables import *


@pytest.mark.parametrize("phone_number_param,change_country,country_code,name", [
    ("999666313", True, "380", "hnJohnJohnJohnJohnJohnJoh"),
    ("999666321", True, "48", "山田山田山田"),
    ("999666342", False, None, "ЖанЖан"),
    ("999666334", True, "421", "John\tSmith\nDoe"),
    ("999666335", True, "43", "GrźżeGółąęń$%123")])
class Test_RegistrationAndLogin(BaseTest):

    def test_registration(self, phone_number_param, change_country, country_code, name):
        home = HomeScreen(self.driver_cli)
        settings_login = home.go_to_settings_login()
        login_or_registration = settings_login.click_general_login_button()
        phone_number = login_or_registration.click_login_or_register(registration=True)
        registration_screen = phone_number.registration_provide_phone_number_and_click_next(phone_number_param, change_country,
                                                                                     country_code, name)
        settings = registration_screen.provide_code_and_click_next(phone_number_param, code=op_code)
        settings.assert_phone_number(assert_phone_number=phone_number_param)
        settings.log_out_account()

    def test_login(self, phone_number_param, change_country, country_code, name):
        home = HomeScreen(self.driver_cli)
        settings = home.go_to_settings_login()
        login_or_registration = settings.click_general_login_button()
        phone_number = login_or_registration.click_login_or_register()
        login_code_screen = phone_number.login_provide_phone_number_and_click_next(phone_number_param, change_country,
                                                                                   country_code)
        settings = login_code_screen.provide_code_and_click_next(assert_phone_number=phone_number_param, code=op_code)
        settings.assert_phone_number(assert_phone_number=phone_number_param)
        settings.assert_name(assert_name=name)
        settings.delete_account()
