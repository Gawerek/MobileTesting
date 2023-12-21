import time

from .BasePageSP import BasePageSP
from .VisitsScreenSP import VisitsScreenSP
from .AddClientScreenSP import AddClientScreenSP
from appium.webdriver.common.appiumby import AppiumBy
from .ManualVisitScreenSP import ManualVisitScreenSP
from Variables.variables import *


class ClientsScreen(BasePageSP):
    visits_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='Wizyty']")
    add_client_button = (AppiumBy.ACCESSIBILITY_ID,'clients-database-add-button')
    add_client_manually_button = (AppiumBy.ACCESSIBILITY_ID,'clients-database-add-manually-button-text')
    import_contacts_button = (AppiumBy.ACCESSIBILITY_ID,'clients-database-import-from-contacts-button-text')


    def click_visits_button(self):
        self.click(self.visits_button)
        return VisitsScreenSP(self.driver)

    def click_add_contacts_manually(self):
        self.click(self.add_client_button)
        self.click(self.add_client_manually_button)
        return AddClientScreenSP(self.driver)

    def click_import_contacts(self):
        self.click(self.add_client_button)
        self.click(self.import_contacts_button)