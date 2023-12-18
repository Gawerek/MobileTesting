from PagesCLI.BasePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from Variables.variables import *
from PagesCLI.SettingsScreen import SettingsScreen

class CodeScreen(BasePage):
    prefix_label = (AppiumBy.ID, "text_input")
    # phone_number_label = (AppiumBy.XPATH, "//android.widget.EditText[@text='Twój kod z SMS']")
    # code_input = (AppiumBy.ACCESSIBILITY_ID, "auth-code-input")
    code_input = (AppiumBy.ACCESSIBILITY_ID,"auth-verification-code-input")
    next_button = (AppiumBy.ACCESSIBILITY_ID, "auth-next-button")
    phone_number_label = (AppiumBy.ACCESSIBILITY_ID, "auth-verification-phone-number-text")
    send_code_again = (AppiumBy.XPATH, '//android.widget.TextView[@text="Wyslij jeszcze raz"]')
    back_button = (AppiumBy.ACCESSIBILITY_ID, "auth-back-button")


    def __init__(self, driver):
        super().__init__(driver)

    # assert_phone_number, - can be usefull when ac id will be created for phone number
    def provide_code_and_click_next(self,assert_phone_number,  code=login_code):
        text = self.getText(self.phone_number_label)
        print("full text" + text)
        parts = text.split(" ")
        phone_number = parts[-1]  # Ostatni element to '111111111'
        print("only phoneNumber" + phone_number)
        print(assert_phone_number)
        assert assert_phone_number == phone_number
        self.type(self.code_input,code)
        self.click(self.next_button)
        return SettingsScreen(self.driver)




