class Patient:
    def __init__(self, patient_id, name, dob):
        if not name.strip():
            raise ValueError("El nombre debe ser una cadena no vacía.")
        
        self.patient_id = patient_id
        self.name = name
        self.dob = dob
        self.medical_history = []

    def update_info(self, name, dob):
        if not name.strip():
            raise ValueError("El nombre debe ser una cadena no vacía.")
        self.name = name
        self.dob = dob

    def add_medical_history(self, entry):
        self.medical_history.append(entry)

    def summary(self):
        return {
            "patient_id": self.patient_id,
            "name": self.name,
            "dob": self.dob,
            "medical_history": self.medical_history
        }
