class Username:
    """
    """

    def __init__(self):
        self._username = self.create_username()

    @property
    def username(self):
        return self._username

    def create_username(self, username):
        username = input("Quel est votre nom d'utilisateur ?")
        return username