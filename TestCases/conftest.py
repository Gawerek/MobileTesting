# import allure
import pytest
# from allure_commons.types import AttachmentType
from appium import webdriver


import pytest
from faker import Faker
import random

# Function to generate random contact
def generate_random_contact():
    faker = Faker()
    name = faker.name()
    phone_number = ''.join([str(random.randint(0, 9)) for _ in range(9)])
    return name, phone_number

# Fixture to provide random contact data
@pytest.fixture(scope="module")
def random_contact():
    return generate_random_contact()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="function")
def appium_driver(request):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['deviceName'] = 'Android'
    desired_caps['automationName'] = 'uiautomator2'
    desired_caps['appPackage'] = 'bbox.pl.client.app.development'
    desired_caps['appActivity'] = 'bbox.pl.client.app.MainActivity'
    desired_caps['noReset'] = True
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    request.cls.driver = driver
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def appium_driver_SP(request):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['deviceName'] = 'Android'
    # desired_caps['appPackage'] = 'bbox.sp.pl.app'
    desired_caps['appPackage'] = 'bbox.sp.pl.app.development'
    desired_caps['appActivity'] = 'bbox.sp.pl.app.MainActivity'
    desired_caps['noReset'] = True
    driver = webdriver.Remote('http://localhost:4725/wd/hub', desired_caps)
    request.cls.driver = driver
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# @pytest.fixture()
# def log_on_failure(request, appium_driver):
#     yield
#     item = request.node
#     driver = appium_driver
#     if item.rep_call.failed:
#         allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
