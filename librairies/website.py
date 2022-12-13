class Website:
    """
    """

    def __init__(self, name):
        if name is None or name == "":
            raise ValueError("Website is empty")
        self._name = name 
    
    @property
    def name(self):
        return self._name
