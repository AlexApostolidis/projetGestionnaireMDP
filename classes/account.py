import json

class Account:
    """
    """

    def __init__(self):
        self._account = self.create_account()

    @property
    def account(self):
        return self._account

    def create_account(self, password):
        self._password = password
    
    @property
    def password(self):
        return self._password
    
    @staticmethod
    def verify_account(connection_password):
        with open("connexionId.json") as file:
            doc = json.load(file)
        return doc['user']['password'] == connection_password