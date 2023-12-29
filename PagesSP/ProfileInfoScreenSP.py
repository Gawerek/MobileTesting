import time
from Utilities.scroll_util import *
from .BasePageSP import BasePageSP
from appium.webdriver.common.appiumby import AppiumBy
from Variables.variables import *


class ProfileInfoScreenSP(BasePageSP):
    profile_name_input = (AppiumBy.ACCESSIBILITY_ID, "profile-name-input")
    profile_description_input =(AppiumBy.ACCESSIBILITY_ID,"profile-description-input")

    def change_profile_name(self, new_name):
        profile_name_element = self.find_element(self.profile_name_input)
        self.clear_field(self.profile_name_input)
        self.type(self.profile_name_input, new_name)
        assert new_name == profile_name_element.text
    def change_description(self, new_description):
        profile_description_element = self.find_element(self.profile_description_input)
        self.clear_field(self.profile_description_input)
        self.type(self.profile_description_input, new_description)
        assert new_description == profile_description_element.text


