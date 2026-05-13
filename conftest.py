import pytest

from drivers.driver_factory import DriverFactory
from utilities.logger import Logger
from utilities.read_json import ReadJson

logger = Logger.get_logger()

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

@pytest.fixture(scope="class")
def driver(browser, config):
    logger.info(f"Launching browser: {browser}")
    driver = DriverFactory.get_driver(browser)
    driver.get(config["base_url"])
    logger.info(f"Launching URL: {config["base_url"]}")
    yield driver
    logger.info("closing browser")
    DriverFactory.quit_driver()