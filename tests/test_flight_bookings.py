from pages.flight_booking_page import FlightBookingPage


class TestFlightBooking:
    def test_validate_user_can_book_flight(self, driver):


        flight_booking_page = FlightBookingPage(driver)

        flight_booking_page.close_authentication_popup()

