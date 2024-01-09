from Utilities.scroll_util import *
import pytest
import time

from TestCases.BaseTest import BaseTest
from Utilities import dataProvider
from Variables import variables as var
from PagesCLI.HomeScreen import HomeScreen


class Test_Favourite(BaseTest):

    def test_add_to_favorite_in_sp_profile(self):
        home_screen_cli = HomeScreen(self.driver)
        favourite_screen = home_screen_cli.go_to_favourites()
        search_screen = favourite_screen.click_search_button()
        search_screen.clear_search_bar()
        map_screen = search_screen.search_professionalist_or_service(var.sp_name)
        sp_profile_screen = map_screen.click_on_check_services()
        sp_profile_screen.click_favorite_button()
        ScrollUtil.swipeDown(4, self.driver)
        sp_profile_screen.click_back_button()
        map_screen.click_back_button()
        home_screen_cli.go_to_favourites()
        favourite_screen.verify_favourite_sp(var.sp_name)
        favourite_screen.click_favourite_button(var.sp_favourite_id)
        favourite_screen.remove_sp_from_favourites()

    def test_add_to_favorite_in_visits_screen(self):
        home_screen_cli = HomeScreen(self.driver)
        visits_screen = home_screen_cli.go_to_visit()
        visits_screen.click_favourite_button()
        favourite_screen = home_screen_cli.go_to_favourites()
        favourite_screen.verify_favourite_sp(var.sp_name)
        favourite_screen.click_favourite_button(var.sp_favourite_id)
        favourite_screen.remove_sp_from_favourites(False)




