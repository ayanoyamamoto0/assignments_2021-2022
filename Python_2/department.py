# Import Patient class from patient.py
from patient import Patient

# Import Treatment class from treatment.py
from treatment import Treatment

# Import DBService class from dbservice.py
from dbservice import DBService

# Import SLL class from sll.py
from sll import SLL

# Import Node class from node.py
from node import Node

# Import datetime module
from datetime import datetime


# Function to display information from triage
def display_triage_info(patient):
    print(f"Triage Time: {patient.triage_time}\n"
          f"Triage Nurse: {patient.triage_nurse}\n"
          f"Body Temperature: {patient.body_temp}°C\n"
          f"Pulse Rate: {patient.pulse_rate}bpm\n"
          f"Respiration Rate: {patient.respiration_rate}bpm\n"
          f"Blood Pressure (Sys/Dia): {patient.bp_systolic}mmHg/{patient.bp_diastolic}mmHg\n"
          f"Triage Summary: {patient.triage_summary}\n"
          f"Priority Value: {patient.priority_value}")


# Function to display treatment information from database
def display_treatment_info(query):
    print(f"-------------------------------------------------------------------------------------\n"
          f"     Admission ID: {query[0]}\n"
          f"-------------------------------------------------------------------------------------\n"
          f"Patient ID: {query[1]}\n"
          f"Patient Name: {query[2]} {query[3]}\n"
          f"Admission Time: {query[4]}\n"
          f"Admission Summary: {query[5]}\n"
          f"Treatment Doctor: {query[6]}\n"
          f"Treatment Summary: {query[7]}")


# Function to validate if input is a number
def number_input(input_string):
    while True:
        i = input(input_string)
        try:
            i = int(i)
        except ValueError:
            try:
                i = float(i)
            except ValueError:
                print("Please enter a number")
                continue
        break
    return i


# Function to validate if input is a positive integer
def int_input(input_string):
    while True:
        i = input(input_string)
        try:
            i = int(i)
        except ValueError:
            print("Please enter an integer")
            continue
        if i < 0:
            print("Please enter a positive number")
            continue
        break
    return i


# Function to validate if input is an integer between 1-10
def priority_value_input(input_string):
    while True:
        i = input(input_string)
        try:
            i = int(i)
        except ValueError:
            print("Please enter an integer between 1-10")
            continue
        if i <= 0 or i > 10:
            print("Please enter an integer between 1-10")
            continue
        break
    return i


# Function to validate if there is an input
def str_input(input_string):
    empty_string = ""
    while True:
        i = input(input_string)
        if i == empty_string:
            print("This field cannot be empty")
            continue
        break
    return i


