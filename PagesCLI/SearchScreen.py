import time
from PagesCLI.BasePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from Variables.variables import *
from PagesCLI.MapScreen import MapScreen


class SearchScreen(BasePage):
    cancel_button=(AppiumBy.XPATH,'//android.view.ViewGroup[@content-desc="search-searvices-input-close-button"]/android.widget.ImageView')
    any_service = (AppiumBy.XPATH, "//android.widget.TextView[@text='DOWOLNA USŁUGA']")
    nails_group = (AppiumBy.ACCESSIBILITY_ID, "search-service-type-item-accordion-1000000")
    hair_group = (AppiumBy.ACCESSIBILITY_ID, "search-service-type-item-accordion-2000000")
    eyebrows_group = (AppiumBy.ACCESSIBILITY_ID, "search-service-type-item-accordion-3000000")
    eyelashes_group = (AppiumBy.ACCESSIBILITY_ID, "search-service-type-item-accordion-4000000")
    makeup_group = (AppiumBy.ACCESSIBILITY_ID, "search-service-type-item-accordion-5000000")
    depilation_group = (AppiumBy.ACCESSIBILITY_ID, "search-service-type-item-accordion-6000000")
    events_group = (AppiumBy.ACCESSIBILITY_ID, "search-service-type-item-accordion-7000000")
    barber_group = (AppiumBy.ACCESSIBILITY_ID, "search-service-type-item-accordion-9000000")
    massage_group = (AppiumBy.ACCESSIBILITY_ID, "search-service-type-item-accordion-10000000")
    search_bar = (AppiumBy.ACCESSIBILITY_ID, "search-input")
    hair_category = "search-service-type-item-accordion-2000000"
    hair_all_services = "search-service-type-item-2000000"
    hair_cut_female = "search-service-type-item-2001000"

    def __init__(self, driver):
        super().__init__(driver)

    def search_professionalist_or_service(self, text):
        self.type(self.search_bar, text)
        search_result_locator = f"//android.widget.TextView[contains(@text,'{text}')]"

        search_result_tuple = (AppiumBy.XPATH, search_result_locator)
        search_id = self.get_element_id(search_result_tuple)

        search_result_tuple_id = (AppiumBy.ACCESSIBILITY_ID, search_id)
        self.click(search_result_tuple_id)
        return MapScreen(self.driver)

    def select_service(self):
        self.click(self.nails_group)

    def clear_search_bar(self):
        self.clear_field(self.search_bar)


