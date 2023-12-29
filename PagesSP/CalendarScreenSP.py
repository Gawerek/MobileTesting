import time

from .BasePageSP import BasePageSP
from appium.webdriver.common.appiumby import AppiumBy
from .ManualVisitScreenSP import ManualVisitScreenSP
from .VisitsScreenSP import VisitsScreenSP
from Variables.variables import *


class CalendarScreenSP(BasePageSP):
    add_manual_visit_button = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Dodaj') and contains(@text, 'wizytę')]")
    visit_tab_button = (AppiumBy.ACCESSIBILITY_ID,"calendar-navigator-visits-tab-text-button-text")

    def __init__(self, driver):
        super().__init__(driver)


    def click_manual_visit_button(self):
        self.click(self.add_manual_visit_button)
        return ManualVisitScreenSP(self.driver)


    def click_visit_tab_button(self):
        self.click(self.visit_tab_button)
        return VisitsScreenSP(self.driver)

