import pytest


@pytest.mark.flaky(reruns=5)
@pytest.mark.usefixtures("log_on_failure", "appium_driver")
class BaseTest:
    pass

@pytest.mark.flaky(reruns=5)
@pytest.mark.usefixtures("log_on_failure", "appium_driver_SP")
class BaseTestSP:
    pass