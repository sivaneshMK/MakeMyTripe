import time

import pytest

import conftest
from pages.flight_booking_page import FlightBookingPage
from utilities.common_utils import CommonUtils
from utilities.db_utility import DbUtility
from utilities.excel_reader import ExcelReader


class TestFlightBooking:

    def test_authentication_popup_is_displayed(self, driver, test_data):
        flight_booking_page = FlightBookingPage(driver)
        conftest.logger.info(test_data["username"]+test_data["password"])
        conftest.logger.info(test_data)
        flag = flight_booking_page.is_authentication_popup_displayed()
        assert flag == True, "The authentication popup is not displayed"



    multiple_city = ExcelReader.get_multiple_test_data("FlightBooking", "test_user_can_select_different_from_city")

    @pytest.mark.wip
    @pytest.mark.parametrize(
        "data", multiple_city
    )
    def test_user_can_select_different_from_city(self, driver, test_data, data):
        # file_path = "C:\\Users\\sivan\\PycharmProjects\\MakeMyTripe\\test_data\\test_data.xlsx"
        # test_data = ExcelReader.get_test_data(file_path, "FlightBooking","test_user_can_select_different_from_city")
        flight_booking_page = FlightBookingPage(driver)
        flight_booking_page.close_authentication_popup()
        flight_booking_page.click_on_from_city_list_box()
        flight_booking_page.enter_from_city_name(data["FromCity"])
        flight_booking_page.select_airport_from_list(data["FromCity"])
        selected_city = flight_booking_page.get_selected_city_from_city_list()
        assert selected_city ==data["FromCity"], "user is not able to select From city"

    def test_db(self, get_db_connection):
        connection = get_db_connection
        data = DbUtility.execute_query(connection, "SELECT * FROM automation2026.std_standared;")
        for row in data:
            print(row["ROLL_NO"])
        print(data)
