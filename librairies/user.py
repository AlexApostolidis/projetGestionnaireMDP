import json


class User:
    """
    """

    def __init__(self, first, last, question):
        if first is None or first == "":
            raise (ValueError, "first is empty")
        if last is None or last == "":
            raise (ValueError, "last is empty")
        if question is None or question == "":
            raise (ValueError, "question is empty")
        self._first_name = first
        self._last_name = last
        self._security_question = question

    def __str__(self):
        return f"Bonjour monsieur{self._last_name} {self._first_name}."

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def question(self):
        return self._security_question


# saving user data in json method
def write_names(firstname, lastname, question):
    if firstname is None or firstname == "":
        raise (ValueError, "firstname is empty")
    if lastname is None or lastname == "":
        raise (ValueError, "lastname is empty")
    if question is None or question == "":
        raise (ValueError, "question is empty")
    with open("data/connexionId.json", "r") as user_data:
        data = json.load(user_data)
    data["firstname"] = firstname
    data["lastname"] = lastname
    data["question"] = question
    with open("data/connexionId.json", "w") as user_data:
        json.dump(data, user_data)