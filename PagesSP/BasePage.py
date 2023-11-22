import logging

from Utilities.LogUtil import Logger
from Utilities import configReader
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

log = Logger(__name__, logging.INFO)

WAIT_TIME = 10


class BasePage:

    def __init__(self, driver):
        self.driver = driver


    def click(self, locator_tuple):
        element = WebDriverWait(self.driver, WAIT_TIME).until(
            EC.presence_of_element_located(locator_tuple)
        )
        element.click()
        log.logger.info(f"Clicked on element with locator: {locator_tuple}")

    def click_index(self, locator_tuple, index):
        elements = WebDriverWait(self.driver, WAIT_TIME).until(
            EC.presence_of_all_elements_located(locator_tuple)
        )
        elements[index].click()
        log.logger.info(f"Clicked on element with locator: {locator_tuple} at index {index}")

    def type(self, locator_tuple, value):
        element = WebDriverWait(self.driver, WAIT_TIME).until(
            EC.presence_of_element_located(locator_tuple)
        )
        element.send_keys(value)
        log.logger.info(f"Typed {value} in element with locator: {locator_tuple}")

    def getText(self, locator_tuple):
        element = WebDriverWait(self.driver, WAIT_TIME).until(
            EC.presence_of_element_located(locator_tuple)
        )
        text = element.text
        log.logger.info(f"Getting text from an element {locator_tuple}")
        return text

    def clear_field(self, locator_tuple):
        element = WebDriverWait(self.driver, WAIT_TIME).until(
            EC.presence_of_element_located(locator_tuple)
        )
        element.clear()
        log.logger.info(f"Cleared text from element with locator: {locator_tuple}")
