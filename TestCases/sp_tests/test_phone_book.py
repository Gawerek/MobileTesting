from Utilities.scroll_util import ScrollUtil
import pytest
import time
from TestCases.BaseTest import BaseTestSP

from PagesSP.HomeScreenSP import HomeScreenSP

from Utilities import dataProvider


class Test_PhoneBook(BaseTestSP):
    def test_add_new_client_to_phone_book(self, random_contact):
        cli_name, cli_phone_number, cli_address = random_contact
        home_screen = HomeScreenSP(self.driver)
        client_screen = home_screen.go_to_clients()
        add_client_screen = client_screen.click_add_contacts_manually()
        add_client_screen.add_new_client(name=cli_name,address=cli_address,phone=cli_phone_number)
        time.sleep(5)



