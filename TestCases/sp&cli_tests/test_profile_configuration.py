from Utilities.scroll_util import ScrollUtil
import pytest
import time
from TestCases.BaseTest import BaseTestSP

from PagesSP.HomeScreenSP import HomeScreenSP
from PagesCLI.HomeScreen import HomeScreen

from Utilities import dataProvider, app_manager


class Test_ProfileConfiguration(BaseTestSP):
    def test_change_name_and_description(self, random_sp):
        sp_name, sp_description = random_sp
        manager = app_manager.AppManager(self.driver)
        home_screen_SP = HomeScreenSP(self.driver)
        profile_screen_SP = home_screen_SP.go_to_profile()
        profile_data_screen_SP = profile_screen_SP.click_profile_button()
        profile_info_screen = profile_data_screen_SP.click_profile_info_tab()
        profile_info_screen.change_profile_name(sp_name)
        profile_info_screen.change_description(sp_description)
        profile_data_screen_SP.click_profile_submit()
        profile_info_screen.verify_profile_name(sp_name)
        profile_info_screen.verify_description(sp_description)
        manager.launch_cli_app()
        home_CLI = HomeScreen(self.driver)
        search_CLI = home_CLI.go_to_search()
        search_CLI.clear_search_bar()
        map_screen = search_CLI.search_professionalist_or_service(sp_name)
        map_screen.assert_name(sp_name)
        sp_profile_screen = map_screen.click_on_check_services()
        sp_profile_screen.verify_sp_name(sp_name)
        sp_profile_info_tab_screen = sp_profile_screen.click_sp_profile_tab_info()
        sp_profile_info_tab_screen.verify_description(sp_description)
        manager.launch_sp_app()
        profile_screen_SP = home_screen_SP.go_to_profile()
        profile_data_screen_SP = profile_screen_SP.click_profile_button()
        profile_info_screen = profile_data_screen_SP.click_profile_info_tab()
        profile_info_screen.change_profile_name("Automation SP")
        profile_data_screen_SP.click_profile_submit()
        profile_info_screen.verify_profile_name("Automation SP")
        time.sleep(2)

