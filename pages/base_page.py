from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from conftest import logger


class BasePage:

    def __init__(self, driver):
        self.driver  = driver

    def click(self, locator, field_name):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()
        logger.info(f"{field_name} is clicked")

    def enter_text(self, locator, text, field_name):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator))

        element.clear()
        element.send_keys(text)
        logger.info(f"Entered {text} in {field_name} field")