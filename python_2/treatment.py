# Class to represent the treatments in the program
class Treatment:

    # Constructor to assign 15 values to the Treatment object, of which 12 are default values
    # Parameters are: patient_id, admission_time, admission_summary
    def __init__(self, patient_id, admission_time, admission_summary):
        self.patient_id = patient_id
        self.admission_time = admission_time
        self.admission_summary = admission_summary
        self.triage_time = ""
        self.triage_nurse = ""
        self.body_temp = ""
        self.pulse_rate = ""
        self.respiration_rate = ""
        self.bp_systolic = ""
        self.bp_diastolic = ""
        self.triage_summary = ""
        self.priority_value = 0
        self.treatment_time = ""
        self.treatment_doctor = ""
        self.treatment_summary = ""

    # Method to assign 9 values to the Treatment object from triage inputs
    def triage(self, triage_time, triage_nurse, body_temp, pulse_rate, respiration_rate, bp_systolic, bp_diastolic,
               triage_summary, priority_value):
        self.triage_time = triage_time
        self.triage_nurse = triage_nurse
        self.body_temp = body_temp
        self.pulse_rate = pulse_rate
        self.respiration_rate = respiration_rate
        self.bp_systolic = bp_systolic
        self.bp_diastolic = bp_diastolic
        self.triage_summary = triage_summary
        self.priority_value = priority_value

    # Method to assign 3 values to the Treatment object from treatment inputs
    # and replace one apostrophe with two apostrophes for writing to database
    def treatment(self, treatment_time, treatment_doctor, treatment_summary):
        self.admission_summary = self.admission_summary.replace("'", "''")
        self.triage_nurse = self.triage_nurse.replace("'", "''")
        self.triage_summary = self.triage_summary.replace("'", "''")
        self.treatment_time = treatment_time
        self.treatment_doctor = treatment_doctor.replace("'", "''")
        self.treatment_summary = treatment_summary.replace("'", "''")
