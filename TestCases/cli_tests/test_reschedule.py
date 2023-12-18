from Utilities.scroll_util import ScrollUtil
import pytest
import time

from TestCases.BaseTest import BaseTest
from Utilities import dataProvider
from Variables.variables import *
from PagesCLI.HomeScreen import HomeScreen


class Test_Reschedule(BaseTest):
    def test_reschedule(self):
        home_screen = HomeScreen(self.driver)
        visits_screen = home_screen.go_to_visit()
        book_visit_screen = visits_screen.click_another_time()
        confirmation_screen = book_visit_screen.click_change_time_button()
        confirmation_screen.verify_and_click_go_to_visit_list()
        time.sleep(1)
        home_screen.go_to_search()
