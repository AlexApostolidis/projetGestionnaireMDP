class Website:
    """
    """

    def __init__(self, name):
        self._name = name 
    
    @property
    def webname(self):
        return self._name