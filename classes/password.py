import random_passWord

class Password:
    """
    """

    def __init__(self):
        self._password = self.create_password

    @property
    def password(self):
        return self._password

    def create_password(self):
        question = input('Voulez vous un mot de passe automatique ?').lower
        if question == "oui":
            password = self.automatic_password()
        else :
            password =  input('Entrez votre mot de passe')
        return password

    def automatic_password(self):
        return random_passWord.automatic_random_password()