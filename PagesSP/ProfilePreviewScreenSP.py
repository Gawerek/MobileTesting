import time
from Utilities.scroll_util import *
from .BasePageSP import BasePageSP
from appium.webdriver.common.appiumby import AppiumBy
from Variables.variables import *


class ProfilePreviewScreenSP(BasePageSP):
    information_tab = (AppiumBy.XPATH, "//android.widget.TextView[@text='Informacje']")