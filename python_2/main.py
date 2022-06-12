# Import DBService class from dbservice.py
from dbservice import DBService

# Import SLL class from sll.py
from sll import SLL

# Import TreatmentList class from department.py
from department import Department

# Create DBService object
database = DBService("ae.db")

# Create SLL object
treatment_sll = SLL()

# Create TreatmentList object
ae = Department("Accident and Emergency", treatment_sll, database)


# Defines the main menu string
main_menu = "Please select one of the following options:\n" \
            "1) Admission\n" \
            "2) Triage\n" \
            "3) Treatment\n" \
            "4) Search treatment records\n" \
            "5) Update patient information\n" \
            "6) Delete patient records\n\n" \
            "Your selection: "

# Defines the admission menu string
admission_menu = "Please select one of the following options:\n" \
                 "1) New patient\n" \
                 "2) Existing patient\n\n" \
                 "Your selection: "

# Defines the search menu string
search_menu = "Please select a field:\n" \
              "1) Patient Name\n" \
              "2) Admission Date\n" \
              "3) Treatment Doctor\n\n" \
              "Your selection: "


# Function to format titles
def print_title(title):
    print("-------------------------------------------------------------------------------------")
    print(f"     {title}")
    print("-------------------------------------------------------------------------------------")


# Sets the initial menu input to 0
menu_input = "0"

while True:

    # Prints a menu title and displays numbers of patients waiting for triage and treatment
    print_title(f"Accident and Emergency Department Menu\n     "
                f"Current Queues: Triage {ae.triage_queue_size()}, "
                f"Treatment {ae.treatment_queue_size()}")

    # Asks user for an input to select from the main menu
    menu_input = input(main_menu)

    # Option 1: Admission
    # Asks user for an input to select from the admission menu
    if menu_input == "1":
        admission_menu_input = input(admission_menu)

        # Admission Option 1: New Patient
        if admission_menu_input == "1":
            ae.add_new_patient()

        # Admission Option 2: Existing Patient
        elif admission_menu_input == "2":
            ae.add_existing_patient()

        # Displays an error message if the input does not match available options
        else:
            print("Invalid selection. Please try again.")

    # Option 2: Triage
    elif menu_input == "2":

        # Displays a message if there are no patients awaiting triage
        if ae.triage_queue_size() == 0:
            print("There are no patients awaiting triage.")

        # Otherwise display admission information of the next patient awaiting triage
        # Asks user to input triage information and updates Treatment object
        else:
            print_title("Triage Patient Information")
            ae.add_triage_info()

    # Option 3: Treatment
    elif menu_input == "3":

        # Displays a message if there are no patients awaiting treatment
        if ae.treatment_queue_size() == 0:
            print("There are no patients awaiting treatment.")

        # Otherwise display admission and triage information of the next patient awaiting treatment
        # Asks user to input treatment information and updates Treatment object
        # Saves the Treatment object in database and removes patient from SLL
        else:
            print_title("Treatment Patient Information")
            ae.add_treatment_info()

    # Option 4: View Treatment Records
    # Asks user for an input to select from the search menu
    elif menu_input == "4":
        search_menu_input = input(search_menu)

        # Search Option 1:
        if search_menu_input == "1":
            ae.search_patient_name()

        # Search Option 2:
        elif search_menu_input == "2":
            ae.search_date()

        # Search Option 3:
        elif search_menu_input == "3":
            ae.search_doctor()

        # Displays an error message if the input does not match available options
        else:
            print("Invalid selection. Please try again.")

    # Option 5: Update Patient Information
    elif menu_input == "5":
        ae.update_patient_info()

    # Option 6: Delete Patient Records
    elif menu_input == "6":
        ae.delete_patient_records()

    # Displays an error message if the input does not match available options
    else:
        print("Invalid selection. Please try again.")

    # Asks user to press Enter to loop back to the menu
    input("\nPress Enter to return to menu...")


