import time

from .BasePageSP import BasePageSP
from appium.webdriver.common.appiumby import AppiumBy
from .ManualVisitScreenSP import ManualVisitScreenSP

from Variables.variables import *
class VisitsScreenSP(BasePageSP):
    add_manual_visit_button = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Dodaj') and contains(@text, 'wizytę')]")

    def click_manual_visit_button(self):
        self.click(self.add_manual_visit_button)
        return ManualVisitScreenSP(self.driver)
