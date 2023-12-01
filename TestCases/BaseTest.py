import pytest


@pytest.mark.flaky(reruns=5)
@pytest.mark.usefixtures("appium_driver")
class BaseTest:
    pass

@pytest.mark.flaky(reruns=5)
@pytest.mark.usefixtures("appium_driver_SP")
class BaseTestSP:
    pass


# class CombinedBaseTest(BaseTest, BaseTestSP):
#     pass


import pytest

@pytest.mark.usefixtures("appium_driver", "appium_driver_SP")
class CombinedBaseTest:
    def __init__(self, driver1, driver2):
        self.driver1 = driver1
        self.driver2 = driver2