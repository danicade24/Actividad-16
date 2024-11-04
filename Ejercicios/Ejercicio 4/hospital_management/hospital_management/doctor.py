class Doctor:
    def __init__(self, doctor_id, name, specialization):
        if not specialization.strip():
            raise ValueError("La especialización debe ser una cadena válida.")
        
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.available_slots = set()

    def add_available_slot(self, slot):
        self.available_slots.add(slot)

    def remove_available_slot(self, slot):
        self.available_slots.discard(slot)

    def summary(self):
        return {
            "doctor_id": self.doctor_id,
            "name": self.name,
            "specialization": self.specialization,
            "available_slots": list(self.available_slots)
        }
