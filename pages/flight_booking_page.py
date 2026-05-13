from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class FlightBookingPage(BasePage):

    close_authentication_popup_button = (By.XPATH, "//span[@data-cy='closeModal']")

    def close_authentication_popup(self):
        self.click(self.close_authentication_popup_button, "Authentication popup close button")

