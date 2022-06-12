# Class to represent a contact in the address book
class Contact:

    # Constructor to assign 11 values to the contact object
    # Parameters are: id, first_name, last_name, company, address, landline, mobile, category, date_created,
    #                   date_updated, modified_by
    def __init__(self, id, first_name, last_name, company, address, landline, mobile, category,
                 date_created, date_updated, modified_by):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.address = address
        self.landline = landline
        self.mobile = mobile
        self.category = category
        self.date_created = date_created
        self.date_updated = date_updated
        self.modified_by = modified_by

    # Method to format how the contact details are displayed
    def display_contact(self):
        print(f"--------------ID: {self.id}--------------\n"
              f"- Name: {self.first_name} {self.last_name}\n"
              f"- Company: {self.company}\n"
              f"- Address: {self.address}\n"
              f"- Landline: {self.landline}\n"
              f"- Mobile: {self.mobile}\n"
              f"- Category: {self.category}\n"
              f"- Date Created: {self.date_created}\n"
              f"- Date Updated: {self.date_updated}\n"
              f"- Modified by: {self.modified_by}")

    # Method to update existing contact object with new details
    def update_contact_details(self, new_contact_details):
        self.id = new_contact_details[0]
        self.first_name = new_contact_details[1]
        self.last_name = new_contact_details[2]
        self.company = new_contact_details[3]
        self.address = new_contact_details[4]
        self.landline = new_contact_details[5]
        self.mobile = new_contact_details[6]
        self.category = new_contact_details[7]
        self.date_created = new_contact_details[8]
        self.date_updated = new_contact_details[9]
        self.modified_by = new_contact_details[10]

    # Method to convert a contact object into a list
    def to_list(self):
        return [self.id, self.first_name, self.last_name, self.company, self.address, self.landline, self.mobile,
                self.category, self.date_created, self.date_updated, self.modified_by]
