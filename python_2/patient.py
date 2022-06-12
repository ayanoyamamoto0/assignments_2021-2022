# Class to represent the patients in the program
class Patient:

    # Constructor to assign 6 values to the Patient object
    # and replace one apostrophe with two apostrophes for writing to database
    # Parameters are: firstname, lastname, dob, address, phone, ppsn
    def __init__(self, firstname, lastname, dob, address, phone, ppsn):
        self.firstname = firstname.replace("'", "''")
        self.lastname = lastname.replace("'", "''")
        self.dob = dob.replace("'", "''")
        self.address = address.replace("'", "''")
        self.phone = phone.replace("'", "''")
        self.ppsn = ppsn.replace("'", "''")

