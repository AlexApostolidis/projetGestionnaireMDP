class Website:
    """This class is used to create a name for a website
    """

    def __init__(self, name):
        """It builds a name which will be used to be the website name

        PRE: the parameter 'name' can be of any type except being empty or 'none'
        POST: create a name
        RAISE: ValueError if the name is equal to 'none' or if it's empty
        """
        if name is None or name == "":
            raise ValueError("Website is empty")
        self._name = name 
    
    @property
    def name(self):
        return self._name
