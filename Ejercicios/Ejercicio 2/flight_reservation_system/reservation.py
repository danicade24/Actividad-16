class Reservation:
    def __init__(self, reservation_id, user, flight, seat_number):
        self.reservation_id = reservation_id
        self.user = user
        self.flight = flight
        self.seat_number = seat_number
        self.status = 'active'

    def cancel_reservation(self):
        self.status = 'cancelled'

    def summary(self):
        return {
            "reservation_id": self.reservation_id,
            "user": self.user.user_id,
            "flight": self.flight.flight_number,
            "seat_number": self.seat_number,
            "status": self.status
        }
