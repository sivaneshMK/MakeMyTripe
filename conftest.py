import base64
from pathlib import Path

import pytest
import pytest_html

from drivers.driver_factory import DriverFactory
from utilities.excel_reader import ExcelReader
from utilities.logger import Logger
from utilities.read_json import ReadJson
from utilities.screenshot import Screenshot

logger = Logger.get_logger()

#pytest_plugin = ["hooks.hooks"]

#inbuild fixture
def pytest_addoption(parser):
    parser.addoption("--env",
                     action="store",
                     default ="test",
                     help = "Environment Setup")

@pytest.fixture(scope="session")
def config(request):
    env = request.config.getoption("--env")
    logger.info(f"Running tests in {env} environment")
    return ReadJson.get_config(env)

@pytest.fixture(scope="session")
def browser(config):
    return config["browser"]

@pytest.fixture(scope="function")
def driver(browser, config):
    logger.info(f"Launching browser: {browser}")
    driver = DriverFactory.get_driver(browser)
    driver.get(config["base_url"])
    logger.info(f"Launching URL: {config["base_url"]}")
    global max_wait_time
    max_wait_time = config["max_wait"]
    yield driver
    logger.info("closing browser")
    DriverFactory.quit_driver()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    print("hooks is tiggered")
    outcome= yield
    report = outcome.get_result()

    if report.when=="call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            path = Screenshot.capture(driver, item.name)

            with open(path, "rb") as image_file:
                encoded_image = base64.b64encode(image_file.read()).decode()

            #attach to report
            extra = getattr(report, "extra", [])
            extra.append(pytest_html.extras.png(encoded_image))
            report.extra = extra

@pytest.fixture(scope="function")
def test_data(request, config):
    test_name = request.node.name
    root_path = Path(__file__).parent
    file_path = root_path/"test_data"/"test_data.xlsx"
    data = ExcelReader.get_test_data(file_path, "FlightBooking", test_name)
    return data
