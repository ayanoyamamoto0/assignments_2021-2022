# Class to represent login details
class Login:

    # Class attributes to set an empty string as username and "password" as the password
    username = ""
    password = "password"

    # Method to store username and check if the password is correct
    def login(self, username, password):
        self.username = username
        if password == self.password:
            return True
        else:
            return False

