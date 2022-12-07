class Password:
    """
    """

    def __init__(self, password):
        self._password = password

    @property
    def password(self):
        return self._password

    @staticmethod
    def testing_password(password):
        list_password_alpha = list(map(lambda x: x.isalpha(), [*password])).count(True)
        list_password_digit = list(map(lambda x: x.isdigit(), [*password])).count(True)
        list_password_non_alpha = list(map(lambda x: x.isalnum(), [*password])).count(False)

        if len(password) >= 12 and list_password_alpha >= 1 and list_password_digit >= 1 and list_password_non_alpha >= 1:
            return 1
        else:
            return 0
