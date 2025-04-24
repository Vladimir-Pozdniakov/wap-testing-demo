import pytest

from framework.devices.device_manager import DeviceManager
from framework.reporter.reporter import (
    add_allure_report_properties,
    clean_report_results,
    generate_report_at_the_end,
)

pytest_plugins = [
    "framework.fixtures.pages",
]


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome-mobile",
        help="Specify the Browser to run the tests on:",
        choices=("chrome", "chrome-mobile", "firefox"),
    )


@pytest.fixture(
    scope="session",
)
def browser(request) -> str:
    try:
        return request.config.getoption("--browser")
    except ValueError:
        raise ValueError("Missed or Incorrect the --browser option")


@pytest.fixture(scope="session")
def driver(browser):
    # Initialize the driver
    driver = DeviceManager(browser).get_driver()
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(15)

    # Yield the driver to the test
    yield driver

    # Cleanup after the test is complete
    driver.quit()


@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart():
    clean_report_results()
    add_allure_report_properties()


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish():
    generate_report_at_the_end()
