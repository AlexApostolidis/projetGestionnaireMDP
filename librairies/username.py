class Username:
    """This class is used to create a username for a website
    """

    def __init__(self, username):
        """It builds a username for a website

        PRE: the parameter 'username' can be of any type except being empty or 'none'
        POST: create a username
        RAISE: ValueError if the username is equal to 'none' or if it's empty
        """
        if username is None or username == "":
            raise ValueError("Username is empty")
        self._username = username

    @property
    def username(self):
        return self._username
