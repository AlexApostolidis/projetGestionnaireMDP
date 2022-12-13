class Password:
    """This class is about password related to a website
    """

    def __init__(self, password):
        """This build the password of the account

        PRE: the parameter 'password' can be of any type except being empty or 'none'
        POST: create a password
        RAISE: ValueError if the password is equal to 'none' or if it's empty
        """
        if password == "" or password is None:
            raise ValueError("Password is empty")
        self._password = password

    @property
    def password(self):
        return self._password

    @staticmethod
    def testing_password(password):
        """It tests if the password is strong enough

        PRE: the parameter 'password' is the password which need to be tested
        POST: return 1 if the password is at least 12 characters long, if there is at least one number
              and if there is at least 1 non-alphanumeric character.
              return 0 if one of the test isn't successful
        RAISE: ValueError if the password is equal to 'None' or if it's empty
        """
        if password is None or password == "":
            raise ValueError("Password is empty")
        list_password_alpha = list(map(lambda x: x.isalpha(), [*password])).count(True)
        list_password_digit = list(map(lambda x: x.isdigit(), [*password])).count(True)
        list_password_non_alpha = list(map(lambda x: x.isalnum(), [*password])).count(False)

        if len(password) >= 12 and list_password_alpha >= 1 and list_password_digit >= 1 \
                and list_password_non_alpha >= 1:
            return 1
        else:
            return 0
