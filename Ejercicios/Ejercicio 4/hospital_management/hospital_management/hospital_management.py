from patient import Patient
from doctor import Doctor
from appointment import Appointment
from treatment import Treatment

class HospitalManagement:
    def __init__(self):
        self.patients = {}
        self.doctors = {}
        self.appointments = {}
        self.treatments = {}
        self.appointment_id_counter = 1
        self.treatment_id_counter = 1

    def manage_patients(self, action, patient=None):
        if action == "add" and patient:
            self.patients[patient.patient_id] = patient
        elif action == "delete" and patient:
            self.patients.pop(patient.patient_id, None)

    def manage_doctors(self, action, doctor=None):
        if action == "add" and doctor:
            self.doctors[doctor.doctor_id] = doctor
        elif action == "delete" and doctor:
            self.doctors.pop(doctor.doctor_id, None)

    def schedule_appointment(self, patient_id, doctor_id, datetime):
        patient = self.patients.get(patient_id)
        doctor = self.doctors.get(doctor_id)
        if not patient or not doctor:
            raise ValueError("Paciente o doctor no encontrado.")
        
        appointment = Appointment(self.appointment_id_counter, patient, doctor, datetime)
        self.appointments[self.appointment_id_counter] = appointment
        self.appointment_id_counter += 1
        return appointment

    def record_treatment(self, patient_id, doctor_id, description, date):
        patient = self.patients.get(patient_id)
        doctor = self.doctors.get(doctor_id)
        if not patient or not doctor:
            raise ValueError("Paciente o doctor no encontrado.")
        
        treatment = Treatment(self.treatment_id_counter, patient, doctor, description, date)
        self.treatments[self.treatment_id_counter] = treatment
        self.treatment_id_counter += 1
        return treatment

    def generate_reports(self):
        return {
            "total_patients": len(self.patients),
            "total_doctors": len(self.doctors),
            "total_appointments": len(self.appointments),
            "total_treatments": len(self.treatments)
        }
