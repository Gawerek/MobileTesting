# import allure
import pytest
# from allure_commons.types import AttachmentType
from appium import webdriver


import pytest
from faker import Faker
import random
from Utilities.app_manager import AppManager


# Function to generate random contact
def generate_random_contact():
    # Initialize a Faker generator with a specific locale
    faker = Faker('pl_PL')  # Polish locale
    name = faker.name()
    phone_number = ''.join([str(random.randint(0, 9)) for _ in range(9)])
    address = faker.address().replace('pl. ', '')  # Remove 'pl.' prefix
    return name, phone_number, address

# Fixture to provide random contact data
@pytest.fixture(scope="function")
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
    # desired_caps['appPackage'] = configReader.readConfiguration("configuration", "app_package")
    # desired_caps['appActivity'] = configReader.readConfiguration("configuration", "app_activity")
    desired_caps['appPackage'] = 'com.leaware.beautybox'
    desired_caps['appActivity'] = 'com.leaware.beautybox.MainActivity'
    # desired_caps['appPackage'] = 'bbox.sp.pl.app'
    # desired_caps['appActivity'] = 'bbox.sp.pl.app.MainActivity'
    desired_caps['newCommandTimeout'] = '5000'

    desired_caps['noReset'] = True
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    request.cls.driver = driver
    driver.implicitly_wait(7)
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def appium_driver_CLI(request):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['deviceName'] = 'Android'
    desired_caps['automationName'] = 'uiautomator2'
    # desired_caps['appPackage'] = 'bbox.pl.client.app'
    desired_caps['appPackage'] = 'bbox.pl.client.app.development'
    desired_caps['appActivity'] = 'bbox.pl.client.app.MainActivity'
    desired_caps['noReset'] = True
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    request.cls.driver = driver
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def appium_driver_SP(request):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['deviceName'] = 'Android'
    # desired_caps['appPackage'] = 'bbox.sp.pl.app'
    # Testing env
    desired_caps['appPackage'] = 'bbox.pl.sp.app.development'
    desired_caps['appActivity'] = 'bbox.sp.pl.app.MainActivity' 
    desired_caps['noReset'] = True
    driver = webdriver.Remote('http://localhost:4725/wd/hub', desired_caps)
    request.cls.driver = driver
    driver.implicitly_wait(10)
    yield driver
    driver.quit()






# Konfiguracja dla testowania na BrowserStack
# @pytest.fixture(scope="function")
# def appium_driver_browserstack(request):
#     userName = 'YOUR_USER'
#     accessKey = 'YOUR_ACCESS_KEY'
#
#     app_manager = AppManager(userName, accessKey)
#     cli_app = app_manager.get_cli_app()
#     sp_app = app_manager.get_sp_app()
#
#     desired_caps = {
#         'platformName': 'Android',
#         'deviceName': 'Samsung Galaxy S21',
#         'app': cli_app,
#         'otherApps': [sp_app],
#         'autoGrantPermissions': True,
#         'browserstack.idleTimeout': 300
#     }
#
#     driver = webdriver.Remote("https://..." + userName + ":" + accessKey + "@hub-cloud.browserstack.com/wd/hub",
#                               desired_caps)
#     request.cls.driver = driver
#     yield driver, app_manager
#     driver.quit()

    # @pytest.fixture()
    # def log_on_failure(request, appium_driver):
    #     yield
    #     item = request.node
    #     driver = appium_driver
    #     if item.rep_call.failed:
    #         allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
