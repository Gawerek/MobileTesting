from Utilities.scroll_util import ScrollUtil
import pytest
import time
from TestCases.BaseTest import BaseTestSP

from PagesSP.HomeScreenSP import HomeScreenSP
from PagesCLI.HomeScreen import HomeScreen
from Utilities.services import ServiceItems

from Utilities import dataProvider, app_manager
from Variables import variables as var


class Test_ProfileConfiguration(BaseTestSP):
    # def test_change_name_and_description(self, random_sp):
    #     sp_name, sp_description = random_sp
    #     manager = app_manager.AppManager(self.driver)
    #     home_screen_SP = HomeScreenSP(self.driver)
    #     profile_screen_SP = home_screen_SP.go_to_profile()
    #     profile_data_screen_SP = profile_screen_SP.click_profile_button()
    #     profile_info_screen = profile_data_screen_SP.click_profile_info_tab()
    #     profile_info_screen.change_profile_name(sp_name)
    #     profile_info_screen.change_description(sp_description)
    #     profile_data_screen_SP.click_profile_submit()
    #     profile_info_screen.verify_profile_name(sp_name)
    #     profile_info_screen.verify_description(sp_description)
    #     manager.launch_cli_app()
    #     home_CLI = HomeScreen(self.driver)
    #     search_CLI = home_CLI.go_to_search()
    #     search_CLI.clear_search_bar()
    #     map_screen = search_CLI.search_professionalist_or_service(sp_name)
    #     map_screen.assert_name(sp_name)
    #     sp_profile_screen = map_screen.click_on_check_services()
    #     sp_profile_screen.verify_sp_name(sp_name)
    #     sp_profile_info_tab_screen = sp_profile_screen.click_sp_profile_tab_info()
    #     sp_profile_info_tab_screen.verify_description(sp_description)
    #     manager.launch_sp_app()
    #     profile_screen_SP = home_screen_SP.go_to_profile()
    #     profile_data_screen_SP = profile_screen_SP.click_profile_button()
    #     profile_info_screen = profile_data_screen_SP.click_profile_info_tab()
    #     profile_info_screen.change_profile_name("Automation SP")
    #     profile_data_screen_SP.click_profile_submit()
    #     profile_info_screen.verify_profile_name("Automation SP")
    #     time.sleep(2)

    # def test_add_service(self):
    #     home_screen_SP = HomeScreenSP(self.driver)
    #     profile_screen_SP = home_screen_SP.go_to_profile()
    #     profile_data_screen_SP = profile_screen_SP.click_profile_button()
    #     profile_service_screen = profile_data_screen_SP.click_services_tab()
    #     profile_service_screen.add_service()
    #     profile_service_screen.configure_service()
    #     profile_data_screen_SP.click_profile_submit()
    #     profile_data_screen_SP.click_back_button()
    #     time.sleep(1)
    #     manager = app_manager.AppManager(self.driver)
    #     manager.launch_cli_app()
    #     home = HomeScreen(self.driver)
    #     search = home.go_to_search()
    #
    #     search.clear_search_bar()
    #     map_screen = search.search_professionalist_or_service("Automation SP")
    #     map_screen.assert_name("Automation SP")
    #     sp_profile_screen = map_screen.click_on_check_services()
    #
    #     service_item = getattr(ServiceItems, "RZĘSY_HENNA_RZĘS", None)
    #     print(service_item)
    #     ScrollUtil.scrollToTextByAndroidUIAutomator("Rzęsy",self.driver)
    #     book_visit_screen = sp_profile_screen.book_service(service_item)
    #     # confirmation_screen = book_visit_screen.click_book_button()
    #     # confirmation_screen.verify_and_click_go_to_visit_list()
    #     #
    #     # visit_screen = home.go_to_visit()
    #     # visit_screen.verify_status(var.statuses['WAITING'])
    #     manager.launch_sp_app()
    #
    #
    # def test_delete_service(self):
    #     home_screen_SP = HomeScreenSP(self.driver)
    #     home_screen_SP.go_to_news()
    #     profile_screen_SP = home_screen_SP.go_to_profile()
    #     profile_data_screen_SP = profile_screen_SP.click_profile_button()
    #     profile_service_screen = profile_data_screen_SP.click_services_tab()
    #     profile_service_screen.delete_service()
    #     profile_data_screen_SP.click_profile_submit()
    #     time.sleep(1)

    def test_add_image(self):
        home_screen_SP = HomeScreenSP(self.driver)
        home_screen_SP.go_to_news()
        profile_screen_SP = home_screen_SP.go_to_profile()
        profile_data_screen_SP = profile_screen_SP.click_profile_button()
        profile_portfolio_screen = profile_data_screen_SP.click_profile_gallery_tab()
        profile_portfolio_screen.add_image()
        profile_data_screen_SP.click_profile_submit()
        profile_data_screen_SP.click_back_button()



