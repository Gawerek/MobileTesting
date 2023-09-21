from Pages.BasePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from Pages.LoginOrRegisterScreen import LoginOrRegisterScreen

class GeneralLoginScreen(BasePage):
    login_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='Zaloguj']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_general_login_button(self):
        self.click(self.login_button)
        return LoginOrRegisterScreen(self.driver)
