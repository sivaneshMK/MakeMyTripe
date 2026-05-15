from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class FlightBookingPage(BasePage):

    authentication_popup_close_button = (By.XPATH, "//span[@data-cy='closeModal']")
    authentication_popup = (By.XPATH, "//section[@class='modalMain tcnFooter']")
    from_city_list_box = (By.XPATH, "//input[@id='fromCity']")
    from_city_search_box = (By.XPATH, "//input[@aria-controls='react-autowhatever-1']")


    def close_authentication_popup(self):
        self.click(self.authentication_popup_close_button, "Authentication popup close button")

    def is_authentication_popup_displayed(self):
        return self.is_displayed(self.authentication_popup, "Authentication popup")

    def click_on_from_city_list_box(self):
        self.click(self.from_city_list_box, "From City List Box")

    def enter_from_city_name(self, from_city):
        self.enter_text(self.from_city_search_box, from_city, "From City search box")


    def select_airport_from_list(self, from_city):
        try:
            self.click((By.XPATH, f"//span[contains(text(),'{from_city}') and @class='revampedCityName']"), f"{from_city} airport")
        except ElementClickInterceptedException:
            self.click((By.XPATH, f"//span[contains(text(),'{from_city}') and @class='revampedCityName']"),
                       f"{from_city} airport")

    def get_selected_city_from_city_list(self):
        return self.get_attribute(self.from_city_list_box, "value")

