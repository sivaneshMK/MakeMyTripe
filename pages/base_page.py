from selenium.common import ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from conftest import logger


class BasePage:

    def __init__(self, driver):
        self.driver  = driver

    def get_web_driver_wait(self):
        return WebDriverWait(self.driver, 10)

    def get_fluent_wait(self, exception):
        return WebDriverWait(self.driver, 10, ignored_exceptions=exception)

    def click(self, locator, field_name):

        self.get_fluent_wait([ElementClickInterceptedException, StaleElementReferenceException]).until(
            EC.element_to_be_clickable(locator)
        ).click()
        logger.info(f"{field_name} is clicked")

    def enter_text(self, locator, text, field_name):
        element = self.get_web_driver_wait().until(
            EC.visibility_of_element_located(locator))

        element.clear()
        element.send_keys(text)
        logger.info(f"Entered {text} in {field_name} field")

    def is_displayed(self, locator, filed_name):

        element = self.get_web_driver_wait().until(
            EC.visibility_of_element_located(locator)
        )
        if element:
            logger.info(f"{filed_name} is Displayed")
            return True
        return False

    def get_attribute(self,locator, attribute):
        return (self.get_web_driver_wait().until(EC.visibility_of_element_located(locator))
                .get_attribute(attribute))

