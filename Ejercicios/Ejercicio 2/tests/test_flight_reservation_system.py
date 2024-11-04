import pytest
from flight_reservation_system import FlightReservationSystem

def test_register_user():
    system = FlightReservationSystem()
    user = system.register_user("John Doe", "johndoe@example.com", "securepassword")
    assert user.name == "John Doe"
    assert user.email == "johndoe@example.com"

def test_add_flight():
    system = FlightReservationSystem()
    system.add_flight("FL123", "Lima", "Cusco", "10:00", "11:30", 10)
    flight = system.flights["FL123"]
    assert flight.origin == "Lima"
    assert flight.destination == "Cusco"

def test_search_flights():
    system = FlightReservationSystem()
    system.add_flight("FL123", "Lima", "Cusco", "10:00", "11:30", 10)
    flights = system.search_flights("Lima", "Cusco")
    assert len(flights) == 1
    assert flights[0]["flight_number"] == "FL123"

def test_reserve_seat():
    system = FlightReservationSystem()
    user = system.register_user("Jane Doe", "janedoe@example.com", "password123")
    system.add_flight("FL456", "Lima", "Arequipa", "12:00", "13:30", 5)
    reservation = system.reserve_seat(user.user_id, "FL456", 1)
    assert reservation.seat_number == 1
    assert reservation.status == 'active'

def test_cancel_reservation():
    system = FlightReservationSystem()
    user = system.register_user("Jane Doe", "janedoe@example.com", "password123")
    system.add_flight("FL789", "Lima", "Trujillo", "14:00", "15:30", 5)
    reservation = system.reserve_seat(user.user_id, "FL789", 2)
    system.cancel_reservation(user.user_id, reservation.reservation_id)
    assert reservation.status == 'cancelled'
