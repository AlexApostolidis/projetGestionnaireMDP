class Username:
    """
    """

    def __init__(self, username):
        if username is None or username == "":
            raise ValueError("Username is empty")
        self._username = username

    @property
    def username(self):
        return self._username
