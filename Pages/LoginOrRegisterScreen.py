from Pages.BasePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from Pages.PhoneNumberScreen import PhoneNumberScreen


class LoginOrRegisterScreen(BasePage):
    login_button = (AppiumBy.ACCESSIBILITY_ID, "auth-login-button")
    register_button = (AppiumBy.ACCESSIBILITY_ID, "auth-register-button")

    def __init__(self, driver):
        super().__init__(driver)

    def click_login_or_register(self, registration=False):
        if not registration:
            self.click(self.login_button)

        else:
            self.click(self.register_button)
        return PhoneNumberScreen(self.driver)
