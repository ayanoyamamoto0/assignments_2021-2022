# Import Patient class from patient.py
from patient import Patient

# Import Treatment class from treatment.py
from treatment import Treatment

# Import sqlite3 module
import sqlite3


# Class to represent the database service in the program
class DBService:

    # Constructor to assign a database filename to the DBService object
    # Connects to the database and sets the cursor
    def __init__(self, filename):
        self.filename = filename
        self.conn = sqlite3.connect(filename)
        self.c = self.conn.cursor()

    # Method to insert Patient object to the database
    def insert_patient_obj(self, new_patient: Patient):

        # Tries to insert object attributes into Patients table
        try:
            query = f"INSERT INTO Patients (firstname, lastname, dob, address, phone, ppsn)" \
                    f"VALUES ('{new_patient.firstname}', '{new_patient.lastname}', '{new_patient.dob}', " \
                    f"'{new_patient.address}', '{new_patient.phone}', '{new_patient.ppsn}');"
            self.c.execute(query)
            self.conn.commit()
            return self.c.lastrowid

        # If there is an error inserting to database, displays the error message
        except Exception as e:
            print(f"\nFailed to write to database\n{e}")
            return

    # Method to insert Treatment object to the database
    def insert_treatment_obj(self, new_treatment: Treatment):

        # Tries to insert object attributes into Treatments table
        try:
            query = f"INSERT INTO Treatments (patient_id, admission_time, admission_summary, " \
                    f"triage_time, triage_nurse, body_temp, pulse_rate, respiration_rate, bp_systolic, " \
                    f"bp_diastolic, triage_summary, priority_value, treatment_time, treatment_doctor, treatment_summary)" \
                    f"VALUES({new_treatment.patient_id}, '{new_treatment.admission_time}', " \
                    f"'{new_treatment.admission_summary}','{new_treatment.triage_time}', '{new_treatment.triage_nurse}'," \
                    f"{new_treatment.body_temp}, {new_treatment.pulse_rate}, {new_treatment.respiration_rate}, " \
                    f"{new_treatment.bp_systolic}, {new_treatment.bp_diastolic}, '{new_treatment.triage_summary}'," \
                    f"{new_treatment.priority_value}, '{new_treatment.treatment_time}'," \
                    f"'{new_treatment.treatment_doctor}', '{new_treatment.treatment_summary}');"
            self.c.execute(query)
            self.conn.commit()
            return True

        # If there is an error inserting to database, displays the error message
        except Exception as e:
            print(f"\nFailed to write to database\n{e}")
            return False

    # Method to check if a specified patient_id exists in the database
    def check_patient_id_in_db(self, patient_id):

        # Tries to query for the specified patient_id in the database
        # If it can fetch the next row of the result successfully, returns True
        # If the result of the fetch is None, returns False
        try:
            self.c.execute(f"SELECT p.patient_id FROM Patients p WHERE p.patient_id = {patient_id}")
            row = self.c.fetchone()
            if row is None:
                return False
            else:
                return True

        # If there is an error, displays the error message and returns False
        except Exception as e:
            print(f"\n{e}")
            return False

    # Method to return the patient's first and last names from the database
    def get_patient_name(self, patient_id):

        # Tries to query the first and last names for the specified patient_id in the database
        try:
            for row in self.c.execute(f"SELECT p.firstname, p.lastname FROM Patients p "
                                      f"WHERE p.patient_id = {patient_id};"):
                return row

        # If there is an error in the query, displays the error message
        except Exception as e:
            print(f"\n{e}")
            return False

    # Method to return treatment records for specified patient's name
    def query_patient_name(self, name):

        # Tries to query the admission ID, patient ID, first name, last name, admission time, admission summary,
        # treatment doctor, and treatment summary for the specified patient's name in the database
        try:
            query = f"SELECT t.admission_id, p.patient_id, p.firstname, p.lastname, t.admission_time, " \
                    f"t.admission_summary, t.treatment_doctor, t.treatment_summary FROM Patients p " \
                    f"INNER JOIN Treatments t ON p.patient_id = t.patient_id " \
                    f"WHERE p.firstname LIKE '%{name}%'" \
                    f"OR p.lastname LIKE '%{name}%'" \
                    f"OR p.firstname || ' ' || p.lastname LIKE '%{name}%'" \
                    f"OR p.firstname || p.lastname LIKE '%{name}%';"
            self.c.execute(query)
            rows = self.c.fetchall()
            return rows

        # If there is an error executing query, displays the error message
        except Exception as e:
            print(f"\n{e}")
            return

    # Method to return treatment records for specified date
    def query_date(self, date):

        # Tries to query the admission ID, patient ID, first name, last name, admission time, admission summary,
        # treatment doctor, and treatment summary for the specified date in the database
        try:
            query = f"SELECT t.admission_id, p.patient_id, p.firstname, p.lastname, t.admission_time, " \
                    f"t.admission_summary, t.treatment_doctor, t.treatment_summary FROM Treatments t " \
                    f"INNER JOIN Patients p ON p.patient_id = t.patient_id " \
                    f"WHERE t.admission_time LIKE '{date}%';"
            self.c.execute(query)
            rows = self.c.fetchall()
            return rows

        # If there is an error executing query, displays the error message
        except Exception as e:
            print(f"\n{e}")
            return

    # Method to return treatment records for specified doctor's name
    def query_doctor(self, name):

        # Tries to query the admission ID, patient ID, first name, last name, admission time, admission summary,
        # treatment doctor, and treatment summary for the specified doctor's name in the database
        try:
            query = f"SELECT t.admission_id, p.patient_id, p.firstname, p.lastname, t.admission_time, " \
                    f"t.admission_summary, t.treatment_doctor, t.treatment_summary FROM Patients p " \
                    f"INNER JOIN Treatments t ON p.patient_id = t.patient_id " \
                    f"WHERE t.treatment_doctor LIKE '%{name}%';"
            self.c.execute(query)
            rows = self.c.fetchall()
            return rows

        # If there is an error executing query, displays the error message
        except Exception as e:
            print(f"\n{e}")
            return

    # Method to update patient's information in the database
    def set_patient_info(self, patient_id, firstname, lastname, dob, address, phone, ppsn):

        # Tries to update patient's information in the database with user input
        try:
            query = f"UPDATE Patients " \
                    f"SET firstname = '{firstname}', lastname = '{lastname}', dob = '{dob}', " \
                    f"address = '{address}', phone = '{phone}', ppsn = '{ppsn}' " \
                    f"WHERE patient_id = {patient_id};"
            self.c.execute(query)
            self.conn.commit()
            return True

        # If there is an error updating the database, displays the error message
        except Exception as e:
            print(f"\nFailed to write to database\n{e}")
            return False

    # Method to delete a patient and their treatment records from database
    def delete_patient(self, patient_id):

        # Tries to delete a patient with the specified patient_id
        try:
            query = f"DELETE FROM Patients WHERE patient_id = {patient_id};"
            self.c.execute("PRAGMA foreign_keys = ON")
            self.c.execute(query)
            self.conn.commit()
            return True

        # If there is an error deleting patient from database, displays the error message
        except Exception as e:
            print(f"\nFailed to delete from database\n{e}")
            return False
