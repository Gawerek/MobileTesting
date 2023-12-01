import time

from .BasePageSP import BasePageSP
from .VisitsScreenSP import VisitsScreenSP
from appium.webdriver.common.appiumby import AppiumBy
from .ManualVisitScreenSP import ManualVisitScreenSP
from Variables.variables import *


class ClientsScreen(BasePageSP):
    visits_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='Wizyty']")

    def click_visits_button(self):
        self.click(self.visits_button)
        return VisitsScreenSP(self.driver)