# Class to represent the department service in the program
class Department:

    # Constructor to assign 3 values to the Department object
    # Parameters are: department_name, sll, db_service
    def __init__(self, department_name, sll: SLL, db_service: DBService):
        self.department_name = department_name
        self.sll = sll
        self.db_service = db_service

    # Method to return the number of patients currently admitted
    def current_admission(self):
        current_admission_list_size = self.sll.list_size()
        return current_admission_list_size

    # Method to return the number of patients awaiting triage
    def triage_queue_size(self):
        counter = 1
        queue_size = 0
        while counter <= self.current_admission():
            tmp_node: Node = self.sll.get_node(counter)
            tmp_patient = tmp_node.get_data()
            if tmp_patient.priority_value == 0:
                queue_size += 1
            counter += 1
        return queue_size

    # Method to return the number of patients awaiting treatment
    def treatment_queue_size(self):
        queue_size = self.current_admission() - self.triage_queue_size()
        return queue_size

    # Method to confirm if a patient ID exists in singly linked list
    def check_patient_id_in_sll(self, patient_id):
        counter = 1
        result = True
        while counter <= self.current_admission():
            tmp_node = self.sll.get_node(counter)
            tmp_patient = tmp_node.get_data()
            if tmp_patient.patient_id == patient_id:
                result = False
            counter += 1
        return result

    # Method to add a new patient in self.sll
    def add_new_patient(self):

        # Asks user to input patient information
        new_patient = Patient(str_input("First Name: "), str_input("Last Name: "),
                              str_input("Date of Birth (YYYY-MM-DD): "), str_input("Address: "),
                              str_input("Phone Number: "), input("PPS Number: "))

        # Inserts new patient information into database and returns the new Patient ID
        new_patient_id = self.db_service.insert_patient_obj(new_patient)

        # If the patient information was successfully inserted,
        # asks user to input admission information and saves them in singly linked list
        if new_patient_id is not None:
            self.sll.add(Treatment(new_patient_id, f"{datetime.now().strftime('%Y-%m-%d, %H:%M:%S')}",
                                   str_input("Admission Summary: ")))

    # Method to add an existing patient in singly linked list
    def add_existing_patient(self):

        # Asks user to input patient ID
        patient_id = int_input("Patient ID: ")

        # Displays a message if the patient ID does not exist in database
        if not self.db_service.check_patient_id_in_db(patient_id):
            print("Patient not found")

        # Displays a message if the patient ID already exists in singly linked list
        elif not self.check_patient_id_in_sll(patient_id):
            print("Patient already admitted")

        # Otherwise asks user to input admission information and saves them in singly linked list
        else:
            self.sll.add(Treatment(patient_id, f"{datetime.now().strftime('%Y-%m-%d, %H:%M:%S')}",
                                   str_input("Admission Summary: ")))

    # Method to return the next patient awaiting triage
    def next_triage_patient(self):
        counter = 1
        while counter <= self.current_admission():
            tmp_node = self.sll.get_node(counter)
            tmp_patient = tmp_node.get_data()
            if tmp_patient.priority_value == 0:
                return tmp_patient
            counter += 1

    # Method to display admission information
    def display_admission_info(self, patient):
        print(f"Name: {self.db_service.get_patient_name(patient.patient_id)[0]} "
              f"{self.db_service.get_patient_name(patient.patient_id)[1]}\n"
              f"Admission Time: {patient.admission_time}\n"
              f"Admission Summary: {patient.admission_summary}")

    # Method to update Patient object with triage information
    def update_triage_in_sll(self, patient_id, triage_time, triage_nurse, body_temp, pulse_rate,
                             respiration_rate, bp_systolic, bp_diastolic, triage_summary, priority_value):
        counter = 1
        while counter <= self.current_admission():
            tmp_node = self.sll.get_node(counter)
            tmp_patient = tmp_node.get_data()
            if tmp_patient.patient_id == patient_id:
                tmp_patient.triage(triage_time, triage_nurse, body_temp, pulse_rate, respiration_rate, bp_systolic,
                                   bp_diastolic, triage_summary, priority_value)
            counter += 1

    # Method to display admission information of the next patient awaiting triage
    # and update Treatment object with user input of triage information
    def add_triage_info(self):
        triage_patient = self.next_triage_patient()
        self.display_admission_info(triage_patient)
        self.update_triage_in_sll(triage_patient.patient_id,
                                  f"{datetime.now().strftime('%Y-%m-%d, %H:%M:%S')}",
                                  str_input("Triage Nurse Name: "), number_input("Body Temperature: "),
                                  int_input("Pulse Rate: "), int_input("Respiration Rate: "),
                                  int_input("Blood Pressure (Systolic): "),
                                  int_input("Blood Pressure (Diastolic): "), str_input("Triage Summary: "),
                                  priority_value_input("Priority Value (1-10): "))

    # Method to return the next patient awaiting treatment and their position in singly linked list
    def next_treatment_patient(self):
        highest_priority_patient = None
        position = 0
        counter = 1
        while counter <= self.current_admission():
            tmp_node = self.sll.get_node(counter)
            tmp_patient = tmp_node.get_data()
            if highest_priority_patient is None:
                highest_priority_patient = tmp_patient
                position = 1
            else:
                if tmp_patient.priority_value > highest_priority_patient.priority_value:
                    highest_priority_patient = tmp_patient
                    position = counter
            counter += 1
        return highest_priority_patient, position

    # Method to update Patient object with treatment information
    def update_treatment_in_sll(self, patient_id, treatment_time, treatment_doctor, treatment_summary):
        counter = 1
        while counter <= self.current_admission():
            tmp_node = self.sll.get_node(counter)
            tmp_patient = tmp_node.get_data()
            if tmp_patient.patient_id == patient_id:
                tmp_patient.treatment(treatment_time, treatment_doctor, treatment_summary)
            counter += 1

    # Method to display admission information of the next patient awaiting treatment
    # and update Treatment object with user input of treatment information
    def add_treatment_info(self):
        treatment_patient = self.next_treatment_patient()[0]
        position = self.next_treatment_patient()[1]
        self.display_admission_info(treatment_patient)
        display_triage_info(treatment_patient)
        self.update_treatment_in_sll(treatment_patient.patient_id, f"{datetime.now().strftime('%Y-%m-%d, %H:%M:%S')}",
                                     str_input("Treatment Doctor Name: "), str_input("Treatment Summary: "))

        # Saves Treatment object to database
        if self.db_service.insert_treatment_obj(treatment_patient):
            # If successfully saved, removes patient from singly linked list
            self.sll.remove(position)

    # Method to search database for patient's name
    def search_patient_name(self):

        # Asks user to input patient's name and searches the database
        input_name = str_input("Please enter the patient name to search: ")
        search_result = self.db_service.query_patient_name(input_name)

        # Displays a message if the patient ID does not exist in database
        if not search_result:
            print("No record found")

        # Otherwise displays treatment information with matching patient's names
        else:
            for row in search_result:
                display_treatment_info(row)

    # Method to search database for patient's admission date
    def search_date(self):

        # Asks user to input date and searches the database
        input_date = str_input("Please enter the admission date to search (YYYY-MM-DD): ")
        search_result = self.db_service.query_date(input_date)

        # Displays a message if the patient ID does not exist in database
        if not search_result:
            print("No record found")

        # Otherwise displays treatment information with matching dates
        else:
            for row in search_result:
                display_treatment_info(row)

    # Method to search database for doctor's name
    def search_doctor(self):

        # Asks user to input doctor's name and searches the database
        input_name = str_input("Please enter the doctor name to search: ")
        search_result = self.db_service.query_doctor(input_name)

        # Displays a message if the patient ID does not exist in database
        if not search_result:
            print("No record found")

        # Otherwise displays treatment information with matching doctor names
        else:
            for row in search_result:
                display_treatment_info(row)

    # Method to update patient information in database
    def update_patient_info(self):

        # Asks user to input patient ID
        patient_id = int_input("Please enter the Patient ID to update: ")

        # Displays a message if the patient ID does not exist in database
        if not self.db_service.check_patient_id_in_db(patient_id):
            print("Patient not found")

        # Otherwise updates database with user input of new patient details
        else:
            if self.db_service.set_patient_info(patient_id, str_input("First Name: ").replace("'", "''"),
                                                str_input("Last Name: ").replace("'", "''"),
                                                str_input("Date of Birth (YYYY-MM-DD): ").replace("'", "''"),
                                                str_input("Address: ").replace("'", "''"),
                                                str_input("Phone Number: ").replace("'", "''"),
                                                input("PPS Number: ").replace("'", "''")):
                patient_name = self.db_service.get_patient_name(patient_id)
                print(f"Patient {patient_name[0]} {patient_name[1]} has been updated.")

    # Method to delete patient information in database
    def delete_patient_records(self):
        # Asks user to input patient ID
        patient_id = int_input("Please enter the Patient ID to delete: ")

        # Displays a message if the patient ID does not exist in database
        if not self.db_service.check_patient_id_in_db(patient_id):
            print("Patient not found")

        # Otherwise deletes the patient information and their treatment records from database
        else:
            patient_name = self.db_service.get_patient_name(patient_id)
            if self.db_service.delete_patient(patient_id):
                print(f"Patient {patient_name[0]} {patient_name[1]} has been deleted.")
