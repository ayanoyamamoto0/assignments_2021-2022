# import the CSV module
import csv

# Import the datetime module
from datetime import datetime

# Import Contact class from contact.py
from contact import Contact


# Function to ask for user input to select category
def select_category():
    while True:
        category_input = input("Please select a category:\n"
                               "1) Development\n"
                               "2) Support\n"
                               "3) Office Fitting\n\n"
                               "Your selection: ")

        # Returns corresponding category name in string
        if category_input == "1":
            return "Development"
        elif category_input == "2":
            return "Support"
        elif category_input == "3":
            return "Office Fitting"

        # Displays an error message if the input does not match available options
        else:
            print("Invalid selection. Please try again.")


# Function to ask for user input to select field
def select_field():
    while True:
        field_input = input("Please select a field:\n"
                            "1) Contact ID\n"
                            "2) First Name\n"
                            "3) Last Name\n"
                            "4) Company\n"
                            "5) Address\n"
                            "6) Landline\n"
                            "7) Mobile\n"
                            "8) Category\n"
                            "9) Date Created\n"
                            "10) Date Updated\n"
                            "11) Modified by\n\n"
                            "Your selection: ")

        # Returns user input if it is valid
        if 1 <= int(field_input) <= 11:
            return field_input

        # Displays an error message if the input does not match available options
        else:
            print("Invalid selection. Please try again.")


# Function to ask for user input of contact details
def contact_details(id, username):
    list_of_details = [id, input("First Name: "), input("Last Name: "), input("Company: "), input("Address: "),
                       input("Landline: "), input("Mobile: "), select_category(),
                       datetime.today().strftime('%Y-%m-%d'), datetime.today().strftime('%Y-%m-%d'), username]
    return list_of_details


