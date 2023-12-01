from Utilities.scroll_util import ScrollUtil
import pytest
import time
from TestCases.BaseTest import BaseTestSP
from PagesSP.HomeScreenSP import HomeScreenSP
from Utilities import dataProvider



class Test_AddManualVisit(BaseTestSP):

    def test_add_manual_mobile_visit_calendar(self, random_contact):
        cli_name, cli_phone_number = random_contact
        home_screen = HomeScreenSP(self.driver)
        calendar_screen = home_screen.go_to_calendar()
        manual_visit_screen = calendar_screen.click_manual_visit_button()
        manual_visit_screen.enter_client_name(cli_name)
        manual_visit_screen.enter_phone_number(cli_phone_number)
        manual_visit_screen.select_service()
        manual_visit_screen.configure_mobile_visits("Opolska, Toruń, Polska", 50)
        manual_visit_screen.save_visit()
        time.sleep(5)
    def test_add_manual_visit_calendar(self, random_contact):
        cli_name, cli_phone_number = random_contact
        home_screen = HomeScreenSP(self.driver)
        calendar_screen = home_screen.go_to_calendar()
        manual_visit_screen = calendar_screen.click_manual_visit_button()
        manual_visit_screen.enter_client_name(cli_name)
        manual_visit_screen.enter_phone_number(cli_phone_number)
        manual_visit_screen.select_service()
        manual_visit_screen.save_visit()





    def test_add_manual_mobile_visit(self, random_contact):
        cli_name, cli_phone_number = random_contact
        home_screen = HomeScreenSP(self.driver)
        clients_screen = home_screen.go_to_clients()
        visits_screen = clients_screen.click_visits_button()
        manual_visit_screen = visits_screen.click_manual_visit_button()
        manual_visit_screen.enter_client_name(cli_name)
        manual_visit_screen.enter_phone_number(cli_phone_number)
        manual_visit_screen.select_service()
        manual_visit_screen.configure_mobile_visits("Opolska, Toruń, Polska", 50)
        manual_visit_screen.save_visit()
        time.sleep(2)

    def test_add_manual_visit_visits(self, random_contact):
        cli_name, cli_phone_number = random_contact
        home_screen = HomeScreenSP(self.driver)
        clients_screen = home_screen.go_to_clients()
        visits_screen = clients_screen.click_visits_button()
        manual_visit_screen = visits_screen.click_manual_visit_button()
        manual_visit_screen.enter_client_name(cli_name)
        manual_visit_screen.enter_phone_number(cli_phone_number)
        manual_visit_screen.select_service()
        manual_visit_screen.save_visit()
        time.sleep(5)