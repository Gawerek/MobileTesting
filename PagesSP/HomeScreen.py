

from .BasePage import BasePage

from .NewsScreen import NewsScreen
from .CalendarScreen import CalendarScreen
from appium.webdriver.common.appiumby import AppiumBy


class HomeScreen(BasePage):
    news_tab_locator = (AppiumBy.ACCESSIBILITY_ID, 'ROUTE_DASHBOARD')
    calendar_tab_locator = (AppiumBy.ACCESSIBILITY_ID, 'ROUTE_VISIT_CALENDAR')
    chat_tab_locator = (AppiumBy.ACCESSIBILITY_ID, 'ROUTE_CHANNEL_LIST')
    favourites_tab_locator = (AppiumBy.ACCESSIBILITY_ID, 'CLIENTS_NAVIGATOR')
    profile_tab_locator = (AppiumBy.ACCESSIBILITY_ID, 'PROFILE_NAVIGATOR')

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_news(self):
        self.click(self.news_tab_locator)
        return NewsScreen(self.driver)

    def go_to_calendar(self):
        self.click(self.calendar_tab_locator)
        return CalendarScreen(self.driver)


    def go_to_chat(self):
        self.click(self.chat_tab_locator)


    def go_to_clients(self):
        self.click(self.favourites_tab_locator)
        # return VillasScreen(self.driver)

    def go_to_profile(self):
        self.click(self.settings_tab_locator)
        return SettingsScreen(self.driver)

    def go_to_settings_login(self):
        self.click(self.settings_tab_locator)
        return GeneralLoginScreen(self.driver)