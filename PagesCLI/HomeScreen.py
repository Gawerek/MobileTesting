from PagesCLI.BasePage import BasePage

from PagesCLI.GeneralLoginScreen import GeneralLoginScreen
from PagesCLI.SettingsScreen import SettingsScreen
from PagesCLI.SearchScreen import SearchScreen
from PagesCLI.VisitsScreen import VisitsScreen
from .FavoriteScreenCLI import FavouriteScreen
from appium.webdriver.common.appiumby import AppiumBy


class HomeScreen(BasePage):
    search_tab_locator = (AppiumBy.ACCESSIBILITY_ID, 'cli-search-tab')
    visit_tab_locator = (AppiumBy.ACCESSIBILITY_ID, 'cli-visits-tab')
    chat_tab_locator = (AppiumBy.ACCESSIBILITY_ID, 'cli-rating-tab')
    favourites_tab_locator = (AppiumBy.ACCESSIBILITY_ID, 'cli-favourites-tab')
    settings_tab_locator = (AppiumBy.ACCESSIBILITY_ID, 'cli-settings-tab')

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_search(self):
        self.click(self.search_tab_locator)
        return SearchScreen(self.driver)

    def go_to_visit(self):
        self.click(self.visit_tab_locator)
        return VisitsScreen(self.driver)

    def go_to_chat(self):
        self.click(self.chat_tab_locator)
        # return VillasScreen(self.driver)

    def go_to_favourites(self):
        self.click(self.favourites_tab_locator)
        return FavouriteScreen(self.driver)

    def go_to_settings(self):
        self.click(self.settings_tab_locator)
        return SettingsScreen(self.driver)

    def go_to_settings_login(self):
        self.click(self.settings_tab_locator)
        return GeneralLoginScreen(self.driver)