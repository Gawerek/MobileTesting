from PagesCLI.BasePage import BasePage
from .SearchScreen import SearchScreen
from selenium.common.exceptions import StaleElementReferenceException
from Utilities.LocatoryFactory import LocatorFactory

from appium.webdriver.common.appiumby import AppiumBy


class FavouriteScreen(BasePage):
    search_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='szukaj']")
    automation_sp_id = "fc124053-f8a8-43bc-9c96-8247b9da6b00"


    def click_search_button(self):
        self.click(self.search_button)
        return SearchScreen(self.driver)

    def click_book_button(self, sp_id):
        book_button = LocatorFactory.create_favourite_schedule_button(sp_id)
        self.click(book_button)

    def click_favourite_button(self, sp_id):
        favourite_button_locator = LocatorFactory.create_favourite_toggle_favourite_button(sp_id)
        self.click(favourite_button_locator)


    def verify_favourite_sp(self, sp_name):
        sp_name_locator = (AppiumBy.XPATH, f'//android.widget.TextView[@text="{sp_name}"]')
        try:
            sp_name_element = self.find_element(sp_name_locator)
            sp_name_text = sp_name_element.text
        except StaleElementReferenceException:
            # Re-find the element in case of StaleElementReferenceException
            sp_name_element = self.find_element(sp_name_locator)
            sp_name_text = sp_name_element.text

        assert sp_name_text == sp_name, f"Expected SP name '{sp_name}', but found '{sp_name_text}'"