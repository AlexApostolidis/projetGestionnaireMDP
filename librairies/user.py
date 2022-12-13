import json


class User:
    """Class representing a user from the application

    Authors : Shayann Gonzalez, Apostolidis Alex, Thomas Jacob
    Date : 13/12/2022
    """

    def __init__(self, first, last, question):
        """It creates a User with a firstname, a lastname and a question about him

        PRE :
             :param first: can't be None or empty, it's the firstname of the User
             :param last: can't be None or empty, it's the lastname of the User
             :param question: can't be None or empty, it's a question about him
        POST : Create three properties first_name which is his firstname, last_name which is his lastname and
        security_question which is the question about him
        """
        if first is None or first == "":
            raise ValueError("first is empty")
        if last is None or last == "":
            raise ValueError("last is empty")
        if question is None or question == "":
            raise ValueError("question is empty")
        self._first_name = first
        self._last_name = last
        self._security_question = question

    def __str__(self):
        """It's says hi to the User
        PRE : -
        POST :
              :return: "Bonjour monsieur last_name firs_name"
        """
        return f"Bonjour monsieur{self._last_name} {self._first_name}."

    @property
    def first_name(self):
        """The firstname of the User
        PRE : -
        POST :
              :return: the first_name property
        """
        return self._first_name

    @property
    def last_name(self):
        """The lastname of the User
        PRE : -
        POST :
              :return: the last_name property
        """
        return self._last_name

    @property
    def question(self):
        """A question about the User
        PRE : -
        POST :
              :return: the security_question property
        """
        return self._security_question


# saving user data in json method
def write_names(firstname, lastname, question):
    """It writes the firstname, the lastname and the question of the User
    In a json file

    PRE :
         :param firstname: can't be None or empty, it's the firstname of the User
         :param lastname: can't be None or empty, it's the lastname of the User
         :param question: can't be None or empty, it's a question about him
    POST : Writes the firstname, lastname and the question in a json file
    """
    if firstname is None or firstname == "":
        raise ValueError("firstname is empty")
    if lastname is None or lastname == "":
        raise ValueError("lastname is empty")
    if question is None or question == "":
        raise ValueError("question is empty")
    with open("data/connexionId.json", "r") as user_data:
        data = json.load(user_data)
    data["firstname"] = firstname
    data["lastname"] = lastname
    data["question"] = question
    with open("data/connexionId.json", "w") as user_data:
        json.dump(data, user_data)
