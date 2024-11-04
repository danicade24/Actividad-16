class Flight:
    def __init__(self, flight_number, origin, destination, departure_time, arrival_time, seats_available):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.seats_available = seats_available
        self.seat_map = {seat: True for seat in range(1, seats_available + 1)}  # True means available

    def reserve_seat(self, seat_number):
        if seat_number not in self.seat_map:
            raise ValueError("El asiento no existe.")
        if not self.seat_map[seat_number]:
            raise ValueError("El asiento ya está reservado.")
        self.seat_map[seat_number] = False  # Mark as reserved

    def cancel_reservation(self, seat_number):
        if seat_number not in self.seat_map:
            raise ValueError("El asiento no existe.")
        if self.seat_map[seat_number]:
            raise ValueError("El asiento no está reservado.")
        self.seat_map[seat_number] = True  # Mark as available

    def summary(self):
        return {
            "flight_number": self.flight_number,
            "origin": self.origin,
            "destination": self.destination,
            "departure_time": self.departure_time,
            "arrival_time": self.arrival_time,
            "seats_available": self.seats_available,
            "seat_map": self.seat_map
        }
