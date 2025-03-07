from appium.webdriver.common.appiumby import AppiumBy

class ScrollUtil:

    @staticmethod
    def scrollToAccessibilityIdByAndroidUIAutomator(accessibility_id, driver, horizontal=False):
        scrollable_selector = "new UiScrollable(new UiSelector().scrollable(true).instance(0))"
        if horizontal:
            scrollable_selector += ".setAsHorizontalList()"
        ui_automator_string = f"{scrollable_selector}.scrollIntoView(new UiSelector().description(\"{accessibility_id}\").instance(0))"
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, ui_automator_string)

    @staticmethod
    def scrollToTextByAndroidUIAutomator(text, driver, horizontal=False):
        scrollable_selector = "new UiScrollable(new UiSelector().scrollable(true).instance(0))"
        if horizontal:
            scrollable_selector += ".setAsHorizontalList()"
        ui_automator_string = f"{scrollable_selector}.scrollIntoView(new UiSelector().textContains(\"{text}\").instance(0))"
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, ui_automator_string)


    @staticmethod
    def swipeUp(howManySwipes,driver):
        for i in range(1,howManySwipes+1):
            driver.swipe(514, 600, 514, 200, 1000)


    @staticmethod
    def swipeDown(howManySwipes,driver):
        for i in range(1, howManySwipes + 1):
            driver.swipe(514, 500, 514, 800, 1000)

    @staticmethod
    def swipeLeft(howManySwipes,driver):
        for i in range(1, howManySwipes + 1):
            driver.swipe(900, 600, 200, 600, 1000)

    @staticmethod
    def swipeRight(howManySwipes,driver):
        for i in range(1, howManySwipes + 1):
            driver.swipe(200, 600, 900, 600, 1000)