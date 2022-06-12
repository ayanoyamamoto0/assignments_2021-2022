# Import AddressBook class from address_book.py
from address_book import AddressBook

# Import Login class from login.py
from login import Login


# Function to format titles
def print_title(title):
    print("-------------------------------------------------------------------------------------")
    print(f"     {title}")
    print("-------------------------------------------------------------------------------------")


# Creates a login object for the program
user_login = Login()


# Prints a welcome message and asks for user input for username and password
print_title("Welcome to the Address Book")
username = input("Username: ")
password = input("Password: ")


# If the password is incorrect, exits program with exit code 1
if not user_login.login(username, password):
    print_title("Incorrect password. Exiting program.")
    exit(1)


# If the password is correct, loads contacts.csv
address_book = AddressBook()


# Defines the menu string
menu = "Please select one of the following options:\n"\
       "1) Load address book\n"\
       "2) Display full address book\n"\
       "3) Display contacts under a category\n"\
       "4) Search for a contact\n"\
       "5) Create a new contact\n"\
       "6) Update a contact\n"\
       "7) Delete a contact\n"\
       "8) Save and exit\n\n" \
       "Your selection: "


# Asks user for an input to select from the menu
menu_input = "0"
active_file = address_book.filename

while True:

    print_title("Address Book Menu")
    menu_input = input(menu)

    # Option 1: Load address book
    if menu_input == "1":
        filename = input("CSV file name: ")
        if address_book.load_csv_file(filename):
            active_file = filename

    # Option 2: Display full address book
    elif menu_input == "2":
        address_book.display_full_address_book()

    # Option 3: Display contacts under a category
    elif menu_input == "3":
        address_book.filter_by_category()

    # Option 4: Search for a contact
    elif menu_input == "4":
        address_book.search_contact()

    # Option 5: Create a new contact
    elif menu_input == "5":
        address_book.create_contact(username)

    # Option 6: Update a contact
    elif menu_input == "6":
        address_book.update_contact(username)

    # Option 7: Delete a contact
    elif menu_input == "7":
        address_book.delete_contact()

    # Option 8: Save and exit
    elif menu_input == "8":
        address_book.write_data(active_file)
        print_title("Exiting program.")
        exit(2)

    # Displays an error message if the input does not match available options
    else:
        print("Invalid selection. Please try again.")

    # Asks user to press Enter to loop back to the menu
    input("\nPress Enter to return to menu...")