# Class to represent an addressbook in the program
class AddressBook:

    # Sets a default csv file as Class attribute
    filename = "contacts.csv"

    # Constructor to create two empty lists for header and contacts rows from csv files
    # Loads contacts.csv as default
    def __init__(self):
        self.header = []
        self.contacts = []
        self.load_csv_file(self.filename)

    # Method to load a csv file specified by user
    def load_csv_file(self, filename):

        # Tries to open the specified csv file
        try:
            file = open(filename)

            # If the csv file is successfully opened, empties existing contacts list
            self.contacts = []

            # Appends each row to the emptied list
            with file as csv_file:
                read_csv = csv.reader(csv_file, delimiter=",")
                self.header = next(read_csv)
                for row in read_csv:
                    self.contacts.append(Contact(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7],
                                                 row[8], row[9], row[10]))

            # Displays a confirmation message and returns True
            print(f"\n{filename} has been loaded")
            return True

        # If there is an error in opening the csv file, displays an error message and returns False
        except OSError:
            print("File not found")
            return False

    # Method to display all contacts
    def display_full_address_book(self):
        for c in self.contacts:
            c.display_contact()

    # Method to display all contacts under selected category
    def filter_by_category(self):

        # Asks for user input to select category
        category_input = select_category()

        # Sets up an empty list
        filtered_list = []

        # Appends contacts that have matching category to the empty list
        for c in self.contacts:
            if category_input == c.category:
                filtered_list.append(c)

        # Displays contacts in the list
        for f in filtered_list:
            f.display_contact()

    # Method to search the address book for all fields
    def search_contact(self):

        # Asks for user input to select field
        field_input = select_field()

        # Sets up an empty list
        filtered_list = []

        # Appends contacts that have matching ID to the empty list
        if field_input == "1":
            input_id = input("Please enter the contact ID to search: ")
            for c in self.contacts:
                if input_id == c.id:
                    filtered_list.append(c)

        # Appends contacts that have matching first name to the empty list
        elif field_input == "2":
            input_first_name = input("Please enter the first name to search: ")
            for c in self.contacts:
                if input_first_name == c.first_name:
                    filtered_list.append(c)

        # Appends contacts that have matching last name to the empty list
        elif field_input == "3":
            input_last_name = input("Please enter the last name to search: ")
            for c in self.contacts:
                if input_last_name == c.last_name:
                    filtered_list.append(c)

        # Appends contacts that have matching company name to the empty list
        elif field_input == "4":
            input_company = input("Please enter the company name to search: ")
            for c in self.contacts:
                if input_company == c.company:
                    filtered_list.append(c)

        # Appends contacts that have matching address to the empty list
        elif field_input == "5":
            input_address = input("Please enter the address to search: ")
            for c in self.contacts:
                if input_address == c.address:
                    filtered_list.append(c)

        # Appends contacts that have matching landline number to the empty list
        elif field_input == "6":
            input_landline = input("Please enter the landline number to search: ")
            for c in self.contacts:
                if input_landline == c.landline:
                    filtered_list.append(c)

        # Appends contacts that have matching mobile to the empty list
        elif field_input == "7":
            input_mobile = input("Please enter the mobile number to search: ")
            for c in self.contacts:
                if input_mobile == c.mobile:
                    filtered_list.append(c)

        # Appends contacts that have matching category to the empty list
        elif field_input == "8":
            input_category = select_category()
            for c in self.contacts:
                if input_category == c.category:
                    filtered_list.append(c)

        # Appends contacts that have matching created date to the empty list
        elif field_input == "9":
            input_date_created = input("Please enter the created date to search (YYYY-MM-DD): ")
            for c in self.contacts:
                if input_date_created == c.date_created:
                    filtered_list.append(c)

        # Appends contacts that have matching updated date to the empty list
        elif field_input == "10":
            input_date_updated = input("Please enter the updated date to search (YYYY-MM-DD): ")
            for c in self.contacts:
                if input_date_updated == c.date_updated:
                    filtered_list.append(c)

        # Appends contacts that have matching modified-by name to the empty list
        elif field_input == "11":
            input_modified_by = input("Please enter the modified-by name search: ")
            for c in self.contacts:
                if input_modified_by == c.modified_by:
                    filtered_list.append(c)

        # Displays an error message if the input does not match available options
        else:
            print("Invalid selection. Please try again.")

        # Displays an error message if no match was found
        if len(filtered_list) == 0:
            print("No match found.")

        # Displays search result
        else:
            for f in filtered_list:
                f.display_contact()

    # Method to ask for user input to create a new contact
    def create_contact(self, username):
        new_id = str(len(self.contacts) + 1)
        new_details = contact_details(new_id, username)
        self.contacts.append(Contact(new_details[0], new_details[1], new_details[2], new_details[3],
                                     new_details[4], new_details[5], new_details[6], new_details[7],
                                     new_details[8], new_details[9], new_details[10]))

        # Checks if the new contact is created, then displays a confirmation message
        for c in self.contacts:
            if new_id == c.id:
                print(f"ID {c.id}: {c.first_name} {c.last_name} has been created.")

    # Method to search for a contact by ID, and ask for user input to update
    def update_contact(self, username):
        input_id = input("Please enter the contact ID to update: ")
        for c in self.contacts:
            if input_id == c.id:
                new_details = contact_details(input_id, username)
                c.update_contact_details(new_details)
                print(f"ID {c.id}: {c.first_name} {c.last_name} has been updated.")
                break
        else:
            print("No match found.")

    # Method to search for a contact by ID and deletes contact object
    def delete_contact(self):
        input_id = input("Please enter the contact ID to delete: ")
        for c in self.contacts:
            if input_id == c.id:
                self.contacts.remove(c)
                print(f"ID {c.id}: {c.first_name} {c.last_name} has been deleted.")
                break
        else:
            print("No match found.")

    # Method to write the address book objects to a csv file
    def write_data(self, filename):

        # Sets up an empty list
        contacts_list = []

        # Converts contact objects into lists and appends to the empty list
        for c in self.contacts:
            contact_csv = c.to_list()
            contacts_list.append(contact_csv)

        # Writes the list of contacts to the specified csv file
        with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(self.header)
            csv_writer.writerows(contacts_list)
