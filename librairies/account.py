import json


class Account:
    """This class is used to create a passwords for an account
    """

    def __init__(self, password):
        """This builds the password of the account

        PRE: the parameter 'password' can be of any type except being empty or 'none'
        POST: create a password
        RAISE: ValueError if the password is equal to 'None' or if it's empty
        """
        if password == "" or password is None:
            raise ValueError("Password Empty")
        self._password = password
    
    @property
    def password(self):
        return self._password

    def verify_account(self, password):
        """It is used to connect yourself to the program

        PRE: the parameter 'password' is the password which need to be used.
             It can be of any type except being empty or 'none'
        POST: return the password given to connect yourself to the program
        """
        if password == "" or password is None:
            raise ValueError("Password is empty")
        return self._password == password

    # @staticmethod
    # def create_account(password):
    #    if password == "":
    #        raise (ValueError, "password is empty")
    #    with open("data/connexionId.json", 'r') as file:
    #        json_dictionary = json.load(file)

    #    json_dictionary["user"]["password"] = password
    #    with open("data/connexionId.json", 'w') as writing_pass:
    #        json.dump(json_dictionary, writing_pass)

    # @staticmethod
    # def renew_password():
    #    """
    #       create a new password (automatic or not)
    #       param: none
    #       return: string the new password
    #    """
    #    next_password = input('Entrez le nouveau mot de passe: ')
    #    return next_password

    # @staticmethod
    # def new_password():
    #    new_password = input(" : ")
    #    return new_password

    # @staticmethod
    # def edit_application_password(new_password):
    #    """
    #        write the new_password for the application
    #        param:
    #            new_password: the new password
    #        return: none
    #    """
    #    with open("connexionId.json", 'r') as file:
    #        json_dictionary = json.load(file)

    #    json_dictionary["user"]["password"] = new_password
    #    with open("connexionId.json", 'w') as writing_pass:
    #        json.dump(json_dictionary, writing_pass)


def save_account(password):
    """It is used to save the new password of the account in the json file

    PRE: the parameter 'password' is the password which need to be saved.
         It can be of any type except being empty or 'none'
    POST: save the new password of the account in the json file which contains the information about the account
    RAISE: ValueError if the password is equal to 'None' or if it's empty
    """
    if password is None or password == "":
        raise ValueError("Password is empty")
    with open("data/connexionId.json", 'r') as file:
        json_dictionary = json.load(file)

    json_dictionary["user"]["password"] = password
    with open("data/connexionId.json", 'w') as writing_pass:
        json.dump(json_dictionary, writing_pass)


