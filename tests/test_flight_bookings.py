import time

import pytest

from pages.flight_booking_page import FlightBookingPage


class TestFlightBooking:

    def test_authentication_popup_is_displayed(self, driver):
        flight_booking_page = FlightBookingPage(driver)
        flag = flight_booking_page.is_authentication_popup_displayed()
        assert flag == True, "The authentication popup is not displayed"

    @pytest.mark.wip
    def test_user_can_select_different_from_city(self, driver):
        flight_booking_page = FlightBookingPage(driver)
        flight_booking_page.close_authentication_popup()
        flight_booking_page.click_on_from_city_list_box()
        flight_booking_page.enter_from_city_name("Chennai")
        flight_booking_page.select_airport_from_list("Chennai")
        selected_city = flight_booking_page.get_selected_city_from_city_list()
        assert selected_city =="Chennai", "user is not able to select From city"

