import json


class Account:
    """
    """

    def __init__(self):
        with open("connexionId.json", 'r') as file:
            password = json.load(file)

        self._password = password["user"]["password"]
    
    @property
    def password(self):
        return self._password

    @staticmethod
    def create_account(password):
        with open("connexionId.json", 'r') as file:
            json_dictionnary = json.load(file)

        json_dictionnary["user"]["password"] = password
        with open("connexionId.json", 'w') as writing_pass:
            json.dump(json_dictionnary, writing_pass)

    @staticmethod
    def verify_account(password):
        with open("connexionId.json") as file:
            doc = json.load(file)
        return doc['user']['password'] == password

    @staticmethod
    def renew_password():
        """
           create a new password (automatic or not)
           param: none
           return: string the new password
        """
        next_password = input('entrez le nouveau mot de passe: ')
        return next_password
