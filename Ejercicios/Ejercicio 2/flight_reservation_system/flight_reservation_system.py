from user import User
from flight import Flight
from reservation import Reservation

class FlightReservationSystem:
    def __init__(self):
        self.users = {}
        self.flights = {}
        self.reservations = {}
        self.user_id_counter = 1
        self.reservation_id_counter = 1

    def register_user(self, name, email, password):
        user = User(self.user_id_counter, name, email, password)
        self.users[self.user_id_counter] = user
        self.user_id_counter += 1
        return user

    def search_flights(self, origin, destination):
        return [flight.summary() for flight in self.flights.values() if flight.origin == origin and flight.destination == destination]

    def add_flight(self, flight_number, origin, destination, departure_time, arrival_time, seats_available):
        flight = Flight(flight_number, origin, destination, departure_time, arrival_time, seats_available)
        self.flights[flight_number] = flight

    def reserve_seat(self, user_id, flight_number, seat_number):
        user = self.users.get(user_id)
        flight = self.flights.get(flight_number)
        if not user or not flight:
            raise ValueError("Usuario o vuelo no encontrado.")
        flight.reserve_seat(seat_number)
        reservation = Reservation(self.reservation_id_counter, user, flight, seat_number)
        user.add_reservation(flight_number, seat_number)
        self.reservations[self.reservation_id_counter] = reservation
        self.reservation_id_counter += 1
        return reservation

    def cancel_reservation(self, user_id, reservation_id):
        reservation = self.reservations.get(reservation_id)
        if not reservation or reservation.user.user_id != user_id:
            raise ValueError("Reserva no encontrada.")
        reservation.cancel_reservation()
        reservation.flight.cancel_reservation(reservation.seat_number)
        reservation.user.cancel_reservation(reservation.flight.flight_number, reservation.seat_number)
