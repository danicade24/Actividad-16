class User:
    def __init__(self, user_id, name, email, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.reservations = []

    def authenticate(self, email, password):
        return self.email == email and self.password == password

    def update_info(self, name, email):
        self.name = name
        self.email = email

    def add_reservation(self, flight_number, seat_number):
        self.reservations.append({"flight_number": flight_number, "seat_number": seat_number})

    def cancel_reservation(self, flight_number, seat_number):
        self.reservations = [res for res in self.reservations if not (res["flight_number"] == flight_number and res["seat_number"] == seat_number)]
