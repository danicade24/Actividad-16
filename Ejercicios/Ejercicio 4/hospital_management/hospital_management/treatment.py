class Treatment:
    def __init__(self, treatment_id, patient, doctor, description, date):
        if not description.strip():
            raise ValueError("La descripción debe ser una cadena no vacía.")
        
        self.treatment_id = treatment_id
        self.patient = patient
        self.doctor = doctor
        self.description = description
        self.date = date

    def update_treatment(self, description):
        if not description.strip():
            raise ValueError("La descripción debe ser una cadena no vacía.")
        self.description = description

    def summary(self):
        return {
            "treatment_id": self.treatment_id,
            "patient_id": self.patient.patient_id,
            "doctor_id": self.doctor.doctor_id,
            "description": self.description,
            "date": self.date
        }
