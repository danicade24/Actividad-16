import pytest
from hospital_management import HospitalManagement
from patient import Patient
from doctor import Doctor

def test_add_patient():
    hospital = HospitalManagement()
    patient = Patient(1, "John Doe", "1990-01-01")
    hospital.manage_patients("add", patient)
    assert 1 in hospital.patients

def test_add_doctor():
    hospital = HospitalManagement()
    doctor = Doctor(1, "Dr. Smith", "Cardiology")
    hospital.manage_doctors("add", doctor)
    assert 1 in hospital.doctors

def test_schedule_appointment():
    hospital = HospitalManagement()
    patient = Patient(1, "John Doe", "1990-01-01")
    doctor = Doctor(1, "Dr. Smith", "Cardiology")
    doctor.add_available_slot("2023-12-01 10:00")
    hospital.manage_patients("add", patient)
    hospital.manage_doctors("add", doctor)
    appointment = hospital.schedule_appointment(1, 1, "2023-12-01 10:00")
    assert appointment.status == "scheduled"

def test_record_treatment():
    hospital = HospitalManagement()
    patient = Patient(1, "John Doe", "1990-01-01")
    doctor = Doctor(1, "Dr. Smith", "Cardiology")
    hospital.manage_patients("add", patient)
    hospital.manage_doctors("add", doctor)
    treatment = hospital.record_treatment(1, 1, "Heart surgery", "2023-11-01")
    assert treatment.description == "Heart surgery"
