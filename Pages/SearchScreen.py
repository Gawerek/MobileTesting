import time
from Pages.BasePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from Variables.variables import *
from Pages.MapScreen import MapScreen


class SearchScreen(BasePage):
    cancel_button=(AppiumBy.XPATH,'//android.view.ViewGroup[@content-desc="search-searvices-input-close-button"]/android.widget.ImageView')
    any_service = (AppiumBy.XPATH, "//android.widget.TextView[@text='DOWOLNA USŁUGA']")
    nails_group = (AppiumBy.ACCESSIBILITY_ID, "search-service-type-item-accordion-1000000")
    hair_group = (AppiumBy.ACCESSIBILITY_ID, "undefined-Włosy")
    eyelashes_group = (AppiumBy.ACCESSIBILITY_ID, "undefined-Rzęsy")
    makeup_group = (AppiumBy.ACCESSIBILITY_ID, "undefined-Makijaż")
    eyebrows_group = (AppiumBy.ACCESSIBILITY_ID, "undefined-Brwi")
    depilation_group = (AppiumBy.ACCESSIBILITY_ID, "undefined-Depilacja")
    events_group = (AppiumBy.ACCESSIBILITY_ID, "undefined-Eventy")
    barber_group = (AppiumBy.ACCESSIBILITY_ID, "undefined-Barber")
    massage_group = (AppiumBy.ACCESSIBILITY_ID, "undefined-Masaż")
    search_bar = (AppiumBy.XPATH, "//android.widget.EditText")
    hair_category = "search-service-type-item-accordion-2000000"
    hair_all_services = "search-service-type-item-2000000"
    hair_cut_female = "search-service-type-item-2001000"

    def __init__(self, driver):
        super().__init__(driver)

    def search_professionalist_or_service(self, text):
        self.type(self.search_bar, text)
        search_result_locator = f"//android.widget.TextView[contains(@text,'{text}')]"
        search_result_tuple = (AppiumBy.XPATH, search_result_locator)
        self.click(search_result_tuple)
        return MapScreen(self.driver)

    def select_service(self):
        self.click(self.nails_group)

    def clear_search_bar(self):
        self.clear_field(self.search_bar)


