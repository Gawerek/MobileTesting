

from .BasePageSP import BasePageSP
from .ProfileDataScreenSP import ProfileDataScreenSP
from .ClientsScreenSP import ClientsScreen
from .ProfileScreenSP import ProfileScreenSP
from .NewsScreenSP import NewsScreenSP
from .CalendarScreenSP import CalendarScreenSP
from appium.webdriver.common.appiumby import AppiumBy


class HomeScreenSP(BasePageSP):
    news_tab_locator = (AppiumBy.ACCESSIBILITY_ID, 'ROUTE_DASHBOARD')
    calendar_tab_locator = (AppiumBy.ACCESSIBILITY_ID, 'CALENDAR_NAVIGATOR')
    chat_tab_locator = (AppiumBy.ACCESSIBILITY_ID, 'ROUTE_CHANNEL_LIST')
    clients_tab_locator = (AppiumBy.ACCESSIBILITY_ID, 'ROUTE_DATABASE_OF_CLIENTS')
    profile_tab_locator = (AppiumBy.ACCESSIBILITY_ID, 'header-avatar-image')

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_news(self):
        self.click(self.news_tab_locator)
        return NewsScreenSP(self.driver)

    def go_to_calendar(self):
        self.click(self.calendar_tab_locator)
        return CalendarScreenSP(self.driver)


    def go_to_chat(self):
        self.click(self.chat_tab_locator)


    def go_to_clients(self):
        self.click(self.clients_tab_locator)
        return ClientsScreen(self.driver)

    def go_to_profile(self):
        self.click(self.profile_tab_locator)
        return ProfileDataScreenSP(self.driver)

    def go_to_settings_login(self):
        self.click(self.settings_tab_locator)
        # return GeneralLoginScreen(self.driver)