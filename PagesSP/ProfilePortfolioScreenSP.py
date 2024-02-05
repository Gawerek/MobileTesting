import time
from Utilities.scroll_util import *
from .BasePageSP import BasePageSP
from .ProfileServiceScreenSP import ProfileServicesScreenSP
from appium.webdriver.common.appiumby import AppiumBy
from .ProfileInfoScreenSP import ProfileInfoScreenSP

from Variables.variables import *


class ProfilePortfolioScreenSP(BasePageSP):
    add_image_button = (AppiumBy.ACCESSIBILITY_ID, "profile-gallery-add-image-button-text")
    select_from_gallery = (AppiumBy.ID, "android:id/button3")
    photo_locator = (AppiumBy.ID, "com.google.android.providers.media.module:id/icon_thumbnail")

    crop_button = (AppiumBy.ID, "bbox.pl.sp.app.development:id/crop_image_menu_crop")
    # description_input = (AppiumBy.ACCESSIBILITY_ID, "profile-gallery-description-input-1")
    # delete_image_button =(AppiumBy.ACCESSIBILITY_ID,"profile-gallery-delete-image-button-1")
    description_input = (AppiumBy.XPATH, "//android.widget.EditText[contains(@content-desc, 'profile-gallery-description-input')]")
    delete_image_button = (
    AppiumBy.XPATH, "//android.view.ViewGroup[contains(@content-desc, 'profile-gallery-delete-image-button')]")

    def add_image(self):
        self.click(self.add_image_button)
        self.click(self.select_from_gallery)
        self.click(self.photo_locator)
        self.click(self.crop_button)
        self.type(self.description_input, 'dupa123')

    def delete_image(self):
        self.click(self.delete_image_button)
