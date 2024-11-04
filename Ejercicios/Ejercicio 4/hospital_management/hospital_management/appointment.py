class Appointment:
    def __init__(self, appointment_id, patient, doctor, datetime):
        if datetime not in doctor.available_slots:
            raise ValueError("Horario no disponible para el doctor.")
        
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.datetime = datetime
        self.status = 'scheduled'

    def schedule(self):
        self.status = 'scheduled'

    def cancel(self):
        self.status = 'cancelled'

    def summary(self):
        return {
            "appointment_id": self.appointment_id,
            "patient_id": self.patient.patient_id,
            "doctor_id": self.doctor.doctor_id,
            "datetime": self.datetime,
            "status": self.status
        }
